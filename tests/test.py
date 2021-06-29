from src.ema.core import Setup, Button, SetupConfiguration
from stubs import  BoardStub
from collections.abc import Mapping


CONFIGURATION = SetupConfiguration(port="COM3", button_mapping={"set_button": 3, "ptt_button": 5})


class V8Setup(Setup):
    def power_off(self):
        self.set_button.press(duration=3)

    def power_on(self):
        self.set_button.press(duration=1)

    def show_phone_book(self):
        self.set_button.press()

    def channel_up(self):
        raise NotImplementedError()

    def channel_down(self):
        raise NotImplementedError()


def get_setup(is_stub=False) -> V8Setup:
    if is_stub:
        v8_setup = V8Setup.construct_from_board(board=BoardStub("Harta"), button_mapping=CONFIGURATION.button_mapping)
    else:
        v8_setup = V8Setup.construct_from_configuration(CONFIGURATION)

    return v8_setup


def integration_basic_test():
    v8_setup = get_setup(is_stub=False)
    v8_setup.toggle_power()


def code_test():
    v8_setup = get_setup(is_stub=True)
    v8_setup.power_on()


def cli():
    v8_stub_setup = get_setup(is_stub=True)

    while True:
        command = input(">>>")

        if command == "exit":
            break

        v8_stub_setup.__getattribute__(command)()


def main():
    code_test()


if __name__ == "__main__":
    main()
