import sqlite3

# queries
create_new_table = "CREATE TABLE IF NOT EXISTS registrants (id INTEGER PRIMARY KEY, first_name  TEXT, last_name TEXT, email TEXT, sport TEXT, password TEXT, CONSTRAINT mail_unique UNIQUE(email));"
insert_user = "INSERT OR IGNORE INTO registrants (first_name, last_name, email, sport, password) VALUES(?,?,?,?,?) ;"
get_all_users = "SELECT first_name,last_name,email,sport FROM registrants;"
get_user = "SELECT * FROM registrants WHERE email= ?;"
get_sport = "SELECT DISTINCT * FROM registrants WHERE sport = ?;"
get_mail = "SELECT DISTINCT password FROM registrants WHERE email = ?;"
drop_user = "DELETE FROM registrants WHERE email = ?;"
update_pass = "UPDATE registrants SET password = ? WHERE email = ?;"
check_exist = "SELECT COUNT(*) FROM old_registrants WHERE (email = ?) ;"


def connect():
    return sqlite3.connect("data.db")


def create_table(connection):
    with connection:
        connection.execute(create_new_table)


def add_user(connection, first_name, last_name, email, sport, password):
    with connection:
        connection.execute(insert_user, [
            first_name, last_name, email, sport, password])


def get_all(connection):
    with connection:
        return connection.execute(get_all_users).fetchall()


def get_pass(connection, email):
    with connection:
        return connection.execute(get_mail, [email]).fetchall()


def reset_pass(connection, email, password):
    with connection:
        connection.execute(update_pass, [password, email])


def get_username(connection, email):
    with connection:
        return connection.execute(get_user, [email]).fetchall()


def drop_user_name(connection, email):
    with connection:
        connection.execute(drop_user, [email])


def sport_list(connection, sport):
    with connection:
        return connection.execute(get_sport, [sport]).fetchall()


def if_exists(connection, email):
    with connection:
        a = connection.execute(check_exist, [email]).fetchall()
        if a == [(0,)]:  # == "[(0,)]":
            return True
        else:
            return False
    # if it returns >0 then it exists.
