# Referred to the documentation: https://docs.python.org/3/library/sqlite3.html

import sqlite3

# Making a connection to the database

conn = sqlite3.connect("data.db")
cursor = conn.cursor()  # this is used to execute the SQL commands

# Creating tables according to the instructions
cursor.execute(
    """
              CREATE TABLE IF NOT EXISTS Data_PolygonTest 
              ( HarvestBlock INTEGER, 
              SquareMeters REAL)"""
)

cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS Data_OperatorTest 
                ( HarvestBlock INTEGER, 
                OperatorCode TEXT)"""
)


# Inserting the data into the tables as per the instructions

cursor.executemany(
    """
                  INSERT INTO Data_PolygonTest (HarvestBlock, SquareMeters) VALUES (?, ?)""",
    [(4091111, 23930.5), (4091111, 31768.2), (4092222, 46395.6)],
)

cursor.executemany(
    """
                  INSERT INTO Data_OperatorTest (HarvestBlock, OperatorCode) VALUES (?, ?)""",
    [(4091111, "AAAA"), (4092222, "BBBB")],
)

# Committing the changes and closing the connection

conn.commit()
conn.close()
