from __future__ import annotations
from collections.abc import Sequence, Mapping
import serial.tools.list_ports
import json


class Button:
    def __init__(self, name: str, button_id: int, port: int):
        self._name = name
        self._button_id = button_id
        self._port = port

    @property
    def name(self) -> str:
        return self._name

    def press(self):
        #TODO: Aliashiv
        print(f"Press: [COM port {self._port}] -> [button id {self._button_id}]")


class Setup:
    def __init__(self, port: int, buttons: Sequence[Button]):
        self._port = port
        self._buttons = {button.name: button for button in buttons}

    @classmethod
    def connect_arduino_port(self):
        connected_ports = list(serial.tools.list_ports.comports())
        if 0 == len(connected_ports):
            print(F"No connected COM ports found")
            return
        elif 1 == len(connected_ports):
            port = connected_ports[0]
        else:
            print(F"Available COM ports:")
            for index, port in enumerate(connected_ports):
                print(F"{index}. {port}")

            choice = int(input(F"\nPlease select COM port: "))
            while choice >= len(connected_ports) or 0 > choice:
                choice = int(input(F"Invalid choice! \nPlease select COM port: "))
            port = connected_ports[choice]

        print(F'Connecting to "{port}"')
        return port

    def get_json_dict(self):
        return dict(port=self._port, buttons=[button_attributes.__dict__ for button_attributes in self._buttons.values()])

    @classmethod
    def save_setup_to_file(cls, setup, setup_file_name: str):
        with open(setup_file_name, 'w') as new_setup_file:
            print(cls.get_json_dict(setup))
            json.dump(cls.get_json_dict(setup), new_setup_file)

    @classmethod
    def load_setup_from_file(cls, setup_file_name):
        with open(setup_file_name, 'r') as setup_file:
            setup_json = json.load(setup_file)
            return Setup(setup_json['port'], [Button(*button_dict.values()) for button_dict in setup_json['buttons']])

    @classmethod
    def construct_from_button_mapping(cls, port: int, button_mapping: Mapping[str, int]) -> Setup:
        buttons = cls.from_button_mapping(port=port, button_mapping=button_mapping)
        return cls(port=port, buttons=buttons)

    @staticmethod
    def from_button_mapping(port: int, button_mapping: Mapping[str, int]):
        return [Button(port=port, name=key, button_id=value) for key, value in button_mapping.items()]

    def __getattr__(self, name):
        # If name is the name of a button - return it.
        if name in self._buttons:
            return self._buttons[name]

        raise AttributeError


def main():
    button_mapping = {"power": 1, "volume_up": 2, "volume_down": 3}
    my_setup = Setup.construct_from_button_mapping(port=4, button_mapping=button_mapping)
    my_setup.power.press()


if __name__ == "__main__":
    main()
