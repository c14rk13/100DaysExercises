
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"


def write_individual_letter():
    # Read letter template per line
    # For each line, replace substring if it occurs
    # then write each clean line to a new file

    with open("./Input/Letters/starting_letter.txt") as input_file:
        file_contents = input_file.read()

    with open("./Input/Names/invited_names.txt") as invited:
        invited_names = invited.readlines()


    for name in invited_names:
        name = name.strip()
        file_contents = file_contents.replace(PLACEHOLDER, name)

        with open(f"./Output/ReadyToSend/invite_{name}.txt", "w") as invite_file:
            invite_file.write(file_contents)


write_individual_letter()