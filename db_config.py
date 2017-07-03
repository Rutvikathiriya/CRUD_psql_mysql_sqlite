#!/usr/bin/python
# -*- coding : utf-8 -*-

import MySQLdb as mdb
import sqlite3
import psycopg2

def connection_sqlite():
    try:
        con = sqlite3.connect('mydb.db')
        cur = con.cursor()
        print "database mydb successfully created"
        print(sqlite3.version)
        return con

    except sqlite3.Error as e:
        print(e)

def connection_mysql():
    try:
        con = mdb.connect('localhost', 'root', 'Drc@1234', 'mydb');
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        ver = cur.fetchone()
        print "databse mydb created"
        print "mysql Database version : %s " % ver
        return con

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)


def connection_postgresql():
    try:
        con = psycopg2.connect(user="rutvi", password = "rutvi", database="mytestdb", host="localhost", port ="5432")
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver
        return con

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
