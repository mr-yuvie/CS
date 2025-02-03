#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n = int(input("Enter max range:"))
def print_pascals_triangle(n):
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        print(" " * (n - i), *row)
        prev_row = row

print_pascals_triangle(n)