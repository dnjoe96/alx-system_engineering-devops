# shell variables
 
`echo $PATH | tr -s ":" "\n"` --> to create a script that counts the number of directories in the PATH
 
`echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"` --> a script that prints all possible combinations of two letters except oo
 
`printf "%.2f\n" $NUM` --> To print a number with two decimal places, followed by a new line

`$commandd\` --> $use 

`alias ls="rm *"` -->'remove all files in the current directory'

`echo "hello $USER"` --> 'says hello the current user'

`export PATH=$PATH:/action` --> 'Adds /action to the PATH global variable'

`env` --> 'prints all the environmental variable'

`BETTY=Holberton` --> 'set a new local variable'

`export HOLBERTON=Betty` --> 'set a new global variable'

`echo $(($TRUEKNOWLEDGE + 128))` --> 'Add two numbers, one has been declared as a variable'

`echo $(($POWER / $DIVIDE))` --> 'Divide two numbers'

`echo $(($BREATH**$LOVE))` --> 'find exponent'
`printf "%x\n" $DECIMAL` --> Cconvert to base 16 from base 10
 
`set` --> list all local, environmental variables and functions
 
