

# Setups
SETUPS = [{"name": "First", "buttons": {"power": 1, "volume_up": 2, "volume_down": 3}}]


class Button(object):
    def __init__(self, name, button_id):
        self._name = name

    @property
    def name(self):
        return self._name

    def press(self):
        button_id = 
        # TODO: Understand which COM port Arduino is in


        # TODO: Communicate with Arduino
        arduino.send("")

        pass


class Setup(object):
    def __init__(self, name, buttons):
        self._name = name
        self._buttons = buttons

    @classmethod
    def from_info(cls, info):
        # Create button objects
        # TODO: Check if button name in dictionary
        button_details = [button_details for button_name in info["buttons"]][0]
		buttons = [Button(name=button_details[0], button_id=button_details[1])]

        return cls(info["name"], buttons)

    def get_button(self, wanted_button_name):
        for button in self._buttons:
            if button.name == wanted_button_name:
                return button

        raise ValueError(f"Button name {wanted_button_name} does not exist.")

    @classmethod
    def get_setup(cls, name):
        for setup_info in SETUPS:
            if setup_info["name"] == name:
                return cls.from_info(setup_info)
        raise ValueError(f"Setup {name} not found")


"""
Usage:
import EMALib

# Press the power button
setup = EMALib.Setup.get_setup("First")
setup.get_button("power").press()

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
