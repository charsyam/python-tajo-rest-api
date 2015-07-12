class ResultSetBase(object):
    def __init__(self):
        self.cur_row = 0
        self.cur = None
        self.schema = None
        self.total_row = 0

    def current_tuple(self):
        return self.cur

    def next(self):
        if self.total_row <= 0:
            return False

        self.cur = self.next_tuple()
        self.cur_row += 1
        if self.cur is not None:
            return True

        return False

    def next_tuple(self):
        raise Exception("Not Implemented")


