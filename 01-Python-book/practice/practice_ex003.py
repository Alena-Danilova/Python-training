
# Списки - list() or [] you can edit him content.
# Кортежи - tuple() - (,) you can't edit it.
# Словари - dict() ключ - значение {}

# 1
singers = ["Erog", "klava", "slava"]
print(singers)

# 2
location = ("225.667", "77.888")
print(location)

# 3
about_me = {"singer": "kino",
            "eay": "blue",}
print(about_me)

# 4
singer = input("You're singer: ")
eay = input("You're eay color: ")

about_user = {"singer": singer,
              "eay": eay}
print(about_user)

# 5
singer = input("You're Favorite singer: ")
song = input("You're Favorite song from It's author: ")

my_dict = {singer: song,
           "victor": "peremen",}
print(my_dict)