from __future__ import annotations
from collections.abc import Sequence, Mapping
from pyfirmata import Board, Arduino
import time


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
    def construct_from_button_mapping(cls, port: int, button_mapping: Mapping[str, int]) -> Setup:
        board = Arduino(f"COM{port}")
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        return cls(board=board, buttons=buttons)

    def __getattr__(self, name):
        # If name is the name of a button - return it.
        if name in self._buttons:
            return self._buttons[name]

        raise AttributeError
