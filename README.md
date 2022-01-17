# [ATREIDES] Flask-registration-app
Flask registration project.

To run type in terminal - flask run 


if that doesn't work try - python -m flask run

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
- Adding user-login system (using password hashing for security)  [Implementing]
- ^ cont.d, Add user password reset / recovery system.
- Adding page for user to deregister (and then send email to confirm deregistration)  [Implementing]
- Adding page to see all listed players for all sport(s).  [Added]
- Adding Index page [Added]

### Screenshots:
![image](https://user-images.githubusercontent.com/81807980/149794399-ba00725d-29c7-4cee-991c-5e6c24710ad8.png)
![image](https://user-images.githubusercontent.com/81807980/149794551-d1b60408-5f68-48b6-ada1-2dd85c6b986a.png)


![image](https://user-images.githubusercontent.com/81807980/149508042-60680256-1c32-4805-9fa4-e6417c323e44.png)
![image](https://user-images.githubusercontent.com/81807980/149794829-2cc4452e-4ff2-4d86-903a-192c076790ce.png)

![image](https://user-images.githubusercontent.com/81807980/149503416-174a3e3e-39d4-4bba-ba46-8dd79c8fd092.png)
![image](https://user-images.githubusercontent.com/81807980/149794929-be49ff99-9e86-4804-a310-5d75457106da.png)
![image](https://user-images.githubusercontent.com/81807980/149502154-610b664f-cce1-4547-bfc1-198a02b7e973.png)
![image](https://user-images.githubusercontent.com/81807980/149795777-ac8f5491-6e1a-4787-a111-0c6fef0c499b.png)


