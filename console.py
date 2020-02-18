#!/usr/bin/python3
""" AirBnb Console """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
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
        all_ins = models.storage.all()
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
        all_ins = models.storage.all()
        if not len(args):
            print("** class name missing **")
        elif args[0] in self.class_list:
            if len(args) < 2:
                print("** instance id missing **")
            elif (args[0] + "." + args[1]) in all_ins:
                del all_ins[(args[0] + "." + args[1])]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
    
    def do_all(self, arg):
        """Prints all string representation of all instances 
        
        Usage: all or all [Class Name]"""
        all_ins = models.storage.all()
        if arg:
            if arg in self.class_list:
                for obj in all_ins.values():
                    if type(obj).__name__ == arg:
                        print(obj)
            else:
                print("** class doesn't exist **")
        else:
            for obj in all_ins.values():
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        all_ins = models.storage.all()
        args = arg.split('"')
        if len(args) > 1:
            value = args[1]
        else:
            value = ""
        args = args[0].split()
        if len(args):
            if args[0] in self.class_list:
                if len(args) >= 2:
                    if (args[0] + "." + args[1]) in all_ins:
                        if len(args) >= 3:
                            if value:
                                obj = all_ins[args[0] + "." + args[1]]
                                setattr(obj, args[2], value)
                                obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
