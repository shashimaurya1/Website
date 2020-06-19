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
