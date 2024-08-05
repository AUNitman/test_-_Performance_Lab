
def find_way_on_array(n: int, m: int):

    if n < m:
        print('Enter true step')
        return

    circular_array = [i for i in range(1, n + 1)]
    path = []
    current_index = 0

    for _ in range(n):
        # print(circular_array[current_index])
        path.append(circular_array[current_index])

        current_index = (current_index + m - 1) % n
        if path[0] == circular_array[current_index]:
            break

    return int(''.join(map(str, path)))


inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

print(find_way_on_array(n, m))
