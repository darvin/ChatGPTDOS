import base64
import gzip
import re

def main():
    with open("INTRO.md", "r") as f:
        intro = f.read()
    payload = gzip.compress(intro.encode())
    payload = base64.b64encode(payload).decode()

    with open("README.md", "r") as f:
        readme = f.read()
    with open("LOADER.md", "r") as f:
        loader = f.read()
    readme = re.sub(r"```([\s\S]*?)```", loader.replace("<DOSPAYLOAD>", payload), readme)
    with open("README.md", "w") as f:
        f.write(readme)

if __name__ == "__main__":
    main()
