This project addresses problem statement:
Writing A Django Management Command that will run and store Records in the Database. Inserts Dummy Users in the Database using management commands. It will also store 100 PST date times in a separate table. There will be a scheduled Cron Job that will run after every 5 minutes and update 10 date times in UTC. Once all 100 date times are in UTC, the cron job will start converting date time objects in PST. and this will continue


This project requires following dependencies:

- python==3.9.13
- asgiref==3.5.2
- Django==4.0.5
- django-crontab==0.7.1
- psycopg2==2.9.3
- pytz==2022.1

The Project has 1 custom management command "create_dummydata" to create dummy data as per requirement
Run "python manage.py crontab add" to add cronjob defined in core/cron.py in your crontab

