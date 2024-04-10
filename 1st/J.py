def double_line(a, b, c, d, e, f):
    y = (a * f - e * c) / (d * a - b * c)
    x = (e - b * y) / a
    return (x, y)


a, b, c, d, e, f = [int(input()) for _ in range(6)]
print(double_line(a, b, c, d, e, f))
