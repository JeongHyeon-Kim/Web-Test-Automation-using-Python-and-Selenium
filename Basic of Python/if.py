# if 문 실습

while True:
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('입력값이 음수여서 0으로 치환!')
    elif x >= 0 and x < 2:
        print('0 이상 2 미만')
    elif x == 2:
        print('2')
    elif x == 3:
        print('3')
    else:
        print('3 초과')
