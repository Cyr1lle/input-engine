import tkinter as tk
import time
import pyautogui
from tkinter import messagebox
import keyboard

func = []
editorfunc = []
file_path = "../datafunc.txt"
posx = 0
posy = 0

def performfunc():
    for i in range(len(func)):
        if func[i][0] == 'MOUSE':
            if func[i][1] == 'LMB':
                pyautogui.click(x=int(func[i][2]), y=int(func[i][3]))
            elif func[i][1] == 'RMB':
                pyautogui.click(x=int(func[i][2]), y=int(func[i][3]))
            else:
                messagebox.showerror("Perform Error", ("Unknown mouse button in line", i+1))

        elif func[i][0] == 'KEYBOARD':
            if func[i][1] == 'WRITE':
                keyboard.write(func[i][2])
            elif func[i][1] == 'PRESS':
                keyboard.press(func[i][2])
            elif func[i][1] == 'RELEASE':
                keyboard.release(func[i][2])
            else:
                messagebox.showerror("Perform Error", ("Unknown key in line", i + 1))
        elif func[i][0] == 'WAIT':
            time.sleep(int(func[i][1]))


root = tk.Tk()
root.title("InputEngine v0.2.0")
root.geometry('600x400')

#File Functions

def debug():
    print('Шаг: ', editorfunc)
    print('Функция: ', func)
    print('Файл:', file_path)
def export():
    func = []
    file_path = '../' + load_name.get()
    with open(file_path, "r", encoding="utf-8") as file:
        # Читаем файл построчно и добавляем каждую строку в список
        for line in file:
            # Удаляем символ новой строки в конце строки
            words = line.strip().split()
            func.append(words)
    print(file_path, func)
    name_file.update()

def get_pos():
    messagebox.showinfo("Получение координат", 'Вы'
                                                'активировали режим получения координат.'
                                                ' После закрытия этого окна, наведите ваш курсор'
                                                'в нужную точку на мониторе и нажмите клавишу'
                                                ' R.')
    keyboard.wait('R')
    print(pyautogui.position())
    messagebox.showinfo("Получение координат", 'Координаты записаны')

#Editor Functions

def refresh():
    global editorfunc
    editorfunc = []
def complete():
    global editorfunc
    func.append(editorfunc)
    editorfunc = []
def add_mouse():
    editorfunc.append('MOUSE')
def add_keyboard():
    editorfunc.append('KEYBOARD')
def add_write():
    a = writeEntry.get()
    editorfunc.append('WRITE')
    editorfunc.append(a)
def add_release():
    a = releaseEntry.get()
    editorfunc.append('RELEASE')
    editorfunc.append(a)
def add_press():
    a = pressEntry.get()
    editorfunc.append('PRESS')
    editorfunc.append(a)
def add_rmb()


#File
title_file = tk.Label(root, text='Настройки файла')
title_file.place(x=10, y=5)
new_button = tk.Button(root, text='Новая функция', )
new_button.place(x=10, y=30)
new_name = tk.Entry(root, width=21)
new_name.place(x=110, y=33)
load_button = tk.Button(root, text='Экспорт из .txt ', command=export)
load_button.place(x=10, y=57)
load_name = tk.Entry(root, width=21)
load_name.place(x=110, y=60)
tag_name = tk.Label(root, text='Активное сохранение:')
tag_name.place(x=10, y=85)
name_file = tk.Label(root, text=file_path)
name_file.place(x=10, y=100)
file_disable = tk.Button(root, text='Деактивировать')
file_disable.place(x=140, y=90)

#Perform
title_perform = tk.Label(root, text='Исполнение функции')
title_perform.place(x=10, y = 130)
tag_count = tk.Label(root, text='Кол-во повторений')
tag_count.place(x=10, y=150)
count = tk.Entry(root, width=18)
count.place(x=130, y=153)
perform_button = tk.Button(root, text='Исполнить функцию', width=32, height=2, command=performfunc)
perform_button.place(x=10, y=180)
debug_button = tk.Button(root, text='Исполнить в debug-режиме', width=32, command=debug)
debug_button.place(x=10, y=220)

#Help
title_help = tk.Label(root, text='InputEngine 0.2.0')
title_help.place(x=10,y=260)
guide_btn = tk.Button(root, text='Руководство по редактору', width=32, height=2)
guide_btn.place(x=10, y=290)
update_btn = tk.Button(root, text='Что нового?', width=32, height=1)
update_btn.place(x=10, y=330)
author_name = tk.Button(root, text='InputEngine 0.2 by Cyr1lle', width=32, height=1, state=["disabled"])
author_name.place(x=10, y=355)

#Editor

title_editor = tk.Label(root, text='Редактор функций')
title_editor.place(x=260, y=5)
pos_btn = tk.Button(root, text='Записать координаты', width=32, command=get_pos)
pos_btn.place(x=260,y=30)
clear_btn = tk.Button(root, text='Очистить действие', width=32, command=refresh)
clear_btn.place(x=260,y=82)
apply_btn = tk.Button(root, text='Применить действие', width=32, command=complete)
apply_btn.place(x=260,y=56)
mouse_edit = tk.Button(root, text='Мышь', width=10,height=4, command=add_mouse)
mouse_edit.place(x=260,y=120)
keyboard_edit = tk.Button(root, text='Клавиатура', width=10,height=4, command=add_keyboard)
keyboard_edit.place(x=260,y=190)
time_edit = tk.Button(root, text='Ожидать', width=10,height=1, command=complete)
time_edit.place(x=260,y=260)

#Moude editor
mouse_lmb = tk.Button(root, text='ЛКМ', width=7,height=1, command=complete)
mouse_lmb.place(x=340,y=120)
mouse_rmb = tk.Button(root, text='ПКМ', width=7,height=1, command=complete)
mouse_rmb.place(x=340,y=145)
mouse_mmb = tk.Button(root, text='Колесико', width=7,height=1, command=complete)
mouse_mmb.place(x=400,y=120)

#Time editor
time_btn = tk.Entry(root,width=18)
time_btn.place(x=340,y=267)

#Keyboard Editor
key_write = tk.Button(root, text='Написать', width=7,height=1, command=add_write)
key_write.place(x=340,y=190)
key_press = tk.Button(root, text='Зажать', width=7,height=1, command=add_press)
key_press.place(x=340,y=215)
key_release = tk.Button(root, text='Отпустить', width=7,height=1, command=add_release)
key_release.place(x=340,y=240)
writeEntry = tk.Entry(root, width=8)
writeEntry.place(x=400,y=193)
pressEntry = tk.Entry(root, width=8)
pressEntry.place(x=400,y=218)
releaseEntry = tk.Entry(root, width=8)
releaseEntry.place(x=400,y=243)



root.mainloop()
