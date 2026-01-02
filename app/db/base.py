from sqlite3 import *
import sqlite3


def ADD_Users(User_id, username):
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Users(User_id, username)  VALUES(?,?)""",(User_id, username))
        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()



def Read_Users():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute(f"select * from Users")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()

'-----------------------------------------------------------------------'


def ADD_Admins(User_id):
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Admins(Admin_id)  VALUES(?)""", (User_id,))
        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()


def Read_Admins():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute(f"select * from Admins")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()


def Delete_Admins(id):
    try:
        connection = sqlite3.connect("teg.db")
        cursor = connection.cursor()
        query = "DELETE FROM Admins WHERE Admin_id = ?"
        cursor.execute(query, (id,))
        connection.commit()
    except (Exception, sqlite3.Error) as error:
        print("Error 404 : ", error)
    finally:
        if connection:
            cursor.close()
            connection.close()



'-----------------------------------------------------------------------'


def ADD_Channels(name):
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Channels(name)  VALUES(?)""", (name,))
        connection.commit()
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()


def Read_Channels():
    try:
        connection = connect("teg.db")
        cursor = connection.cursor()
        cursor.execute(f"select * from Channels")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as eror:
        print("Error 404 : ", eror)
    finally:
        if connection:
            cursor.close()
            connection.close()


def Delete_Channels(id):
    try:
        connection = sqlite3.connect("teg.db")
        cursor = connection.cursor()
        query = "DELETE FROM Channels WHERE name = ?"
        cursor.execute(query, (id,))
        connection.commit()
    except (Exception, sqlite3.Error) as error:
        print("Error 404 : ", error)
    finally:
        if connection:
            cursor.close()
            connection.close()




