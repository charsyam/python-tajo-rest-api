import httplib2 as Http
import json

class TajoConnection(object):
    def __init__(self, base):
        self.base = base
        self.request = Http.Http()
        self.common_headers = {'Content-Type': 'application/json'}

    def add_header(self, key, value):
        self.common_headers[key] = value

    def post(self, uri, body, headers = None):
        return self._request("POST", uri, body, headers)

    def get(self, uri, body, headers = None):
        return self._request("GET", uri, body, headers)

    def _request(self, method, uri, body = None, headers = None):
        url = "%s/%s"%(self.base, uri)
        aheaders = self.common_headers.copy()
        if headers is not None:
            aheaders.update(headers)

        return self.request.request(url, method, body=json.dumps(body), headers=aheaders)
