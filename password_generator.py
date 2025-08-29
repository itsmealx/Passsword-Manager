from tkinter import messagebox
import json


class PasswordGenerator:
    def __init__(self, app):
        self.app = app

    def generate(self) -> None:
        """Generates a random password and inserts it into the password entry field."""
        import random  # Importing here to limit scope

        self.app.password_entry.config(state="normal")  # Enable editing
        self.app.password_entry.delete(0, "end")  # Clear existing password

        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

        # List comprehensions to generate random characters
        let = [random.choice(letters) for _ in range(random.randint(8, 10))]
        num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
        sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]

        password_list = let + num + sym  # Combine lists
        random.shuffle(password_list)  # Shuffle the combined list
        password = "".join(password_list)  # Join list into a string

        self.app.password_entry.insert(0, password)  # Insert new password

    def add(self) -> None:
        """Saves the entered credentials to a JSON file."""

        # Get user input from entry fields
        website = self.app.website_entry.get().title()
        email = self.app.email_entry.get()
        password = self.app.password_entry.get()

        if not website or not email or not password:
            messagebox.showerror(
                title="Warning", message="Please don't leave any fields empty!"
            )
        else:
            password_data = {website: {"email": email, "password": password}}
            try:

                # Try to open and read existing data
                with open("output/passwords.json", mode="r") as file:
                    data = json.load(file)
                    data.update(password_data)  # update old data with new data
            except FileNotFoundError:
                # If file doesn't exist, create it with the new data
                with open("output/passwords.json", mode="w") as file:
                    json.dump(password_data, file, indent=4)
            else:
                # If file exists, write the updated data back to the file
                with open("output/passwords.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                self.app.website_entry.delete(0, "end")
                self.app.website_entry.focus()
                self.app.password_entry.delete(0, "end")
                self.app.password_entry.config(state="disabled")
                messagebox.showinfo(title="Success", message="Password has been added!")

    def search(self) -> None:
        """Searches for the credentials of a given website and displays them."""
        website = self.app.website_entry.get().title()

        if not website:
            messagebox.showerror(title="Error", message="Please enter a website name.")
            return

        try:
            with open("output/passwords.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=website, message=f"Email: {email}\nPassword: {password}"
                )
            else:
                messagebox.showerror(
                    title="Error", message=f"No details for {website} exists."
                )
