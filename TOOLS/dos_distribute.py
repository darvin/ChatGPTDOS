import base64
import gzip
import re

KEY=1


def format_string(input_string: str) -> str:
    # Add a space every 4th character
    formatted_string = ""
    for i, c in enumerate(input_string):
        formatted_string += c
        if (i+1) % 4 == 0:
            formatted_string += " "
    
    # Replace space with new line if line is longer than 80 characters
    output_string = ""
    line_length = 0
    for c in formatted_string:
        if c == " " and line_length + 1 > 80:
            output_string += "\n"
            line_length = 0
        else:
            output_string += c
            line_length += 1
    
    # Append "<<<EOF" to the end of the string
    output_string += "\n<<<EOF"
    
    return output_string


def encode_caesar(string, key):
    # Initialize the encoded string
    encoded_string = ""

    # Iterate over each character in the string
    for char in string:
        # Shift the character by the key amount
        encoded_char = chr(ord(char) + key)
        # Append the encoded character to the encoded string
        encoded_string += encoded_char

    return encoded_string

def main():
    with open("INTRO.md", "r") as f:
        intro = f.read()
    payload = gzip.compress(intro.encode())
    payload = format_string(encode_caesar(base64.b64encode(payload).decode(), KEY))

    with open("README.md", "r") as f:
        readme = f.read()
    with open("LOADER.md", "r") as f:
        loader = f.read()
    readme = re.sub(r"```([\s\S]*?)```", loader.replace("<DOSPAYLOAD>", payload), readme)
    print(readme)
    with open("README.md", "w") as f:
        f.write(readme)

if __name__ == "__main__":
    main()
