"""
Core classes and features for ema library.
"""
from __future__ import annotations
import time
from collections.abc import Sequence, Mapping
from pyfirmata import Board, Arduino
import serial.tools.list_ports
import yaml


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
        """
        Press button for a given duration.
        """
        self.hold()
        time.sleep(duration)
        self.unhold()

    def hold(self):
        """
        After called, button will stay pressed until unhold() is called.
        """
        self._board.digital[self._button_id].write(1)

    def unhold(self):
        self._board.digital[self._button_id].write(0)


class Setup:
    def __init__(self, board: Board, buttons: Sequence[Button]):
        self._board = board
        self._buttons = buttons

    @staticmethod
    def choose_available_port():
        """
        CLI utility for automatically choosing a COM port.
        """
        connected_ports = list(serial.tools.list_ports.comports())

        if 0 == len(connected_ports):
            raise RuntimeError(f"No connected COM ports found")

        elif 1 == len(connected_ports):
            port = connected_ports[0]

        else:
            print(F"Available COM ports:")
            for index, port in enumerate(connected_ports):
                print(f"{index}. {port}")

            choice = int(input(f"\nPlease select COM port: "))
            while choice >= len(connected_ports) or 0 > choice:
                choice = int(input(f"Invalid choice! \nPlease select COM port: "))
            port = connected_ports[choice]

        print(F'Connecting to "{port}"')
        return port

    @classmethod
    def construct_from_configuration_file(cls, filename: str) -> Setup:
        return cls.construct_from_configuration(SetupConfiguration.load_from_file(filename))

    @classmethod
    def construct_from_configuration(cls, configuration: SetupConfiguration) -> Setup:
        return cls.construct_from_port(port=configuration.port, button_mapping=configuration.button_mapping)

    @classmethod
    def construct_from_port(cls, port: str, button_mapping: Mapping[str, int]) -> Setup:
        return cls.construct_from_board(board=Arduino(port), button_mapping=button_mapping)

    @classmethod
    def construct_from_board(cls, board: Board, button_mapping: Mapping[str, int]) -> Setup:
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        return cls(board=board, buttons=buttons)

    def __getattr__(self, name):
        # If name is the name of a button - return it.
        if name in self._buttons:
            return self._buttons[name]

        raise AttributeError


class SetupConfiguration:
    def __init__(self, port: str, button_mapping: Mapping[str, int]):
        self.port = port
        self.button_mapping = button_mapping

    def save_to_file(self, filename):
        with open(filename, "w") as output_file:
            yaml.dump(dict(port=self.port, button_mapping=self.button_mapping), output_file)

    @classmethod
    def load_from_file(cls, filename) -> SetupConfiguration:
        with open(filename, 'r') as input_file:
            contents = yaml.safe_load(input_file)
            return cls(port=contents["port"], button_mapping=contents["button_mapping"])
