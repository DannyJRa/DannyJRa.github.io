$ # clone the sources
git clone https://github.com/app-generator/flask-dashboard-adminator.git
cd flask-dashboard-adminator
$
$ # install modules using a virtualenv
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ python app.py
$ # app is running on port 5000


$ # clone the sources
git clone https://github.com/app-generator/flask-dashboard-adminlte.git
git clone https://github.com/app-generator/flask-material-dashboard.git
cd flask-material-dashboard
$
install modules using a virtualenv
pipenv install
pipenv shell
$ source env/bin/activate
$

pipenv install -r requirements.txt
python app.py
$ # app is running on port 5000