from tkinter import *
from tkinter import ttk


def main_roop(calc, title: str, text_label: str, test: bool = False) -> None:
    """
    Simple Gui that has 1 input line and 1 display line and a button used to run function 'calc'

    :param calc: Function that requires 1 str and returns Any
    :param title:
    :param text_label:
    :param test: Type bool, default False, runs try-except syntax if not False
    :return: None
    """

    global e2, e3

    def run(dcalc, dtest):
        n = e2.get()
        e3.delete(0, len(e3.get()))
        if dtest:
            try:
                e3.insert(0, str(dcalc(n)))
            except Exception as e:
                e3.insert(0, f"ERROR: {e}")
        else:
            e3.insert(0, dcalc(n))

    def clear():
        e2.delete(0, len(e2.get()))
        e3.delete(0, len(e3.get()))

    font = "Arial 24"

    window = Tk()  # 창 생성
    window.geometry("770x314")  # 크기
    window.title(title)
    window.resizable(False, False)

    l1 = Label(window, text=text_label, font=font)
    l1.place(x=240, y=10)

    l2 = Label(window, text="n:", font=font)
    l3 = Label(window, text="ans:", font=font)

    l2.place(x=55, y=75)
    l3.place(x=35, y=140)

    e2 = ttk.Entry(window, width=35, font=font)
    e3 = ttk.Entry(window, width=35, font=font)

    e2.place(x=115, y=75)
    e3.place(x=115, y=140)

    b1 = ttk.Button(window, text="RUN", width=10, command=lambda: run(calc, test))
    b2 = ttk.Button(window, text="DEL", width=10, command=clear)

    b1.place(x=115, y=200)
    b2.place(x=210, y=200)

    window.mainloop()


if __name__ == "__main__":
    main_roop(lambda x: int(x) ** 2)
