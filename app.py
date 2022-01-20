
from flask import Flask, render_template, request, redirect,  url_for
import re
import db
import emailer
import logger
import pyhash

app = Flask(__name__)

name = "Rohan"
sports = ["Cricket", "Football", "Basketball", "Tennis"]

# ----------------------------------- functions


def checker(first_name, last_name, user_email, sprt):
    flag = True
    if sprt not in sports:
        flag = False

    if not first_name or re.search("^\s*$", first_name):
        # String is either None or Empty or contain spaces only
        flag = False

    if not last_name or re.search("^\s*$", last_name):
        flag = False

    if not user_email or re.search("^\s*$", user_email):
        flag = False

    return flag


def add_user(first_name, last_name, user_email, sprt, password):
    pyhash.make_hash(first_name, last_name, user_email, sprt, password)


def if_exists(email):
    # returns true if doesnt exists
    connection = db.connect()
    print(str(db.if_exists(connection, email)))
    return (db.if_exists(connection, email))


def remove_user(first_name, user_email):
    connection = db.connect()
    db.drop_user_name(connection, first_name, user_email)


def list_all_users():
    connection = db.connect()
    return db.get_all(connection)


def send_reg_email(user_email):
    subject = "Registration Successful"
    emailer.sendmail(user_email, subject, 1)


def send_dereg_email(user_email):
    subject = "You have Deregistered"
    emailer.sendmail(user_email, subject, 2)


# -----------------------------------routes


@ app.route("/")
def index():
    return render_template("index.html")


@ app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@ app.route("/deregister", methods=["POST"])
def deregister():
    fname = request.form.get("first_name")
    lname = request.form.get("last_name")
    if id:
        remove_user()


@ app.route("/result", methods=["POST"])
def result():
    if request.method == 'POST':

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        user_email = request.form.get("email")
        sprt = request.form.get("sport")
        password = request.form.get("password")

        # checker () to verify user details
        if (checker(first_name, last_name, user_email, sprt)):
            # returns false if bad input
            # returns true if all good
            if(if_exists(user_email)):
                # checks if user already exists
                print(
                    f"\n\n{first_name} {last_name}  signed up as  {user_email}  for  {sprt}\n\n")
                logger.write_log(first_name, last_name, user_email, sprt)
                add_user(first_name, last_name, user_email, sprt, password)
                # send_reg_email(user_email)
                return render_template('result.html')
            else:
                try:
                    return render_template('register.html')
                except sqlite3.IntegrityError:
                    return render_template('register.html')

        return render_template('error.html')
    return render_template('error.html')


@ app.route("/registrants")
def registrants():
    user_list = list_all_users()
    # the error for noneType was due to list_all_user() func didnt return a list back here.
    # print(user_list)
    return render_template("registrants.html", user_list=user_list)


@ app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@ app.route("/profile", methods=["POST"])
def profile():
    if request.method == 'POST':

        user_email = request.form.get("email")
        password = request.form.get("password")
        if(if_exists(user_email)):

            # 1
            if(pyhash.check_hash(user_email, password)):
                print(
                    f"\n\n{user_email}  logged in \n\n")
                return render_template('/profile.html')
        error = "Invalid Username/Password"
        return render_template('login.html', error=error)
    error = "Invalid Username/Password"
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
