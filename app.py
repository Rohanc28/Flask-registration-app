from flask import Flask, render_template, request, redirect,  url_for
import db
import emailer
import logger

app = Flask(__name__)

name = "Rohan"
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
    return db.get_all(connection)


def send_reg_email(user_email):
    subject = "Registration Successful"
    emailer.sendmail(user_email, subject, 1)


def send_dereg_email(user_email):
    subject = "You have Deregistered"
    emailer.sendmail(user_email, subject, 2)
# -----------------------------------routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    return render_template("register.html")


@app.route("/deregister", methods=["POST"])
def deregister():
    fname = request.form.get("first_name")
    lname = request.form.get("last_name")
    if id:
        remove_user()


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        user_email = request.form.get("email")
        sprt = request.form.get("sport")
        if sprt == "Sport":
            return render_template('error.html')
        print(
            f"\n\n{first_name} {last_name}  signed up as  {user_email}  for  {sprt}\n\n")

# lets save the data in a txt file as a log file
        logger.write_log(first_name, last_name, user_email, sprt)
        add_user(first_name, last_name, user_email, sprt)
        send_reg_email(user_email)
        return render_template('result.html')

    return render_template('error.html')


@app.route("/registrants")
def registrants():
    user_list = list_all_users()

    # the error for noneType was due to list_all_user() func didnt return a list back here.
    # print(user_list)
    return render_template("registrants.html", user_list=user_list)


if __name__ == "__main__":
    app.run()
