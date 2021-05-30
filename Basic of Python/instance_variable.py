class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = [] # 인스턴스 변수 -> 지역 변수, 인스턴스 내에서만 사용

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over') # d(Fido)에 붙음
e.add_trick('play daed') # e(Buddy)에 붙음

print(d.tricks)
print(e.tricks)
