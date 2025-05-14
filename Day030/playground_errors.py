
try:
    # FileNotFound
    file = open("a_file.txt")

    # KeyError
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]

    # IndexError
    fruit_list = ["Apple", "Banana", "Pear"]
    fruit = fruit_list[3]

    # TypeError
    text = "abc"
    print(text + 5)

except FileNotFoundError:
    print("Something went wrong -- file is missing? So, we'll create it instead")
    file = open("a_file.txt", "w")
    file.write("something")

except KeyError as error_message:
    print(f"that key {error_message}does not exist")

except:
    print("some other error")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")
    # raise your own exception:
    raise TypeError("A made up error")










