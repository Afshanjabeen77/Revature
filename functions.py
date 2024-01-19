# functions.py

import pandas as pd
import sqlite3

def connect_to_database():
    return sqlite3.connect('Inflationdata.db')

def insert_data(conn, Countries, Inflation2022, Global_rank, Available_data):
    duplicate_check_query = 'SELECT COUNT(*) FROM inflationranks WHERE Countries=?'
    existing_count = conn.execute(duplicate_check_query, (Countries,)).fetchone()[0]

    if existing_count > 0:
        print("Duplicate entry! Duplicates are not allowed.")
        return

    query = '''
        INSERT INTO inflationranks (Countries, Inflation2022, Global_rank, Available_data)
        VALUES (?, ?, ?, ?)
    '''
    conn.execute(query, (Countries, Inflation2022, Global_rank, Available_data))
    conn.commit()
    print("Data inserted successfully.")

def select_data(conn):
    query = 'SELECT * FROM inflationranks'
    result = pd.read_sql_query(query, conn)
    return result

def update_data(conn, Countries, new_inflation):
    query = 'UPDATE inflationranks SET Inflation2022=?  WHERE Countries=?'
    conn.execute(query, (new_inflation, Countries))
    conn.commit()
    print("Data updated successfully.")

def delete_data(conn, Countries):
    existence_check_query = 'SELECT COUNT(*) FROM inflationranks WHERE Countries=?'
    existing_count = conn.execute(existence_check_query, (Countries,)).fetchone()[0]

    if existing_count == 0:
        print("The value does not exist. Deletion not allowed.")
        return

    query = 'DELETE FROM inflationranks WHERE Countries=?'
    conn.execute(query, (Countries,))
    conn.commit()
    print("Data deleted successfully.")
