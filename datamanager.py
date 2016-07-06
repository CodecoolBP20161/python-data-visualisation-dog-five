import psycopg2
import getpass
import os


class DataManager:
    '''Handles all of the database related methods'''
    def __init__(self):
        if self.check_dsn_txt():
            self.get_dsn()
        else:
            # if login.txt doesn't exist yet, saves the data source name (dsn) into a .txt file based on user input
            dbname = input("Database name: ")
            user = input("User name: ")
            host = input("Host: ")
            password = getpass.getpass()
            dsn = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
            with open("login.txt", "w") as myfile:
                myfile.write(str(dsn))
                print("Login file is created")
            self.get_dsn()

    @staticmethod
    def check_dsn_txt():
        return os.path.isfile('./login.txt')

    def get_dsn(self):
        # retrieves the string of the dsn from login.txt
        with open("login.txt", "r") as myfile:
            self.dsn = str(myfile.readline())

    def connect(self):
        # opens connection between the program and the database server
        self.connection = psycopg2.connect(self.dsn)
        return self.connection

    def create_tables(self, query):
        # query for creating the main tables in the database
        self.connect()
        with self.connection as conn:
            with conn.cursor() as curs:
                curs.execute(open(query, "r").read())
                # print('Tables created in database.')
        conn.close()

    def run_query(self, query):
        # runs queries
        self.connect()
        with self.connection as conn:
            with conn.cursor() as curs:
                curs.execute(open(query, "r").read())
                self.data = list(curs.fetchall())
                # for row in self.data:
                #     print(row)
        conn.close()
        return self.data

# manager = DataManager()
# manager.create_tables('base_data.sql')
# manager.run_query('project-names.sql')
