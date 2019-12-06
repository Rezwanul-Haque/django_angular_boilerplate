# Please install virtualenv on your local computer
``` pip install virtualenv ```

### This is what I like do when creating a virtual environment (you can change whatever you like)
(I always like to called the virtual environment as venv)
# Creating virtual environment

``` virtualenv venv ```

``` cd venv ```

## For Windows
``` scripts\activate ```

## For Linux
``` source bin\activate ```

``` cd .. ```

## Installing requirements
``` cd backend ```
``` cd src ```

``` pip install -r requirements-dev.txt ```

### And for production environment

``` pip install -r requirements-prod.txt ```

# Custom management command
A management custom command added to rename project name and all the related places where changes must be done to run the project.
## For changing the project name run the following command.
``` python manage.py rename project_name ```

For security purpose this boilerplate's backend uses python-decouple to secure all sensitive variables like SECRECT_KEY, Production level database username, password etc to a secure file called .env

## A example of the .env file given as .env.example

### For local development you can rename the .env.example file to .env to run the project on local computer.

# goto frontend folder
```cd frontend```
# Install node pakages
```npm install```
# Compile VueJS App
```npm run build```
# goto backend folder
```cd backend/src```
# collect static files in public folder
```python manage.py collectstatic```
# start django server in localhost
```python manage.py runserver```

# Deploying
There are two instruction file(project folder) on how to deploy django projects on heroku and digital ocean (I am continuously updating these to file) and more like AWS and others will be added in the future.

# Core app
Django suggest if any custom command has to create for a project it should be on the core > management > command folder.
Like I created the rename command

# Lets talk about the settings of the project
src > mysite > settings
There are three file
1. base.py
2. developement.py
3. production.py

base.py file has contain things that both needed for both development and production settings.

# Development settings
Development settings included Django debug tools and which is helpful for debugging a Django project.

# Production settings
Production settings I configured Database to use PostgreSQL so to secure the database sensitive information like DB_NAME,  DB_USER, DB_PASSWORD etc I use the python-decouple module.

By default python-decouple check for .env file for sensitive information of the project.

### This .env file should not be push on the public repository. You can create variable on the hosting site so just created their will auto fetch value by python-decouple module.

Checkout the .env.example file to create a .env file

# Note .env.example file contain the Django project SECRET_KEY and it's just a 50 character long random number so you change it when you use this boilerplate.

# Final instruction
If anyone want to change the project to use the production settings just change one place only.

# Edit manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
to
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')
