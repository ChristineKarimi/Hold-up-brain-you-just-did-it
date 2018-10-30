from .abstract_retrieve_handler import AbstractRetrieveHandler
from flask.views import MethodView
from flask import jsonify,abort

class RetrieveHandler(MethodView):

    __metaclass__=AbstractRetrieveHandler

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def inject_dependencies(cls,storageHandler):
        cls.storageHandler=storageHandler

    def get(self,*args, **kwargs):
        try:
            user_id=kwargs.pop("user_id")
            data=self.storageHandler.retrieve_users(user_id)
            if data:
                return jsonify({"users":data})
            raise ValueError("Invalid user_id")
        except Exception as e:
            print(e)
            return abort(404)
        
    def post(self,*args, **kwargs):
        pass

