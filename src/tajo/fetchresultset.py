from tajo.resultsetbase import ResultSetBase
from tajo.resultset import TajoMemoryResultSetRequest, TajoMemoryResultSet

class TajoFetchResultSet(ResultSetBase):
    def __init__(self, client, query_id, resultset_info, fetch_row_num = 100):
        super(TajoFetchResultSet, self).__init__()
        self.fetch_row_num = fetch_row_num
        self.query_id = query_id
        self.resultset_info = resultset_info
        self.finished = False
        self.resultset = None
        self.schema = resultset_info.schema()
        self.offset = -1
        self.client = client

    def is_finished(self):
        return self.finished

    def fetch(self):
        return self.client.query_resultset(self.resultset_info, self.fetch_row_num)

    def next_tuple(self):
        if self.is_finished() is True:
            return None

        t = None
        if self.resultset is not None:
            self.resultset.next()
            t = self.resultset.current_tuple()

        if self.resultset is None or t is None:
            if self.resultset is None or (self.resultset is not None and self.resultset.eos == False):
                self.resultset = self.fetch()

            if self.resultset is None:
                self.finished = True
                return None

            if self.offset == -1:
                self.offset = 0

            self.offset += self.fetch_row_num

            self.resultset.next()
            t = self.resultset.current_tuple()

        if t is None:
            if self.resultset is not None:
                self.resultset = None

            self.finished = True

        return t
