eb-django
=========

Currently Found At:
-------------------
http://eb-django.us-west-2.elasticbeanstalk.com/

Goals:
------
* Make a decent portfolio site that explains my skill set
    * host on AWS Beanstalk
    * deploy with CodePipeline for CI/CD
* Use Different AWS Data Sources
    * RDS
    * DynamoDB
* Add usefull apps to the portfolio to showcase my skills
    * Add Metabase (an open source data visualization tool) example
    * Serverless App (via AWS API-Gateway, Lambda, Cognito etc.)

Virtual Environment
-----------------
    $ pipenv install
    $ pipenv shell

In the shell install django. (All other packages can be added outside the shell with pipenv or inside the shell with pip).

    $ pip install django==1.11.4

Following installations I would recommend running pip freeze > requirements.txt

    $ pip freeze > requirements.txt

Settings
--------

Will be moved to myproject/settings/. But currently normal settings file.

Basic Commands
--------------
Getting into the Beanstalk Django Shell through SSH

    $ eb ssh
    $ passphrase: YOUR_PASSPHRASE
    $ cd /opt/python/current/app
    $ source ../env
    $ python manage.py shell

    >> (Prompt)

Setting Up Your Users
---------------------

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll be logged in and ready to go.

* To create a **superuser account**, use this command (once SSH'ed to Django instance)::

        $ python manage.py createsuperuser


Testing
--------------
In the shell

    $ python manage.py test

To see more detail about the test execution, set the verbosity to a higher level:
---------------------------------------------------------------------------------
    $ python manage.py test --verbosity=2

Scheduled Tasks
---------------

This app uses CloudWatch to trigger events for Lambda functions that hit the primary API endpoints.


Deployment
----------

The following details how to deploy this application.

1. git push branch
2. pull request
3. with approval code deploys to AWS Beanstalk Via CodePipeline


Next Steps
----------
* Zappa serverless deployment of this web app

**Thanks for checking my portfolio out!**