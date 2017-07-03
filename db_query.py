# -*- coding : utf-8 -*-

import db_config 
import MySQLdb as mdb
import sqlite3
import psycopg2
import sys
import warnings

def create_table_mysql(con):
        try:
            cur = con.cursor()
            #cur.execute("DROP TABLE IF EXISTS student")
            cur.execute("CREATE TABLE student(Id INT PRIMARY KEY AUTO_INCREMENT,Firstname VARCHAR(10),City VARCHAR(20));")
        except Exception as e:
            print "Table is created"


def retrive_data_mysql(con): 
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM student")

        for i in range(cur.rowcount):
            row = cur.fetchone()
            print row["Id"], row["Firstname"], row["City"]

def insert_data_mysql(con):
        try:
            cur = con.cursor()
            Id = 0
            Firstname = raw_input("Enter Your First Name ")
            City = raw_input("Enter Your City")
            cur.execute("INSERT INTO student VALUES (%s, %s, %s)",(Id, Firstname, City))
            print "Record Inserted"
        except mdb.Warning, e:
            pass

def update_data_mysql(con):
        firstname = raw_input('enter updated name:')
        id = raw_input('enter id where u can update ur name:')
        city = raw_input('enter city to update:')

        cur = con.cursor()
        cur.execute("UPDATE student SET Firstname = %s, City = %s  WHERE Id = %s",
                    (firstname, city, id))
        print "Number of rows updated:", cur.rowcount

def delete_data_mysql(con):
        id = raw_input('enter a id to delete:')
        cur = con.cursor()
        cur.execute("DELETE FROM student WHERE Id = %s" % (id))
        print "Delete a row"


#*----------------------------------------------------------------------------------------

def create_table_sqlite(con):
    try:
        cur.execute('''
        CREATE TABLE student (name TEXT, phone TEXT, country TEXT)''')
    except Exception as e:
        print "Table is created"

def insert_sqlite(con):
    cur = con.cursor()
    name1 = raw_input("name :")
    phone1 = raw_input("phone :")
    country1 = raw_input("country:")

    cur.execute("INSERT INTO student(name, phone, country)VALUES(?,?,?)", (name1,phone1,country1))
    print('User inserted query')

def retrive_data_sqlite(con):
    cur = con.cursor()
    cur.execute("SELECT name,phone,country FROM student")
    rows = cur.fetchall()
    if len(rows) == 0:
        print "No records found"
    else:
        print rows

def delete_sqlite(con):
    cur = con.cursor()
    name = str(raw_input('Please enter name to del:'))
    cur.execute('''DELETE FROM student WHERE name = ? ''',(name,))
    print "The record which contains name = %s is deleted" % name

def update_sqlite(con):
    cur = con.cursor()
    name = raw_input('enter name for update :')
    phone = raw_input('enter phone num where updated record')
    cur.execute('''UPDATE student SET name = ? WHERE phone = ? ''',
     (name,phone))
    print ("Your record is update")

#-------------------------------------------------------------------------


def create_table_post(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Emp")
        cur.execute(
            "CREATE TABLE Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25));")
        print 'Employee Table created'

def insert_data_post(con):
    with con:

        try:
            cur = con.cursor()
            Name = raw_input("Enter Your Name ")
            Company_Name = raw_input("Enter Your Company Name")
            Designation = raw_input("Enter Your Designation")
            cur.execute("INSERT INTO Emp  (Name, Company_Name, Designation) VALUES(%s, %s, %s )",
                        (Name, Company_Name, Designation))
            print "Record Inserted"
            con.commit()
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrive_data_post(con):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Emp")

        rows = cur.fetchall()
        for row in rows:
            if rows == None:
                print 'Table is Empty'
                break
            else:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3}'.format(
                    row[0], row[1], row[2], row[3]))

def update_data_post(con):
    with con:

        try:
            cur = con.cursor()
            #cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3}'.format(
                    row[0], row[1], row[2], row[3]))

            e_id = input("Enter id You want to update")
            name = raw_input("Enter Name for Update Record")
            cname = raw_input("Enter Company Name for Update Record")
            deg = raw_input("Enter Designation for Update Record")

            cur.execute("UPDATE Emp SET name =%s, Company_Name = %s, Designation = %s WHERE Id = %s",
                        (name, cname, deg, e_id))

            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

def delete_data_post(con):
    with con:
        try:
            cur = con.cursor()
            #cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} '.format(
                    row[0], row[1], row[2], row[3]))

            id = raw_input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Emp WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist'