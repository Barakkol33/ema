from utils import get_setup, cli


def integration_basic_test():
    v8_setup = get_setup(is_stub=False)
    v8_setup.toggle_power()


def code_test():
    v8_setup = get_setup(is_stub=True)
    v8_setup.power_on()


def package_test():
    import ema
    ema.Setup


def main():
    integration_basic_test()


if __name__ == "__main__":
    main()
