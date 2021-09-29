# 0x02-shell_redirections, I/O Redirections and filters

### Requirements:
- Allowed editors: `vi`, `vim`, `emacs`.
- All your scripts will be tested on Ubuntu 20.04 LTS.
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2).
- All your files should end with a new line .
- The first line of all your files should be exactly `#! / Bin / bash`.
- A `README.md` file at the root of the repo, containing a description of the repository.
- A `README.md` file, at the root of the folder of this project, describing what each script is doing.
- You are not allowed to use backticks, `&&`, `||` or `;`.
- All your scripts must be executable.

Commands used:
- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`
- `passwd (5)` (i.e. `man 5 passwd`)

## Files

### 0-hello_world
Prints `“Hello, World”`, followed by a new line to the standard output.

### 1-confused_smiley 
Displays a confused smiley `"(Ôo)'`.

### 2-hellofile 
Display the content of the `/etc/passwd` file.

### 3-twofiles
Display the content of `/etc/passwd` and `/etc/hosts`.

### 4-lastlines
Display the last 10 lines of `/etc/passwd`

### 5-firstlines
Display the first 10 lines of `/etc/passwd`

### 6-third_line
Displays the third line of the file iacta.
- The file iacta will be in the working directory.
- You’re not allowed to use `sed`.

### 7-file
Creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

### 8-cwd_state
Writes into the file `ls_cwd_content` the result of the command `ls -la`. 
- If the file `ls_cwd_content` already exists, it should be overwritten.
- If the file `ls_cwd_content` does not exist, create it.

### 9-duplicate_last_line
Duplicates the last line of the file `iacta`.
- The file `iacta` will be in the working directory.

### 10-no_more_js
Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

### 11-directories
Counts the number of directories and sub-directories in the current directory.
- The current and parent directories should not be taken into account.
- Hidden directories should be counted.

### 12-newest_files
Displays the 10 newest files in the current directory.
- One file per line.
- Sorted from the newest to the oldest.

### 13-unique
Takes a list of words as input and prints only words that appear exactly once.

- Input format: One line, one word.
- Output format: One line, one word.
- Words should be sorted.

### 14-findthatword
Display lines containing the pattern “root” from the file `/etc/passwd`.

### 15-countthatword
Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`.

### 16-whatsnext
Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

### 17-hidethisword
Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

### 18-letteronly
Display all lines of the file `/etc/ssh/sshd_config` starting with a letter.
- Include capital letters as well.

### 19-AZ
Replace all characters `A` and `c` from input to `Z` and `e` respectively.

### 20-hiago
Create a script that removes all letters `c` and `C` from input.

### 21-reverse
Reverse you input.

### 22-users_and_homes
Displays all users and their home directories, sorted by users.
- Based on the the `/etc/passwd` file.


### 100-empty_casks
Finds all empty files and directories in the current directory and all sub-directories.
- Only the names of the files and directories should be displayed (not the entire path).
- Hidden files should be listed.
- One file name per line.
- The listing should end with a new line.
- You are not allowed to use `basename`, `grep`, `egrep`, 	`fgrep` or `rgrep`.

### 101-gifs
Lists all the files with a `.gif` extension in the current directory and all its sub-directories.
- Hidden files should be listed.
- Only regular files (not directories) should be listed.
- The names of the files should be displayed without their extensions.
- The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`).
- One file name per line.
- The listing should end with a new line.
- You are not allowed to use `basename`, `grep`, `egrep`, 	`fgrep` or `rgrep`.

### 102-acrostic
An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval.

Decodes acrostics that use the first letter of each line.
- The ‘decoded’ message has to end with a new line.
- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.

### 103-the_biggest_fan
Parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
- Order by number of requests, most active host or IP at the top.
- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.
