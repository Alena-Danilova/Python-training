
a = 2.2 + 2.2
print(a) 



def f(x):
    return x * 2

result = f(5)
print(result)



def f(x):
    return x + 1

z = f(4)



if z == 5:
    print("z = 5!")
else:
    print("z != 5!")


def f(z, u, i):
    return z + u + i

result = f(5, 6, 10)
print(result)


def f():
    z = 1 + 4
    return z

result = f()
print(result)
 
r = len ("Hello world")
print(r)

o = str(100)
print(o)

# will be error
o = int("Prince") 
i = type(o) is float
print(i)




age = input("you're age")
int_age = int(age)

if int_age < 21:
    print("You're young!")
else: 
    print("You're old man!") 


def even_odd (x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd (2)
even_odd (3)


def even_odd():
    n = input("enter a number: ")
    n = int(n)
    if n % 2 == 0:
        print("n - even")
    else:
        print("n - odd")


even_odd()
even_odd()
even_odd()


def message():
    myName = input("Whats you're name?")
    myAge = input("How old are you?")
    print("Hello " + myName + " you're old " + myAge)

message()
 


def f(x = 2):
    return x ** x

print(f())
print(f(4))


def add_it (x, y = 10):
    return x + y

result = add_it(2, 5)
print(result)




def f():
    x = 8    
    print(x)

f()

not work
if x > 100:
    print("x > 100")

x = 100

def f():
    global x 
    x += 1
    print(x)

f()




try:
    a = input("number: ")
    b = input("number 2: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("error!")


try:
    10 / 0
    c = "i'll never defined"
except ZeroDivisionError:
    print(c)


