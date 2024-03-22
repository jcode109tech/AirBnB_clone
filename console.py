#!/usr/bin/python3
"""
   command line interpreter 
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


#----------------------------------------------
import sys
import json
from models.base_model import BaseModel
from models.user import User  # Import the User class

# Define command functions for all operations

# Function to retrieve all instances of a class
def all_instances(args):
    """
    Prints all string representation of all instances based on the class name.
    Usage: all <class name>
    """
    if len(args) == 0:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in globals():
        print("** class doesn't exist **")
        return
    instances = globals()[class_name].all()
    if not instances:
        print("No instances found for class:", class_name)
        return
    for instance in instances:
        print(instance)

# Define your class that inherits from cmd.Cmd

# Define the commands dictionary
commands = {
    "all": all_instances,  # Use all_instances directly instead of do_all method
    # Add other commands for create, show, destroy, update with BaseModel and User
}

# Function to handle the command interpreter
def command_interpreter():
    while True:
        user_input = input("(hbnb) ")
        args = user_input.split()
        if len(args) == 0:
            continue
        command = args[0]
        if command not in commands:
            print("** Unknown command **")
            continue
        commands[command](args[1:])


#----------------------------------------------
class HBNBCommand(cmd.Cmd):
    """
      Runs cmd as shell
    """

    prompt = '(hbnb)'

    # names = ["BaseModel", "User", "State",
    #           "City", "Amenity","Place", "Review"]

    def do_quit(self, arg):
        """ <Quits/Exits> programm """
        return True

    def do_EOF():
        """ End of file """
        print("Exiting...")
        return True

    # def do_help(self, arg: str) -> bool | None:
    #     """ Help documentation : always updataed """
    #     return super().do_help(arg)
    def help_quit(self):
        """Help message for : quit command."""
        print("Quit command to exit the program\n")
    
    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all BaseModel or all.
        Usage2: all<class name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            # print(storage.all())
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return   
        # instances = storage.all()
        # instances = globals()[class_name].all()
        cls = globals()[class_name]
        if not hasattr(cls, 'all'):
            print(f"** {class_name} doesn't have 'all' method **")
            return
        instances = cls.all()
        class_instances = [str(instance) for key, instance in instances.items() if class_name in key]
        # print(class_instances)
        if not class_instances:
            print("No instances found for class:", class_name)
            return
        for instance in class_instances:
            print(instance)

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + " " + instance_id
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + " " + instance_id
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()
        print("** class instance destroyed **")


    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update BaseModel 1234-1234-1234 email "aibnb@mail.com".
             : (hbnb)update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + " " + instance_id
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value_str = args[3]
        if attribute_value_str.startswith('"') and attribute_value_str.endswith('"'):
            attribute_value_str = attribute_value_str[1:-1]
        attribute_value = None
        try:
            attribute_value = int(attribute_value_str)
        except ValueError:
            try:
                attribute_value = float(attribute_value_str)
            except ValueError:
                 attribute_value = attribute_value_str
        setattr(instances[key], attribute_name, attribute_value)
        instances[key].save()
        print("** updated **")

    def default(self, line):
        print("** Command not recognized **")

    # def command_interpreter():
    #     """
    #         Handle command interpreter
    #     """

    #     while True:
    #         user_input = input()
    #         args = user_input.split('.')
    #         if len(args) == 0:
    #             continue
    #         Users = args[0]
    #         command = args[1]
    #         if Users == "User":
    #             if command not in HBNBCommand.commands:
    #                 print("** Unknown command **")
    #                 continue
    #             HBNBCommand.commands[command](args[1:])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
