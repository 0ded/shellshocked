#!/bin/bash

if [ -f $1 ]
then
chmod +x $1
sudo cp $1 /usr/local/bin/
else
  echo "$1 does not exist"
fi