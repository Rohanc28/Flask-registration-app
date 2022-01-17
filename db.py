import sqlite3

# queries
create_new_table = "CREATE TABLE IF NOT EXISTS registrants (id INTEGER PRIMARY KEY, first_name  TEXT, last_name TEXT, email TEXT, sport TEXT);"
insert_user = "INSERT INTO registrants (first_name, last_name, email, sport) VALUES(?,?,?,?) ;"
get_all_users = "SELECT first_name,last_name,email,sport FROM registrants;"
get_user = "SELECT * FROM registrants WHERE first_name LIKE ? AND last_name LIKE ?;"
get_sport = "SELECT DISTINCT * FROM registrants WHERE sport = ?;"
drop_user = "DELETE FROM registrants WHERE first_name Like ? AND last_name LIKE ?;"


def connect():
    return sqlite3.connect("data.db")


def create_table(connection):
    with connection:
        connection.execute(create_new_table)


def add_user(connection, first_name, last_name, email, sport):
    with connection:
        return connection.execute(insert_user, [
            first_name, last_name, email, sport])


def get_all(connection):
    with connection:
        return connection.execute(get_all_users).fetchall()


def get_name(connection, first_name):
    with connection:
        return connection.execute(get_user, [first_name]).fetchall()

#get_user = "SELECT * FROM registrants WHERE first_name AND last_name = ?,?;"


def get_user_name(connection, first_name, last_name):
    with connection:
        return connection.execute(get_user, [first_name, last_name]).fetchall()
# DELETE FROM registrants WHERE first_name = ?;"


def drop_user_name(connection, first_name, last_name):
    with connection:
        connection.execute(drop_user, [first_name, last_name])


def sport_list(connection, sport):
    with connection:
        return connection.execute(get_sport, [sport]).fetchall()


#alter = "DESCRIBE registrants;"
#connection = connect()
# with connection:
#    print(connection.execeute(alter).fetchall())
