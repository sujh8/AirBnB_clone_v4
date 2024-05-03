#!/usr/bin/python3
<<<<<<< HEAD
"""This module implement a rule that returns the status of the application"""
from flask import jsonify
import models
from api.v1.views import app_views
=======
""" Index """
>>>>>>> 0e65ac42c5444cf4fa86bb7a612bf44af6275520
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
<<<<<<< HEAD


@app_views.route("/status", strict_slashes=False)
def view_status():
    """View function that return a json message"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def view_stats():
    """Veiw function that retrieves the number of each object by type"""
    return jsonify({
        "amenities": models.storage.count(Amenity),
        "cities": models.storage.count(City),
        "places": models.storage.count(Place),
        "reviews": models.storage.count(Review),
        "states": models.storage.count(State),
        "users": models.storage.count(User)
    })
=======
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
>>>>>>> 0e65ac42c5444cf4fa86bb7a612bf44af6275520
