# File IO = use open() to open a file, default will be read-only, we can use 2nd positional "w" to write
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

with open("notes.txt","w") as f:
    f.write("hello\n")
    f.write("second line\n")
    f.close()


with open("hello1.txt") as f:
    contents = f.read().split()
    print(contents)

with open("hello1.txt") as f:
    f.seek(0)
    lines = f.readlines() #returns a list 
    cleaned_lines = [line.strip("\n") for line in lines]
    print(lines)
    print(cleaned_lines)

# Context Managers = No need to explicity close the file 
with open("hello.txt") as f:
    print(f.read())

with open("hello1.txt") as f:
    our_list = [line.strip("\n") for line in f]
    print(our_list)

# opening multiple files
with open("notes.txt") as src, open("uppercase.txt","w") as dest:
    for line in src:
        dest.write(line.upper())