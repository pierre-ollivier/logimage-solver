from board import Board
from logimage import Logimage
import tkinter as tk


def create_window(logimage: Logimage):
    win = tk.Tk()
    MAX_HEIGHT = 600  # 500 for the logimage, 100 for the constraints
    MAX_WIDTH = 600  # 500 for the logimage, 100 for the constraints
    LOG_WIDTH = logimage.width
    LOG_HEIGHT = logimage.height

    # TODO: add support for non-squared logimages and adjust the place taken by the constraints

    canvas = tk.Canvas(width=601, height=601)
    canvas.create_line(0, 100, 600, 100)
    canvas.create_line(100, 0, 100, 600)

    for vline_index in range(LOG_WIDTH):
        canvas.create_line(100 + (1 + vline_index) * 500/LOG_WIDTH,
                           0, 100 + (1 + vline_index) * 500/LOG_WIDTH, 600)
        canvas.create_text(100 + (1 + vline_index) * 500 /
                           LOG_WIDTH, 0, text=str(logimage.top_constraints[vline_index]))

    for hline_index in range(LOG_HEIGHT):
        canvas.create_line(0, 100 + (1 + hline_index) * 500 /
                           LOG_HEIGHT, 600, 100 + (1 + hline_index) * 500/LOG_WIDTH)
        canvas.create_text(0, 100 + (1 + hline_index) * 500 /
                           LOG_HEIGHT, text=str(logimage.left_constraints[hline_index]))
    canvas.pack()

    win.mainloop()
