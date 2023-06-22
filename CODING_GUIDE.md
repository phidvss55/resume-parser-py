### Install steps

---

1. Create virtual environment

```
python -m venv env
```

or

```
python3 -m venv env
```

2. Active the virtual environment

_For window_

```
env\Scripts\activate
```

_For Linux_

```
source env/bin/activate
```

3. Install dependencies

```
cd project-name
```

**Solution 1: Run this**

```
pip install -r requirements.txt
```

**Solution 3: Run the section below**

```
pip install Django
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install python-dotenv
pip install djangorestframework
pip install pyresparser
```

4. Serve the application

```
python manage.py runserver
```

_Or for whose using python3_

```
python3 manage.py runserver
```

---

### For bugs

```
OSError at /
[E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a Python package or a valid path to a data directory
```

_Run beblow_

```
pip install nltk

pip install spacy==2.3.5

pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

pip install pyresparser
```
