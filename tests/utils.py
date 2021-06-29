from src.ema.core import SetupConfiguration
from stubs import BoardStub
from v8setup import V8Setup


CONFIGURATION = SetupConfiguration.load_from_file("v8.yml")


def get_setup(is_stub=False) -> V8Setup:
    if is_stub:
        v8_setup = V8Setup.construct_from_board(board=BoardStub("Harta"), button_mapping=CONFIGURATION.button_mapping)
    else:
        v8_setup = V8Setup.construct_from_configuration(CONFIGURATION)

    return v8_setup


def cli(setup):
    while True:
        command = input(">>>")

        if command == "exit":
            break

        setup.__getattribute__(command)()
