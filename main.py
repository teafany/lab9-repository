def encode(password):
    encoded = ""
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded


def decode(password):
    decoded_password = ""
    for char in password:
        new_char = str((int(char) - 3) % 10)
        decoded_password += new_char
    return decoded_password


def main():
    encoded_password = ""
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()
        elif option == "3":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
