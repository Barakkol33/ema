from EMALib import Setup, Button
from stubs import BoardStub
from collections.abc import Mapping


class V8Setup(Setup):
    def toggle_power(self):
        self.set_button.press(duration=3)

    def show_phone_book(self):
        self.set_button.press()

    def answer(self):
        self.answer_button.press()


def get_setup(button_mapping: Mapping[str, int], is_stub=False) -> Setup:
    if is_stub:
        board = BoardStub("Harta")
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        generic_setup = Setup(board, buttons=buttons)
    else:
        generic_setup = Setup.construct_from_button_mapping(port=4, button_mapping=button_mapping)

    return generic_setup


def integration_basic_test():
    v8_button_mapping = {"set_button": 3, "answer_button": 5}
    v8_setup = V8Setup.construct_from_button_mapping(port=4, button_mapping=v8_button_mapping)
    v8_setup.toggle_power()


def code_test():
    v8_button_mapping = {"set_button": 3, "answer_button": 5}
    generic_setup = get_setup(is_stub=True, button_mapping=v8_button_mapping)
    generic_setup.set_button.press()


def cli():
    v8_button_mapping = {"set_button": 3, "answer_button": 5}
    board = BoardStub("Harta")
    buttons = {key: Button(board=board, name=key, button_id=value) for key, value in v8_button_mapping.items()}
    v8_stub_setup = V8Setup(board, buttons=buttons)

    while True:
        command = input(">>>")

        if command == "exit":
            break

        v8_stub_setup.__getattribute__(command)()


def main():
    cli()


if __name__ == "__main__":
    main()
