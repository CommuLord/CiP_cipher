import tkinter as tk
from PIL import ImageTk, Image

class Op(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        input_label_op = tk.Label(self, text='Программа сделана при помощи:', font='bold')
        input_label_op.pack(pady=10)

        input_label_op = tk.Label(self, text='TKinter', font='bold')
        input_label_op.pack()

        input_label_op = tk.Label(self, text='Bootstrap', font='bold')
        input_label_op.pack()

        image = Image.open("hoho.png")
        resized_image = image.resize((100, 100))
        image_tk = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(self, image=image_tk)
        image_label.image_tk = image_tk
        image_label.pack()

        hello_label4 = tk.Label(self, text='© Кузнецов Т. Е., Шифратор/Дешифратор "CiP" v4.2, 2023')
        hello_label4.pack(side="bottom")

        input_label_op = tk.Label(self, text='Написано на языке программирования Python в 2023 году, релизная версия 4.2',)
        input_label_op.pack(pady=10, side='bottom')