class TajoClientError(Exception):
    """The base class for other Tajo Client exceptions"""

    def __init__(self, value):
        super(TajoClientError, self).__init__(value)
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return ("<TajoClientError in " + repr(self.value) + ">")

class NotImplementedMethodError(TajoClientError):
    """The NotImplementedMethodError exceptions"""

    def __init__(self, value):
        super(NotImplementedMethodError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<NotImplementedMethodError in " + repr(self.value) + ">")

class InvalidStatusError(TajoClientError):
    """Invalid Status Error exceptions"""

    def __init__(self, value):
        super(InvalidStatusError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<InvalidStatusError in " + repr(self.value) + ">")

class InvalidRequestError(TajoClientError):
    """Invalid Request Error exceptions"""

    def __init__(self, value):
        super(InvalidRequestError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<InvalidResquestError in " + repr(self.value) + "is not valid>")

class NotFoundError(TajoClientError):
    """NotFound Error exceptions"""

    def __init__(self, value):
        super(NotFoundError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<NotFoundError in " + repr(self.value) + ">")

class NullQueryIdError(TajoClientError):
    """NotFound Error exceptions"""

    def __init__(self):
        super(NullQueryIdError, self).__init__()

    def __repr__(self):
        return ("<NullQueryIdError>")

class InternalError(TajoClientError):
    """NotFound Error exceptions"""

    def __init__(self, value):
        super(InternalError, self).__init__(value)
        self.value = value

    def __repr__(self):
        return ("<InternalError in " + repr(self.value) + ">")
