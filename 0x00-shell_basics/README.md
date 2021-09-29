# 0x00-shell_basics, executable scripts.

## File 0-current_working_directory
Prints the absolute path name of the current working directory.

## File 1-listit
Displays the contents list of your current directory.

## File 2-bring_me_home 
Changes the working directory to the user’s home directory.
- You are not allowed to use any shell variables

## File 3-listfiles
Displays current directory contents in a long format.

## File 4-listmorefiles
Displays current directory contents, including hidden files (starting with `.`). Use the long format.

## File 5-listfilesdigitonly
Displays current directory contents.
- Long format.
- with user and group IDs displayed numerically.
- And hidden files (starting with `.`).

## File 6-firstdirectory
Creates a directory called `my_first_directory` in the `/tmp/` directory.

## File 7-movethatfile
Moves the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

## File 8-firstdelete
Deletes the file `betty`.
- The file `betty` is in `/tmp/my_first_directory`.

## File 9-firstdirdeletion
Deletes the directory `my_first_directory` that is in the `/tmp` directory.

## File 10-back
Changes the working directory to the previous one.

## File 11-lists
Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

## File 12-file_type
Prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.

## File 13-symbolic_link
Create a symbolic link to `/bin/ls`, named `__ls__`.
- The symbolic link should be created in the current working directory.

## File 14-copy_html
Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
- You can consider that all HTML files have the extension `.html`.


## File 100-lets_move
Moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- You can assume that the directory `/tmp/u` will exist when we will run your script.

## File 101-clean_emacs
Deletes all files in the current working directory that end with the character `~`.

## File 102-tree
Creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.
- You are only allowed to use two spaces (and lines) in your script, not more.

## File 103-commas
Write a command that lists all the files and directories of the current directory, separated by commas (`,`).
- Directory names should end with a slash (`/`).
- Files and directories starting with a dot (`.`) should be listed.
- The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning.
- Only digits and letters are used to sort; Digits should come first.
- You can assume that all the files we will test with will have at least one letter or one digit.
- The listing should end with a new line.

## File school.mgc
Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.
