#!/usr/bin/env python3

from __future__ import print_function, absolute_import

from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from controllers import api, static
from persistence import db
import settings


app = Flask(__name__, template_folder='../templates')
app.config.from_object(settings)

db.init_app(app)

app.register_blueprint(static.controller)
app.register_blueprint(api.controller, url_prefix='/api')


if __name__ == '__main__':
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
