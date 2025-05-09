with open("./files/file1.txt") as file1:
    file_num_1 = file1.readlines()

with open("./files/file2.txt") as file2:
    file_num_2 = file2.readlines()

numbers_1 = [int(n) for n in file_num_1]
numbers_2 = [int(n) for n in file_num_2]

result = [n for n in numbers_1 if n in numbers_2]

print(result)