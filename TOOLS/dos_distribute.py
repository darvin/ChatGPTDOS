import base64
import gzip
import re

KEY=1

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
    payload = encode_caesar(base64.b64encode(payload).decode(), KEY)

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
