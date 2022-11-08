import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

imPath = "test"

main_window = tk.Tk()
insert_label = tk.Label(text="Ajoutez votre image ici")
insert_label.pack()

image = tk.Label()


def load_image_button_pressed():
    openImageFile()


def validation_button_pressed():
    print("Button pressed")


def openImageFile():
    global img, image
    imPath = filedialog.askopenfilename(initialdir=".", title="Open an image", filetypes=(
        ("Image file", "*.png"), ("Image file", "*.jpeg"), ("Image file", "*.jpg"), ("All File Types", "*.*")))
    print("Image successfully loaded")
    if imPath:
        PILimg = Image.open(imPath)
        PILimg = PILimg.resize((200, 200))
        img = ImageTk.PhotoImage(PILimg)
        image.configure(image=img)


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

main_window.mainloop()
