from .handlers.retrieve_handler import RetrieveHandler
from .handlers.storage_handler import JsonStorageHandler
from . import api

def register_api(view, endpoint, url, pk, pk_type='int'):
    view_func = view.as_view(endpoint)
    api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET',])

# first lets inject dependency to our handlers
RetrieveHandler.inject_dependencies(
    JsonStorageHandler()
)
register_api(RetrieveHandler, 'user_api', '/v1/get-user/','user_id')

