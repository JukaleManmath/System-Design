import sqlite3

class DatabaseConnection:
    _instance = None  # holds single instance

    def __init__(self, db_file):
        if DatabaseConnection._instance is not None:
            raise Exception("Use get_instance() instead of creating directly.")

        # simulate a database connection
        self.connection = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")

    @staticmethod
    def get_instance(db_file="app.db"):
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = DatabaseConnection(db_file)
        return DatabaseConnection._instance

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("Executed:", query)

    def close(self):
        self.connection.close()
        print("Connection closed.")


# Module 1
db1 = DatabaseConnection.get_instance()
db1.execute_query("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")

# Module 2 (somewhere else in the program)
db2 = DatabaseConnection.get_instance()
db2.execute_query("INSERT INTO users(name) VALUES ('Alice')")

# Check that db1 and db2 are the same
print(db1 is db2)  # True

# Close connection
db1.close()
