class Authentication:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        # Check if the username already exists
        self.db.cursor.execute("SELECT * FROM Users WHERE Username = ?", username)
        if self.db.cursor.fetchone():
            raise ValueError("Username already exists.")

        # Insert new user
        self.db.cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", username, password)
        self.db.commit()

    def login(self, username, password):
    # Check if the username and password match
        self.db.cursor.execute("SELECT UserID FROM Users WHERE Username = ? AND Password = ?", username, password)
        user = self.db.cursor.fetchone()
        if user:
            return user[0]  # Return the user ID
        else:
            return None

