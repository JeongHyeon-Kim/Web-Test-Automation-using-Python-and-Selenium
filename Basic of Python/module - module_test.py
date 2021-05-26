# module_tesy.py
# 모듈 실습 - count_char()  참조

import count_module

s = 'supercalifrageilisticexpialidocious'
input_char = input("세어보기 원하는 알파벳 입력: ")

a  = count_module.count_char(s, input_char)
print("입력된 문자 = %c 이고 몇 개가 들어있나? %d개" %(input_char, a))
