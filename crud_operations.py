# crud_operations.py

from functions import *

def perform_insert(conn):
    Countries = input("Enter countries: ")
    Inflation2022 = float(input("Enter inflation: "))
    Global_rank = int(input("Enter global rank: "))
    Available_data = input("Enter available data: ")

    insert_data(conn, Countries, Inflation2022, Global_rank, Available_data)

def perform_update(conn):
    Countries = input("Enter countries to update: ")
    new_inflation = float(input("Enter new inflation: "))
    update_data(conn, Countries, new_inflation)

def perform_delete(conn):
    Countries = input("Enter countries to delete: ")
    delete_data(conn, Countries)

def perform_display(conn):
    data = select_data(conn)
    print("Table:")
    print(data)
