class Dog:
    tricks = [] # 클래스 변수 -> 전역 변수, 인스턴스끼리 공유
    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over') # trick에 처음 들어가고
e.add_trick('play daed') # 추가로 붙어들어감

print(d.tricks)
