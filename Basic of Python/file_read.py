f = open("구구단.txt", "r")

for i in f.readlines():
    i = i.replace('\n',"") # 개행 문자 제거
    print(i)

f.close()
