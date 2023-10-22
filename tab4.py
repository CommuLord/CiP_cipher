import tkinter as tk
from tkinter import messagebox

class Tab4(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.english_alphabet = "abcdefghijklmnopqrstuvwxyz"

        hello_label3 = tk.Label(self, text='© Кузнецов Т. Е., Шифратор/Дешифратор "CiP" v4.2, 2023')
        hello_label3.pack(side="bottom")

        def atbash_cipher(text, alphabet):
            result = ""
            for char in text:
                if char.isalpha():
                    if char.isupper():
                        result += chr(ord(alphabet[-1]) - (ord(char) - ord(alphabet[0])))
                    else:
                        result += chr(ord(alphabet[-1]) - (ord(char) - ord(alphabet[0])))
                else:
                    result += char
            return result

        def encrypt():
            text = input_text4.get()
            language_var = language_var4.get()
            if language_var == 'Русский':
                alphabet = self.russian_alphabet
                if any(char in self.english_alphabet for char in text):
                    messagebox.showwarning('Ошибка', 'Выбран русский язык, но введен английский текст.')
                    return
            else:
                alphabet = self.english_alphabet
                if any(char in self.russian_alphabet for char in text):
                    messagebox.showwarning('Ошибка', 'Выбран английский язык, но введен русский текст.')
                    return
            encrypted_text = atbash_cipher(text, alphabet)
            output_text4.delete(0, tk.END)
            output_text4.insert(tk.END, encrypted_text)

        def decrypt():
            text = output_text4.get()
            language_var = language_var4.get()
            if language_var == 'Русский':
                alphabet = self.russian_alphabet
                if any(char in self.english_alphabet for char in text):
                    messagebox.showwarning('Ошибка', 'Выбран русский язык, но введен английский текст.')
                    return
            else:
                alphabet = self.english_alphabet
                if any(char in self.russian_alphabet for char in text):
                    messagebox.showwarning('Ошибка', 'Выбран английский язык, но введен русский текст.')
                    return
            decrypted_text = atbash_cipher(text, alphabet)
            input_text4.delete(0, 'end')
            input_text4.insert('end', decrypted_text)

        language_label4 = tk.Label(self, text='Выберите язык:', font='bold')
        language_label4.pack()
        language_var4 = tk.StringVar()
        language_var4.set('Английский')

        language_option_menu4 = tk.OptionMenu(self, language_var4, 'Русский', 'Английский')
        language_option_menu4.pack()

        input_label4 = tk.Label(self, text="Введите текст:", font='bold')
        input_label4.pack()

        input_text4 = tk.Entry(self, width=30)
        input_text4.pack()

        encrypt_button4 = tk.Button(self, text="Зашифровать", command=encrypt)
        encrypt_button4.pack(pady=10)

        output_label4 = tk.Label(self, text="Результат:", font='bold')
        output_label4.pack()

        output_text4 = tk.Entry(self, width=30)
        output_text4.pack()

        decrypt_button4 = tk.Button(self, text="Расшифровать", command=decrypt)
        decrypt_button4.pack(pady=10)