# Splitwise Clone
A CLI app that simulates the features of the mobile app 'Splitwise'

## Contributors
- Adolfo, John Kenneth
- Ramos, Quim Zyrell
- Santos, Jimwell
- Salazar, Ian

## Dependencies
- pip
- pipenv
- mysql-python-connector

## Pre-requisites
1. Must have `mariadb` or `mysql` installed on your local machine
2. Create the tables and seed the database by using the SQL query dumps provided
3. Create a copy of the .env.copy file to ".env" file, then populate the fields

## How to run
1. You must have python3 and pipenv installed
2. After that, open up your terminal. Make sure you're in the directory with the source code (you should've `cd'd` to the source code by now)
3. Install the libraries needed by running `pipenv install` or `python3 -m pipenv install`
4. After installing the packages, open up a new shell environment with the installed libraries by running `pipenv shell` or `python3 -m pipenv shell`
5. Lastly, run the cli by running `python3 cli.py`
