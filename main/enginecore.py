import keyboard
import pyautogui
import tkinter
from tkinter import messagebox
import time

func = []

file_path = "../datafunc.txt"


# Открываем файл для чтения
with open(file_path, "r", encoding="utf-8") as file:
    # Читаем файл построчно и добавляем каждую строку в список
    for line in file:
        # Удаляем символ новой строки в конце строки
        words = line.strip().split()
        func.append(words)



print("Содержимое файла загружено в список:", func)



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

