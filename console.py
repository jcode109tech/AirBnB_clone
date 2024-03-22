#!/usr/bin/python3
"""
   command line interpreter 
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


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

    def help_quit(self):
        """Help message for : quit command."""
        print("Quit command to exit the program\n")
    
    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

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


    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all BaseModel or all.
        Usage2: all<class name>
        """
        args = line.split()
        if len(args) == 0:
            print(storage.all())
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        instances = storage.all()
        class_instances = [str(instance) for key, instance in instances.items() if class_name in key]
        print(class_instances)


    def do_count(self, line):
        """
        Counts the number of instances of a class.
        Usage: <class name>.count()
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        instances = storage.all()
        class_instances = [instance for key, instance in instances.items() if class_name in key]
        print(len(class_instances)) 


    def default(self, line):
        """
        Handle command interpreter
        """
       
        commands = {'all': self.do_all,
                    "count": self.do_count,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update}
        
        args = line.split(".")
        print(args[0], args[1])
        if len(args) != 2:
            print("** Incorrect command format. Use 'User.command()' format. **")
            return

        class_name, command = args[0], args[1].strip("(")
        print(class_name)
        print("command", command)
        cmd_command = command.strip('()')
        # print("cmd_command  : ", cmd_command[0])
        # print("cmd_command2  : ", cmd_command[1])
        bracket = command[1].split(')')[0]
        # print("bracket", bracket)
        all_args = bracket.split(',')
        # print("all_args", all_args)
        instance_id = command.strip('()')
        print(instance_id)

        if class_name != "User":
            print("** Command not recognized **")
            return

        if cmd_command  in commands.keys():
            if cmd_command == "all" and bracket == "":
                # Handle the case of "<class name>.all()"
                return self.do_all(class_name)
            elif cmd_command != "update":
                return commands[
                        cmd_command]("{} {}".format(
                            class_name, bracket))
            elif cmd_command == "update":
                obj_id = all_args[0]
                attribute_name = all_args[1]
                attribute_value = all_args[2]
                return commands[
                        cmd_command]("{} {} {} {}".format(
                            class_name, obj_id, attribute_name,
                            attribute_value))
            elif cmd_command == "show":
                commands[command]("{} {}".format(class_name, instance_id))
            elif cmd_command == "count":
                instances = storage.all()
                class_instances = [instance for key, instance in instances.items() if class_name in key]
                print(len(class_instances))
                return
            else:
                if not class_name:
                    print("** class name missing **")
                    return

                try:
                    call = commands[cmd_command]
                    return call("{} {}".format(class_name, bracket))
                except Exception:
                    pass
                 # commands[command]([])      
        else:
            print("*** Unknown syntax: {}".format(line))
            return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
