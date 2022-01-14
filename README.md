# Flask-registration-app
Flask registration project.

To run type in terminal - flask run 


if that doesn't work try - python -m flask run

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
- Adding unique user only (remove duplicates of same person) from database.
- Adding page for user to deregister (and then send email to confirm deregistration)
- Adding page to see all listed players for a/all sport(s).
- Improving CSS for all pages
- reducing file sizes for web-pages.
- prevent SQLi (SQL injection from user)
