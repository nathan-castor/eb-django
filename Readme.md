eb-django
=========

Goals:
------
* Make a decent portfolio site that explains my skill set
    * host on AWS Beanstalk
    * deploy with CodePipeline for CI/CD
* Use Different AWS Data Sources
    * RDS
    * DynamoDB
* Add usefull apps to the portfolio to showcase my skills
    * Add Metabase example

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
