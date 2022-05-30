# ToDoList Django app
![Image alt](https://github.com/first-muchacho/ToDoList/raw/remake/img_for_readme.JPG)

## About project

A web app that lets you keep track of your to-do list.

Features of the project:

- user registration with email verification

- password reset via email

- user profile (where user can add or change info about him)

- create/change/view/delete task

- сompleted tasks are marked and crossed out

- search by task

## Deployment instructions
1. Create and activate a virtual environment
> python -m venv {name}

>{name}\Scripts\activate.bat
2. Copy repositoreies
 
Copy this repo in your root derictory (where you create and activate virtual env.)

3. Install requirements

> pip install -r requirements.txt

4. Launch preparation

> python manage.py collectstatic

> python manage.py mekamigrations

> python manage.py migrate

5. Launch a project

> python manage.py runserver

Check at http://127.0.0.1:8000/
