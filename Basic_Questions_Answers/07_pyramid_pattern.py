rows = 4
row = 1
while row <= rows:
    spaces = " " * (rows - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)
    row += 1
