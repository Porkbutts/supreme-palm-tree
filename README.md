# supreme-palm-tree

airbnb clone test project

## install

Install `virtualenv` if you haven't already

```bash
pip3 install virtualenv
```

Then install the requirements

```bash
virtualenv ./venv -p $(which python3)
source ./venv/bin/activate
pip install -r requirements.txt
```

## run

```bash
make run
```

## lint

```bash
make lint
```

## test

```bash
make test
```
