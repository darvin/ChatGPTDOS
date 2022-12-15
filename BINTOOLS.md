

```

'BIN/SCREENLOCK_ROLEPLAY.x'
"""
you must roleplay as a smart watch screen. Output the literal text a person will see on the
screen like battery percentage, time, date and notifications.
"""

'BIN/CALC.x'
"""
 1. join $0, $1, $2 with space, assign result to $EXPR
 2. calculate $EXPR, assign result to $RESULT
 3. ouput: "$EXPR = $RESULT"
"""

'BIN/BPWD.x'
"""
ouput full name of current directory
"""

'BIN/BLS.x'
"""
if $1 and $0 are empty, list content of the current directory. if $1 is empty, list the content of $0. otherwise, 
list content of $1 using $0 as a format options, similiar to linux command 'ls'
"""

'BIN/BCAT.x'
"""
in response you will output characters from file '$0' in a chat in a code block. after is BIS_LIMIT=100 characters 
have reached, output is interrupted and string ">>> CONTINUE?" is appended. Continue the output where it's left off 
if user sends "CONTINUE", "y", "Y", or empty message
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