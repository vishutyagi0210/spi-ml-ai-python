from logic import generate_word

# it - is incomplete 
def accuracy(insert_begin , insert_end):
    number = 19
    expected_output = []

    for i in range(number):
        expected_output.append(generate_word(str(i)))

    print(expected_output)
    