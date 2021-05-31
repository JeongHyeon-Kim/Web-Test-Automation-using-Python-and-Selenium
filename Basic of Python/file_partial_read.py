f = open("구구단.txt", "r")

for i in f.readlines()[0:26]: # 일부만 가져와서 읽기
    i = i.replace('\n',"") # 개행 문자 제거
    print(i)

f.close()
