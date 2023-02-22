# AntiqueAndRare
Books Trading Platform


Steps for run the project on server:
1. Check that you have python installed using the following command:

  python --version

(use python3 for all following commands if you have python version 3.x)

2. Install Django using the following command:

  pip install django
  
3. Navigate to the project directory in the terminal using the following command:

  cd <name_of_the_directory>
  
4. Create a virtual enviroment using the following command:

  python -m venv env
  
5. Activate the virtual enviroment using the following command:

  source env/bin/activate
  
6. Install project dependencies by running the following command:

  pip install -r requirements.txt
  
7. Set up the database by running the following commands:

  python manage.py makemigrations

and 
 
  python manage.py migrate
  
8. Create a superuser by running the following command and following the prompts:

  python manage.py createsuperuser

9. Finally :), to run the server using the following command:

  python manage.py runserver

10. Go to 'python manage.py runserver'

11. Create Categories in admin mode. For do it:
 - go to "url/admin"
 - log in with super user account
 - add categories by template: "number_of_category) name_of_category" sorted by age
 - log out





#####################################################


*Steps to Setup PostgreSQL (from sqlite3):*
1. move `.env` file to `book_trader/` directory (it should be done already after merging pr)
2. install django-environ `pip install django-environ`
3. install postgres `pip install psycopg2` (you probably already have it installed)
4. dump existing data to a json file `python manage.py dumpdata > whole.json` (optional)
5. change `book_trader/settings.py` (already done)
6. go to psql using `psql -U postgres`
  a) create a new database `REATE DATABASE your_db_name;`
  b) create a new user `CREATE USER your_name WITH ENCRYPTED PASSWORD 'your_password';
  c) grant all access to this user `GRANT ALL PRIVILEGES ON DATABASE antique_and_rare TO your_name;`
  d) Save the db name, username, and password for further use. 
7. delete all your migration directories, and your sqlite3 db, and all the pycache directories.
8. make migrations `python manage.py makemigrations`
9. migrate `python manage.py migrate`, if encounter error saying `psycopg2.errors.UndefinedTable: relation "some table" does not exist`, migrate each app indivisually, then migrate again.
10. run `python manage.py migrate --run-syncdb ` to make sure db is connected
11. open python shell, `python manage.py shell`
  a)`>>>from django.contrib.contenttypes.models import ContentType`
  b)`>>>ContentType.objects.all().delete()
12. load your saved data into new db `python manage.py loaddata whole.json`
13. run python server `python manage.py runserver`
  
