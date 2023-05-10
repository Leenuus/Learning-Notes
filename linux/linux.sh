#! /bin/bash

# signals
## SIGHUP 1 
## SIGINT 2 <C-c> 
## SIGKILL 9 

## use kill to send a signal
## kill -<signal> <pid>

## use trap to trap signals, SIGINT, SIGHUP, SIGSTP
trap "echo 'I trapped ctrl + c'" SIGINT
## cancel trap
## trap -- <Signal>

## use tee to redirect stdin and stdout to a file, also print to screen
## use -a option to append but not overwrite
echo "hello" | tee -a command.log


# function

## define
## function name {}
## name(){}

## function return value
## 1. return INTEGER
## 2. echo 
## 3. decided by the last command

# redirect and file descriptor

## file descriptor
## 0: stdin
## 1: stdout
## 2: stderr

## merge stdout: &> 
## temperial redirect output to: >&[descriptor]
## pernament redirect: exec [descriptor]> [file|descriptor]

## redirect stdin from a file: exec 1< [file]
## backup stdin: exec [descriptor]<&0

## custom file descriptor 
## overwrite: exec [descriptor]>[file|descriptor]
## append: exec [descriptor]>>[file]

## close file descriptor
exec [descriptor]>&-

## list current process's file descriptors
lsof -a -p $$ 

## discard output
## > /dev/null
## clear a file
## [file] < /dev/null

# special variables
## $# number of arguments
## $@ all arguments, as tuple
## $* all arguments, as one 
## $? exit code 
## $! pid of last program running in the background
## $$ pid 

# niceness
## nice -<niceness> <command>
## renice -n <niceness> -p <pid>



