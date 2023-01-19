import simple_gui


def calc(a: str) -> str:
    with open("Pi - Dec.txt", "r") as pi:
        pi.read(2)
        b = len(a)
        text = ""
        for i in range(b):
            text += pi.read(1)

        for i in range(2, 10**9):
            if a == text:
                return f"{i-1} ~ {i-2+b}번째 자리에서 등장."

            text = text[1:] + pi.read(1)

        return f"{a}が見つかりません"


simple_gui.main_roop(calc)
