import sys
from logic import generate_word

def main():
    # u_input = input("Hello from mumma!!!! my limit is 999999 \n" 
    # "Enter the number: ")
    
    # print(f"{u_input}: {generate_word(u_input)}")

    number = 19
    expected_output = []

    for i in range(number):
        expected_output.append(generate_word(str(i)))

    print(expected_output)

sys.exit(main())