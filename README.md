# FOODPLAN
[Russian](RU_README.md)

## Site Demo



## Features

- Recipe Viewing: Users can view recipes.
- Favorite Recipes: Ability to favorite recipes by liking them.
- Meal Planning: Users can plan their meals for the week. A new menu is generated each day, consisting of breakfast, lunch, and dinner.
- User Accounts: User registration and authorization to save personal data.

## Installation
- Clone the repository:
```console

git clone https://github.com/Skripko-A/foodplan.git
```
- Create virtual environment and install dependencies with the command
```
pip install -r requirements.txt
```
- Create a `.env` file next to `manage.py` and fill in the following details:

    `SECRET_KEY` -
    Default: '' (empty string).
    The secret key for installing Django. It is used to provide cryptographic signatures and must have a unique value.

    django-admin startproject automatically adds a randomly generated SECRET_KEY to every new project.
    `DEBUG` -
    One of the main features of debug mode is the display of detailed error pages. If your application raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all currently defined Django settings (from settings.py)
    `ALLOWED_HOSTS` -
    Default: [] (empty list).
    A list of strings representing the hostnames/domains this Django site can serve. This is a security measure to prevent HTTP host header attacks, which are possible even with many seemingly secure web server configurations.

- Run migrations:
```
python manage.py migrate
```
- Create a superuser to work with the admin panel:
```
python manage.py createsuperuser
```
- Run the server with the command:
```
python manage.py runserver
```
The site will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Project goal
Team project on the online course for web developers [dvmn.org](https://dvmn.org/).
--- 
Worked on the project: 
* [Gulfia Vakhlakova](https://github.com/Gulfia83) 
* [Alexander Skripko](https://github.com/Skripko-A)