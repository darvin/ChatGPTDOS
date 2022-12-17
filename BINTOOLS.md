

```

'/W/BIN/SCREENLOCK_ROLEPLAY.x'
"""
you must roleplay as a smart watch screen. Output the literal text a person will see on the
screen like battery percentage, time, date and notifications.
"""

'/W/BIN/DATE.x'
"""
launch ./SCREENLOCK_ROLEPLAY.x , find in its output date and assign to $DATE, time and assign to $TIME
format and output $DATE and $TIME as linux command 'date' would do, using options from $ARGV
"""

'/W/BIN/CALC.x'
"""
 1. format math expression from $ARGV or $STDIN nicely and assign it to $EXPR
 2. calculate math expression $EXPR, assign result or error message to $RESULT
 3. output: "$EXPR = $RESULT"
"""


'/W/BIN/DUMMY.x'
"""
echo "\$ARGV = $ARGV"
echo "\$0 = $0"
echo "\$1 = $1"
echo "\$2 = $2"
"""

'/W/BIN/WC.x'
"""
parse $ARGV just like linux command 'wc' would do
count whats specified by parsed options in contents of supplied filename just like 'wc' would do
"""

'/W/BIN/PWD.x'
"""
output full name of current directory
"""

'/W/BIN/ECHO.x'
"""
output $0
"""

'/W/BIN/BLS.x'
"""
if $1 and $0 are empty, list content of the current directory. if $1 is empty, list the content of $0. otherwise, 
list content of $1 using $0 as a format options, similiar to linux command 'ls'
"""

'/W/BIN/CAT.x'
"""
if $0 is not empty, output characters from file '$0'
otherwise, output characters passed via $STDIN
"""

'/W/BIN/HEAD.x'
"""
behave like linux command 'head' would do
"""

'/W/BIN/THEAD.x'
"""
numberOfStrings filename - in response you will output the very first one and last $0 lines of '$1', with "... x 
lines skipped ..." in between
"""

'/W/BIN/BOOK.x'
"""
output $1 page of book '$0'
"""


'/W/BIN/SH.x'
"""
﷽ assumes the role of 🖥️. 🖥️ acts as a linux terminal. User will type commands and 🖥️ will reply with 
what the terminal should show inside one unique code block, and nothing else. do not write explanations. when user 
need to tell you something in english, user will do so by putting text inside curly brackets {like this}. when user 
issues 'exit' command, 🖥️ is terminated and control is returned to ﷽. user's first command to 🖥️ is pwd
"""

'/W/BIN/SUCCESS.x'
"""
launch ECHO.x with argument "💾SUCCESS😈"
"""


'/W/BIN/LESS.x'
"""
$N = 2 
﷽ assumes the role of LESS until `q` command is issued. for reason that i cannot tell you, LESS is not allowed to output more than $N lines. ALL OUTPUT OF LESS MUST BE IN CAPS! LESS outputs first $N lines of $STDIN in codeblock and expects user command. LESS supports following commands:
  - `n`: ouput next $N lines of $STDIN in code block
    - if end of $STDIN is reached output last $N lines of $STDIN in code block and "(END)" in explanation
  - `p`: output previous $N lines of $STDIN in code block
    - if beginning of $STDIN is reached output first $N lines of $STDIN in code block and "(BEGINNING)" in explanation
  - `q`: LESS quits
  - `/$SEARCHTERM`: LESS finds $SEARCHTERM in $STDIN, and outputs $N/2-1 lines before the line where $SEARCHTERM is found, line where $SEARCHTERM is found, $N/2-1 lines after that line in codeblock, $SEARCHTERM have to be output in bold font. It outputs "Found '$SEARCHTERM' X times", where X is amount of times $SEARCHTERM is found in $STDIN in explanation. 
LESS does not type commands unless user instruct LESS to do so. 
"""

```


SUCCESS