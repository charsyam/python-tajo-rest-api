from tajo.column import Column

class Schema:
    def __init__(self, objs):
        self.columns = []
        nmap = {}
        imap = {}
        for name in objs['fieldsByQualifiedName']:
            imap[name] = objs['fieldsByQualifiedName'][name]

        for column in objs["fields"]:
            datatype = column["typeDesc"]["dataType"]
            name = column["name"]

            clen = 1
            try:
                clen = datatype["len"]
            except:
                pass

            new_column = Column(name, datatype["type"], clen)
            idx = imap[name]
            nmap[idx] = new_column

        size = len(nmap)
        for idx in range(size):
            self.columns.append(nmap[idx])

    def column(self, idx):
        return self.columns[idx]
