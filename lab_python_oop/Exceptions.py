# Let's pretend that this is a production code, not some garbage from bmstu...


class LabException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BadArguments(LabException):
    pass
