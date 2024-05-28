import tkinter as tk
import time
import pyautogui
from tkinter import messagebox
import keyboard
import os

func = []
editorfunc = []
posx = 0
posy = 0



def toggle_editor():
    if apply_btn['state'] == tk.NORMAL:
        mouse_button.config(state=tk.NORMAL)
        keyboard_button.config(state=tk.NORMAL)
        time_button.config(state=tk.NORMAL)
        apply_btn.config(state=tk.DISABLED)
    else:
        mouse_button.config(state=tk.DISABLED)
        keyboard_button.config(state=tk.DISABLED)
        time_button.config(state=tk.DISABLED)
        apply_btn.config(state=tk.NORMAL)

def toggle_buttons():
    state = tk.NORMAL if checkbox_var.get() else tk.DISABLED
    debug_button.config(state=state)

def performfunc():
    for j in range(int(count.get())):
        for i in range(len(func)):
            if func[i][0] == 'MOUSE':
                if func[i][1] == 'LMB':
                    pyautogui.click(x=int(func[i][2]), y=int(func[i][3]))
                elif func[i][1] == 'RMB':
                    pyautogui.rightClick(x=int(func[i][2]), y=int(func[i][3]))
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
            elif func[i][0] == 'TIME':
                time.sleep(int(func[i][1]))

#File Functions

def save_matrix_to_file():
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for row in func:
                file.write(' '.join(map(str, row)) + '\n')
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось записать файл: {e}")
def create_new_file():
    global func, file_path
    func = []
    new_file_name = new_name.get()
    if not new_file_name:
        messagebox.showerror("Ошибка", "Пожалуйста, введите имя файла.")
        return
    file_path = os.path.join('..', new_file_name + '.txt')
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write("")  # Создать пустой файл
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось создать файл: {e}")
    name_file.config(text=new_name.get())
    file_path = new_file_name

def debug():
    print('Шаг: ', editorfunc)
    print('Функция: ', func)
    print('Файл:', file_path)
def export():
    global func,file_path
    func = []
    file_path = '../' + load_name.get() + '.txt'
    with open(file_path, "r", encoding="utf-8") as file:
        # Читаем файл построчно и добавляем каждую строку в список
        for line in file:
            # Удаляем символ новой строки в конце строки
            words = line.strip().split()
            func.append(words)
    print(file_path, func)
    name_file.config(text=load_name.get())


def get_pos():
    messagebox.showinfo("Получение координат", 'Вы'
                                                'активировали режим получения координат.'
                                                ' После закрытия этого окна, наведите ваш курсор'
                                                'в нужную точку на мониторе и нажмите клавишу'
                                                ' R.')
    keyboard.wait('R')
    x, y = pyautogui.position()
    messagebox.showinfo("Получение координат", 'Координаты записаны')
    global posx, posy
    posx = x
    posy = y


#Editor Functions

def refresh():
    global editorfunc
    editorfunc = []
def complete():
    global editorfunc
    func.append(editorfunc)
    editorfunc = []
    toggle_editor()
def mouseaction():
    selected = varmouse.get()
    if selected == optionsmouse[0]:
        editorfunc.append('MOUSE')
        editorfunc.append('LMB')
        editorfunc.append(str(posx))
        editorfunc.append(str(posy))
    elif selected == optionsmouse[1]:
        editorfunc.append('MOUSE')
        editorfunc.append('RMB')
        editorfunc.append(str(posx))
        editorfunc.append(str(posy))
    toggle_editor()
def keyaction():
    selected = varkeyboard.get()
    if selected == optionskeyboard[0]:
        editorfunc.append('KEYBOARD')
        editorfunc.append('WRITE')
        editorfunc.append(entry_key.get())
    elif selected == optionskeyboard[1]:
        editorfunc.append('KEYBOARD')
        editorfunc.append('PRESS')
        editorfunc.append(entry_key.get())
    elif selected == optionskeyboard[2]:
        editorfunc.append('KEYBOARD')
        editorfunc.append('RELEASE')
        editorfunc.append(entry_key.get())
    toggle_editor()
def timeaction():
    editorfunc.append('TIME')
    editorfunc.append(entry_time.get())
    toggle_editor()


root = tk.Tk()
root.title("InputEngine v0.2.2")
root.geometry('500x400')

checkbox_var = tk.IntVar()
editor_var = tk.IntVar()
file_path = "none"






#File

title_file = tk.Label(root, text='Настройки файла')
title_file.place(x=10, y=5)
new_button = tk.Button(root, text='Новая функция', command=create_new_file, width=13 )
new_button.place(x=10, y=30)
new_name = tk.Entry(root, width=21)
new_name.place(x=110, y=33)
load_button = tk.Button(root, text='Экспорт из .txt ', command=export, width=13)
load_button.place(x=10, y=57)
load_name = tk.Entry(root, width=21)
load_name.place(x=110, y=60)
save_button = tk.Button(root, text='Импорт в .txt ',width=13, command=save_matrix_to_file)
save_button.place(x=10, y=84)
save_name = tk.Entry(root, width=21)
save_name.place(x=110, y=87)
tag_name = tk.Label(root, text='Активное сохранение:')
tag_name.place(x=10, y=115)
name_file = tk.Label(root, text=file_path)
name_file.place(x=10, y=130)

#Perform
title_perform = tk.Label(root, text='Исполнение функции')
title_perform.place(x=10, y = 160)
tag_count = tk.Label(root, text='Кол-во повторений')
tag_count.place(x=10, y=180)
count = tk.Entry(root, width=18)
count.place(x=130, y=183)
perform_button = tk.Button(root, text='Исполнить функцию', width=32, height=2, command=performfunc)
perform_button.place(x=10, y=210)
debug_button = tk.Button(root, text='Исполнить в debug-режиме', width=32, command=debug, state=tk.DISABLED)
debug_button.place(x=10, y=250)

#Help
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
clear_btn = tk.Button(root, text='Отменить запись действия', width=32, command=refresh)
clear_btn.place(x=260,y=82)
apply_btn = tk.Button(root, text='Записать действие в функцию', width=32, command=complete, state=tk.DISABLED)
apply_btn.place(x=260,y=56)

title_mouse = tk.Label(root, text='Действия с мышкой')
title_mouse.place(x=260,y=110)
optionsmouse = ['Нажатие левой кнопки мыши', 'Нажатие правой кнопки мыши', 'Нажатие колесика мыши']
varmouse = tk.StringVar(root)
varmouse.set(optionsmouse[0])
dropdownmouse = tk.OptionMenu(root,varmouse, *optionsmouse,)
dropdownmouse.place(x=260,y=130)
mouse_button = tk.Button(root, text='Действие мышкой', width=32, command=mouseaction)
mouse_button.place(x=260,y=160)

title_keyboard = tk.Label(root, text='Действия с клавиатурой')
title_keyboard.place(x=260,y=190)
optionskeyboard = ['Написать слово/символ', 'Нажать на клавишу', 'Отпустить клавишу']
varkeyboard = tk.StringVar(root)
varkeyboard.set(optionskeyboard[0])
dropdownkeyboard = tk.OptionMenu(root,varkeyboard, *optionskeyboard,)
dropdownkeyboard.place(x=260,y=210)
keyboard_button = tk.Button(root, text='Действие клавиатурой', width=32, command=keyaction)
keyboard_button.place(x=260,y=240)
entry_key = tk.Entry(root, width=7)
entry_key.place(x=440,y=216)

title_time = tk.Label(root, text='Действия с паузами')
title_time.place(x=260,y=270)
entry_time = tk.Entry(root, width=38)
entry_time.place(x=260,y=290)
time_button = tk.Button(root, text='Добавить паузу', width=32, command=timeaction)
time_button.place(x=260,y=310)

#Other
checkbox = tk.Checkbutton(root, text="Режим разработчика", variable=checkbox_var, command=toggle_buttons)
checkbox.place(x=300,y=370)




root.mainloop()
