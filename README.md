# supreme-palm-tree
airbnb clone test project

## install
Install `virtualenv` if you haven't already
```
pip3 install virtualenv
```

Then install the requirements
```
virtualenv ./venv -p /usr/local/bin/python3
source ./venv/bin/activate
pip install -r requirements.txt
```

## run
```
uvicorn app.main:app --reload
```

## lint
```
pylint $(git ls-files '*.py')
```

## test
```
pytest
```
