import sys
from logic import generate_word

def main():
    u_input = input("Hello from mumma!!!! my limit is 999999 \n" 
    "Enter the number: ")
    
    print(f"{u_input}: {generate_word(u_input)}")

sys.exit(main())