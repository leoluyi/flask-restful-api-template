from flask import jsonify
from flask_restful import Resource


class StudentsResource(Resource):
    """docstring for Student"""

    def get(self, name):
        return jsonify({"student": name})
