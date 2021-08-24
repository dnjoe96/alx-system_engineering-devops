#!/bin/bash

if [ $1 == '--help' ]
then
	echo 'USAGE: ./easy.sh filename command usage'
	exit

elif [ $# -ne 3 ]
then
	echo 'Sorry Incomplete Paramters'
        echo " "
        exit
else
	echo 'processing file'
fi


filename=$1
commandd=$2
use=$3

echo "$filename"

echo "creating file"
touch 0x03-shell_variables_expansions/$filename

echo "enter file information - $commandd"
echo "#!/bin/bash" > 0x03-shell_variables_expansions/$filename
echo "$commandd" >> 0x03-shell_variables_expansions/$filename

echo "setting permissions"
chmod u+x 0x03-shell_variables_expansions/$filename

echo "writing readme file"

echo "\`$commandd\` --> $use" >> 0x03-shell_variables_expansions/README.md 
echo " " >> 0x03-shell_variables_expansions/README.md

echo "DONE"
#./0x00-shell_basics/1-listit

echo "wc -l\n" 
wc -l 0x03-shell_variables_expansions/$filename

# you can change the directory with the syntax
# :%s/oldname/newname/    ENTER

