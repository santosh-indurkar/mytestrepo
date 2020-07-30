#!/bin/bash

# Print name of the script
echo "Name of this script : $0"

read -p "Please enter your name : " USER
echo -e "\n\nHello this is $USER!!!"

# Use a variable
MYNAME="Linus Torvalds"
printf "\nFather of Linux : $MYNAME\n"

# Looping through command line inputs
for NAME in $@
do
  # Test the conditions using if-else-fi
  if [ $NAME = "Arjun" ]
  then
    echo "$NAME U R GR8"
  elif [ $NAME = "Suvarna" ]
  then
    echo "Nice to meet you $NAME"
  else
    echo "Hello $NAME"
  fi
done
