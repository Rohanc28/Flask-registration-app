import email
import bcrypt
import random
from datetime import datetime
import db

# register - hash password and insert db


def make_hash(fname, lname, user_email, sport, password):
    p = password.encode('utf-8')
    hash = bcrypt.hashpw(p, bcrypt.gensalt())
    # print(hash)
    #
    connection = db.connect()
    db.create_table(connection)
    db.add_user(connection, fname, lname, user_email, sport, hash)
    print("Row added.")

# login - match hash


def check_hash(user_email, password):
    #
    connection = db.connect()
    # do implement db and add values
    hash = db.get_pass(connection, user_email)
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False

# reset - hash new password and insert db


def reset_hash(user_email, password):
    connection = db.connect()
    chek = db.get_pass(connection, user_email)
    if bcrypt.checkpw(password, chek):
        # password should not be same as old password
        return False
    #
    p = password.encode('utf-8')
    hash = bcrypt.hashpw(p, bcrypt.gensalt())
    #
    db.reset_pass(connection, user_email, hash)
    return True


#fname = "Rohan"
#lname = "chat"
#user_email = "bro@g.com"
#sport = "Cricket"
#password = "Rohan123@"
#make_hash(fname, lname, user_email, sport, password)
