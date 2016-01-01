# Flask-Seed

A simple seed application for building a web application with Flask, skipping all the setup ceremony.

## Features

* SQLAlchemy integration with database versioning support (alembic)
* Deployment server included (`./start.sh`)
* Environmental specific settings (`PY_ENV` should be `dev`/`test`/`prod`, default: `prod`)
* Testing integrated (`py.test`)
* Jinja2 examples

If you want to use a different database, you'll need to install the driver (e.g. postgres -> `psycopg2`).

## Migrations

* `python src/server.py db migrate`: Create a migration (automagic discovery)
* `python src/srver.py db upgrade`: Run all migrations
