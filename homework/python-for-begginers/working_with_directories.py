# We gonna use pathlib to deal with directories and files
from pathlib import Path

# Absolute path -  start from Root drive - C:/Program/files etc . 

# Relative path - ./for parent directory 
path = Path() #points to the parent directory

for file in (path.glob('*.py')):
    print(file) #print all our py files in the working relative path from our python-for-begginers directory

