from src.ema.core import Setup


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
