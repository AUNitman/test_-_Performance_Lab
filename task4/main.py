import sys
file_name = sys.argv[1]
# file_name = './task4/test.txt'

with open(file_name, 'r') as f:
    numbers = [int(num.strip()) for num in f]

numbers.sort()

# удаление дубликатов
numbers = list(dict.fromkeys(numbers))

if len(numbers) % 2 == 0:
    median = numbers[len(numbers) // 2 - 1]
else:
    median = numbers[len(numbers) // 2]

count = sum(abs(num - median) for num in numbers)
print(count)
