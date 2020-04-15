# Выполнить вычисления, записать в переменную и вывести в результате целую часть и дробную часть от деления:
#(a^c - b + d) / f
#(15^2 - 20 + 5.5) / 6
#(63/2 + 45 - 8) / 2^5
#7^3 + 20 * (10/3 + 6)
#83/8 * (43/20 + 5^7)
#72 + 36 / 7 * (72-6^5)

a=15
c=2
b=20
d=5.5
f=6
y=(a**c-b+d)
print(y//f)
print(y%f)

print((63/2+45-8)/2**5)

a, b, c, d, e = 63, 2, 45, 8, 5
s=a/b+c-d
f=b**e
print(s//f)
print(s%f)
print("+-+")

def calculate(argument1, argument2, argument3, argument4, argument5):
    d=(argument1**argument2-argument3+argument4)/argument5
    print(d)

calculate(15, 2, 20, 5.5, 6)