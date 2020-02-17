#!/usr/bin/python3
""" AirBnb Console """
import cmd
from models.base_model import BaseModel
from models import storage
import sys

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnt) "
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Exits the program """
        return True

    def do_EOF(self, arg):
        """The program closes because no more input can be read """
        return True
    
    def do_create(self, arg):
        """Creates a new class instance
        
        Usage: create [Class Name]"""
        if not len(arg):
            print('** class name missing **')
        elif arg in self.class_list:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id

        Usage: show [Class Name] [ID]"""
        args = arg.split()
        all_ins = storage.all()
        if not len(args):
            print("** class name missing **")
        elif args[0] in self.class_list:
            if len(args) < 2:
                print("** instance id missing **")
            elif (args[0] + "." + args[1]) in all_ins:
                print(all_ins[(args[0] + "." + args[1])])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id
        
        Usage: destroy [Class Name] [ID]"""
        args = arg.split()
        all_ins = storage.all()
        if not len(args):
            print("** class name missing **")
        elif args[0] in self.class_list:
            if len(args) < 2:
                print("** instance id missing **")
            elif (args[0] + "." + args[1]) in all_ins:
                del all_ins[(args[0] + "." + args[1])]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
