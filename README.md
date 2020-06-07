Create Bacic Setup 

1. Clone the repository from below URL:
   https://github.com/bhagyashrishitole/taskmanagement-backend

2. Go to below directory to run backend app
   > taskmanagement-backend\src

3. Install required libraries
   > pip install -r requirements.txt

4. To start with fresh database configuration 
   4.1 You need to initiate db in our case it's migration directory 
       python manage.py db init
   4.2 To create migration scripts
       python manage.py db migrate
   4.3 To create db schema
       python manage.py db upgrade

Note: If db schema is changed or DDL/DML operations needs to be performed then execute 2.2 and 2.3 commands

5. To run actual backendup application execute below command.
   > python manage.py run

Run Prepared Setup - with existing db[Recommended]

1. Clone the repository from below URL:
   https://github.com/bhagyashrishitole/taskmanagement-backend

2. Go to below directory to run backend app
   > taskmanagement-backend\src

3. Install required libraries
   > pip install -r requirements.txt

4. To run actual backendup application execute below command.
   > python manage.py run

Note: Database has already populated with required data. To use this db, please use existing user details to login.