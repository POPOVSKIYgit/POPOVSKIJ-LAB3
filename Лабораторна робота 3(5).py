max_val = -1
max_index = -1
current_index = 0

while True:
    n = int(input())
    if n == 0:
        break

    if n > max_val:
        max_val = n
        max_index = current_index

    current_index += 1

print(max_index)
