
class DigitalStub:
    def __init__(self, name):
        self._name = name

    def write(self, value):
        print(f"Board write: [{self._name}] -> [value {value}]")


class BoardStub:
    def __init__(self, name):
        self._name = name
        self.digital = [DigitalStub(name)] * 10
