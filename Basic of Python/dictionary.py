# 사전 실습 - 학번 출력
student_info = {'홍길동': 1234, '철수': 5678, '영희': 9100}

while True:
    student_name = input("학생 이름을 입력하세요: ")

    for d_name in student_info.keys():
        if student_name == d_name:
            student_number = student_info[d_name]
            print("이름 : %s" %(student_name))
            print("학번 : %d" %(student_number))
            break

    '''
    student_number = input("학번을 입력하세요: ")

    for d_number in student_info.values():
        if student_number == d_number:
            student_number = student_info[d_name]
            print("이름 : %s" %(student_name))
            print("학번 : %d" %(student_number))
            break
    '''
