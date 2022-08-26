#importing modules
import mysql.connector as sqltor
import streamlit as st
#defining main function
def mysqlconnection():
    global mycon,cursor#declaring global variables
    #establishing mysql connection
    mycon=sqltor.connect(**st.secrets["mysql"])

    if mycon.is_connected():
        cursor=mycon.cursor()#creating mysql cusrsor
        createtablefn()#calling creation of tables function
    else:
        print("ERROR")

#defing creation of table function
def createtablefn():
    #defining query string for creating user details table
    querystr1='''CREATE TABLE IF NOT EXISTS User_Details
    (Unique_ID  bigint(32) Primary Key,
    Shop_Name   varchar(100),
    User_Name   varchar(100),
    Ph_No       bigint(10),
    Pwd         varchar(30))'''

    #defining query string for creating shop details table
    querystr2='''CREATE TABLE IF NOT EXISTS Shop_Details
    (Unique_ID  bigint(32) Primary Key,
    Latitude    varchar(30),
    Longitude   varchar(30),
    Categories  varchar(50),
    Items_Price varchar(100),
    Shop_Name varchar(100))'''

    #defing query string for creating online status table
    querystr3='''CREATE TABLE IF NOT EXISTS Online_Status
    (Unique_ID bigint(32) Primary Key,
    Online_Status int(1))'''


    #executing queries
    cursor.execute(querystr1)
    cursor.execute(querystr2)
    cursor.execute(querystr3)

    #saving changes
    mycon.commit()

mysqlconnection()

