#!/usr/bin/env bash

set -o errexit

pip install pipenv
pipenv install --system --deploy --dev

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py loaddata game/fixtures/game.json
