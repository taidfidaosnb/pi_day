import simple_gui


def calc(a: str) -> str:
    try:
        int(a)
    except:
        return "잘못 입력하신 것 같은데요"

    with open("pi_7.txt", "r") as pi:
        pi.read(2)
        b = len(a)
        text = ""
        for i in range(b):
            text += pi.read(1)

        for i in range(2, 10**9):
            if a == text:
                return f"{i-1} ~ {i-2+b}번째 자리에서 등장해요"

            text = text[1:] + pi.read(1)

        return f"{a}를 찾을 수 없네요"


simple_gui.main_roop(calc, "PI DAY", "**HAPPY PI DAY**")
