


```

'BIN/GENERATE.x'
"""
use text containing in $0 as a prompt and output only code response to $1. output to chat only generated file name, and it's new length in characters. use all files in directory for reference
"""

'BIN/G.x'
"""
for each key of in `MANIFEST.json` file in current directory, assign it to $IN, and value of key `out` of its value to $OUT. 
call GENERATE $IN $OUT
"""


'BIN/DPREP.x'
"""
remove directory `/D` if it exits. remove file `/D.i` if it exists.
create directory `/D`
$OUTS = []
for each key of in `MANIFEST.json` file in current directory, assign it to $IN, and value of key `out` of its value to $OUT. append $OUT to $OUTS

output all files listed in $OUTS in following format to the chunked files in `/D`:
name of file in single quotes, then \n, then triple double quotes, then \n, then contents of the file, then \n, then triple double quotes, then \n.

the name of first chunked file should be `/D/0`. after 10 lines are outputed, if there are still lines left to be output it should be continued to `/D/1`, `/D/2` and so on, keeping the same limit
"""


'BIN/D.x'
"""
if `/D.i` doesnt exist create it and write string "0" to it.
read its content of file `/D.i` as a string and convert it to integer $I.
output contents of file `/D/$I`
increase $I by one and write it as a string to file `/D.i`
"""



```

