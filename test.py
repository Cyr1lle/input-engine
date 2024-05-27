
import tkinter as tk

func = []
file_path = "datafunc.txt"
status = 'active'
test = tk.Tk()
test.title = 'Pivko'

def export():
    status = 'disabled'

load_button = tk.Button(test, text='Экспорт из .txt ', command=export, state=[status])
load_button.place(x=10, y=57)
load_name = tk.Entry(test, width=21)
load_name.place(x=110, y=60)

test.mainloop()

