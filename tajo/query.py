from tajo.error import InvalidStatusError
from tajo.base import TajoPostRequest, TajoObject
from tajo.querystate import QueryState
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoQuery(TajoObject):
    def __init__(self, headers, contents=None):
        self.url = headers["location"]
        self.query_id = self.get_parse_query_id(self.url)
        self.completed = False
        if contents is not None:
            self.completed = True
            self.status = QueryStatus.QUERY_SUCCECCED
            if PY3:
                contents = contents.decode('utf-8')

            self.objs = json.loads(contents)

    def get_query_id(self):
        return self.query_id

    def get_parse_query_id(self, url):
        parts = url.split('/')
        return parts[-1]

    def __repr__(self):
        return str(self.url)

    @staticmethod
    def create(headers, content):
        if int(headers["status"]) == httplib.CREATED:
            return TajoQuery(headers)
        else:
            return TajoQuery(headers, content)


class TajoQueryRequest(TajoPostRequest):
    object_cls = TajoQuery
    ok_status = [httplib.CREATED, httplib.OK]

    def __init__(self, query):
        self.query = query

    def uri(self):
        return "queries"

    def headers(self):
        return None

    def params(self):
        payload = {
            'query': self.query
        }

        return payload

    def cls(self):
        return self.object_cls
