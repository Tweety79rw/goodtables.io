from flask import Blueprint, request, abort
from flask.json import jsonify
from .. import helpers


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/task', methods=['POST'])
def create_task():

    payload = request.get_json()

    if not payload or 'source' not in payload:
        abort(400)

    task_id = helpers.create_task(payload)

    return task_id


@api.route('/task')
def list_tasks():
    return jsonify(helpers.get_task_ids())


@api.route('/task/<task_id>')
def get_task(task_id):
    return jsonify(helpers.get_task(task_id))


@api.route('/')
def hi():
    return "hi"
