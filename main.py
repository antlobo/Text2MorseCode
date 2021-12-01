# Data extracted from http://www.sckans.edu/~sireland/radio/code.html
CHAR_TO_MORSE = {
    "A": "•-",     "B": "-•••",   "C": "-•-•",   "D": "-••",
    "E": "•",      "F": "••-•",   "G": "--•",    "H": "••••",
    "I": "••",     "J": "•---",   "K": "-•-",    "L": "•-••",
    "M": "--",     "N": "-•",     "O": "---",    "P": "•--•",
    "Q": "--•-",   "R": "•-•",    "S": "•••",    "T": "-",
    "U": "••-",    "V": "•••-",   "W": "•--",    "X": "-••-",
    "Y": "-•--",   "Z": "--••",   "1": "•----",  "2": "••---",
    "3": "•••--",  "4": "••••-",  "5": "•••••",  "6": "-••••",
    "7": "--•••",  "8": "---••",  "9": "----•",  "0": "-----",
    ".": "•-•-•-", ",": "--••--", ":": "---•••", "?": "••--••",
    "'": "•----•", "-": "-••••-", "/": "-••-•",  "(": "-•--•-",
    '"': "•-••-•", " ": "\\",
}

ART = '''
      _______        _     ___    __  __                        _____          _      
     |__   __|      | |   |__ \  |  \/  |                      / ____|        | |     
        | | _____  _| |_     ) | | \  / | ___  _ __ ___  ___  | |     ___   __| | ___ 
        | |/ _ \ \/ / __|   / /  | |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \\
        | |  __/>  <| |_   / /_  | |  | | (_) | |  \__ \  __/ | |___| (_) | (_| |  __/
        |_|\___/_/\_\\\__| |____| |_|  |_|\___/|_|  |___/\___|  \_____\___/ \__,_|\___|
    '''


def convert_text_morse(text: str) -> tuple:
    """
    Converts a string to Morse code
    :param text: string to convert
    :return: a tuple with the result string (text converted to Morse code) and a list of chars which couldn't be converted
    """
    upper_text = text.upper()
    errors = []
    result = ""
    for char in upper_text:
        try:
            result += f"{CHAR_TO_MORSE[char]} "
        except KeyError:
            # Uncomment line below if you want to show the characters which couldn't be converted in the result
            # result += char
            errors.append(char)

    return result, errors


def main():
    while(text := input("\nWrite the text to convert to Morse code or 'exit': ")) != "exit":
        result, errors = convert_text_morse(text.upper())
        if result:
            print(f'Text: "{text}" converted to Morse code is: {result}')

        if errors:
            print(f'[Error] {" ".join(errors)} could not be translated to Morse code')


if __name__ == '__main__':
    print(ART)
    main()
