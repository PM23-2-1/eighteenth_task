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
            if name.get_name() != None:
                cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % name.get_name())
                return True
        except pymysql.err.MySQLError:
            return None
        
class Tables_in_db():
    def get_tables(self):
        try:
            name = db_names.DB_names()
            conn = pymysql.connect(host='localhost',
                                    user=env.USER,
                                    password=env.PASSWORD,
                                    database=name.get_name(),
                                    cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES;")
            return cursor.fetchall()
        except pymysql.err.MySQLError as e:
            return None
        
    def create_table(self,):
        try:
            name = db_names.DB_names()
            if name.get_name_table() != None:
                conn = pymysql.connect(host='localhost',
                                        user=env.USER,
                                        password=env.PASSWORD,
                                        database=name.get_name(),
                                        cursorclass=pymysql.cursors.DictCursor)
                cursor = conn.cursor()
                with open('create_structure.sql', 'r') as sql_file:
                    sql_script = sql_file.read()
                    cursor.execute(sql_script % name.get_name_table())
                    conn.commit()
                    return True
            return False
        except pymysql.err.MySQLError as e:
            print(e)
            return None
        
    def table_to_xlsx(self, ):
        name = db_names.DB_names()
        if name.get_name_table() != None:
            try:
                conn = pymysql.connect(host='localhost',
                                        user=env.USER,
                                        password=env.PASSWORD,
                                        database=name.get_name(),
                                        cursorclass=pymysql.cursors.DictCursor)
                new_df = pd.read_sql("SELECT * FROM " + name.get_name_table(), conn)
                new_df.to_excel("out.xlsx")
            except pymysql.err.DatabaseError as e:
                print(e)
        return
    
    def add_values_to_sql(self, date_import, department, type_of_furniture, price):
        name = db_names.DB_names()
        if name.get_name_table() != None:
            try:
                conn = pymysql.connect(host='localhost',
                                        user=env.USER,
                                        password=env.PASSWORD,
                                        database=name.get_name(),
                                        cursorclass=pymysql.cursors.DictCursor)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO " + name.get_name_table() + f" (date_import, department, type_of_furniture, price) VALUES (%s, %s, %s, %s)", (date_import, department, type_of_furniture, price))
                conn.commit()
                return True
            except pymysql.err.DatabaseError as e:
                print(e)
        return False
    
    def get_all_values(self, ):
        name = db_names.DB_names()
        if name.get_name_table() != None:
            try:
                conn = pymysql.connect(host='localhost',
                                        user=env.USER,
                                        password=env.PASSWORD,
                                        database=name.get_name(),
                                        cursorclass=pymysql.cursors.DictCursor)
                new_df = pd.read_sql("SELECT * FROM " + name.get_name_table(), conn)
                return new_df
            except pymysql.err.DatabaseError as e:
                print(e)
        return False