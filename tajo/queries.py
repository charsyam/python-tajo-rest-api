from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoQueryInfo(TajoObject):
    def __init__(self, objs):
        self.objs = objs

    def __repr__(self):
        return "(%s:%s)"%(self.objs["queryIdStr"], self.objs["sql"])

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        queries = []
        objs = json.loads(content)["queries"]
        for obj in objs:
            queries.append(TajoQueryInfo(obj))

        return queries

class TajoQueriesRequest(TajoRequest):
    object_cls = TajoQueryInfo
    ok_status = [httplib.OK]

    def __init__(self, database_name):
        self.database_name = database_name

    def uri(self):
        return "queries"

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
