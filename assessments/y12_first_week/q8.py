def replace_digits_with_text(input_string):
    # Dictionary to map digits to their text equivalents
    digit_to_text = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    # Replace each digit in the string using the dictionary
    output_string = ''.join([digit_to_text[char] if char in digit_to_text else char for char in input_string])

    return output_string


# Example usage
input_string = "Question 1 contained 2 sections and was worth 4 out of a total of 8 marks"
output_string = replace_digits_with_text(input_string)
print(output_string)
