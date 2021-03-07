x = int(input("Enter an x value: "))
# f(x) = 3 * x ** 2 + 7 * x + 5
#3 * x ** 2 + 7 * x + 5
x_value = x
print(x_value)
F = input("Enter a function f(x)")
# 3 * x ** 2 x + x 7 * x + 5
F = list(F)
print(F)
for index in F:
    if index == " ":
        F.remove(index)
print(F)
#['3', '*', 'x', '*', '*', '2', '+', '7', '*', 'x', '+', '5']
nums = []
funcs = []
brack = []
while len(F) > 0:
    if F[0].isnumeric():
        nums.append(int(F[0]))
        F.remove(F[0])
    elif F[0] == "*" or "/" or "-" or "+":
        funcs.append(F[0])
        F.remove(F[0])
    elif F[0] == "x":
        value = x_value
        print(F[0])
        if F[1] == "*" and F[2] == "*":
            value = value**int(F[3])
            print(F[3])
            print(value)
            value = str(value)
            nums.append(value)
            for x in range(0, 3):
                F.remove(F[x])
        else:
            nums.append(value)
            F.remove(F[0])
print(nums)
print(funcs)




