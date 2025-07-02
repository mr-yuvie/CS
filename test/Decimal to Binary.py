import math


def Binary(num):
    t = num
    c = 0
    while t >= 2:
        t = t / 2
        c += 1
    for i in range(c, -1, -1):
        if (num / (math.pow(2, i))) >= 1:
            print("1", end="")
        elif (num / (math.pow(2, i))) < 1:
            print("0", end="")
        num = num % (math.pow(2, i))


# num = int(input("Enter decimal number:"))
# Binary(num)


def Binary_Online_1(num):
    if num >= 1:
        Binary(num // 2)
        print(num % 2, end="")


# num = int(input("Enter:"))
# Binary_Online_1(num)


def Binary_Online_2(n):
    s = bin(n)
    s1 = s[2:]
    print(s1)


# n = int(input("Enter Decimal Nummber:"))
# Binary_Online_2(n)
