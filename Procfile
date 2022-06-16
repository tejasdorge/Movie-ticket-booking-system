release: python src/manage.py migrate
web: gunicorn src.core.wsgi --log-file=-
