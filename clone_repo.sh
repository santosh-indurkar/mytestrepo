#!/bin/bash

# Read the file containing repository links
file_path='/home/vagrant/myrepo/mytestrepo/repolist.txt'
read -p "Enter the directoy for cloning : " dirname

# Creating new directory as user input
if [ ! -d "$dirname" ]
then
  echo -e "\n Creating new directory.\n"
  mkdir -p -- "$dirname"
else
  echo "Directory already exists."
fi

# Change to newly created directory
cd "$dirname"
pwd

# Cloning the repos one by one in newly created directory
while read line
do
  git clone $line
done < "$file_path"

# Wait for 10 sec and then delete the newly cloned repos
echo "Sleeping for 10 sec..."
sleep 10
cd ..
pwd
echo -e "Deleting newly created repos from : $dirname"
rm -rf $dirname/
