#!/usr/bin/python3
<<<<<<< HEAD
"""Create a new view for User objects"""
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/user/all_users.yml', methods=['GET'])
def users():
    """Get all stored users"""
    res = [
        user.to_dict() for user in storage.all(User).values()
    ]
    return jsonify(res)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def user_by_id(user_id):
    """Get a User object by id"""
    res = storage.get(User, user_id)
    if res is None:
        abort(404)
    return jsonify(res.to_dict())
=======
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())
>>>>>>> 0e65ac42c5444cf4fa86bb7a612bf44af6275520


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
<<<<<<< HEAD
    """Delete an User object by its id """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def insert_user():
    """Insert a new User object"""
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'Not a JSON'})
    if 'email' not in body:
        return abort(400, {'message': 'Missing email'})
    if 'password' not in body:
        return abort(400, {'message': 'Missing password'})
    new_user = User(**body)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def update_user_by_id(user_id):
    """Update an User object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    body = request.get_json()
    if type(body) != dict:
        return abort(400, {'message': 'Not a JSON'})
    for key, value in body.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
=======
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
>>>>>>> 0e65ac42c5444cf4fa86bb7a612bf44af6275520
