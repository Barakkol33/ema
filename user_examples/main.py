from ema import Setup


def main():
    setup = Setup.construct_from_configuration_file("example.yml")
    setup.set_button.press()


if __name__ == "__main__":
    main()
