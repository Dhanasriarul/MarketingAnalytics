import mysql.connector
import streamlit as st

#connection

conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="mydb"
)
c=conn.cursor()

#fetch

def view_all_data():
    c.execute("SELECT * FROM Marketing ORDER BY id ASC")

    data=c.fetchall()
    return data
