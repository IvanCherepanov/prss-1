from tkinter import *
from dependency import root
from server import task_28, task_1, task_4, task_7, task_10


def create_frame_1(label_text):
    def task_28_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            z = task_28(x=x, y=y)
            result_label.config(text=f"z = {z:.4f}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry1 = Entry(frame)
    entry1.pack(anchor=NW, padx=6, pady=6)

    entry2 = Entry(frame)
    entry2.pack(anchor=NW, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_28_client)
    compute_button.pack()
    return frame


def create_frame_1(label_text):
    def task_28_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            z = task_28(x=x, y=y)
            result_label.config(text=f"z = {z:.4f}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry1 = Entry(frame)
    entry1.pack(anchor=NW, padx=6, pady=6)

    entry2 = Entry(frame)
    entry2.pack(anchor=NW, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_28_client)
    compute_button.pack()
    return frame


def create_frame_2(label_text):
    def task_1_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            u = float(entry3.get())
            t = float(entry4.get())
            z = task_1(a=x, b=y, c=u, d=t)
            result_label.config(text=f"{z}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    # Создаем фрейм для первой пары Entry
    entry_frame1 = Frame(frame)
    entry_frame1.pack(anchor=NW)

    entry1 = Entry(entry_frame1)
    entry1.pack(side=LEFT, padx=6, pady=6)

    entry2 = Entry(entry_frame1)
    entry2.pack(side=LEFT, padx=6, pady=6)

    # Создаем фрейм для второй пары Entry
    entry_frame2 = Frame(frame)
    entry_frame2.pack(anchor=NW)

    entry3 = Entry(entry_frame2)
    entry3.pack(side=LEFT, padx=6, pady=6)

    entry4 = Entry(entry_frame2)
    entry4.pack(side=LEFT, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_1_client)
    compute_button.pack()
    return frame


def create_frame_3(label_text):
    def task_4_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            u = float(entry3.get())
            z = task_4(a1=y, a2=y, a3=u)
            result_label.config(text=f"{z}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry1 = Entry(frame)
    entry1.pack(anchor=NW, padx=6, pady=6)

    entry2 = Entry(frame)
    entry2.pack(anchor=NW, padx=6, pady=6)

    entry3 = Entry(frame)
    entry3.pack(anchor=NW, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_4_client)
    compute_button.pack()
    return frame


def create_frame_4(label_text):
    def task_7_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            z = task_7(x=x, y=y)
            result_label.config(text=f"{z}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry1 = Entry(frame)
    entry1.pack(anchor=NW, padx=6, pady=6)

    entry2 = Entry(frame)
    entry2.pack(anchor=NW, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_7_client)
    compute_button.pack()
    return frame

def create_frame_5(label_text):
    def task_10_client():
        try:
            x = float(entry1.get())
            y = float(entry2.get())
            c = float(entry3.get())
            res_1, res_2, res_3 = task_10(a=x, b=y, c=c)
            result_label.config(text=f"{res_1, res_2, res_3}")
        except ValueError:
            result_label.config(text="Ошибка: Введите корректные числа!")

    frame = Frame(borderwidth=1, relief=SOLID)

    # добавляем на фрейм метку
    label = Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry1 = Entry(frame)
    entry1.pack(anchor=NW, padx=6, pady=6)

    entry2 = Entry(frame)
    entry2.pack(anchor=NW, padx=6, pady=6)

    entry3 = Entry(frame)
    entry3.pack(anchor=NW, padx=6, pady=6)

    # Метка для вывода результата
    result_label = Label(frame, text="")
    result_label.pack()

    compute_button = Button(frame, text="Вычислить", command=task_10_client)
    compute_button.pack()
    return frame
