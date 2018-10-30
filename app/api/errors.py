from flask import make_response,jsonify
from . import api

@api.errorhandler(404)
def error_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@api.errorhandler(400)
def error_400(error):
    return make_response(jsonify({'error': 'Access denied'}), 400)

@api.errorhandler(500)
def error_500(error):
    return make_response(jsonify({'error': 'Server error'}), 500)
