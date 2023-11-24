import psycopg2

from config import host, user, password, db_name


def insert_db(ip, port):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            # print(f"Server version: {cursor.fetchone()}")
            # print(sqlalchemy.__version__  )

    # # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE openproxy (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             ip_address INET NOT NULL,
    #             port_address INET NOT NULL,
    #             UNIQUE(ip_address)
    #             );"""
    #     )
    #     print("[INFO] Table created successfully")

        # insert data into a table
        with connection.cursor() as cursor:
            cursor.execute(
                "insert into openproxy (ip_address, port_address) values(%s, %s)", (ip, port))

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


if __name__ == '__main__':

    insert_db()
