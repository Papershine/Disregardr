import sqlite3
import globalvars

from sqlite3 import Error


def add_scanned(post_id):
    sql_insert_scanned_table = "INSERT INTO scanned(post_id) VALUES(%d);" % post_id
    try:
        c = globalvars.conn.cursor()
        c.execute(sql_insert_scanned_table)
        globalvars.conn.commit()
        print("[DataService] post inserted into list")
        c.close()
    except Error as e:
        print(e)


def is_scanned(post_id):
    sql_search_scanned = "SELECT EXISTS(SELECT 1 FROM scanned WHERE post_id=%d)" % post_id
    try:
        c = globalvars.conn.cursor()
        if c.fetchone():
            print("[DataService] post id found")
            return True
        else:
            print("[DataService] post id not found")
            return False
    except Error as e:
        print(e)
    return False


# noinspection SqlNoDataSourceInspection
def init():
    globalvars.conn = connect()
    sql_create_scanned_table = """ CREATE TABLE IF NOT EXISTS scanned (post_id integer PRIMARY KEY); """

    try:
        c = globalvars.conn.cursor()
        c.execute(sql_create_scanned_table)
    except Error as e:
        print(e)


def connect():
    conn = None
    try:
        conn = sqlite3.connect('')
        print("[DataService] database connected")
        return conn
    except Error as e:
        print(e)

    return conn


def close():
    globalvars.conn.close()
