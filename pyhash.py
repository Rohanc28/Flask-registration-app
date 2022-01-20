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
    hash = hash.decode('utf-8')
    r = db.add_user(connection, fname, lname, user_email, sport, hash)
    print(r)

# login - match hash


def check_hash(user_email, password):
    p = password.encode('utf-8')
    
    #
    connection = db.connect()
    # do implement db and add values
    hash = (str(db.get_pass(connection, user_email)))[3:-4]
    hhash = hash.encode('utf-8')

    if bcrypt.checkpw(p, hhash):
        print("Match")
        return True
    else:
        print("Not match")
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

