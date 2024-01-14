#!/usr/bin/python3
"""Module for the console"""


from models import storage
from models.base_model import BaseModel
from models.user import User
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Is the main Class for creating the command and the action
    """
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                   "Review"]

    def do_show(self, args):
        """Print the string representaion of an instance"""
        class_representation = ""
        go_on = HBNBCommand.validate_args(args)
        if go_on:
            return
        args_list = args.split(" ")
        class_name = args_list[0]
        id = args_list[1]
        for key, kwargs in storage.all().items():
            c_name, c_id = key.split(".")
            if c_id == id and class_name == c_name:
                class_representation = kwargs
                break
        print(class_representation)

    def do_all(self, args):
        """Prints all string representation of all instances"""
        args_exist = True
        args_list = args.split(" ")
        if args_list[0] != "" and len(args_list) >= 1:
            if args_list[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
                args_exist = False
                return
        obj_list = []
        if args_exist and args_list[0] != "":
            class_name = args_list[0]
            for key, kwargs in storage.all().items():
                c_name, c_id = key.split(".")
                if class_name == c_name:
                    obj_list.append(str(kwargs))
        else:
            for key, kwargs in storage.all().items():
                obj_list.append(str(kwargs))
        print(obj_list)

    def do_destroy(self, args):
        """Delete an instance base on the class name and id
        """
        go_on = HBNBCommand.validate_args(args)
        if go_on:
            return
        args_list = args.split(" ")
        class_name = args_list[0]
        id = args_list[1]
        key = f"{class_name}.{id}"
        del storage.all()[key]
        storage.save()

    def do_create(self, args):
        """Create new instance of and prints the id"""

        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        dict_classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }
        if not args:
            print("** class name missing **")
            return
        class_name = args.split(" ")[0]
        if class_name not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        obj = dict_classes[class_name]()
        obj.save()
        print(obj.id)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""

        self.cmdName = "update"

        go_on = HBNBCommand.validate_args(args, self.cmdName)
        if go_on:
            return

    def do_EOF(self, args):
        """EOF method
        """
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Empty the last command
        """
        pass

    def precmd(self, args):
        """Prepare the command
        """
        if not sys.stdin.isatty():
            print()
        return cmd.Cmd.precmd(self, args)

    def onecmd(self, line):
        """Onecmd function to treat custom comman writing"""
        args_list = line.split(".", maxsplit=1)

        if len(args_list) > 1:
            class_name, cmd_args = args_list
            if len(args_list) > 1:
                cmd_args_list = cmd_args.split('(')
                if len(cmd_args_list) > 1:
                    command, id_c_bracket = cmd_args_list
                    c_id = id_c_bracket.strip(')')
                    if command in ["all", "count"]:
                        line = f"{command} {class_name}"
                    elif command in ["show", "destroy"]:
                        c_id = c_id.strip("\"")
                        line = f"{command} {class_name} {c_id}"
                    if command in ["update"] and len(c_id) > 1:
                        s_list = c_id.split(", ", maxsplit=1)
                        id_arguments, arguments = s_list

                        id_arguments = id_arguments.strip("\"")
                        arguments = arguments.strip("\"'")
                        if (arguments.startswith("{")):
                            arguments = arguments.strip("{}")
                            arguments_list = arguments.split(", ")
                            for i, arg_line in enumerate(arguments_list):
                                key_arg, value_arg = arg_line.split(": ")
                                line = "{} {} {} {} {}".format(command,
                                                               class_name,
                                                               id_arguments,
                                                               key_arg,
                                                               value_arg)
                                if i == len(arguments_list) - 1:
                                    return cmd.Cmd.onecmd(self, line)
                                else:
                                    cmd.Cmd.onecmd(self, line)
                        else:
                            key_arg, value_arg = arguments.split(", ")
                            line = "{} {} {} {} {}".format(command,
                                                           class_name,
                                                           id_arguments,
                                                           key_arg,
                                                           value_arg)
        return cmd.Cmd.onecmd(self, line)

    def do_count(self, line):
        """Do counting of instances"""
        count = 0
        args_list = line.split()
        class_name = args_list[0]
        if class_name not in HBNBCommand.class_names:
            print(count)
            return
        for key, kwargs in storage.all().items():
            c_name, _ = key.split(".")
            if class_name == c_name:
                count += 1
        print(count)

    @staticmethod
    def validate_args(args, cmdName=None):
        """Validate arguments
        """
        class_exist = False

        if not args:
            print("** class name missing **")
            return 1
        args_list = args.split(" ")

        if args_list[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return 1

        if len(args_list) < 2:
            print("** instance id missing **")
            return 1

        class_name = args_list[0]
        id = args_list[1]
        for key, _ in storage.all().items():
            c_name, c_id = key.split(".")
            if c_id == id and class_name == c_name:
                class_exist = True
                break
        if not class_exist:
            print("** no instance found **")
            return 1
        if cmdName == "update":
            return (HBNBCommand.validate_update(args_list, class_name))
        return 0

    @staticmethod
    def validate_update(args_list, class_name):
        """Helper function for validate args in the case of update cmd"""
        if len(args_list) >= 3:
            if len(args_list) >= 4:
                if type(args_list[3]) not in [str, int, float]:
                    return
                else:
                    attr_name = args_list[2].strip("\"'")
                    attr_value = args_list[3].strip("\"'")

                    search_key = f"{args_list[0]}.{args_list[1]}"

                    for key, value in storage.all().items():
                        if key == search_key:
                            try:
                                attr = getattr(storage.all()[key], attr_name)
                                if HBNBCommand.is_integer(attr):
                                    setattr(storage.all()[key], attr_name,
                                            int(attr_value))
                                elif HBNBCommand.is_float(attr):
                                    setattr(storage.all()[key], attr_name,
                                            float(attr_value))
                                else:
                                    setattr(storage.all()[key], attr_name,
                                            str(attr_value))
                            except AttributeError:
                                setattr(storage.all()[key], attr_name,
                                        str(attr_value))
                            # print(f"attr:\t{attr}")
                        else:
                            setattr(storage.all()[key], attr_name,
                                    str(attr_value))
                    storage.save()
                    pass
            else:
                print("** value missing **")
                return 1
        else:
            print("** attribute name missing **")
            return 1
        return 0

    @staticmethod
    def is_integer(string):
        """Method to check if string is an integer"""
        s = str(string)
        return s.isdigit()

    @staticmethod
    def is_float(s):
        """Method to check if a string is a floating number"""
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
