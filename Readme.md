eb-django
=========

Virtual Environment
-----------------
    $ pipenv shell
    $ pipenv install
You might also need to install Django seperately. Installs inside the shell can use regular pip. Otherwise use pipenv:

    $ pipenv install django

Settings
--------

Will be moved to myproject/settings/. But currently normal settings file.

Basic Commands
--------------
coming soon...

Setting Up Your Users
---------------------

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll be logged in and ready to go.

* To create an **superuser account**, use this command::

        $ python manage.py createsuperuser


Testing
--------------

    $ python manage.py test

Running tests with py.test
--------------------------

    $ py.test


Scheduled Tasks
---------------

This app uses CloudWatch to trigger events for Lambda functions that hit the primary API endpoints.



Deployment
----------

The following details how to deploy this application.


AWS Beanstalk Via CodePipeline
^^^^^^






