# Hotel Management

To create virual env,
```
	python -m venv .venv
```

To activate environment
```
	.venv\Scripts\activate
```

To install all required libriaries for this app
```
	pip install -r requirements.txt
```

If any changes in db or model files, need to migrate
```
	python manage.py makemigrations
	python manage.py migrate
```

To run this app
```
	python manage.py runserver
```