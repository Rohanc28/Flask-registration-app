from flask import Flask, render_template, request, redirect,  url_for
import db
import emailer
import logger

app = Flask(__name__)

name = "Rohan"
sports = ["Cricket", "Football", "Basketball", "Tennis"]


def add_to_database(first_name, last_name, user_email, sprt):
    connection = db.connect()
    db.create_table(connection)
    db.add_user(connection, first_name, last_name, user_email, sprt)


def send_email(user_email):

    subject = "Registration Successful"
    emailer.temp_1(user_email, subject)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")


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
        add_to_database(first_name, last_name, user_email, sprt)
        send_email(user_email)
        return render_template('result.html')

    return render_template('error.html')


if __name__ == "__main__":
    app.run()
