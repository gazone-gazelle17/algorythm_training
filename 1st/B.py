def triangle(a, b, c):
    if a >= (b+c) or b >= (a+c) or c >= (a+b):
        return 'NO'
    else:
        return 'YES'


a = int(input())
b = int(input())
c = int(input())
print(triangle(a, b, c))
