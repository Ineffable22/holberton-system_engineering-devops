# 0x03-shell_variables_expansions, init files, variables and expansions.

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
- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`

### Files

### 0-alias
Creates an alias.
- Name: `ls`.
- Value: `rm *`.

### 1-hello_you
Prints `hello user`, where user is the current Linux user.

### 2-path
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

### 3-paths
Counts the number of directories in the `PATH`.

### 4-global_variables
Lists environment variables.

### 5-local_variables
Lists all local variables and environment variables, and functions.

### 6-create_local_variable
Creates a new local variable.
- Name: `BEST`.
- Value: `School`.

### 7-create_global_variable
Creates a new global variable.
- Name: `BEST`.
- Value: `School`.

### 8-true_knowledge
Prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.

### 9-divide_and_rule
Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
- `POWER` and `DIVIDE` are environment variables.

### 10-love_exponent_breath
Displays the result of `BREATH` to the power `LOVE`.
- `BREATH` and `LOVE` are environment variables.
- The script should display the result, followed by a new line.

### 11-binary_to_decimal
Converts a number from base 2 to base 10.
- The number in base 2 is stored in the environment variable `BINARY`.
- The script should display the number in base 10, followed by a new line.

### 12-combinations
Prints all possible combinations of two letters, except `oo`.
- Letters are lower cases, from `a` to `z`.
- One combination per line.
- The output should be alpha ordered, starting with `aa`.
- Do not print `oo`.
- Your script file should contain maximum 64 characters.

### 13-print_float
Write a script that prints a number with two decimal places, followed by a new line.
- The number will be stored in the environment variable `NUM`.

### 100-decimal_to_hexadecimal
Write a script that converts a number from base 10 to base 16.
- The number in base 10 is stored in the environment variable `DECIMAL`.
- The script should display the number in base 16, followed by a new line.

### 101-rot13
Encodes and decodes text using the rot13 encryption. Assume ASCII.

### 102-odd
Prints every other line from the input, starting with the first line.

### 103-water_and_stir
Adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.
- `WATER` is in base `water`.
- `STIR` is in base `stir.`.
- The result should be in base `bestchol`.
