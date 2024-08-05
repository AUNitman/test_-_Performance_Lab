import sys
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

# file_name1 = './task2/file1.txt'
# file_name2 = './task2/file2.txt'

with open(file_name1, 'r') as f1:
    array1 = f1.read()

with open(file_name2, 'r') as f2:
    array2 = f2.read()

array1 = [float(i) for i in array1.split()]
array2 = [float(i) for i in array2.split()]
r = array1[2]

for i in range(0, len(array2) - 1, 2):
    distance = (array2[i] - array1[0]) ** 2 + (array2[i + 1] - array1[1]) ** 2
    r_quad = r * r

    if r_quad > distance:
        print(1)
    elif r_quad == distance:
        print(0)
    else:
        print(2)
