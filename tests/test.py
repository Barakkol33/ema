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


def package_test():
    import ema
    ema.Setup


def main():
    package_test()


if __name__ == "__main__":
    main()
