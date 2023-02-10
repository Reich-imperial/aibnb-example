#!/usr/bin/python3
""" This module defines the (hbnb) console """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ EOF signal to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del (storage.all()[f"{args[0]}.{args[1]}"])
            storage.save(self)

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name """
        args = arg.split()
        if len(args) == 0:
            print([str(value) for key, value in storage.all().items()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            store = storage.all().items()
            print([str(v) for k, v in store if k.startswith(args[0])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
