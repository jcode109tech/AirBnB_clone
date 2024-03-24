#!/usr/bin/python3
"""
command line interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Runs cmd as shell
    """

    prompt = '(hbnb) '

    State_names = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        'End of file'
        print()
        return True

    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Usage: create BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.State_names:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
        Usage: show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.State_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + "." + instance_id
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Usage: destroy BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.State_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + "." + instance_id
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        storage.save()
        print("** class instance destroyed **")

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update BaseModel 1234-1234-1234 email "aibnb@mail.com".
            : (hbnb)update BaseModel 49faff9a-6318-451f-87b6-910505c55907
            first_name "Betty"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.State_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = storage.all()
        key = class_name + "." + instance_id
        print(key)
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        att_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        att_value_str = args[3]
        if att_value_str.startswith('"') and att_value_str.endswith('"'):
            att_value_str = att_value_str[1:-1]
        attribute_value = None
        try:
            att_value = int(att_value_str)
        except ValueError:
            try:
                att_value = float(att_value_str)
            except ValueError:
                att_value = att_value_str
        setattr(instances[key], att_name, attribute_value)
        instances[key].save()
        print("** updated **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        Usage: all BaseModel or all.
        Usage2: all<class name>
        """
        args = line.split()
        if len(args) == 0:
            print(storage.all())
            return
        class_name = args[0] if args else None
        if class_name not in HBNBCommand.State_names:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        class_instances = [str(instance)
                           for key, instance in instances.items()
                           if class_name in key]
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
        class_instances = [instance
                           for key, instance in instances.items()
                           if class_name in key]
        print(len(class_instances))

    def default(self, line):
        """
        Handle command interpreter
        """

        commands = {'all': self.do_all,
                    'count': self.do_count,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update,
                    }

        args = line.split('.')

        if len(args) != 2:
            print("** Incorrect command format.")
            print("Use 'User.command()' format. **")
            return

        class_names = line.split('(')[0]
        # print(class_names)
        command = line.split('(')[1].split(')')[0]
        # print(command)
        comd_commands = class_names.split('.')
        class_name_User = comd_commands[0]
        cmd_command = comd_commands[1]
        # print(cmd_command)

        if class_name_User not in HBNBCommand.State_names:
            print("** Command not recognized **")
            return

        if cmd_command in commands.keys():
            if cmd_command == "all" and command == "":
                return self.do_all(class_name_User)
            elif cmd_command == "show":
                command_update = command.split(',')
                obj_id = command_update[0]
                new_obj_id = obj_id.split('"')
                save_new_obj_id = new_obj_id[1]
                return commands[cmd_command]("{} {}".format(class_name_User,
                                                            save_new_obj_id))
            elif cmd_command == "count":
                instances = storage.all()
                class_instances = [instance
                                   for key, instance in instances.items()
                                   if class_name_User in key]
                print(len(class_instances))
                return
            elif cmd_command == "destroy":
                command_update = command.split(',')
                obj_id = command_update[0]
                new_obj_id = obj_id.split('"')
                save_new_obj_id = new_obj_id[1]
                return commands[cmd_command]("{} {}".format(class_name_User,
                                                            save_new_obj_id))
            elif cmd_command == "update":
                command_update = command.split(',')
                obj_id = command_update[0]
                new_obj_id = obj_id.split('"')
                save_new_obj_id = new_obj_id[1]
                attribute_name = command_update[1]
                attribute_value = command_update[2]
                return commands[
                        cmd_command]("{} {} {} {}".format(
                            class_name_User, save_new_obj_id,
                            attribute_name, attribute_value))
            else:
                if not class_name_User:
                    print("** class name missing **")
                    return

                try:
                    call = commands[cmd_command]
                    return call("{} {}".format(class_name_User, command))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(line))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
