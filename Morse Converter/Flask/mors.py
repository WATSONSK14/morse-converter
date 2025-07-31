import json

def read_json(filename):
    try:
        with open("morse_alphabet.json", "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON {e}")
    except Exception as e:
        print(f"EXCEPTION {e}")
    return {}


def text_to_morse(word, mors_dict):
    return " ".join([mors_dict.get(letter.upper(), "[?]") for letter in word])


def morse_to_text(word, string_dict):
    return "".join(string_dict.get(letter, "[?]") for letter in word.strip().split(" "))


class MorseConverter:
    def __init__(self):
        self.morse_dict = None
        self.string_dict = None
        self.conv = None

    def convert(self, word, code, filename):
        self.morse_dict = read_json(filename)
        if not self.morse_dict:
            return
        self.string_dict = {v: k for k, v in self.morse_dict.items()}


        if code == 1:
            self.conv = text_to_morse(word, self.morse_dict)

        elif code == 2:
            self.conv= morse_to_text(word, self.string_dict)
        else:
            print("Invalid input")
        return self.conv

