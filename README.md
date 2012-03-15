## Installation

1. Get python > 2.5
2. Install http://pypi.python.org/pypi/virtualenv

    pip install virtualenv

3. Clone the repository from github into `psi` folder. That folder needs to be empty or to not exist in order to clone into it. Change into that folder then.

    git clone git@github.com:gryzzly/publicspaceinvaders.git psi && cd psi

4. Create independent virtual environment

    virtualenv --no-site-packages psi

   This will create a folder `psi` in current folder. All environment we use to run application locally is stored in this folder.

5. Activate this virtual environment

    source psi/bin/activate

6. Install the dependencies

    pip install -r requirements.txt

   This will install all the dependencies. You can review currently installed packages

    yolk -l

   The list you will see should match what you will find in requirments.txt file

7. Remove the leftover `build` directory from the root of the application

    rm -rf build

8. Create a database and a user matching local settings of the repository

    mysql -u root < setupdb.sql

   Or if you need password

    mysql -u root -p < setupdb.sql

9. Sync database to create appropriate tables and admin user. Remember the password :-)

    python manage.py syncdb --settings.settings.local



