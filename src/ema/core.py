from __future__ import annotations
from collections.abc import Sequence, Mapping
from pyfirmata import Board, Arduino
import time
import serial.tools.list_ports
import json


class Button:
    def __init__(self, name: str, button_id: int, board: Board):
        self._name = name
        self._button_id = button_id
        self._board = board

        # TODO: Add is_held attribute

    @property
    def name(self) -> str:
        return self._name

    def press(self, duration: float = 0.1):
        self.hold()
        time.sleep(duration)
        self.unhold()

    def hold(self):
        self._board.digital[self._button_id].write(1)

    def unhold(self):
        self._board.digital[self._button_id].write(0)


class Setup:
    def __init__(self, board: Board, buttons: Sequence[Button]):
        self._board = board
        self._buttons = buttons

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
        board = Arduino(f"COM{port}")
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        return cls(board=board, buttons=buttons)

    def __getattr__(self, name):
        # If name is the name of a button - return it.
        if name in self._buttons:
            return self._buttons[name]

        raise AttributeError
