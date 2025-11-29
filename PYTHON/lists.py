# marks = [33,55,66,77,88]

# # print(marks[3:len(marks)])
# # print(len(marks))

# marks.append(99)
# marks.insert(2,100)
# marks.sort()
# marks.reverse()
# print(marks)

number = [2,4,6,8,10]
i = 0
x = 8

for num in number:
    if num==x:
        print(f"{x} found at idx = {i}")
        break
    i += 1

