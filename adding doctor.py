
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Ahmed Mohamed\Desktop\Khaled\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1109x794")
window.configure(bg = "#343E71")


canvas = Canvas(
    window,
    bg = "#343E71",
    height = 794,
    width = 1109,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    554.0,
    397.0,
    image=image_image_1
)

canvas.create_rectangle(
    778.9999677625146,
    345.0,
    1099.999755859375,
    348.0633326052027,
    fill="#202854",
    outline="")

canvas.create_text(
    842.0,
    292.0,
    anchor="nw",
    text="Doctor’s Name",
    fill="#FFFFFF",
    font=("Inter", 28 * -1)
)

canvas.create_text(
    467.0,
    6.0,
    anchor="nw",
    text="Our Pharmacy",
    fill="#FFFFFF",
    font=("Inter", 28 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=2.0,
    y=471.0,
    width=45.0,
    height=31.0
)

canvas.create_rectangle(
    76.0,
    220.0,
    751.0,
    742.0,
    fill="#2F396B",
    outline="")

canvas.create_text(
    214.0,
    515.0,
    anchor="nw",
    text="Doctor’s Password",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_rectangle(
    353.0,
    498.0,
    611.0,
    536.0,
    fill="#202854",
    outline="")

canvas.create_text(
    214.0,
    443.0,
    anchor="nw",
    text="Doctor’s Username",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_rectangle(
    353.0,
    430.0,
    611.0,
    468.0,
    fill="#202854",
    outline="")

canvas.create_text(
    227.0,
    371.0,
    anchor="nw",
    text="Doctor’s DoB",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_rectangle(
    353.0,
    362.0,
    611.0,
    400.0,
    fill="#202854",
    outline="")

canvas.create_text(
    221.0,
    305.0,
    anchor="nw",
    text="Doctor’s Name",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=337.0,
    y=603.0,
    width=160.0,
    height=44.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=3.0,
    y=341.0,
    width=41.0,
    height=41.0
)

canvas.create_rectangle(
    353.0,
    294.0,
    611.0,
    332.0,
    fill="#202854",
    outline="")
window.resizable(False, False)
window.mainloop()
