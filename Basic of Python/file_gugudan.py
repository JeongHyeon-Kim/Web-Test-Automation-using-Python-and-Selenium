f = open('구구단.txt', 'w')



for table in range(2, 13):
    table_name = "*** " + str(table) + "단" + " ***" + "\n"
    f.write(table_name)

    for num in range(1, 13):
        table_line = str(table) + " * " + str(num) + " = " + str(table * num) + "\n"
        f.write(table_line)


f.close()

