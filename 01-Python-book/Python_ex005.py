n1 = input("Lead the noun: ")
v = input("Head the adjective: ")
adj = input("Lead the noun: ")
n2 = input("Head the adjective: ")

r = """ how sometimes, {} {} {} {}
    """.format(n1, v, adj, n2)

print(r)

# -----------------------------------------

r = "я прыгную через голову! Это целых 2 метра".split("!")
print(r)

# -----------------------------------------

first_three = "abs"
result = "+".join(first_three)
print(result)

# -----------------------------------------

words = ["ee",
         "tt",
         "oo"]
one = " ".join(words)
print(one)

# -----------------------------------------

s = "   moscow    "
s = s.strip()

a = ("ooo " + s + " ooo")
print(a)

# -----------------------------------------

equ = "all animals are the same"
equ = equ.replace("a", "@")
print(equ)

# -----------------------------------------

y = "hello"
try:
    y = y.index("o")
    print(y)
except:
    print("not found")

# -----------------------------------------

r = "cat" in " at home"
print(r)

# -----------------------------------------

r = "cat" not in "cat at home"
print(r)