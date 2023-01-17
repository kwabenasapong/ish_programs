#!/usr/bin/env bash
# tests if file is a regular file
# the file will be given to the script as an argument
if test -f "$1" ;
then
	echo "$1 exists"
else
	echo "$1 does not exist"
fi
