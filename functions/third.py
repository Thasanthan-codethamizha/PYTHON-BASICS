def hello(x):
    if x < 5:
        return(x+1)
    else:
        return(x+hello(x-1))


print(hello(6))
