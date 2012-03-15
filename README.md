## Installation

1. Get python > 2.5

    You can see what pyton version you have by doing the following
    
        python 
        >>> import sys
        >>> sys.version
        '2.7.1 etc.'
        >>> # press ctrl + d to exit from REPL
        
    If you don't have python installed at all on your system, consult google on installing python on your system
    
2. You also need some database system running on your system. Default is mysql. Consult google on installing it. 
However, you can also use sqlite. To do that, change settings in `settings/settings.local` accordingly.
        
3. Install http://pypi.python.org/pypi/virtualenv

        pip install virtualenv

4. Clone the repository from github into `psi` folder. That folder needs to be empty or to not exist in order to clone into it. Change into that folder then.

        git clone git@github.com:gryzzly/publicspaceinvaders.git psi && cd psi

5. Create independent virtual environment

        virtualenv --no-site-packages psi

    This will create a folder `psi` in current folder. All environment we use to run application locally is stored in this folder.

6. Activate this virtual environment

        source psi/bin/activate

7. Install the dependencies

        pip install -r requirements.txt
    
    This will install all the dependencies. You can review currently installed packages

        yolk -l

    The list you will see should match what you will find in `requirments.txt` file

8. Remove the leftover `build` directory from the root of the application

        rm -rf build

9. Create a database and a user matching local settings of the repository (running
this command will delete existing `publicspaceinvaders_db` database, if you have one!)

        mysql -u root < setupdb.sql

    Or if you need password

        mysql -u root -p < setupdb.sql

10. Sync database to create appropriate tables and admin user. Remember the password :-)

        python manage.py syncdb --settings=settings.local
        
11. Start the development server

        python manage.py runserver --settings=settings.local
        
12. Hack hack hack



