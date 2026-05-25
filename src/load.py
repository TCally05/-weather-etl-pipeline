import sqlite3
import os
from sqlalchemy import create_engine

# The database file will be created in the data/ folder
DB_PATH = os.path.join("data", "weather.db")

def load_weather(df):
    """
    Loads the clean weather DataFrame into a SQLite database.
    - Creates the data/ folder if it doesn't exist
    - Creates the database file if it doesn't exist
    - Replaces the table each run (so we always have fresh data)
    """

    print("Loading data into SQLite database...")

    # Create the data/ folder if it doesn't already exist
    os.makedirs("data", exist_ok=True)

    # Create a connection to the SQLite database
    # SQLAlchemy handles creating the file automatically
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Write the DataFrame to a table called "weather_forecast"
    # if_exists="replace" means each run starts fresh
    df.to_sql("weather_forecast", engine, if_exists="replace", index=False)

    print(f"  Loaded {len(df)} rows into '{DB_PATH}' → table: weather_forecast")
    print("Done!")


def query_preview():
    """
    Runs a quick SQL query so you can see your data in the terminal.
    This is just for checking — not part of the pipeline itself.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n--- Preview: first 5 rows from database ---")
    cursor.execute("SELECT * FROM weather_forecast LIMIT 5")
    rows = cursor.fetchall()

    # Print column names
    col_names = [desc[0] for desc in cursor.description]
    print(" | ".join(col_names))
    print("-" * 80)

    for row in rows:
        print(" | ".join(str(v) for v in row))

    conn.close()
