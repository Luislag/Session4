print(dir("hi"))
methods = dir("hi")
useful_methods = []
for method in methods:
    if"__" in method:
        continue
    useful_methods.append(method)
print(useful_methods)

print(help("hi".capitalize))
print("cat".capitalize())
s = "i go to school everyday"
print(s.capitalize())

print(help("".casefold))
print("I LIKE CAKE".casefold())

print("hello".center(30 , "*"))
print("bananabababababa".count("b"))

print("Ana ana ana banana".find("ana"))

print("abcdebg".index("b", 2))

words = ("i" , "like" , "to" , "sing")
print(" ".join(words))

s = "I like to go hiking"
print(s.replace(" " , "! ¡").split())
print(s.upper())