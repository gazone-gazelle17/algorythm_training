def if_castle(a, b, c, d, e):
    brick_sides = [a, b, c]
    hole_sides = [d, e]
    brick_sides.sort()
    hole_sides.sort()
    if brick_sides[0] <= hole_sides[0] and brick_sides[1] <= hole_sides[1]:
        return 'YES'
    else:
        return 'NO'


a, b, c, d, e = [int(input()) for _ in range(5)]
print(if_castle(a, b, c, d, e))
