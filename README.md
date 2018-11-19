# simple-django-docker-app

A simple-as-it-gets example of a Django web app with NGINX frontent and MySQL/MariaDB backend, deployed by docker-compose.

The objective is to serve locally a simple content from a data source using common tools.

This is a simple, quick, do-not-use for production demonstrator. Security was not a thought.

To run:
```
1. Checkout code
2. docker-compose up
3. Browse to 127.0.0.1:8080
```

Notes:
- If not using 127.0.0.1, update ALLOWED_HOSTS on djangoproject/settings.py
- Checking for the DB to be up is crude, should be at app level (Django)
- Python3 not used due to native Python3 MySQL client not yet available as alpine 3.8 package (but on edge-testing as py3-pymysql)
- Security is pretty much non-existent
