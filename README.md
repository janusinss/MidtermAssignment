############# Setup Instructions ############

        NOTE: 
        The `py` command is a Python shortcut mainly used on Windows.  
        For better cross-platform compatibility, it's recommended to use `python` instead.
        If you're working with forms, always include {% csrf_token %} to prevent security issues.

############ INSTALL ############

        Install `pipenv`:  
        - `pip install pipenv`
        Install Django inside the virtual environment:  
        - `pipenv install django`

############ CREATING DJANGO PROJECT AND APP  ############

        Create a new Django project:  
        - `django-admin startproject SMSProject`
        Navigate into the project directory:  
        - `cd C:\xampp\htdocs\StudentManagementSystem\SMSProject`
        Create a new Django app:  
        - `python manage.py startapp SMSApp`  
        Run the development server:  
        - `python manage.py runserver`

############ INSTALL AND CONFIGURE MYSQL ############

        Activate the virtual environment:  
        - `pipenv shell`
        Navigate into the project directory:  
        - `cd C:\xampp\htdocs\StudentManagementSystem\SMSProject`
        Install the `mysqlclient` library:  
        - `pipenv install mysqlclient`
        Create a new MySQL database (e.g., using phpMyAdmin).

############## Configure database,apps settings in `settings.py`: ############

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'nameofthedatabase',  # Replace with your actual database name
                'USER': 'root',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'SMSApp.apps.SmsappConfig' # Replace with your app's settings (apps.py)
        ]

############## CREATE AND APPLY DATABASE MIGRATION ############

        Create database migrations:  
        - `python manage.py makemigrations`
        Apply database migrations:  
        - `python manage.py migrate`

############## Static and Templates ############

Folder Structure

    SMSProject/  
    │-- SMSApp/     # Main App directory
    │   │-- static/  
    │   │   ├── styles/  
    │   │   │   ├── editStyles.css  
    │   │   │   ├── indexStyles.css  
    │   │   ├── js/  
    │   │   │   ├── scripts.js  
    │   │-- templates/  
    │   │   ├── temp/  
    │   │   │   ├── editPage.html  
    │   │   │   ├── index.html  
    │-- SMSProject/  # Main Project directory  
    │-- manage.py  

Modify settings.py to ensure Django recognizes your custom static folder:

    import os  # Ensure 'os' is imported at the top

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'SMSApp', 'static'),
    ]

In every HTML file that needs static assets, add this at the top:

    {% load static %}

How to Use Static Files in HTML

    <link rel="stylesheet" href="{% static 'styles/indexStyles.css' %}">
    <script src="{% static 'js/scripts.js' %}"></script>
