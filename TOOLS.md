```
'SRC/TOOLS/manifest_create.py.md'
"""
script takes a directory as an argument, if its not passed - it uses current working directory.
it iterates over all files in directory recursively. it creates json file, containing full path to ".*.md" (note the double extension: `file.c.md` matches, `file.md` - doesn't) files in the
directory as a keys, and dictionaries with key `out`: $OUT_FILENAME as a values. $OUT_FILENAME is a file name with ".md" from the end removed.

for example, for directory with contents:

root/
├── subdir1/
│   ├── script.sh
│   ├── readme.py.md
│   └── main.c
└── subdir2/
    ├── script.sh
    ├── readme.c.md
    └── main.c


it must print out each added to MANIFEST file, like that:

"root/subdir1/readme.py.md -> "root/subdir1/readme.py"


it will create following `MANIFEST.json` file:

{
	"root/subdir1/readme.py.md": {"out": "root/subdir1/readme.py"},
	"root/subdir2/readme.c.md": {"out": "root/subdir2/readme.c"}
}

it must print out each added to MANIFEST file, like that:

"root/subdir1/readme.py.md -> "root/subdir1/readme.py"


"""

'SRC/TOOLS/upload.py.md'
"""
script takes a directory as an argument, if its not passed - it uses current working directory.
for each file listed in keys of `MANIFEST.json` file in that directory:

file is outputed in following format:

name of file in single quotes, then \n, then triple double quotes, then \n, then contents of the file, then \n, then triple double quotes, then \n.


program pause outputs in chunks of 50 lines or 200 characters, whichever shorter. it expects user to press any key to continue

"""


'SRC/TOOLS/download_receive.py.md'
"""
script takes a filename as an argument and reads its content as input, if no arguments are passed - it uses stdin as input

input represents multiple files concantenated in following format: 

name of file in single quotes, then \n, then triple double quotes, then \n, then contents of the file, then \n, then triple double quotes, then \n.

it creates files with specified names and contents in current directory. if they exist, it overrides them

"""







```