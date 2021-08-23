#!/bin/bash

filename=$1
commandd=$2

echo "$filename"

echo "creating file"
touch 0x02-shell_redirections/$filename

echo "enter file information - $commandd"
echo "#!/bin/bash" > 0x02-shell_redirections/$filename
echo "$commandd" >> 0x02-shell_redirections/$filename

echo "setting permissions"
chmod u+x 0x02-shell_redirections/$filename

echo "DONE"
#./0x00-shell_basics/1-listit

echo 'wc -c' 
tail -1 0x02-shell_redirections/$filename | wc -c
