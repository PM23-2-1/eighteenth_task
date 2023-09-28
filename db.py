import pymysql.cursors
import pandas as pd

import env
import db_names

class Databases():
    def get_databases(self):
        try:
            conn = pymysql.connect(host='localhost',
                                    user=env.USER,
                                    password=env.PASSWORD,
                                    cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES")
            return cursor.fetchall()
        except pymysql.err.MySQLError as e:
            return None
        
    def create_database(self, ):
        try:
            conn = pymysql.connect(host='localhost',
                                    user=env.USER,
                                    password=env.PASSWORD,
                                    cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            name = db_names.DB_names()
            cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % name.get_name())
            return True
        except pymysql.err.MySQLError:
            return None
        
class tables_in_db():
    def get_tables(self):
        try:
            name = db_names.DB_names()
            conn = pymysql.connect(host='localhost',
                                    user=env.USER,
                                    password=env.PASSWORD,
                                    database=name.get_name(),
                                    cursorclass=pymysql.cursors.DictCursor)
            new_df = pd.read_sql("SELECT * FROM " + name.get_name_table(), conn)
            return new_df
        except pymysql.err.MySQLError as e:
            return None

def check_db() -> None:
    try:
        conn = pymysql.connect(host='localhost',
                                user=env.USER,
                                password=env.PASSWORD,
                                cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % DB_Names.db_names.get_name())
    except pymysql.err.ProgrammingError as e:
        print(e)

    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=DB_Names.db_names.get_name(),
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    print("База данных подключена")

    with open('create_structure.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.execute(sql_script % DB_Names.db_names.get_name_table())
        conn.commit()
        print("Скрипт SQL успешно выполнен")
    return

def save_result(operation, result):
    try:
        conn = pymysql.connect(host='localhost',
                                user=env.USER,
                                password=env.PASSWORD,
                                database=DB_Names.db_names.get_name(),
                                cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO " + DB_Names.db_names.get_name_table() + f" (operat, result) VALUES (%s, %s)", (operation, str(result)))
        conn.commit()
    except pymysql.err.DataError as e:
        print('Ошибка с данными:', e)
    except pymysql.err.DatabaseError as e:
        print(e)
    return

def save_db_to_xlxs():
    try:
        conn = pymysql.connect(host='localhost',
                                user=env.USER,
                                password=env.PASSWORD,
                                database=DB_Names.db_names.get_name(),
                                cursorclass=pymysql.cursors.DictCursor)
        new_df = pd.read_sql("SELECT * FROM " + DB_Names.db_names.get_name_table(), conn)
        new_df.to_excel("out.xlsx")
    except pymysql.err.DatabaseError as e:
        print(e)
    return

def print_db():
    try:
        conn = pymysql.connect(host='localhost',
                                user=env.USER,
                                password=env.PASSWORD,
                                database=DB_Names.db_names.get_name(),
                                cursorclass=pymysql.cursors.DictCursor)
        new_df = pd.read_sql("SELECT * FROM " + DB_Names.db_names.get_name_table(), conn)
        print(new_df)
    except pymysql.err.DatabaseError as e:
        print(e)
    return