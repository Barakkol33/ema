from collections.abc import Sequence, Mapping

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
        print(f"Press: {self._port} -> {self._button_id}")

    @classmethod
    def from_button_mapping(cls, port, button_mapping: Mapping[str, int]):
        return [cls(port=port, name=key, button_id=value) for key,value in button_mapping.items()]


class Setup:
    def __init__(self, port: int, buttons: Sequence[Button]):
        self._port = port
        self._buttons = {button.name: button for button in buttons}

    @classmethod
    def from_info(cls, port: int, button_mapping: Mapping[str, int]):
        buttons = Button.from_button_mapping(port=port, button_mapping=button_mapping)
        return cls(port=port, buttons=buttons)

    def get_button(self, button_name):
        # TODO: Raise indicative exception?
        return self._buttons[button_name]


def main():
     button_mapping = {"button_mapping": {"power": 1, "volume_up": 2, "volume_down": 3}}


if __name__ == "__main__":
    main()

"""
Usage:
import EMALib

# Press the power button
setup = EMALib.Setup.get_setup("First")
setup.get_button("power").press()
SETUPS = [{"name": "First", "buttons": {"power": 1, "volume_up": 2, "volume_down": 3}}]

# Protocol

## Request format:
CMD (byte) | Payload

### Request CMDs:
1 - Press Button

### Press Button Command format:
CMD (byte) (=1) | Duration (byte) | Button name length (byte) | Button name

## Response format:
Code (byte)

### Response Codes:
101 - OK
102 - Button name does not exist
103 - Internal Error 





"""
