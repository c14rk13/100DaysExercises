from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Import and print the logo from art.py when the program starts.
print(logo)

#Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'
def caesar(original_text, shift_amount, encode_or_decode):
    alphabet_length = len(alphabet)
    output_text = ""
    shift_sign = shift_amount

    if direction == "decode":
        shift_sign *= -1

    for char in original_text:
        if char in alphabet:
            shift_adjusted = alphabet.index(char) + shift_sign
            shift_adjusted %= abs(alphabet_length)
            output_text += alphabet[shift_adjusted]
        else:
            output_text += char

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Run the caesar cipher, keep playing until the user says not to
keep_playing = True

while keep_playing:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        caesar(text, shift,direction)
    else:
        print("That is not a valid request.")

    keep_playing = True if input("Type 'yes' if you want to go again: ").lower() == "yes" else False

