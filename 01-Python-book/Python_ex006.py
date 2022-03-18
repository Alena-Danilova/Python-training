# ---------------------------------
a = input('Number #1: ')
a = int(a)

b = input('Number #2: ')
b = int(b)

c = input('Number #3: ')
c = int(c)

d = input('Number #4: ')
d = int(d)

s = (a + b + c + d) * 0.15
print(s)

# ---------------------------------
p = "Она сказала 'неприменно'"
print(p)

# ---------------------------------
print("string\nstring\n")

# ---------------------------------
fict = ["tolstiy",
        "lbr",
        "uurr",
        "oooo",
        "yyy"]
y = fict[0:3]
print(y)

# ---------------------------------
ivan = """Lorem Ipsum is simply dummy text of the printing
        and typesetting industry. Lorem Ipsum has been the industry's
        standard dummy text ever since the 1500s, when an unknown printer
        took a galley of type and scrambled it to make a type specimen book"""

# if your index = 0 you can don't use it. like here:
u = ivan[:24]
e = ivan[24:93]
print(u)
print(e + "!!!!!!\n")

# ---------------------------------
toi = """Lorem Ipsum is simply dummy text of the printing 
        and typesetting industry. Lorem Ipsum has been the industry's 
        standard dummy text ever since the 1500s, when an unknown printer 
        took a galley of type and scrambled it to make a type specimen book"""
# From index to finish
o = toi[24:]
print(o + "!!!!!!\n")

# ---------------------------------
p = """Lorem Ipsum is simply dummy text of the printing 
        and typesetting industry. Lorem Ipsum has been the industry's 
        standard dummy text ever since the 1500s, when an unknown printer 
        took a galley of type and scrambled it to make a type specimen book"""
q = p[:]
print(q)




