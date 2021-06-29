from tkinter import *
from src.ema import core as emalib


def toggle_on_off_button(on_off_button, is_on: list, on_command, off_command):
    if is_on[0]:
        on_off_button.config(text='On')
        if off_command:
            off_command()
        is_on[0] = False
    else:
        on_off_button.config(text='Off')
        if on_command:
            on_command()
        is_on[0] = True


def press_5_ptt():
    print("5 PTT!")


def hold_button(event):
    print("Holding button...")


def release_button(event):
    print("Releasing button...")


def create_hold_down_button(window, button_text, column=1, row=0, command=None):
    hold_down_button = Button(window, text=button_text, bd=5, padx=10, pady=10)
    hold_down_button.grid(column=column, row=row)

    if command:
        hold_down_button.config(command=command)

    hold_down_button.bind('<ButtonPress-1>', hold_button)
    hold_down_button.bind('<ButtonRelease-1>', release_button)

    return hold_down_button


def create_button(window, button_text, column=1, row=0, command=None):
    button = Button(window, text=button_text, command=command, bd=5, padx=10, pady=10)
    button.grid(column=column, row=row)

    return button


def On():
    print("On")


def Off():
    print("Off")


def create_tk_window(title, width, height):
    root = Tk()

    root.title(title)
    root.geometry(F"{width}x{height}")

    return root


def main():
    is_device_on = [False]

    main_window = create_tk_window('Radio V8!', 600, 400)

    device_on_off_button = \
        create_button(main_window, "On", 1, 0, command=lambda: toggle_on_off_button(device_on_off_button, is_device_on, On, Off))
    ptt_button = create_hold_down_button(main_window, "Hold PTT", 2, 0)
    button_5_ptt = create_button(main_window, "5 x PTT", 3, 0, command=press_5_ptt)

    main_window.mainloop()


if __name__ == '__main__':
    main()







