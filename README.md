# simple-django-docker-app
A simple-as-it-gets example of a Django web app with NGINX frontent and MySQL/MariaDB backend, deployed by docker.

To run:
```
docker build -f Dockerfile.simpleapp . -t web
docker run -p 127.0.0.1:8080:8080 web
```

And browse to 127.0.0.1:8080.