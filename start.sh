set -e
cd myproject
python manage.py migrate --noinput
python manage.py create_deploy_superuser || true
python manage.py collectstatic --noinput
exec gunicorn myproject.wsgi --bind 0.0.0.0:${PORT:-8000}