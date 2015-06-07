from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoQueryStatus(TajoObject):
    def __init__(self, objs):
        self.objs = objs
        self.state = objs["queryState"]

    def __repr__(self):
        return "QueryStatus"

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        return TajoQueryStatus(json.loads(content))


class TajoQueryStatusRequest(TajoRequest):
    object_cls = TajoQueryStatus
    ok_status = [httplib.OK]

    def __init__(self, query_id, base):
        self.url = query_id.url
        self.base = base

    def uri(self):
        return self.url[len(self.base):]

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
