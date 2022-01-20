from flask import Flask, render_template, request, redirect,  url_for
import db
import emailer
import logger

app = Flask(__name__)


sports = ["Cricket", "Football", "Basketball", "Tennis"]

# -----------------------------------import call functions


def add_user(first_name, last_name, user_email, sprt):
    connection = db.connect()
    db.create_table(connection)
    db.add_user(connection, first_name, last_name, user_email, sprt)


def remove_user(first_name, last_name):
    connection = db.connect()
    db.drop_user_name(connection, first_name, last_name)


def list_all_users():
    connection = db.connect()
    db.get_all(connection)


def send_email(user_email):
    subject = "Registration Successful"
    emailer.temp_1(user_email, subject)

# -----------------------------------routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def register():
    fname = request.form.get("first_name")
    lname = request.form.get("last_name")
    user_email = request.form.get("email")
    sprt = request.form.get("sport")
    if not fname or not lname:
        return render_template("error.html")
    print(
        f"\n\n{fname} {lname}  signed up as  {user_email}  for  {sprt}\n\n")

# lets save the data in a txt file as a log file
    logger.write_log(fname, lname, user_email, sprt)
    add_user(fname, lname, user_email, sprt)
    send_email(user_email)
    return render_template("/result")




@app.route("/register", methods=["GET", "POST"])
def result():
    return render_template('register.html')


@app.route("/registrants")
def registrants():
    user_list = list_all_users()
    return render_template("registrants.html", reg=user_list)


if __name__ == "__main__":
    app.run()
