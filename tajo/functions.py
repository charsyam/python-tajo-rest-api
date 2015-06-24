from tajo.error import InvalidStatusError
from tajo.base import TajoRequest, TajoObject
from tajo.py3 import httplib, PY3

try:
    import simplejson as json
except ImportError:
    import json

class TajoFunction:
    def __init__(self, function_type, name, param_types, return_type):
        self.name = name
        self.param_types = param_types
        self.return_type = return_type["type"]
        self.function_type = function_type

    def __repr__(self):
        return "%s:%s"%(self.name, self.return_type)


class TajoFunctions(TajoObject):
    @staticmethod
    def create(headers, content):
        if PY3:
            content = content.decode('utf-8')

        functions = json.loads(content)
        results = []
        for f in functions:
            results.append(TajoFunction(f["functionType"], f["name"], f["paramTypes"], f["returnType"]))

        return results;


class TajoFunctionsRequest(TajoRequest):
    object_cls = TajoFunctions
    ok_status = [httplib.OK]

    def __init__(self):
        pass

    def uri(self):
        return "functions"

    def headers(self):
        return None

    def params(self):
        return None

    def cls(self):
        return self.object_cls
