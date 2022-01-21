# [ATREIDES] Flask-registration-app
Flask registration project.

### How to run
Download the repo and pip install these libraries (if you have not installed them before)

- sqlite3 (for database management)
- bcrypt (for password-hashing function)
- flask 
- smtplib (to send email to "user" on registration/deregistration )

Now you can open terminal and run the app by
```
flask run
```

OR 

```
python -m flask run
```


### Emailer.py error:
( Please do not use your work, main account for this),


Have a side account preferably gmail. Remove Phone sign-in, 2-Step Verify from the email you will be sending email as. Turn on Less Secure app access, can be found under Google>myaccount.google.com>security.


Go to emailer.py and add EMAIL_ADDRESS = 'your_email' and EMAIL_PASSWORD = 'your email password' and it should work.


## Contents
- templates - contains all html pages and stylesheets. (still developing)
- app.py - main flask app. to run.
- data.db - SQLite3 database of registrants 
- database_text - python program to add, find user, find user of 'sport', return list of all user, deregister user (Only used to check/edit database, to be ignored)
- db.py - python file to import that contains all the queries to execeute to database.
- emailer.py - python script that sends pre-templated html email (registration success or deregistration success) to given user. 
- log_1.txt - simple text file that logs time, date each time new user successfully registers  (only for debug use, to be ignored)
- logger.py - python program that appends, reads log file (only for debug use, to be ignored )
- tester.py - program to test, debug other programs, scripts (only for debug use, to be ignored)

## Next updates (coming)
- Adding user-login system (using password hashing for security)  [Added]
- Profile page for user  [Added]
- Adding page for user to deregister (and then send email to confirm deregistration)  [Done]
- Adding page to see all listed players for all sport(s).  [Added]
- Adding Index page [Added]
- Reduce HTML file size [Done]
- Uniform CSS theme for all pages [Done]

### Screenshots:
![image](https://user-images.githubusercontent.com/81807980/150361917-640f4912-7820-4773-a084-52c1da436cc3.png)
![image](https://user-images.githubusercontent.com/81807980/150362056-7e33f9b2-9e1d-4f35-a3a2-9615a43fb0f1.png)

![image](https://user-images.githubusercontent.com/81807980/150362135-55edfb58-18b6-4cb4-a51c-51445cad4290.png)


![image](https://user-images.githubusercontent.com/81807980/150514739-c4b4ed16-687b-4e1d-9bc3-66031c409de8.png)

![image](https://user-images.githubusercontent.com/81807980/149794829-2cc4452e-4ff2-4d86-903a-192c076790ce.png)

![image](https://user-images.githubusercontent.com/81807980/149503416-174a3e3e-39d4-4bba-ba46-8dd79c8fd092.png)

![image](https://user-images.githubusercontent.com/81807980/150362224-a96b84b3-f6e7-4db3-a018-8c070d24f589.png)


![image](https://user-images.githubusercontent.com/81807980/149502154-610b664f-cce1-4547-bfc1-198a02b7e973.png)
![image](https://user-images.githubusercontent.com/81807980/149795777-ac8f5491-6e1a-4787-a111-0c6fef0c499b.png)

![image](https://user-images.githubusercontent.com/81807980/150552327-2621f00a-12e0-414a-b638-f667183c8eec.png)

