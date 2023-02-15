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
