"""
Stubs for simulating an Arduino Board.
"""


class DigitalStub:
    def __init__(self, name, pin_id):
        self.name = name
        self.pin_id = pin_id

    def write(self, value):
        print(f"Board write: {self.name}.{self.pin_id} = {value}")


class BoardStub:
    def __init__(self, name):
        self._name = name
        self.digital = [DigitalStub(name, i) for i in range(10)]
