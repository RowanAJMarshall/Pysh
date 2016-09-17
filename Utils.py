import os
import shutil


def ls(args):
    (columns, lines) = shutil.get_terminal_size((80, 30))
    letter_count = 0
    for root, dirs, files in os.walk(".", topdown=True):
        # Print files
        for name in files:
            letter_count += len(name) + 2
            if letter_count > columns:
                print("\n", end="")
                letter_count = len(name) + 2
            print(name, end="  ")
        # Print directories
        for name in dirs:
            letter_count += len(name) + 2
            if letter_count > columns:
                print("\n", end="")
                letter_count = len(name) + 2
            print(name, end="  ")
    print("\n", end="")


def cd(args):
    current_path = os.getcwd()
    new_path = os.path.join(current_path, args[1])
    # print(new_path)
    try:
        os.chdir(new_path)
    except FileNotFoundError:
        os.chdir(current_path)
        print("Pysh: cd: " + args[1] + " No such file or directory")


def clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')


def cat0(args):
    filename = args[1]
    try:
        with open(filename) as my_file:
            for line in my_file:
                print(line, end="")
    except FileNotFoundError:
        print("Pysh: cat: " + args[1] + " No such file or directory")
