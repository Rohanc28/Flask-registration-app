import os
import random
from datetime import datetime
from datetime import date


def write_log(fname, lname, email, sport, file="log_1.txt"):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    today = date.today()
    f = open(str(file), 'a')
    f.write(f"\n{fname} {lname} {email} {sport} | {time} {today}")
    f.close()


def read_log(file="log_1.txt"):
    f = open(file, 'r')
    print(f.readlines())
    f.close()
# def clear_log():

# def create_log():


#write_log("Rohan", "Chaturvedi", "brohxnc@gmail.com", "Cricket", "log_1.txt")
# read_log()
