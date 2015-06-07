from tajo.session import TajoSessionRequest, TajoSession
from tajo.query import TajoQueryRequest, TajoQuery
from tajo.queries import TajoQueriesRequest, TajoQueries
from tajo.querystatus import TajoQueryStatusRequest, TajoQueryStatus
from tajo.resultsetinfo import TajoResultSetInfoRequest, TajoResultSetInfo
from tajo.resultset import TajoMemoryResultSetRequest, TajoMemoryResultSet
from tajo.fetchresultset import TajoFetchResultSet
from tajo.connection import TajoConnection
from tajo.cluster import TajoCluster, TajoClusterRequest
from tajo.querystate import QueryState

import time

class TajoClient(object):
    def __init__(self, base = 'http://127.0.0.1:26880/rest/',
                 username = 'tajo', database = 'default',
                 rowNum = 1024):
        self.clear()
        self.base = base
        self.username = username
        self.database = database
        self.rowNum = rowNum
        self.conn = TajoConnection(self.base)
        self.session = self.create_session()

    def clear(self):
        self.base = None
        self.username = "tajo"
        self.database = "default"
        self.rowNum = 1024
        self.conn = None
        self.session = None

    def create_session(self):
        request = TajoSessionRequest(self.username, self.database)
        self.session = request.request(self.conn)
        self.conn.add_header("X-Tajo-Session", str(self.session))

    def execute_query(self, query):
        req = TajoQueryRequest(query, self.database)
        return req.request(self.conn)

    def queries(self):
        req = TajoQueriesRequest(self.database)
        return req.request(self.conn)

    def query_status(self, query_id):
        req = TajoQueryStatusRequest(query_id, self.base)
        return req.request(self.conn)

    def query_resultset_info(self, query_id):
        req = TajoResultSetInfoRequest(query_id, self.base)
        return req.request(self.conn)

    def query_resultset(self, resultsetinfo, count = 100):
        req = TajoMemoryResultSetRequest(resultsetinfo, self.base, count)
        return req.request(self.conn)

    def fetch(self, query_id, fetch_row_num = 100):
        resultset_info = self.query_resultset_info(query_id)
        return TajoFetchResultSet(self, query_id, resultset_info, fetch_row_num)

    def create_nullresultset(self, queryId):
        return TajoMemoryResultSet(None, True, 0, 0, None)

    def execute_query_wait_result(self, query):
        query_id = self.execute_query(query)
        status = self.query_status(query_id)
        while self.is_query_complete(status.state) == False:
            time.sleep(0.1)
            status = query_status(query_id)

        if status.state == QueryState.QUERY_SUCCEEDED:
            return self.fetch(query_id)

        return self.create_nullresultset(query_id)

    def is_query_waiting_for_schedule(self, state):
        return state == QueryState.QUERY_NOT_ASSIGNED or \
                state == QueryState.QUERY_MASTER_INIT or \
                state == QueryState.QUERY_MASTER_LAUNCHED

    def is_query_inited(self, state):
        return state == QueryState.QUERY_NEW

    def is_query_running(self, state):
        return self.is_query_inited(state) or (state == QueryState.QUERY_RUNNING)

    def is_query_complete(self, state):
        return self.is_query_waiting_for_schedule(state) == False and \
        self.is_query_running(state) == False

    def cluster_info(self):
        req = TajoClusterRequest()
        return req.request(self.conn)
