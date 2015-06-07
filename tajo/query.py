from tajo.error import InvalidStatusError
from tajo.base import TajoPostRequest, TajoObject
from tajo.py3 import httplib

try:
    import simplejson as json
except ImportError:
    import json

class TajoQuery(TajoObject):
    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return str(self.url)

    @staticmethod
    def create(headers, content):
        return TajoQuery(headers["location"])


class TajoQueryRequest(TajoPostRequest):
    object_cls = TajoQuery
    ok_status = [httplib.CREATED]

    def __init__(self, query, database_name):
        self.query = query
        self.database_name = database_name

    def uri(self):
        return "databases/%s/queries"%(self.database_name)

    def headers(self):
        return None

    def params(self):
        payload = {
            'query': self.query
        }

        return payload

    def cls(self):
        return self.object_cls
