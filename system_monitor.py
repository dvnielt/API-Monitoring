import tkinter
from tkinter import *
from remote_tools import Statistics
import json
import requests

def color_value(value):
    if 25 < value < 75:
        return 'blue'
    elif 0 <= value < 25:
        return 'grey'
    elif 75 <= value < 100:
        return 'blue'


gui = tkinter.Tk()
gui.title('System Monitor (Auto Update 5s)')
gui.geometry('500x100')
gui.resizable(False, False)

main_title = Label(gui,
                   text="System Monitor (Auto Update 5s)",
                   font='Arial 10 bold',
                   width=250)
main_title.pack()

cpu_use = Label(gui,
                width=500,
                font='Arial 15',
                bg=color_value((int(Statistics.cpu_usage(self=None)))))
cpu_use.pack()

disk_space = Label(gui,
                   width=500,
                   font='Arial 15',
                   bg=color_value(int(Statistics.disk_usage(self=None))))
disk_space.pack()

memory = Label(gui,
               width=500,
               font='Arial 15',
               bg=color_value(int(Statistics.mem_usage(self=None))))
memory.pack()


def stats_update(self=None):
    cpu = requests.get("http://localhost:8000/cpu").json()
    cpu_use['text'] = f'CPU Usage % : {cpu}'
    disk = requests.get("http://localhost:8000/disk").json()
    disk_space['text'] = f'DISK Usage % : {disk}'
    mem = requests.get("http://localhost:8000/mem").json()
    memory['text'] = f'MEM Usage % : {mem}'

    gui.after(5000, stats_update)


stats_update()
gui.mainloop()
