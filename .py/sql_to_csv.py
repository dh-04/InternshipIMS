import sqlite3
import csv

def write_csv():
    with sqlite3.connect("../db/inventory.db") as connection:
        csvWriter = csv.writer(open("../db/inventory.csv", "w"))
        c = connection.cursor()
        c.execute("SELECT * FROM inventory")
        rows = c.fetchall()
        csvWriter.writerow(['prod_name', 'prod_id', 'variant', 'stock'])
        csvWriter.writerows(rows)



if __name__ == "__main__":
    write_csv()