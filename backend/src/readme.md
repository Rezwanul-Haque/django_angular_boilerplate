# Instruction
As we are using sqlite3 database for this example app and we are going to use sqlite3 command shell tool so 
sqlite3.exe must me in the src folder so that we can load dummy data using sqlite3 command line tool

### Running sqlite3 command line tool
```
python manage.py dbshell
```
## Showing table in sqlite3
```
.table
```
## Clear shell screen
```
.shell cls
```
## Schema of a table
```
.schema auth_user
```
## Loading the database from a file
```
.read schedules.sql
```
## Showing data in the command line tool
```
.mode column
.header on
SELECT * FROM flights_schedule
```

## Quite the sqlite command tool
```
.exit
```