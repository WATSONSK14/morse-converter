import json

def read_file(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return {}

def text_to_mors(word, mors_dictionary):
    return ' '.join([mors_dictionary.get(letter.upper(), "[?]") for letter in word])

def mors_to_text(word, string_dict):
    return ''.join([string_dict.get(letter, "[?]") for letter in word.strip().split(" ")])

def converter():
    mors_dict = read_file("morse_alphabet.json")

    if not mors_dict:
        return
    string_dict = {v: k for k, v in mors_dict.items()}

    try:
        code = int(input("Press 1 to Convert Text to Morse\nPress 2 to Convert Morse to Text\n-->>"))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

    if code == 1:
        word = input("Enter the word: ")
        print(text_to_mors(word, mors_dict))

    elif code == 2:
        word = input("Enter the word: ")
        print(mors_to_text(word, string_dict))
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    converter()