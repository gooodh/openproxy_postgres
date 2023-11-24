import psycopg2
import sqlalchemy
from config import host, user, password, db_name


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
        print(f"Server version: {cursor.fetchone()}")
        print(sqlalchemy.__version__  )

    # # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )
    #     print("[INFO] Table created successfully")

    # # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE openproxy (
    #             id serial primary key,
    #             ip_address INET NOT NULL,
    #             port_address INT NOT NULL,
    #             UNIQUE(ip_address)
    #             );"""
    #     )
    #     print("[INFO] Table created successfully")

    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO openproxy (ip_address, port_address) VALUES
    #         ('23.29.152.91', '8080');

    #         """
    #     )
    #     print("[INFO] Data was succefully inserted")

    #     # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM openproxy ;"""
    #     )

    #     print(cursor.fetchone())

#     # delete a table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """DROP TABLE openproxy;"""
#         )

#         print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
