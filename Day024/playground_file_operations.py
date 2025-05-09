file = open("my_file.txt")
print(file.read())
file.close()


with open("my_file.txt") as file2:
    contents = file2.read()
    print(contents)
    #no need to explicitly close the file

with open("my_file.txt", mode="w") as file2:
    file2.write("oh, hello yourself!")

with open("my_file.txt", mode="a") as file2:
    file2.write("\noh, hello yourself, too!")

with open("Day024_new_file.txt", mode="w") as file2:
    file2.write("New file, doesn't exist yet")



relative_path_file = "files/my_file2.txt"
with open(relative_path_file, mode="w") as file2:
    file2.write("testing relative paths")

with open(relative_path_file, mode="a") as file2:
    file2.write("\noh, hello yourself, too!")



relative_path_file2 = "../../TestFiles/TestFilePaths.txt"
with open(relative_path_file2, mode="w") as file2:
    file2.write("testing relative paths - 2")

with open(relative_path_file2, mode="a") as file2:
    file2.write("\noh, hello yourself, too - 2!")




absolute_path_file = "/00Files/Python/100days/100DaysCode/files/my_file2.txt"
with open(absolute_path_file, mode="a") as file2:
    file2.write("\nUsing absolute file path")