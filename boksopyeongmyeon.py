import turtle


# 복소수를 입력받아서 그래프에 표시하는 함수
# lst: 복소수의 리스트
def get_complex(lst):
    turtle.setup(width=1000, height=1000)
    t=turtle.Turtle()
    t.speed(0)
    t.ht()
    t.pu()
    #좌표평면 그리기
    t.goto(-500,0)
    t.pd()
    t.goto(500,0)
    t.pu()
    t.goto(0,500)
    t.pd()
    t.goto(0,-500)
    t.pu()

    for x in range(-500, 501, 25):
        t.goto(x, -5)
        t.pd()
        t.goto(x, 5)
        if x != 0:
            t.write(x//25, font=("Arial", 8, "normal"))
        t.pu()
    for y in range(-500, 501, 25):
        t.goto(-5, y)
        t.pd()
        t.goto(5, y)
        if y != 0:
            t.write(y//25, font=("Arial", 8, "normal"))
        t.pu()
    for i in lst:
        t.goto(i[0]*25,i[1]*25)
        t.pd()
        t.dot(10, "red")
        t.pu()
