from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject, TajoPostRequest, TajoDeleteRequest
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoTable(TajoObject):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s"%(self.name)

    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        data = json.loads(content)
        return data


class TajoTableInfo(TajoObject):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s"%(self.name)


class TajoTablesInfo(TajoObject):
    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        data = json.loads(content)
        tables = []
        for table in data['tables']:
            tables.append(TajoTableInfo(table))

        return tables


class TajoTablesRequest(TajoRequest):
    object_cls = TajoTablesInfo
    ok_status = [httplib.OK]

    def __init__(self, database_name):
        self.database_name = database_name

    def uri(self):
        return "databases/%s/tables"%(self.database_name)

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls


class TajoTableRequest(TajoRequest):
    object_cls = TajoTable
    ok_status = [httplib.OK]

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def uri(self):
        return "databases/%s/tables/%s"%(self.database_name, self.table_name)

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
