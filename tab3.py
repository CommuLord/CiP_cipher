import tkinter as tk
from tkinter import messagebox


class Tab3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.english_alphabet = "abcdefghijklmnopqrstuvwxyz"

        language_label = tk.Label(self, text='Выберите язык:', font='bold')
        language_label.pack()
        self.language_var = tk.StringVar()
        self.language_var.set('Английский')

        self.language_option_menu = tk.OptionMenu(self, self.language_var, 'Русский', 'Английский')
        self.language_option_menu.pack()

        input_label_vigenere = tk.Label(self, text='Введите текст:', font='bold')
        input_label_vigenere.pack()

        self.input_text_vigenere_entry = tk.Entry(self, width=30)
        self.input_text_vigenere_entry.pack()

        key_label = tk.Label(self, text='Введите ключ:')
        key_label.pack()

        self.key_entry = tk.Entry(self, width=30)
        self.key_entry.pack()

        encrypt_button_vigenere = tk.Button(self, text='Зашифровать', command=self.encrypt_text)
        encrypt_button_vigenere.pack(pady=10)

        encrypted_label_vigenere = tk.Label(self, text='Расшифрованный текст:', font='bold')
        encrypted_label_vigenere.pack()

        self.encrypted_text_vigenere_entry = tk.Entry(self, width=30)
        self.encrypted_text_vigenere_entry.pack()

        decrypt_button_vigenere = tk.Button(self, text='Расшифровать', command=self.decrypt_text)
        decrypt_button_vigenere.pack(pady=10)

        hello_label2 = tk.Label(self, text='© Кузнецов Т. Е., Шифратор/Дешифратор "CiP" v4.2, 2023')
        hello_label2.pack(side="bottom")

    def encrypt_text(self):
        plaintext = self.input_text_vigenere_entry.get().lower()
        key = self.key_entry.get().lower()

        if not self.validate_input(plaintext, key):
            return

        encrypted_text = ""
        key_index = 0
        alphabet = self.get_alphabet()

        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord(alphabet[0])
                char_index = alphabet.index(char)
                encrypted_char = alphabet[(char_index + shift) % len(alphabet)]
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char

        self.encrypted_text_vigenere_entry.delete(0, tk.END)
        self.encrypted_text_vigenere_entry.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        # Получаем зашифрованный текст и ключ из соответствующих полей ввода
        encrypted_text = self.encrypted_text_vigenere_entry.get().lower()
        key = self.key_entry.get().lower()

        # Проверяем валидность введенных данных
        if not self.validate_input(encrypted_text, key):
            return

        decrypted_text = ""  # Инициализируем переменную для расшифрованного текста
        key_index = 0  # Индекс символа ключа
        alphabet = self.get_alphabet()  # Получаем алфавит

        # Проходим по каждому символу зашифрованного текста
        for char in encrypted_text:
            if char.isalpha():  # Если символ является буквой
                shift = ord(key[key_index % len(key)]) - ord(alphabet[0])  # Вычисляем сдвиг на основе символа ключа
                char_index = alphabet.index(char)  # Находим индекс текущего символа в алфавите
                decrypted_char = alphabet[(char_index - shift) % len(alphabet)]  # Расшифровываем символ
                decrypted_text += decrypted_char  # Добавляем расшифрованный символ к результату
                key_index += 1  # Увеличиваем индекс символа ключа для следующей итерации
            else:  # Если символ не является буквой, добавляем его без изменений
                decrypted_text += char

        # Очищаем поле ввода и добавляем туда расшифрованный текст
        self.input_text_vigenere_entry.delete(0, tk.END)
        self.input_text_vigenere_entry.insert(tk.END, decrypted_text)

    def validate_input(self, text, key):
        alphabet = self.get_alphabet()
        for char in text:
            if not char.isalpha() or char not in alphabet:
                messagebox.showwarning("Ошибка", "Недопустимый символ в тексте")
                return False

        if not key:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите ключ")
            return False

        return True

    def get_alphabet(self):
        language_var = self.language_var.get()
        if language_var == 'Русский':
            return self.russian_alphabet
        else:
            return self.english_alphabet