from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoCluster(TajoObject):
    def __init__(self, objs):
        self.objs = objs

    def __repr__(self):
        return str(self.objs)

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        return TajoCluster(content)


class TajoClusterRequest(TajoRequest):
    object_cls = TajoCluster
    ok_status = [httplib.OK]

    def __init__(self):
        self.objs = None

    def uri(self):
        return "cluster"

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
