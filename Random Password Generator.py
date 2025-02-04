import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_set = ""
    if use_letters:
        char_set += string.ascii_letters #A-Z and a-z
    if use_numbers:
        char_set += string.digits  #0-9
    if use_symbols:
        char_set += string.punctuation   #special characters

    if not char_set:
        print("Error: Atleast one character set must be selected. ")
        return None
    return "".join(random.choice(char_set) for _ in range(length))
def main():
    try:
        length = int(input("Enter password length to be:"))
        use_letters = input("Include letters? (Y/N): ").strip().upper() == 'Y'
        use_numbers = input("Include numbers? (Y/N): ").strip().upper() == 'Y'
        use_symbols = input("Include symbols? (Y/N): ").strip().upper() == 'Y'

        if length <= 0:
            print("Error: Password length must be a positive number")
            return

        password = generate_password(length,use_letters, use_numbers, use_symbols)
        if password:
            print("\n Password Generated:", password)
    except ValueError:
        print("Invalid Input.Please enter again a numeric value for length")
if __name__ == "__main__":
    main()