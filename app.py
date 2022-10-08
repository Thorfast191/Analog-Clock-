import tkinter
import tkinter as ui
import math
import time


window = ui.Tk()
window.title("Analog Clock")
window.geometry("400x400")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # updating seconds hand
    seconds_x = sec_hand_len * math.sin(math.radians(seconds * 6)) + x
    seconds_y = -1 * sec_hand_len * math.cos(math.radians(seconds * 6)) + y
    canvas.coords(sec_hand, x, y, seconds_x, seconds_y)

    # updating minutes hand
    minutes_x = min_hand_len * math.sin(math.radians(minutes * 6)) + x
    minutes_y = -1 * min_hand_len * math.cos(math.radians(minutes * 6)) + y
    canvas.coords(min_hand, x, y, minutes_x, minutes_y)

    # updating hours hand
    hours_x = hour_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + x
    hours_y = -1 * hour_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + y
    canvas.coords(hour_hand, x, y, hours_x, hours_y)

    window.after(1000, update_clock)

canvas = ui.Canvas(window ,width=500, height=500, bg= "black")
canvas.pack(expand=True, fill="both")

bg = ui.PhotoImage(file="dial_400.png")
canvas.create_image(200,200,image=bg)

x = 200
y = 200

sec_hand_len = 90
min_hand_len = 75
hour_hand_len = 60


sec_hand= canvas.create_line(200,200,200+sec_hand_len,200+sec_hand_len,width=1.5,fill="red")
min_hand= canvas.create_line(200,200,200+min_hand_len,200+min_hand_len,width=2,fill="white")
hour_hand= canvas.create_line(200,200,200+hour_hand_len,200+hour_hand_len,width=4,fill="red")


update_clock()
window.mainloop()





