import tkinter as tk
from tkinter import messagebox

class Tab1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def encrypt_text(input_text, encrypted_text, language):
            text = input_text.get().upper()
            encrypted_message = ''
            morse_code = get_morse_code(language)
            for char in text:
                if char in morse_code:
                    encrypted_message += morse_code[char] + ' '
                else:
                    messagebox.showwarning('Ошибка', f'Символ "{char}" не поддерживается')
                    return

            encrypted_text.delete(0, tk.END)
            encrypted_text.insert(0, encrypted_message)

        def decrypt_text(encrypted_text, input_text, language):
            morse_code = get_morse_code(language)
            morse_code_dict = {v: k for k, v in morse_code.items()}
            encrypted_message = encrypted_text.get().split(' ')
            decrypted_message = ''

            for code in encrypted_message:
                if code in morse_code_dict:
                    decrypted_message += morse_code_dict[code]
                elif code == '':
                    decrypted_message += ''
                else:
                    messagebox.showwarning('Ошибка', f'Код "{code}" не поддерживается')
                    return

            input_text.delete(0, tk.END)
            input_text.insert(0, decrypted_message)

        def get_morse_code(language):
            morse_code_ru = {
                'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.',
                'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
                'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..',
                'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
                'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
                'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
                'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
                'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
            }
            morse_code_en = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                '0': '-----',
            }
            if language.lower() == 'русский':
                return morse_code_ru
            else:
                return morse_code_en


        language_label = tk.Label(self, text='Выберите язык:', font='bold')
        language_label.pack()

        self.language_var = tk.StringVar()
        self.language_var.set('Английский')

        language_optionmenu = tk.OptionMenu(self, self.language_var, 'Русский', 'Английский')
        language_optionmenu.pack()

        input_label = tk.Label(self, text='Введите текст:', font='bold')
        input_label.pack()

        self.input_text = tk.Entry(self, width=30)
        self.input_text.pack()

        encrypt_button = tk.Button(self, text='Зашифровать',
                                   command=lambda: encrypt_text(self.input_text, self.encrypted_text,
                                                                self.language_var.get()))
        encrypt_button.pack(pady=10)

        encrypted_label = tk.Label(self, text='Зашифрованный текст:', font='bold')
        encrypted_label.pack()
        self.encrypted_text = tk.Entry(self, width=30)
        self.encrypted_text.pack()

        decrypt_button = tk.Button(self, text='Расшифровать',
                                   command=lambda: decrypt_text(self.encrypted_text, self.input_text,
                                                               self.language_var.get()))
        decrypt_button.pack(pady=10)

        hello_label = tk.Label(self, text='© Кузнецов Т. Е., Шифратор/Дешифратор "CiP" v4.2, 2023')
        hello_label.pack(side="bottom")