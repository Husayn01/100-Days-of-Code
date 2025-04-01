def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 6))

def calc(**kwargs):
    for (key, value) in kwargs.items():
        print(key)
        print(value)
calc(add=3, multiply =3)