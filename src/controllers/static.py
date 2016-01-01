from flask import Blueprint, render_template

controller = Blueprint('static', __name__)


@controller.route('/')
def index_view():
    return render_template('index.html')
