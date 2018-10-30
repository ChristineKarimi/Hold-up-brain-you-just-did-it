from .abstract_storage_handler import  AbstractStorageHandler
from flask import current_app
import json

class JsonStorageHandler(AbstractStorageHandler):

    def __init__(self, *args, **kwargs):
        pass

    def retrieve_users(self,user_id:int=None):
        try:
            with open(current_app.config["FAKE_USERS_JSON_FILE"],"r") as jfile:
                data=json.load(jfile) 
            if user_id and data:
                return data[str(user_id)]
            else:
                return data

        except Exception as e:
            print(e)
            return False

    def write(self):
        pass

class SqlStorageHandler(AbstractStorageHandler):
    
    def __init__(self, *args, **kwargs):
        pass

    def retrieve_users(self,user_id:int=None):
        pass

    def write(self):
        pass