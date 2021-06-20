def hello(*name):
    for x in name:
        print(x)
    print(type(name))


hello("Thasa", "Rumesh", "Umar")
