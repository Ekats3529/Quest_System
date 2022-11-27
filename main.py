import pymysql

from db import password, host, user, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#"*20)

    try:
        # cursor = connection.cursor()

        #create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `quests`(id int AUTO_INCREMENT," \
                                 " name varchar(32)," \
                                 " status varchar(32), PRIMARY KEY (id));"

            cursor.execute(create_table_query)
            print("Table created successfully")


    finally:
        connection.close()
except Exception as ex:
    print("Connection refused...")
    print(ex)
