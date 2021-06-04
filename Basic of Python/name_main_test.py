import class_exercise

a = class_exercise.Calculator()
b = class_exercise.Calculator()

a.input_num(4, 2)
b.input_num(3, 7)

print(a.sum())
print(a.mul())
print(a.div())

print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())
