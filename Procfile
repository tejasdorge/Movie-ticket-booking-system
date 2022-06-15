release: python manage.py migrate
web: gunicorn core.wsgi --log-file=-
web: python core/manage.py runserver 0.0.0.0:$PORT --noreload