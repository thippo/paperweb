import sqlite3

def connect_db():
     return sqlite3.connect("/data/login.db")
