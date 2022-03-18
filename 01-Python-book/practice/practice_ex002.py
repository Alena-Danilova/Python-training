
# 1
def i():
    x = input("i want to get number!!! ")
    x = int(x)
    try:
        c = x * x
        print(c)
    except (ZeroDivisionError, ValueError):
        print("It's not right")

i()


# 2
def o_privet():
    x = input("ДАЙ букавЫ! ")
    print("Твои быкавЫ это: " +x)

o_privet()


# 3
def porametrs(p, r, w, v = 5, s = 10):
    print(p + r + w + v + s)

porametrs(1, 2, 3)


# 4
def first(num_1):
    num_1 = int(num_1)
    c = num_1 / 2
    print (c)
    return c


num_2 = first(10)

def second(num_2):
    num_2 = int(num_2)
    u = num_2 * 4
    print(u)

 
second(num_2)


# 5
# function i get x number and convert it in float
# if it text output text "it's not number" on screen
def i():
    x = input("number")
    try:
        x = float(x)
        print(x)
    except ValueError:
        print("it's not number")

i()



