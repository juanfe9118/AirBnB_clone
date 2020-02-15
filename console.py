#!/usr/bin/python3
""" AirBnb Console """
import cmd
import sys


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnt) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ The program closes because no more input can be read """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
