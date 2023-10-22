import tkinter as tk
from tkinter import messagebox

class Tab2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def encrypt_c():
            text = input_text_cesar_entry.get()
            key = shift_value.get()
            encrypted_text = ""
            language = language_var.get()

            if not key.isdigit():
                messagebox.showwarning('Ошибка', 'Введите число в поле сдвига')
                return

            key = int(key)

            if language == 'Английский':
                for char in text:
                    if char.isalpha():
                        if char.islower():
                            encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
                        else:
                            encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
                    else:
                        encrypted_text += char

                for char in text:
                    if char.isalpha() and char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        messagebox.showwarning('Ошибка', f'Символ "{char}" не поддерживается')
                        return

            elif language == 'Русский':
                russian_alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                russian_alphabet_upper = russian_alphabet_lower.upper()

                for char in text:
                    if char.isalpha():
                        if char in russian_alphabet_lower:
                            index = russian_alphabet_lower.index(char)
                            encrypted_text += russian_alphabet_lower[(index + key) % len(russian_alphabet_lower)]
                        elif char in russian_alphabet_upper:
                            index = russian_alphabet_upper.index(char)
                            encrypted_text += russian_alphabet_upper[(index + key) % len(russian_alphabet_upper)]
                    else:
                        encrypted_text += char

                for char in text:
                    if char.isalpha() and char not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                        messagebox.showwarning('Ошибка', f'Символ "{char}" не поддерживается')
                        return

            encrypted_text_cesar_entry.delete(0, tk.END)
            encrypted_text_cesar_entry.insert(0, encrypted_text)

        def decrypt_c():
            encrypted_text = encrypted_text_cesar_entry.get()
            key = shift_value.get()
            decrypted_text = ""
            language = language_var.get()

            if not key.isdigit():
                messagebox.showwarning('Ошибка', 'Введите число в поле сдвига')
                return

            key = int(key)

            if language == 'Английский':
                for char in encrypted_text:
                    if char.isalpha():
                        if char.islower():
                            decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
                        else:
                            decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
                    else:
                        decrypted_text += char

                for char in encrypted_text:
                    if char.isalpha() and char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        messagebox.showwarning('Ошибка', f'Символ "{char}" не поддерживается')
                        return

            elif language == 'Русский':
                russian_alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                russian_alphabet_upper = russian_alphabet_lower.upper()

                for char in encrypted_text:
                    if char.isalpha():
                        if char in russian_alphabet_lower:
                            index = russian_alphabet_lower.index(char)
                            decrypted_text += russian_alphabet_lower[(index - key) % len(russian_alphabet_lower)]
                        elif char in russian_alphabet_upper:
                            index = russian_alphabet_upper.index(char)
                            decrypted_text += russian_alphabet_upper[(index - key) % len(russian_alphabet_upper)]
                    else:
                        decrypted_text += char

                for char in encrypted_text:
                    if char.isalpha() and char not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                        messagebox.showwarning('Ошибка', f'Символ "{char}" не поддерживается')
                        return

            input_text_cesar_entry.delete(0, tk.END)
            input_text_cesar_entry.insert(0, decrypted_text)

        languages = ['Английский', 'Русский']
        language_var = tk.StringVar()
        language_var.set(languages[0])

        language_label = tk.Label(self, text='Выберите язык:', font='bold')
        language_label.pack()

        language_menu = tk.OptionMenu(self, language_var, *languages)
        language_menu.pack()

        input_label_cesar = tk.Label(self, text='Введите текст:', font='bold')
        input_label_cesar.pack()

        input_text_cesar_entry = tk.Entry(self, width=30)
        input_text_cesar_entry.pack()

        shift_label = tk.Label(self, text='Введите сдвиг:')
        shift_label.pack()

        shift_value = tk.Entry(self, width=5)
        shift_value.pack()

        encrypt_button_cesar = tk.Button(self, text='Зашифровать', command=encrypt_c)
        encrypt_button_cesar.pack(pady=10)

        encrypted_label_cesar = tk.Label(self, text='Зашифрованный текст:', font='bold')
        encrypted_label_cesar.pack()

        encrypted_text_cesar_entry = tk.Entry(self, width=30)
        encrypted_text_cesar_entry.pack()

        decrypt_button_cesar = tk.Button(self, text='Расшифровать', command=decrypt_c)
        decrypt_button_cesar.pack(pady=10)

        hello_label1 = tk.Label(self, text='© Кузнецов Т. Е., Шифратор/Дешифратор "CiP" v4.2, 2023')
        hello_label1.pack(side="bottom")