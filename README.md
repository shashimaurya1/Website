# GreenClothaWay

## prerequisites
`python >= 3.6`

`pip3 lts`

`python-virtualenv`

## preperation
create a virtual environment and update pip and wheel
```
python3 -m venv <venvname>
source <venvname>/bin/activate
pip install -U pip
pip install -U wheel
```

## installation
install package
```
pip install greenclothaway-<release_version>-py3-none-any.whl
```

## configuration
```
mv <venvname>/lib/python3.8/site-packages/website/settings.py.sample <venvname>/lib/python3.8/site-packages/website/settings.py
```

in this settings.py you now have to add a django secrete key. for a development server any random 50 character long string will do.
also if you want to use another databse then the default(sqlite) you have to configure it here.

after that you will have to migrate django database stuff n all.

```
manage.py makemigrations
manage.py migrate
```
the manage.py command will be available in your virtual environment after the installation.

now youre all set to turn on your testserver on localhost

```
manage.py runserver
```



if you want to run this application on a productive server youll have to set up a webserver and configure it according to djangos how to.
but thats on you dude!