"""
    Name: db.py
    Author: Rajshankar M
    Description: Python script file that creates a connection with an SQLite database.
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
        Create a database connection to a SQLite Database
        db_file: Database file
        returns a Connection object or None.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """
        Create a table from the create_table_sql statement
        conn: Connection object
        Void function
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    """
        Main function. Calls a function to create a database and then makes tables in said database.
    """

    #Create database
    database = r"db\inventory.db"
    conn = create_connection(database)

    #Create table
    inventory = """
                        CREATE TABLE IF NOT EXISTS inventory (
                            id integer PRIMARY KEY,
                            mat_desc text NOT NULL,
                            mat_code text NOT NULL,
                            variant text,
                            stock integer NOT NULL
                        );
                    """
    if conn is not None:
        #Create a table
        create_table(conn, inventory)
    else:
        print("Cannot create database connection.")


if __name__ == '__main__':
    main()