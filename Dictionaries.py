person ={
    "name" : "Hemanth",
    "age" : 24,
    "city" : "Guntur",
    "hobby" : ["travel", "music", "programming"]
}

# print(person)
# print(person["name"])
# print(len(person))
# print(type(person))
person["email"] = "hemanths7.dev@gmail.com"
person["age"] = 25
# for key, value in person.items():
#     print(f"{key} : {value}")

for data in person:
    print(f"{data} : {person[data]}")