class Column:
    def __init__(self, name, datatype, length = 1):
        self.name = name
        self.datatype = datatype.upper()
        self.length = length
