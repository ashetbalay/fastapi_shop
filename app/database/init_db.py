import psycopg2
import config

connection = psycopg2.connect(user=config.USER, password=config.PASSWORD)
cursor = connection.cursor()
connection.autocommit = True
create_database_sql = f"CREATE DATABASE {config.DATABASE}"

try:
    cursor.execute(create_database_sql)
except psycopg2.errors.DuplicateDatabase:
    pass

cursor.close()
connection.close()
