import os
import sys
import json

def create_manifest(path):
    manifest = {}
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".md"):
                out_path = os.path.splitext(os.path.join(dirpath, filename))[0]
                manifest[os.path.join(dirpath, filename)] = {"out": out_path}
                print(f"{os.path.join(dirpath, filename)} -> {out_path}")
    with open("MANIFEST.json", "w") as f:
        json.dump(manifest, f)

if len(sys.argv) == 2:
    create_manifest(sys.argv[1])
else:
    create_manifest(os.getcwd())