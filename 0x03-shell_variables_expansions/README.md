# shell variables
 
`echo $PATH | tr -s ":" "\n"` --> to create a script that counts the number of directories in the PATH
 
`echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"` --> a script that prints all possible combinations of two letters except oo
 
`printf "%.2f\n" $NUM` --> To print a number with two decimal places, followed by a new line
 
