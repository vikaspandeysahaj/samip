import traceback
from json import dumps
from flask import Blueprint, request

from samip.helper.user_helper import get_user_json_attr_from_hash
from samip.models.user import User

user_routes = Blueprint("user", "user", static_folder='static')

@user_routes.route('/user/create', methods=['POST'])
def create_user():
    try:
        user_hash = get_user_json_attr_from_hash(request.json)
        if User.is_valid_hash(user_hash):
            user = User.create_user(user_hash)
            return dumps(user.as_json())
    except ValueError as e:
        return dumps(e.message), 400
    except Exception as e:
        print(e.message)
        print(traceback.print_exc())
        return dumps(e.message), 400
