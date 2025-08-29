from interface import PasswordManager
from password_generator import PasswordGenerator

password = PasswordGenerator(None)  # Temporary None, will be set later
app = PasswordManager(
    generate=password.generate, add=password.add, search=password.search
)
password.app = app  # Link back the app instance

app.run()
