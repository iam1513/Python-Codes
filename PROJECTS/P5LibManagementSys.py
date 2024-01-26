class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def authenticate(self, entered_password):
        """
        Authenticates the user by comparing the entered password with the stored password.

        Parameters:
        - entered_password (str): The password entered by the user.

        Prints a welcome message upon successful authentication or an error message if authentication fails.
        """
        if entered_password == self.password:
            self.is_authenticated = True
            print(f"Welcome, {self.username}! You are now authenticated.")
        else:
            print("Authentication failed. Incorrect password.")

class UserManagementSystem:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        """
        Registers a new user with the provided username and password.

        Parameters:
        - username (str): The desired username for the new user.
        - password (str): The password for the new user.

        Checks if the username is already taken before creating a new user and adding it to the system.
        """
        # Check if the username is already taken
        if any(user.username == username for user in self.users):
            print("Username already taken. Please choose a different username.")
        else:
            new_user = User(username, password)
            self.users.append(new_user)
            print(f"User '{username}' registered successfully.")

    def login_user(self, username, password):
        """
        Attempts to log in a user with the provided username and password.

        Parameters:
        - username (str): The username of the user trying to log in.
        - password (str): The password entered by the user for authentication.

        Finds the user with the given username and attempts to authenticate using the provided password.
        Prints a success message or an error message accordingly.
        """
        # Find the user with the given username
        user = next((user for user in self.users if user.username == username), None)

        if user:
            user.authenticate(password)
        else:
            print("User not found. Please register or check your username.")

def main():
    user_management_system = UserManagementSystem()

    # Register users
    user_management_system.register_user("alice", "password123")
    user_management_system.register_user("bob", "securepass")

    # Attempt to login
    user_management_system.login_user("alice", "password123")
    user_management_system.login_user("bob", "wrongpassword")

if __name__ == "__main__":
    main()
