from pathlib import Path
from os import getcwd, chdir

# What is Pathlib?
# Pathlib is a module that allows us to work with files and directories in a more object-oriented way.
# It is a part of the Python standard library, so we don't need to install it.

# Why use Pathlib?
# Pathlib makes working with files and directories much easier.
# It is also cross-platform, so it works on Windows, Mac, and Linux.

# When to use Pathlib?
# When you need to work with files and directories.

# How to use Pathlib?
# We can create a Path object by passing it a string of the file or directory path.
# We can also use the Path() function to create a Path object.
# We can use the Path object's methods to work with files and directories.

def main():
    # Let's create a Path object that represents the current directory.
    # We can use the getcwd() function to get the current working directory.
    # We can then pass the current

    # print("Current working directory:", Path.cwd())

    # Home directory
    # We can use the home() function to get the home directory.
    # print("Home directory:", Path.home())

    # check if path exists
    # print("Current working directory:", Path.cwd())
    # path = Path("test.txt")
    # print("Does path exist?", path.exists())
    # print("Is path a file?", path.is_file())
    # print("Is path a directory?", path.is_dir())

    # create a new directory
    # path = Path("new_dir")
    # path.mkdir()
    # print("Does path exist?", path.exists())
    # print("Is path a file?", path.is_file())
    # print("Is path a directory?", path.is_dir())

    # # create a new file
    # path = Path(".env")
    # path.touch() # create a new file
    # print("Does path exist?", path.exists())
    # print("Is path a file?", path.is_file())
    # print("Is path a directory?", path.is_dir())

    # # rename a file
    # path = Path("new_file.txt")
    # path2  = path.rename("new_file_renamed.txt")
    # print("Does path exist?", path2.exists())
    # print("Is path2 a file?", path2.is_file())

    # # delete a file
    # path = Path("new_file.txt")
    # path.unlink()
    # print("Does path exist?", path.exists())

    # # delete a directory
    # path = Path("new_dir")
    # path.rmdir()
    # print("Does path exist?", path.exists())

    # # get the parent directory
    # path = Path("test.txt")
    # print("Parent directory:", path.parent.cwd())

    # # get the file name
    # path = Path("test.txt")
    # print("File name:", path.name)

    # # get the file suffix
    # path = Path("test.txt")
    # print("File suffix:", path.suffix)

    # # get the file stem
    # path = Path("test.txt")
    # print("File stem:", path.stem)

    # # get the file size
    current_dir = Path.cwd()
    print("Current directory:", current_dir)
    path = Path("test.txt")
    print("File size:", path.stat().st_size)

if __name__ == "__main__":
    main()
