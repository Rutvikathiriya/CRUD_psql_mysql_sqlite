# -*- coding : utf-8 -*-
import sys
import db_query 


def crud_sqlite(con):
    print "1.Create"
    print "2.Delete"
    print "3.Retrive"
    print "4.Insert"
    print "5.Update"
    print "6.Exit"
    user = raw_input("Enter your choice : ")
    if user == "1":
        db_query.create_table_sqlite(con)
        crud_sqlite(con)
    elif user == "2":
        db_query.delete_sqlite(con)
        crud_sqlite(con)
    elif user == "3":
        db_query.retrive_data_sqlite(con)
        crud_sqlite(con)
    elif user == "4":
        db_query.insert_sqlite(con)
        crud_sqlite(con)
    elif user == "5":
        db_query.update_sqlite(con)
        crud_sqlite(con)
    elif user == "6":
        exit()

def crud_mysql(con):
    print "-----------------------"
    print "1.Create"
    print "2.Retrive"
    print "3.Insert"
    print "4.Delete"
    print "5.Update"
    print "6.Exit"
    print "-----------------------"
    user = raw_input("Enter your choice : ")

    if user == "1":
        db_query.create_table_mysql(con)
        crud_mysql(con)
    elif user == "2":
        db_query.retrive_data_mysql(con)
        crud_mysql(con)
    elif user == "3":
        db_query.insert_data_mysql(con)
        crud_mysql(con)
    elif user == "4":
        db_query.delete_data_mysql(con)
        crud_mysql(con)
    elif user == "5":
        db_query.update_data_mysql(con)
        crud_mysql(con)
    elif user == "6":
        exit()



def crud_postgresql(con):

    print "-----------------------"
    print "1.Create"
    print "2.Retrive"
    print "3.Insert"
    print "4.Delete"
    print "5.Update"
    print "6.Exit"
    print "-----------------------"
    user = raw_input("Enter your choice?")

    if user == "1":
        db_query.create_table_post(con)
        crud_postgresql(con)
    elif user == "2":
        db_query.retrive_data_post(con)
        crud_postgresql(con)
    elif user == "3":
        db_query.insert_data_post(con)
        crud_postgresql(con)
    elif user == "4":
        db_query.delete_data_post(con)
        crud_postgresql(con)
    elif user == "5":
        db_query.update_data_post(con)
        crud_postgresql(con)
    elif user == "6":
        exit()

def choice():
    print "---------------"
    print "1.Sqlite"
    print "2.Mysql"
    print "3.Postgresql"
    print "4.Exit"
    print "---------------"

    user = raw_input("Enter your choice : ")

    if user == "1":
        con = db_query.db_config.connection_sqlite()
        crud_sqlite(con)
    elif user == "2":
        con = db_query.db_config.connection_mysql()
        crud_mysql(con)
    elif user == "3":
        con = db_query.db_config.connection_postgresql()
        crud_postgresql(con)
    elif user == "4":
        exit()

choice()