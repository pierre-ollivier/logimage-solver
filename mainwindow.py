import tkinter as tk

main_window = tk.Tk()
insert_label = tk.Label(text="Ajoutez votre image ici")
insert_label.pack()


def validation_button_pressed():
    print("Button pressed")


validation_button = tk.Button(
    text="Valider", command=validation_button_pressed)
validation_button.pack()

main_window.mainloop()
