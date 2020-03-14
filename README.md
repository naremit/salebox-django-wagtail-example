This repo is a simple "cookiecutter" project template to create ecommerce websites powered by https://salebox.io, using Django, Wagtail CMS and django-allauth.

This repo is a starting point for your project, it is not a *one size fits all* ecommerce solution, however much we would like it to be.


### Getting started

1. Create and enter a python3 `virtualenv` environment
2. Clone this repo:

        git clone git@github.com:naremit/salebox-django-wagtail-example.git www

3. Remove the `.git` folder, as we are copying this repo, not altering it

        cd www
        rm -rf .git

4. Install the dependencies to your virtual enviroment

        pip install -r requirements.txt

5. Add your postgres databse settings to the `DATABASES` section of `www/settings/dev.py` file. Then populate that database by running:

        python manage.py migrate

6. Start the development server to run the project:

        python manage.py runserver


### Connect to you salebox.io account

1. Stop the development server if it is still running.

2. Create a file to enter your account's settings as provided by your Salebox account manager.

        cp www/settings/local.example.py www/settings/local.py

3. Edit the `www/settings/local.py` file and fill-in all the missing data. Your Salebox account manager will be able to help you if you have any problems.

4. Sync your local database with your Salebox account. Note: this step could take a long time depending on the amount of data which needs to be transferred.

        python manage.py saleboxsync

5. Run the development server again. Assuming your Salebox account has active products available, you will now be able to see them on the homepage.

        python manage.py runserver

