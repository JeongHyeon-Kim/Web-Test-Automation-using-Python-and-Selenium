# 함수 실습 - supercalifrageilisticexpialidocious
def count_char(s, input_char):
    len_s = len(s)
    count = 0

    while True:
        for index in range(0, len_s):
            s_char = s[index]
            if input_char == s_char:
                count = count + 1
        break

    return count

# 함수 호출
s = 'supercalifrageilisticexpialidocious'
# input_char = 'i' # 하드 코딩
input_char = input("세어보기 원하는 알파벳 입력: ") # 입력 받기
a = count_char(s, input_char)
print("입력된 문자 = %c 이고 몇 개가 들어있나? %d개" %(input_char, a))
