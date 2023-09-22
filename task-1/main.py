from tkinter import *

from dependency import root
from client import create_frame_1, create_frame_2, create_frame_3, create_frame_4, create_frame_5


def init_task():
    root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
    root.geometry("600x500")  # устанавливаем размеры окна

    label = Label(text="Tasks 28, 1, 4, 7, 10")  # создаем текстовую метку
    label.pack()  # размещаем метку в окне

    # task 1
    name_frame = create_frame_1("28. Даны действительные числа x,y. Вычислить значение функции z=arcsin(x+y)")
    name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

    # task 2
    name_frame = create_frame_2(
        "1. Даны действительные числа А,В,С,D. Выяснить, можно ли уместить прямоугольник со сторонами А,В внутри прямоугольника со сторонами C,D")
    name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

    # task 3
    name_frame = create_frame_3(
        "4.Определить, лежит ли точка D(c,b), где с= sqrt(a1+a2), b = a1 + 0,7 * a3, внутрипрямоугольника со сторонами 5 и 10 (а1,а2,а3 - произвольные числа)?")
    name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

    # task 4
    name_frame = create_frame_4("7. Даны действительные числа x,y. Вычислить значение функции z=log(x-y)- x/y")
    name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

    # task 5
    name_frame = create_frame_5("10. Вывести на печать переменные А,В,С в порядке их возрастания")
    name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    init_task()
