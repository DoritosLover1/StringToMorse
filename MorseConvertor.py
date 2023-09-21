MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}



def appender(array, obj_str):
    # You can use it for appending string to array
    for x in range(len(obj_str)):
        array.append(obj_str[x])


def mainprocess(array1, array2):
    # It is main process for converting. :)
    for letter in array2:
        if f"{letter}" in MORSE_CODE_DICT:
            array1.append(MORSE_CODE_DICT.get(f"{letter}"))
        if letter == " ":
            array1.append(" ")


class StringToMorse:
    def __init__(self):
        self.convertor()

    @staticmethod
    def convertor():

        # Taking string from user
        string = input("Enter your sentence: ")

        # Capitalization for all letters which include in entered sentence that is also string. :)
        capitalized_string = string.upper()
        string_array = []

        # It is for appending letter/letters to array/list/dict/ not tuple. :)
        appender(string_array, capitalized_string)

        converted_array = []
        mainprocess(converted_array, string_array)
        converted_string = " ".join(converted_array)

        print(converted_string)

        """
        for x in range(0, len(capitalized_string)):
            array[x].append(capitalized_string[x])
        """

        """
        should_continue = True
        while should_continue:
            for x in range(0, len(capitalized_string)):
                if MORSE_CODE_DICT.get(f"{capitalized_string[x]}"):
                    print(capitalized_string[x])
                    should_continue = True
                    return should_continue
        """
