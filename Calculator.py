addition_list = []
reducing_list = []
multiply_list = []
divide_list = []


def Convert(string):
    li = list(string.split())
    return li


def VConvert(val):
    for i in range(0, len(val)):
        val[i] = float(val[i])
    return val


fv = input("Fist values: ")
sv = input("Second values: ")
x = Convert(fv)
y = Convert(sv)
q = VConvert(x)
r = VConvert(y)
for num1, num2 in zip(q, r):
    addition_list.append(num1 + num2)
    reducing_list.append(num1 - num2)
    multiply_list.append(num1 * num2)
    divide_list.append(num1 / num2)

print("addition: ", addition_list, "\nreducing: ", reducing_list,
      "\nmultiply: ", multiply_list, "\nDividing: ", divide_list)
