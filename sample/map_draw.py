#!/usr/bin/env/python

import tkinter as tk
import tkinter.font as tkfont
import numpy as np

frame_dim = 1000
canvas_dim = 900

def show_map(gen_map):
    map_root = tk.Tk()
    map_frame = MapFrame(master=map_root, drawn_map=gen_map)
    map_frame.mainloop()

class MapFrame(tk.Frame):
    def __init__(self, master, drawn_map):
        super().__init__(master)
        self.pack()
        self.add_quit_button(master)
        self.draw_map(drawn_map)

    def draw_map(self, drawn_map):
        self.map_canvas = tk.Canvas(self, width=frame_dim, height=frame_dim)
        self.map_canvas.pack()
        it = np.nditer(drawn_map.map_array, flags=["multi_index"])
        field_size = canvas_dim / drawn_map.m_s
        while not it.finished:
            if (it[0] == 0):
                fill_color = "blue"
            elif (it[0] == 1):
                fill_color = "orange"
            self.map_canvas.create_rectangle(it.multi_index[0]*field_size, it.multi_index[1]*field_size,
                                            (it.multi_index[0]+1)*field_size+1, (it.multi_index[1]+1)*field_size+1,
                                            fill=fill_color)
            it.iternext()

    def add_quit_button(self, master):
        but_font = tkfont.Font(family="Helvetica", size=16)
        self.quit = tk.Button(self, text="QUIT", fg="black", font=but_font, padx=24, pady=8, command=master.destroy)
        self.quit.pack(side="bottom")
