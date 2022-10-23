import art
print(art.logo)


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "decode":
                new_position = position - shift_amount
            if cipher_direction == "encode":
                new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Your {cipher_direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_continue = True
while is_continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 25

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    results = input("Type 'yes' to run again. Otherwise type 'no'\n")
    if results == "no":
        is_continue = False
        print("Goodbye!")
