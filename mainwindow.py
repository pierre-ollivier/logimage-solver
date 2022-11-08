import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from board import Board
import numpy as np
from images import grayscale_img, resize_img, to_board

imPath = "test"

main_window = tk.Tk()
insert_label = tk.Label(text="Ajoutez votre image ici")
insert_label.pack()

image = tk.Label()


def load_image_button_pressed():
    openImageFile()


def validation_button_pressed():
    global imPath, canvas_logimage
    board = board_from_image(imPath)
    draw_board_in_canvas(canvas_logimage, board)


def openImageFile():
    global img, image, imPath
    imPath = filedialog.askopenfilename(initialdir=".", title="Open an image", filetypes=(
        ("Image file", "*.png"), ("Image file", "*.jpeg"), ("Image file", "*.jpg"), ("All File Types", "*.*")))
    print("Image successfully loaded")
    if imPath:
        PILimg = Image.open(imPath)
        PILimg = PILimg.resize((200, 200))
        img = ImageTk.PhotoImage(PILimg)
        image.configure(image=img)

def draw_board_in_canvas(canvas: tk.Canvas, board: Board) -> None:
    data = board.data
    #board.draw()
    for i, j in np.ndindex(data.shape):
        if data[i][j] == 1:
            canvas.create_rectangle(i * 200/6, j * 200/6, (i + 1) * 200/6, (j + 1) * 200/6, fill="#000")
        else:
            canvas.create_rectangle(i * 200/6, j * 200/6, (i + 1) * 200/6, (j + 1) * 200/6, fill="#fff")

def board_from_image(path: str):
    global slider
    img = grayscale_img(path)
    img = resize_img(img, (6, 6)) #TODO
    arr = np.array(img)
    board = to_board(arr, 255 - slider.get())
    return board



load_image_button = tk.Button(
    text="Choisissez une image...", command=load_image_button_pressed)
load_image_button.pack()

image.pack()

slider = tk.Scale(from_=0, to=255, tickinterval=32,
                  length=250, orient="horizontal")
slider.pack()

validation_button = tk.Button(
    text="Valider", command=validation_button_pressed)
validation_button.pack()

canvas_logimage = tk.Canvas(width=202, height=202)
canvas_logimage.pack()

LINES_COUNT = 6
COLUMNS_COUNT = 6
for line_number in range(LINES_COUNT + 1):
    print(line_number)
    print((0, line_number * 200/LINES_COUNT, 200, line_number * 200/LINES_COUNT))
    canvas_logimage.create_line(0, line_number * 200/LINES_COUNT, 200, line_number * 200/LINES_COUNT)
for column_number in range(COLUMNS_COUNT + 1):
    canvas_logimage.create_line(column_number * 200/COLUMNS_COUNT, 0, column_number * 200/COLUMNS_COUNT, 200)

main_window.mainloop()
