from tkinter import *


class PasswordManager:
    # Initializes the Password Manager GUI application.
    def __init__(self, **kwargs):
        self.generate = kwargs.get("generate")
        self.add = kwargs.get("add")
        self.search = kwargs.get("search")
        self.root = Tk()
        self.root.title("Password Manager")
        self.root.config(padx=50, pady=50)
        self._bg_img = PhotoImage(file="assets/logo.png")
        self.display()

    def display(self):
        """Sets up the main window layout."""
        self._lockscreen()
        self._canvas()
        self._labels()
        self._entries()
        self._buttons(self.generate, self.add, self.search)

    def _lockscreen(self):
        """Centers the window on the screen and prevents resizing."""
        self.root.resizable(False, False)
        window_width = 530
        window_height = 400

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def _canvas(self):
        """Sets up the canvas with the logo image."""
        canvas = Canvas(width=200, height=200, highlightthickness=0)
        canvas.create_image(120, 100, image=self._bg_img)
        canvas.grid(row=0, column=1)

    def _labels(self):
        """Sets up the labels for the input fields."""
        website_label = Label(text="Website:")
        website_label.grid(row=1, column=0)

        email_label = Label(text="Email/Username:")
        email_label.grid(row=2, column=0)

        password_label = Label(text="Password:")
        password_label.grid(row=3, column=0)

    def _entries(self):
        """Sets up the entry fields for user input."""
        self.website_entry = Entry(width=32)
        self.website_entry.focus()
        self.website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
        self.email_entry.insert(0, "sample@email.com")

        self.password_entry = Entry(width=32, state="disable")
        self.password_entry.grid(row=3, column=1, sticky="W")

    def _buttons(self, generate, add, search):
        """Sets up the buttons for generating passwords and adding entries."""
        generate_password_button = Button(
            text="Generate Password", width=15, command=generate
        )
        generate_password_button.grid(row=3, column=2, sticky="E")

        add_button = Button(text="Add", width=36, command=add)
        add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

        search_button = Button(text="Search", width=15, command=search)
        search_button.grid(row=1, column=1, columnspan=2, sticky="E")

    def run(self):
        """Starts the main event loop."""
        self.root.mainloop()
