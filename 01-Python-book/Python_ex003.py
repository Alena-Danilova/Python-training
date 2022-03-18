def add(x, y):
    """
    Return x + y
    x - it is An integer
    y - even number
    return the amount x & y
    """
    t = x + y
    print(t)

add(6, 5)

print("hello".upper())

fruit = ["apple", "book", "2.0"]
print(fruit)
fruit.append("5")
print(fruit)

fruit = ["apple", "book", "hello"]
print(fruit[3])

colors = ["red", "blue", "white"]
print(colors)
colors[2] = "hello"
print(colors)

colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)

color1 = ["red", "yellow"]
color2 = ["6", "7"]
print(color1 + color2)

colors = ["red", "yellow"]
print("2" not in colors)

colors = ["red", "yellow"]
print(len(colors))


colors = ["red", "yellow"]
guess = input("Guess the color")

if guess in colors:
    print("You win!")
else:
    print("No, try again")

my_tuple = ()
print(my_tuple)

x = (True, 654, "hi",)
print(type(x))

# Will be error
x_tuple = ("hello", "world")
x_tuple[1] = "Russia"

my_tuple = ("text", 999, True)
print(998 not in my_tuple)



fruits = {}
print(fruits)


facts = dict()

facts["code"] = "funny"
print(facts["code"])

facts["color"] = "red"
print(facts["color"])

print(facts)

bill = {"Bill G": "шедрый"}

print("Bill" not in bill)
print(type(bill))

book = {"book": "red", "drakyla": "monster"}
del book ["drakyla"]
print(book)

numbers = {"1": "red",
           "2": "green"}

n = input("Give a number")
if n in numbers:
    numbers = numbers[n]
    print(numbers)
else:
    print("It's not find!")


rhymes = {"5": "color",
          "1": "657"}

i = input("num: ")
if i in rhymes:
    rhymes = rhymes[i]
    print(rhymes)


lists = []
rap = ["basta", "kravc", "25 - 17"]
rock = ["kino", "aria"]
djs = ["Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap = lists[0]
print(rap)

rap = lists[0]
rap.append("Our business")
print(rap)
print(lists)

locations = []

moscow = (55.7522, 37.6155)
tula = (54.555, 90.0000)

locations.append(moscow)
locations.append(tula)

print(locations)

y = ["777", 77, True, "00"]
x = ["privet", "hello"]

var = (y, x)
print(var)

bday = {"чел",
        "17.26.05",
        }

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ru = {
    "x": (True, "ttt"),
    "y": [666, "rrr"],
    "u": {"a": "ooo"},
}

print(ru)
