#  리스트 실습 - supercalifrageilisticexpialidocious
s = 'supercalifrageilisticexpialidocious'
list_s = list(s)
input_char = input("세어보기 원하는 알파벳 입력: ")

result = list_s.count(input_char)

print("입력된 문자 = %c 이고 몇 개가 들어있나? %d개" %(input_char, result))
