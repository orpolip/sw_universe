def connect_to_db():
    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='localhost' password='{}'".format(
            config.db_name, config.user, config.password))
        conn.autocommit = True
    except psycopg2.Error:
        print("""Connection with database failed. You made a typo in your database name, username or password.
            You should check your config.py""")
        sys.exit(0)
    return conn


def create_registration_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
  ID serial,
  UserName varchar(255) NOT NULL,
  Password varchar(255) NOt Null,
  PRIMARY KEY (ID));""")