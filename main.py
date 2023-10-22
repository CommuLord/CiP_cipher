import tkinter as tk
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3
from tab4 import Tab4
from op import Op
import ttkbootstrap as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style('custom')
        style.theme_use('custom2')

        self.title('Шифратор/Дешифратор "CiP" v4.2')
        self.iconbitmap(default="logo.ico")
        self.geometry("485x400")
        self.wm_minsize(300, 300)

        self.tab_control = ttk.Notebook(self)
        self.tab1 = Tab1(self.tab_control)
        self.tab2 = Tab2(self.tab_control)
        self.tab3 = Tab3(self.tab_control)
        self.tab4 = Tab4(self.tab_control)
        self.op = Op(self.tab_control)

        self.tab_control.add(self.tab1, text='Морзе')
        self.tab_control.add(self.tab2, text='Цезарь')
        self.tab_control.add(self.tab3, text='Виженер')
        self.tab_control.add(self.tab4, text='Атбаш')
        self.tab_control.add(self.op, text='О программе')
        self.tab_control.pack(expand=True, fill='both')

        self.change_style_button1 = tk.Button(self, text='Светлая тема', command=self.change_style1)
        self.change_style_button1.pack(side='left', padx=1, pady=1)

        self.change_style_button = tk.Button(self, text='Тёмная тема', command=self.change_style)
        self.change_style_button.pack(side='left', padx=1, pady=1)

        self.change_style_button = tk.Button(self, text='Сырная тема', command=self.change_style3)
        self.change_style_button.pack(side='left', padx=1, pady=1)

    def change_style(self):
        style = ttk.Style('custom')
        style.theme_use('custom3')
    def change_style1(self):
        style = ttk.Style('custom')
        style.theme_use('custom2')

    def change_style3(self):
        style = ttk.Style('custom')
        style.theme_use('cheese')

if __name__ == '__main__':
    app = App()
    app.mainloop()