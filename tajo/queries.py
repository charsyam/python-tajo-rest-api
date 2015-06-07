from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoQueries(TajoObject):
    def __init__(self, objs):
        self.objs = objs

    def __repr__(self):
        return "Queries"

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        return TajoQueries(json.loads(content))


class TajoQueriesRequest(TajoRequest):
    object_cls = TajoQueries
    ok_status = [httplib.OK]

    def __init__(self, database_name):
        self.database_name = database_name

    def uri(self):
        return "databases/%s/queries"%(self.database_name)

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
