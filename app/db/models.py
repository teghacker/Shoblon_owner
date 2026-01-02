from sqlite3 import *


def Creat_Users():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE Users(
        id INTEGER PRIMARY KEY,
        User_id INTEGER,
        username TEXT);''')

        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()




def Creat_Admins():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE Admins(
        id INTEGER PRIMARY KEY,
        Admin_id INTEGER);''')
        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()


def Creat_Channels():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE Channels(
        id INTEGER PRIMARY KEY,
        name TEXT);''')
        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()







# Creat_Users()
# Creat_Admins()
# Creat_Channels()




