from flask import Flask, render_template
import sqlite3

# Referred to the documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/

# Setting up Flask
app = Flask(__name__)


# Creating the sqlite database connection
def db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = (
        sqlite3.Row
    )  # This will return the rows by the database connection
    return conn


# This is the endpoint where we can see the data in table format
@app.route("/")
def index():
    conn = db_connection()
    query = """
    SELECT 
        Data_OperatorTest.OperatorCode,
        Data_OperatorTest.HarvestBlock,
        SUM(Data_PolygonTest.SquareMeters / 10000) as Hectares
    FROM
        Data_OperatorTest
    JOIN
        Data_PolygonTest ON Data_OperatorTest.HarvestBlock = Data_PolygonTest.HarvestBlock
    GROUP BY
        Data_OperatorTest.OperatorCode, Data_OperatorTest.HarvestBlock
    """

    data = conn.execute(query).fetchall()
    conn.close()

    # Convert data into dictionary format
    records = [dict(row) for row in data]

    # Extract unique operator code in case if there are multiple operators of the same name
    operators = list(set([record["OperatorCode"] for record in records]))

    return render_template("index.html", data=records, operators=operators)


# Running the flask application
if __name__ == "__main__":
    app.run(debug=True)
