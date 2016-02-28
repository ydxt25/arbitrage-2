#!/bin/sh

#openssl des3 -salt -k password -in file -out file.des3
#openssl enc -des3 -d -in file.des3 -out file

crpyt_file=../etc/passwd.des3

if [ ! -f $crpyt_file ];then
	echo "passwd.des3 not found"
	exit 0
fi

openssl enc -des3 -d -in $crpyt_file
