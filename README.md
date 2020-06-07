To create venv
python3 -m venv /path/to/new/virtual/environment

To install required 
pip install -r requirements.txt

$source venv/bin/activate

Go to taskmanagement-backend\src to execute below db commands

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

Go to taskmanagement-backend\src\app\main directory - To access task_management.db
[To execute some insert queries]

Run below command to use db

sqlite3 task_management.db

insert into priority(name) values("High");
insert into priority(name) values("Medium");
insert into priority(name) values("Low");

insert into status(name) values("New");
insert into status(name) values("InProgress");
insert into status(name) values("Completed");

insert into label(name) values("Personal");
insert into label(name) values("Work");
insert into label(name) values("Shopping");
insert into label(name) values("Others");

Go to taskmanagement-backend\src to run application
python manage.py run
