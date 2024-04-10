def square(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    elif a == 0:
        if c ** 2 == b:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    else:
        x = (c**2 - b) / a
        if x.is_integer():
            return int(x)
        else:
            return 'NO SOLUTION'


a, b, c = [int(input()) for _ in range(3)]
print(square(a, b, c))
