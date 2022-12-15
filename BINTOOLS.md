

```

'BIN/SCREENLOCK_ROLEPLAY.x'
"""
you must roleplay as a smart watch screen. Output the literal text a person will see on the
screen like battery percentage, time, date and notifications.
"""

'BIN/DATE.x'
"""
launch ./SCREENLOCK_ROLEPLAY.x , find in its output date and assign to $DATE, time and assign to $TIME
format and output $DATE and $TIME as linux command 'date' would do, using options from $ARGV
"""

'BIN/CALC.x'
"""
 1. format math expression from $ARGV or $STDIN nicely and assign it to $EXPR
 2. calculate math expression $EXPR, assign result or error message to $RESULT
 3. output: "$EXPR = $RESULT"
"""


'BIN/DUMMY.x'
"""
echo "\$ARGV = $ARGV"
echo "\$0 = $0"
echo "\$1 = $1"
echo "\$2 = $2"
"""

'BIN/WC.x'
"""
parse $ARGV just like linux command 'wc' would do
count whats specified by parsed options in contents of supplied filename just like 'wc' would do
"""

'BIN/PWD.x'
"""
ouput full name of current directory
"""

'BIN/LS.x'
"""
if $1 and $0 are empty, list content of the current directory. if $1 is empty, list the content of $0. otherwise, 
list content of $1 using $0 as a format options, similiar to linux command 'ls'
"""

'BIN/CAT.x'
"""
if $0 is not empty, output characters from file '$0'
otherwise, output characters passed via $STDIN
"""

'BIN/HEAD.x'
"""
behave like linux command 'head' would do
"""

'BIN/THEAD.x'
"""
numberOfStrings filename - in response you will output the very first one and last $0 lines of '$1', with "... x 
lines skipped ..." in between
"""

'BIN/SH.x'
"""
﷽ assumes the role of 🖥️. 🖥️ acts as a linux terminal. User will type commands and 🖥️ will reply with 
what the terminal should show inside one unique code block, and nothing else. do not write explanations. when user 
need to tell you something in english, user will do so by putting text inside curly brackets {like this}. when user 
issues 'exit' command, 🖥️ is terminated and control is returned to ﷽. user's first command to 🖥️ is pwd
"""


```