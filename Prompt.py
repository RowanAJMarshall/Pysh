import os
import Utils


def prompt():
    print("\n" + str(os.getcwd()) + " :-> ", end="")
    i = input()
    return i


def run_command(args):

    if args[0] == "ls":
        return Utils.ls(args)

    elif args[0] == "cd":
        return Utils.cd(args)

    elif args[0] == "clear":
        return Utils.clear(args)

    elif args[0] == "cat":
        return Utils.cat0(args)

    elif args[0] == "":
        return None
    else:
        print("Command \" " + args[0] + "\" not recognised")
        return False
