from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoResultSetInfo(TajoObject):
    def __init__(self, objs):
        self.objs = objs
        self.link = self.objs["resultset"]["link"]

    def schema(self):
        return self.objs["schema"]

    def link(self):
        return self.link;

    def __repr__(self):
        return self.link

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        objs = json.loads(content)
        if objs['resultCode'] != "OK":
            raise InvalidStatusError(int(headers['status']))

        return TajoResultSetInfo(objs)


class TajoResultSetInfoRequest(TajoRequest):
    object_cls = TajoResultSetInfo
    ok_status = [httplib.OK]

    def __init__(self, query_id, base):
        self.url = query_id.url
        self.base = base

    def uri(self):
        url = "%s/result"%(self.url[len(self.base):])
        return url

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
