number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 10, 12]


def hello(x):
    return (x % 2 == 1)


new_list = list(filter(
    hello, number_list
))

print(new_list)
