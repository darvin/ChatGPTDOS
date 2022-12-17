
import hashlib
import re
from collections import defaultdict
def compress_string(input_string):
    # Split the input string into a list of words
    words = input_string.split()

    # Create an empty dictionary to store the count of each word
    word_count = {}

    # Iterate through the list of words and update the count of each word in the dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Create an empty list to store the compressed string
    compressed = []
    emojis_used = {}
    # Iterate through the list of words again
    for word in words:
        # If the count of the word in the dictionary is greater than 1, replace the word with the result of the word_to_emoji() function
        if word_count[word] > 1:
            emojis_used[word_to_emoji(word)] = word
            compressed.append(word_to_emoji(word))
        # If the count is 1, simply append the word to the compressed list
        else:
            compressed.append(word)

    # Join the elements in the compressed list and return the resulting string
    output_string = ' '.join(compressed)

    output_string = output_string.replace("\n", word_to_emoji(">N<"))
    output_string = output_string.replace("     ", word_to_emoji(">S4<"))
    output_string = output_string.replace("    ", word_to_emoji(">S3<"))
    output_string = output_string.replace("   ", word_to_emoji(">S2<"))

    # Append the dictionary of emojis used to the end of the string
    output_string += "\n\n{"
    for emoji, word in emojis_used.items():
        output_string += f"{emoji}{word}"
    output_string += f"{word_to_emoji('>S4<')}>S4<"
    output_string += f"{word_to_emoji('>S3<')}>S3<"
    output_string += f"{word_to_emoji('>S2<')}>S2<"
    output_string += f"{word_to_emoji('>N<')}>N<"
    output_string += "}\n"

    return output_string

def word_to_emoji(word: str) -> str:
    # Calculate the hash of the word
    word_hash = hashlib.sha256(word.encode()).hexdigest()
    
    # Convert the hash to an integer
    emoji_code = int(word_hash, 16)
    
    # Map the integer to a Unicode emoji character
    # The range of Unicode emoji characters is from U+1F600 to U+1F64F
    emoji_range = 0x1F64F - 0x1F600 + 1
    emoji_code %= emoji_range
    emoji_code += 0x1F600
    
    return chr(emoji_code)

import re



def main():
    with open("INTRO.small.txt", "r") as f:
        intro = f.read()

    compressed = compress_string(intro)
    print (f"{len(intro)} -> {len(compressed)} ")
    payload = compressed + "<<<EOF"

    with open("README.md", "r") as f:
        readme = f.read()
    with open("LOADER.md", "r") as f:
        loader = f.read()
    readme = re.sub(r"```([\s\S]*?)```", loader.replace("<DOSPAYLOAD>", payload), readme)
    #print(readme)
    with open("README.md", "w") as f:
        f.write(readme)

if __name__ == "__main__":
    main()
