from EMALib import Setup, Button
from stubs import  BoardStub
from collections.abc import Mapping


class V8Setup(Setup):
    def toggle_power(self):
        self.set_button.press(duration=3)

    def show_phone_book(self):
        self.set_button.press(duration=0.5)


def get_setup(button_mapping: Mapping[str, int], is_stub=False) -> Setup:
    if is_stub:
        board = BoardStub("Harta")
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        v8_setup = Setup(board, buttons=buttons)
    else:
        v8_setup = Setup.construct_from_button_mapping(port=4, button_mapping=button_mapping)

    return v8_setup


def integration_basic_test():
    v8_button_mapping = {"set_button": 3, "answer_button": 5}
    v8_setup = V8Setup.construct_from_button_mapping(port=4, button_mapping=v8_button_mapping)
    v8_setup.toggle_power()


def code_test():
    v8_button_mapping = {"set": 3, "answer": 5}
    v8_setup = get_setup(is_stub=True, button_mapping=v8_button_mapping)
    v8_setup.power.press()


def main():
    integration_basic_test()


if __name__ == "__main__":
    main()
