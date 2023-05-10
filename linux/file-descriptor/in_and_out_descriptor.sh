#! /bin/bash

exec 3<> a
read line <&3
echo "read: $line"
echo -n "abcd" >&3

