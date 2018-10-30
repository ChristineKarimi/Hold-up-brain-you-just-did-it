import abc
import forgery_py
from random import choice
import json
from flask import current_app


SCHEMA={
    "name":"",
    "class":"",
    "image":"",
}

CLASSES=["MC1","MC2","MC3","MPFT19","MC7","MC13"]

DEFAULT_AVATAR_LINK="http://placekitten.com/g/200/300"


class AbstractFakeUsers(abc.ABC):

    def __init__(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def generate_to_db(self,n:int,storageHandler):
        pass

    @abc.abstractmethod
    def generate_to_json_file(self,n:int):
        pass


class FakeUsers(AbstractFakeUsers):
    
    def __init__(self,*args, **kwargs):
        pass

    def generate_to_db(self,n:int,storageHandler):
        pass

    def generate_to_json_file(self,n:int):
        try:
            data={}
            for i in range(1,n+1):
                data[str(i)]={
                    "name":forgery_py.name.full_name(),
                    "class":choice(CLASSES),
                    "image":DEFAULT_AVATAR_LINK
                }
            
            with open(current_app.config["FAKE_USERS_JSON_FILE"],"w") as jfile:
                json.dump(data,jfile) 
            return True
        except Exception as e:
            print(e)
            return False


        