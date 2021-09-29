# 0x01-shell_permissions, executable scripts

# File 0-iam_betty
Switches the current user to the user `betty`.
- You should use exactly 8 characters for your command (+1 character for the new line).
- You can assume that the user `betty` will exist when we will run your script.

# File 1-who_am_i
Prints the effective username of the current user.

# File 2-groups
Prints all the groups the current user is part of.

# File 3-new_owner
Changes the owner of the file `hello` to the user `betty`.

# File 4-empty
Creates an empty file called `hello`.

# File 5-execute
Adds execute permission to the owner of the file `hello`.
- The file hello will be in the working directory.

# File 6-multiple_permissions
Adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
- The file `hello` will be in the working directory.

# File 7-everybody
Adds execution permission to the owner, the group owner and the other users, to the file `hello`.
- The file hello will be in the working directory.
- You are not allowed to use commas for this script.

# File 8-James_Bond
Sets the permission to the file `hello` as follows:
- Owner: no permission at all.
- Group: no permission at all.
- Other users: all the permissions.
- The file `hello` will be in the working directory You are not allowed to use commas for this script.


# File 9-John_Doe
Sets the mode of the file `hello` to `-rwxr-x-wx`.
- The file `hello` will be in the working directory.
- You are not allowed to use commas for this script.

# File 10-mirror_permissions
Sets the mode of the file `hello` the same as `olleh’s` mode.
- The file `hello` will be in the working directory.
- The file `olleh` will be in the working directory.

# File 11-directories_permissions
Adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

# File 12-directory_permissions
Creates a directory called `my_dir` with permissions 751 in the working directory.

# File 13-change_group
Changes the group owner to `school` for the file `hello`.
- The file `hello` will be in the working directory.

# File 100-change_owner_and_group
Change the owner to `vincent` and the group owner to `staff` for all files and directories in the working directory.

# File 101-symbolic_link_permissions
Changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.
- The file `_hello` is in the working directory.
- The file `_hello` is a symbolic link.

# File 102-if_only
Changes the owner of the file `hello` to `vincent` only if it is owned by the user `guillaume`.
- The file hello will be in the working directory.

# File 103-Star_Wars
Write a script that will play the StarWars IV episode in the terminal.
