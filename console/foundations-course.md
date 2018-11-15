# Console Foundations

### Table of Contents
- Installing Software
- Environment and Redirection
- Processes
- Users and Permissions
- Getting Started

# Console: Installing Software 
> installing and configuring software is common in the CLI.

> Two main ways to install:
1. (best!) use a package manager to install software for you.
2. build the software from its source code files

## Introduction to Package Managers

Having a package manager on your computer can make managing your software much easier.
 
Package manager names:
* APT, for Debian-based Linux (such as Ubuntu)
* YUM is for some GNU/Linux distro's
* RPM is for some Linux too 
 
What else do package managers do?
* manage dependencies
* handle updates
* uninstall
 
### Commands

```
sudo apt-get update

sudo apt-cache search <PATTERN>

sudo apt-get install <PACKAGE>

sudo apt-get upgrade

sudo apt-get remove <PACKAGE>
```

* apt-get update Update your package catalog on your computer
    * good to run every once in a while
    * example: to see if git is installed, type:  git   
* apt-cache search PATTERN Search the available packages for a pattern
* apt-get install PACKAGE Install one or more packages
* apt-get upgrade Upgrade to the latest version of all the packages installed
    * also good to run every once in a while
        * latest packages often have protective security updates
    * usually wanna run upgrade after you run update.
* apt-get remove PACKAGE Remove or uninstall package from your computer
 
## Building Software From Source

### Procedure Overview:
1. DL src file
2. untar file
3. run ./configure script
4. make 
5. sudo make install

### Linux-Specific Commands

```
sudo apt-get update

sudo apt-get install build-essential

curl -O <URL>

tar -xvf FILENAME.tar.gz

./configure

make

sudo make install
```

* sudo apt-get update Update your computer's catalog of available software
* sudo apt-get install build-essential Install the tools needed to build software from source code.
    * [x]done on Linux machine, once and for all.
    * make is among those programs that this installs
        * make is a program we use to build and install software from source
        * After the install command, if you type which make, and see the path /usr/bin/make appear, you can conclude [x]the build tools were successfully installed
* curl -O URL Download the file at the URL
    * curl is a prgm that makes requests to the internet
    * (from above)   -O (CAPITAL O!!) is the option to save file to our machine
* tar -xvf FILENAME.tar.gz Decompress the tar.gz file to the current directory
    * a tar file, or tarball, is like a zip file.
    * To untar is to unzip (syn.)
    * -xvf  This may vary with other consoles.  x is extract, v is verbose output, f points to tar file. 
* ./configure Run the configure script that comes with the source code. This creates a Makefile
    * The dot (".") means our current directory (without the dot the system would search elsewhere in our computer)
* make Run the build specified in the Makefile
    * after this, executable files are created, but we can't run it yet -- those executables must be moved to our path 
* sudo make install Run the install script from the Makefile. This installs the program
 



# Console: Environment and Redirection

> The environment is a general term that refers to a particular configuration of hardware or software. It defines where the computer should look for programs, where your important folders are, and other configuration data. We will look at how to manage your environment and how to do other useful things, like finding files on your computer.

## Environment Variables

> Environment variables store configuration information on our computers. Here, we learn how to read and write values to the environment.

```
which <pgrm>
which echo
export PATH=/home/treehouse/bin:$PATH
```

(This cmd appends the new path to the front of the variable PATH)

`echo $PATH`

(PATH is where executable files will be searched for and found)
(example: echo is an executable file)

```
ls -la

nano .bashrc

export PATH=/home/treehouse/bin:$PATH
```

ls -la

(This shows .bashrc file, or .bash profile file)

`. ~/.bashrc`

(The above line will restart bash.)

nano .bashrc

(This edits the file that runs every time we start up bash)

(Within nano, I can add to bottom of this .bashrc file: )

export PATH=/home/treehouse/bin:$PATH

(next time you log out and back in, the PATH will be updated for me)

</end>


 
### Commands

```
VARIABLE=value

export VARIABLE=value

env

bash

echo

```

* VARIABLE=value - set a local environment variable
* export VARIABLE=value - set an environment variable that will be visible to child processes
* env - view environment variables
* bash - start a new session within your current session
* echo - display the arguments sent to echo


## Find and Grep

extremely useful when you are trying to find files.
 
### Troubleshooting
If you have deleted your hello.txt and want it back *from a cloud-based environment*, run the following command to restore it to your home directory.
(Note: this might only work in Treehouse-provided console)

`curl -Lo ~/hello.txt http://trhou.se/console_hello`

### Commands: find

```
find . -name "filename.txt"

find / -name "filename.txt" 

find searchdir1 searchdir2 -name "filename.txt"

man find
```

* find
    * look for files with the name search starting from your current location 
        * find . -name "filename.txt"
            * The period (.) indicates the current directory.
        * find / -name "filename.txt" 
            * The slash (/) indicates the root directory -- search is done in entire system
    * find searchdir1 searchdir2 -name "filename.txt" - to search two or more directories at once
    * Use quotes around filenames for good practice. They are optional; they can allow multiple words to be in one argument.
    * man find -- shows the manual for using find

## grep: Global Reg-Ex Print

### Commands

```
grep "pattern" file

grep -n <TARGET_WORD> filename.txt

grep -i <TARGET_WORD> filename.txt

grep -v <TARGET_WORD> filename.txt

man grep
```

* grep "pattern" file - find any lines that contain the pattern in the given file
* grep options:
    * grep -n targetword filename.txt -- prints the line number of each appearance of targetword 
    * grep -i targetword filename.txt -- case-insensitive search for targetword 
    * grep -v targetword filename.txt -- prints the lines without the targetword 
    * man grep -- shows the manual for using grep


## Pipes and Redirection

> Being able to manipulate the input and output of programs means you can construct some very useful commands by using the simple commands you know in new and interesting ways.

### Commands

```
somecommand < inputfile

somecommand > outputfile

command1 | command2

```

### Descriptions

* `somecommand < inputfile` run somecommand with input from inputfile, instead of the keyboard
* `somecommand > outputfile` run somecommand with output to outputfile instead of the terminal screen.
* `command1 | command2` This pipes the output of command1 to the input of command 2
sort    This pipes the output of command1 to the input of command 2
 
### Examples

`grep happy hello.txt > grep_output.txt`

[cmd] [str] [in_file]  [out_file] 

(by default, single > overwrites output.txt file)
 
`grep happy hello.txt`

[cmd] [str] [in_file]
 
  (searches for 'happy' in hello.txt file, and by default outputs it to console)

`grep happy`

[cmd] [str]

  (searches for 'happy', by default searching in the user cmd prompt)
 
`grep happy > hello.txt`

[cmd] [str] [out_file]

  (This still searches for 'happy' in the user cmd prompt; but it outputs results into .txt file. 
   by default, grep searches the user cmd prompt.)
 
`grep sugar hello.txt >> grep_output.txt`

(double >> appends search results of 'sugar' into output.txt file)
 
 
## Redirecting "stream #2":
Stream #2 is Standard Error (the standard output destination for errors).
By default this is printed to the user console.

`find / -name "sudoers"` (default)

`find / -name "sudoers" 2> error_log.txt`
-- Now it writes errors (stream #2: Standard Error) to the .txt file.
 
`find / -name "sudoers" 2> /dev/null`
-- Special file that will delete anything written into it.




# Console: Processes 

> A process is the building block of how our computers run programs. It represents an instance of a program running. You can run multiple instances of a single program by creating multiple processes. Anything that is running has a process, and understanding how to manage your processes will keep you in control of your computer. 
 
## Processes

> Processes are instances of running programs on your computer. You can run multiple instances of a single program by creating multiple processes. Understanding how processes work is crucial for using the console effectively.
 
## Programs

```
top

ps

ps aux
```

### Descriptions

* top - Show active processes (NOT in DELL XPS)
    * top is interactive, live-updated, and sorted list
* input commands into top:
    * sort (type F or O)
    * help menu (type the question mark)
    * quit (type Q)
* ps - Show process statuses 
    * ps aux   (all processes, for user x.)
        * (NOT in DELL XPS)
        * (note: aux is an option, even though we don't type a hyphen, or -aux)
        * displays process ID for specific task (eg 1012)
        * pts/1 or pts/2: the terminals or windows into our system
    * Bash interprets console keystrokes, and formats output of that onto screen
* grep - Search for a pattern

### Find a process by name

> Use the following command to search for a running process using a pattern.

`ps aux | grep "SEARCH_PATTERN"`
 
## Pausing and Resuming

> You can pause a running process in the console in order to perform some other action. It can easily be resumed allowing you to multitask from a single console window.
 
## Definitions:

job: a process you own, that you started in your console window.  jobs are numbered as job 1, job 2, etc.
 
### Key Sequences
* `ctrl + z` Stop (pause) a process
* `ctrl + c` Terminate (exit) a process

### Commands

* `fg`             -- Bring a job to the foreground

* `jobs`          -- List jobs for your current session (as opposed to processes on the system)

Sending a process straight to the background : ampersand (&)

`nano &`

`top &`
 

## Killing Processes

> Sometimes a process gets out of control and you have to kill it yourself. There are several options available when killing processes and great care must be taken whenever you use the kill command.

### Commands

* `kill`     -- kill is the name of a program that sends a signal to a process

### Signals
* KILL or 9 - Force a process to exit
* TERM (default) - Request a process terminate normally
* STOP - Stop or pause a process

### Examples

for process ID 1234.

```
kill -KILL 1234

kill -TERM 1234
 
kill -STOP 1234 
```

(akin to ctrl+z)

> `TERM` sends a signal to the process to end, and will trigger any cleanup routines programmed into the running application to tidy up before exiting.

> `-KILL` (aka -9) will kill the process immediately without any cleanup. This is sometimes necessary if the process is really stuck and -TERM doesn't work.
 



# Console: Users and Permissions

(09-Sep-2018 Mon)

How to setup and manage users, and how permissions are applied to files and folders.

## Creating Users

```
whoami

adduser

su

sudo

!!

sudo !!

exit
```


whoami
adduser
su       -- switch user
sudo
!!       -- runs previous command.  aka "two bangs"
sudo !!  -- runs previous command as superuser
exit     -- exits from the secondary user, back to the superuser

## File Permissions

A file mode: refers to permissions settings of a file

`chmod` -- change permissions of a file or a dir

`-rwxrwxrwx`, -uuugggooo (user, group, owner)

(the first hyphen means regular file, from stackoverflow)


### example: 

```
chmod 640

rw-r-----
```

If a file has the permissions "-r-x-w----" and the ownership is "user:treehouse, group:teachers" and I am the user "mike" and I belong to the group "teachers", may I write to this file?  (try it, by adding a user/ changing a file's owner )


To add the read permissions only for the user and group of a file:

`chmod ug+r`


## File Ownership

changing owner, not permissions

```
sudo chown mike hello.txt

sudo chown mike:mike hello.txt
```

## Sudo

root user: overrides every permission on every file

when sudo command prompts for a password, it wants user's password, NOT the root password.

(06-Sep-2018 Th)




# Console: Getting Started

The Unix OS family (aka Unix derivatives):

* attributes:
    * POSIX compatibility
* members:
    * GNU Linux 
    * Mac OS X
    * BSD


Reasons to learn Linux shell scripting:
* Ubiquity:
    * Most servers are Linux-based. Most websites are hosted there 
    * Many systems are Linux/Unix-based
    * Apache and nginx are common Linux-based web server software
* Linux distributions:
    * Ubuntu
    * Redhat
    * CentOS
    * Parrot
OS (from Unit 5: installing software)
* Linux has many package managers
* Ubuntu is based on Debian Linux.
* Linux distributions share the same core.However, tools, configs and options vary from distro to distro
home
"On the Mac, the home directories are in /users/username"
"On Linux, this directory is in /home/username"
* 3 ways to go to home dir
    * cd /home/myusername
    * cd $HOME
    * cd ~


to view text file:
commands to view (but not modify) the contents of a text file:
* less is a open-source alias of more  
* more works in Dell XPS PC


to edit: in-console text editors
(Note: Neither nano nor pico (nor vim nor emacs) work in Del XPS PC.) :(
     nano: an open-source alias of pico
     pico
         Compared to Vim and Emacs:
             nano is easier to learn 
             nano is less powerful


Bash commands
~             (tilde): home dir
.             (dot): current dir
..               (dot dot): move up one dir
clear
pwd      (print working dir)
ls           (list)
    ls -l    (long list format)
    ls -a    (includes hidden files)
    
`ls /dir1/dir2`

To demonstrate that you don't have to move your present location, in order to list files in another directory

concatenate: `cat file1.txt file2.txt`

rename file: `mv old_name.txt new_name.txt`

copy a file: `cp old_name.txt new_name.txt`

copy a directory: `cp -r dir1 dir2`

remove a file: `rm unwated_file.txt`

remove a directory: `rm -r dir1`

`mkdir` -- make dir

by default, only allowed to make 1 directory level at a time.

Example of nested directory creation:

`mkdir -p dir_lev1/dir_lev2/dir_lev3`

