#!/bin/bash

filename=$1
commandd=$2

echo "$filename"

echo "creating file"
touch 0x00-shell_basics/$filename

echo "enter file information - $commandd"
echo "#!/bin/bash" >> 0x00-shell_basics/$filename
echo "$commandd" >> 0x00-shell_basics/$filename

echo "setting permissions"
chmod u+x 0x00-shell_basics/$filename

echo "run script"
./0x00-shell_basics/1-listit

