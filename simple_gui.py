from tkinter import *
from tkinter import ttk


def main_roop(calc, exceptions: int = 0) -> None:  # tkinter를 이용한 간단한 GUI
    """
    Simple Gui that has 1 input line and 1 display line and a button used to run function 'calc'

    :param calc: Function that requires 1 str and returns Any
    :param exceptions: Type int, default 0, runs try-except syntax if not False
    :return: None
    """

    global e2, e3

    def run(calc, exceptions):
        n = e2.get()
        e3.delete(0, len(e3.get()))
        if exceptions:
            try:
                e3.insert(0, str(calc(n)))
            except Exception as e:
                e3.insert(0, f"ERROR: {e}")
        else:
            e3.insert(0, x(n))

    window = Tk()  # 창 생성
    window.geometry("270x170")  # 크기

    l2 = Label(window, text="n:")
    l3 = Label(window, text="ans:")
    l2.place(x=10, y=40)
    l3.place(x=10, y=70)

    e2 = ttk.Entry(window, width=30)
    e3 = ttk.Entry(window, width=30)
    e2.place(x=50, y=40)
    e3.place(x=50, y=70)

    b1 = ttk.Button(window, text="RUN", command=lambda: run(calc, exceptions))
    b2 = ttk.Button(window, text="DEL", command=lambda: e2.delete(0, len(e2.get())))
    b1.place(x=40, y=100)
    b2.place(x=130, y=100)

    window.mainloop()
