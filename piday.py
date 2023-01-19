import itertools

class MyIterator:
    def __init__(self):
        self.data = '1'
        self.count = 0

    def setdata(self):
        self.data += '1'
        return self.data

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count != 3:
            self.data += '1'
            self.count += 1
            return self.data
        raise StopIteration

    


with open("piday/pi_to_billion_dec.txt", 'r') as pi:
    a = pi.read()
    b = input()
    c = 0
    
    for i in range(2, 10**9) :

        if b == a[i:i+len(b)] : 
            print(f"소수점 아래 {i-1}번째 자리부터 {i-2+len(b)}번째 자리까지에서 처음 나타납니다")
            c = 1
            break

    if c == 0 : print(f"와우! {b}는 대단한 숫자에요!")