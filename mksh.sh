#!/bin/bash

if [ -f $1 ]
then
touch $1
chmod +x $1
else
  echo "$1 does not exist"
fi