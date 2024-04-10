def notebook(a, b, c, d):
    dimensions = [
        (max(a, c), b + d),
        (max(a, d), b + c),
        (a + c, max(b, d)),
        (a + d, max(b, c)),
        (max(b, d), a + c),
        (max(b, c), a + d),
        (b + c, max(a, d)),
        (b + d, max(a, c))
    ]

    min_area = float('inf')
    result = (0, 0)
    for length, width in dimensions:
        area = length * width
        if area < min_area:
            min_area = area
            result = (length, width)

    return result


a, b, c, d = map(int, input().split())
table_length, table_width = notebook(a, b, c, d)
print(table_length, table_width)
