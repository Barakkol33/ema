from EMALib import Setup, Button
from stubs import  BoardStub
from collections.abc import Mapping


def get_setup(button_mapping: Mapping[str, int], is_stub=False) -> Setup:
    if is_stub:
        board = BoardStub("Harta")
        buttons = {key: Button(board=board, name=key, button_id=value) for key, value in button_mapping.items()}
        v8_setup = Setup(board, buttons=buttons)
    else:
        v8_setup = Setup.construct_from_button_mapping(port=4, button_mapping=button_mapping)

    return v8_setup


def main():
    button_mapping = {"power": 1, "volume_up": 2, "volume_down": 3}
    v8_setup = get_setup(is_stub=True, button_mapping=button_mapping)
    v8_setup.power.press()


if __name__ == "__main__":
    main()
