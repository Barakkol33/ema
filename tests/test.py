"""
Tests and usages of ema library.
"""
from utils import get_setup, cli


def integration_basic_test():
    v8_setup = get_setup(is_stub=False)
    v8_setup.power_on()


def code_only_sanity_test():
    """
    Tests basic features: Loading setup from configuration file,
       getting button by name, and pressing the button.
    """
    v8_setup = get_setup(is_stub=True)
    v8_setup.power_on()


def package_sanity_test():
    import ema
    print(ema.Setup)


def cli_sanity_test():
    cli(get_setup(is_stub=True))


def main():
    cli_sanity_test()


if __name__ == "__main__":
    main()
