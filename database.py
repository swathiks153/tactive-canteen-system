import sqlite3

DATABASE = "canteen.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    connection.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        total INTEGER NOT NULL,
        order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    count = connection.execute(
        "SELECT COUNT(*) FROM foods"
    ).fetchone()[0]

    if count == 0:
        connection.executemany(
            "INSERT INTO foods (name, price, stock) VALUES (?, ?, ?)",
            [
                ("Burger", 80, 10),
                ("Pizza", 120, 5),
                ("Sandwich", 60, 8)
            ]
        )

    connection.commit()
    connection.close()