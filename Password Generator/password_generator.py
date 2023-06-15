import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the desired password length (or enter 0 to exit): "))
        
        if length == 0:
            print("Exiting the program...")
            break
        
        password = generate_password(length)
        print("Generated Password:", password)
        print()
    
        print("Thank you for using the password generator!")

if __name__ == "__main__":
    main()
