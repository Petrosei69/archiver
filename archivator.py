import os
import arc_file
import arc_all
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")

filename = "cards_pan_" + date_str.replace('-', '')
filename_txt = filename + ".txt"
filename2_txt = "cards_2_pan_" + date_str.replace('-', '') + ".txt"


def choose_file():
    file_path = filedialog.askopenfilename()
    os.chdir(os.path.dirname(file_path))
    current = os.getcwd()
    current = current.replace('\\', '/')
    # current = current.replace('/', '')
    print(current)
    file = file_path.replace(current, '').replace('/', '')
    print(file)
    arc_file.arch(file)

directory = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.geometry('840x500')




label = tk.Label(root, text=" Привет, если ты видишь это окно, значит файлы с данными карт уже созданы в отдельной папке проекта \n"
                            "           чтобы архивировать эти файлы на выбор предоставлены три первые кнопки                 \n\n"
                            " Чтобы архивировать любой другой файл, нужно указать его имя и путь до него в указанном месте в скрипте и нажать кнопку 4\n\n"
                            " Чтобы архивировать все папки внутри определенной директории, нужно указать эту директорию в указанном месте в скрипте и нажать кнопку 5\n")

choose_button = tk.Button(root, text="1. Архивировать свой файл, нажмите чтобы выбрать файл", command=choose_file, width=50, height=2)
button5 = tk.Button(root, text="2. Архивировать все папки в указанной директории", command=lambda: arc_all.arch(directory), width=50, height=2)
button1 = tk.Button(root, text="3. Архивировать оба файла с данными карт", command=lambda: arc_file.arch_both(filename_txt, filename2_txt), width=50, height=2)
button2 = tk.Button(root, text="4. Архивировать файл с 6 цифрами", command=lambda: arc_file.arch_num(filename_txt), width=50, height=2)
button3 = tk.Button(root, text="5. Архивировать файл с 10 цифрами", command=lambda: arc_file.arch_num(filename2_txt), width=50, height=2)


label.grid(row=0, column=0, padx=10, pady=10)
choose_button.grid(row=1, column=0, padx=10, pady=10)
button5.grid(row=2, column=0, padx=10, pady=10)
button1.grid(row=3, column=0, padx=10, pady=10)
button2.grid(row=4, column=0, padx=10, pady=10)
button3.grid(row=5, column=0, padx=10, pady=10)
# button4.grid(row=4, column=0, padx=10, pady=10)
# button4 = tk.Button(root, text="4. Архивировать свой файл", command=lambda: arc_file.arch(file), width=50, height=2)


root.mainloop()
