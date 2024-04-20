#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Todd_Arnold', 'Toddarnold@gmail.com', 'password')" | python manage.py shell
python manage.py collectstatic --no-input

# python manage.py makemigrations
python manage.py showmigrations

# python manage.py migrate --fake api zero
python manage.py migrate
