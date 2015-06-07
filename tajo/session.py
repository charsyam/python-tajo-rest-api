from tajo.error import InvalidStatusError
from tajo.base import TajoPostRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoSession(TajoObject):
    def __init__(self, session_id):
        self.session_id = session_id

    def __repr__(self):
        return str(self.session_id)

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode("utf-8")

        objs = json.loads(content)
        if objs["resultCode"] != "OK":
            raise InvalidStatusError("parse body failed!")

        if "id" not in objs:
            raise InvalidStatusError("parse body failed!")

        return TajoSession(objs["id"])


class TajoSessionRequest(TajoPostRequest):
    object_cls = TajoSession
    ok_status = [httplib.CREATED]

    def __init__(self, username, database_name):
        self.username = username
        self.database_name = database_name

    def uri(self):
        return "sessions"

    def headers(self):
        return None

    def params(self):
        payload = {
            'userName': self.username,
            'databaseName': self.database_name
        }

        return payload

    def cls(self):
        return self.object_cls
