#insert user
#delete user
#current user?

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="databasepassword1",
    database="hisbooks_db",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

# store user info 

val = ''

while val != 'q':
    val = input("What do you want to do? i/d/q => input/delete/quit\n")
    if val == 'q':
        break
    elif val == 'i':
        user_id = input("Enter your id (has to be in form of ...@handong.edu): ")
        user_password = input("Enter your password: ")
        insertion_query = ("""
        insert into User_Info
        (user_id, password, phone_num, total_sells, complain_numbers) 
        values 
        (%s, %s, %s, %s, %s)
        """)
        cursor.execute(insertion_query, (user_id, user_password, '010', 0, 0, ))
    elif val == 'd':
        del_id = input("Enter id to delete\n")
        deletion_query = ("""
        DELETE FROM User_Info WHERE user_id = %s
        """)
        cursor.execute(deletion_query, (del_id,))


    else:
        print("invalid input")


query1 = ("use hisbooks_db;")
query2 = ("show tables ;")



db.commit()


