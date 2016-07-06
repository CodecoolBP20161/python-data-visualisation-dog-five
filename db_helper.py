import psycopg2
import getpass
import os

schema = 'base_data.sql'
dsn_file = 'login.txt'
first = 'project-names.sql'
def write_dsn_in_file():
    dbname = input("Database name: ")
    user = input("User name: ")
    host = input("Host: ")
    password = getpass.getpass()
    dsn = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
    with open(dsn_file, "w") as myfile:
        myfile.write(str(dsn))
        print("Login file is created")
def get_dsn_from_file():
    with open(dsn_file, "r") as myfile:
        dsn = str(myfile.readline())
    return dsn
def delete_dsn():
    open(dsn_file, "w")
    os.remove("login.txt")
    print("Login file deleted.")
def create_tables(schema):
    dsn = get_dsn_from_file()
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as curs:
            curs.execute(open(schema, "r").read())
            rows = curs.fetchall()
            return rows
        print('Tables created in database.')
    conn.close()
write_dsn_in_file()
create_tables(first)
# delete_dsn()