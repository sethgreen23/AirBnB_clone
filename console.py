#!/usr/bin/python3
"""Module for the console"""

import cmd
import sys
import importlib
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Is the main Class for creating the command and the action
    """
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                   "Review"]

    def do_create(self, args):
        """Create new instance of BaseModel, save it and print the id
        """
        # test for the right input
        if not args:
            print("** class name missing **")
            return
        if args not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        # create new instance
        obj = args()
        # save the new instance
        obj.save()

    def do_show(self, args):
        """Print the string representaion of an instance based on the class
name and i
        """
        # testing the argument
        # test is the name is missing
        # test if the id is missing
        # test if the class name doesnt exist
        # test if the instance of the class name doesnt exist
        # class_exist = False
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
        """Prints all string representation of all instances based on
        or not the class name
        """
        # test if class doesnt exist
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
        # test if the class name is missing
        # test if the class name doesnt exist
        # test if id is missing
        # test if the id
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
        """Create new instance of BaseModel,
            save it and print the id
        """
        # test for the right input
        if not args:
            print("** class name missing **")
            return
        class_name = args.split(" ")[0]
        if class_name not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        copy_class_name = class_name
        if copy_class_name == "BaseModel":
            copy_class_name = "Base_Model"
        module_name = f"models.{copy_class_name.lower()}"
        module = importlib.import_module(module_name)
        class_obj = getattr(module, class_name)

        # create new instance
        obj = class_obj()
        # save the new instance
        obj.save()
        print(obj.id)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
updating attribute"""
        # check if class name is missing
        # check if class name is a valid class name. eg. BaseModel
        # check if id is missing
        # check if an insntance of the class with the id provided exisits
        # check if attribute name is missing
        # check if the attribute value exists
        self.cmdName = "update"
        # print(args)
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
        # We need to check if the console is interacting with a terminal in the
        # preloop() method
        if not sys.stdin.isatty():
            print()
        return cmd.Cmd.precmd(self, args)

    def onecmd(self, line):
        args_list = line.split(".")

        if len(args_list) > 1:
            # class_name = args_list[0]
            # command = args_list[1].strip("()")
            # line = f"{command} {class_name}"
            class_name, cmd_args = args_list
            if len(args_list) > 1:
                cmd_args_list = cmd_args.split('(')
                if len(cmd_args_list) > 1:
                    command, id_c_bracket = cmd_args_list
                    c_id = id_c_bracket.strip(')')
                    if command in ["all", "count"]:
                        line = f"{command} {class_name}"
                    elif command in ["show", "destroy"]:
                        line = f"{command} {class_name} {c_id}"
                    if command in ["update"] and len(c_id) > 1:
                        s_list = c_id.split(", ", maxsplit=1)
                        id_arguments, arguments = s_list
                        # Task16 we need to strip the "cotes" from ids 
                        # The ids needs to be surrounded by "cotes"
                        # exemple User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
                        # this apply to show to
                        # User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
                        # i taged the places with "Update TASK16" 
                        id_arguments = id_arguments.strip("\"")
                        arguments = arguments.strip("\"'")
                        if (arguments.startswith("{")):
                            arguments = arguments.strip("{}")
                            arguments_list = arguments.split(", ")
                            # print(arguments_list)
                            for i, arg_line in enumerate(arguments_list):
                                print(arg_line)
                                key_arg, value_arg = arg_line.split(": ")
                                print(key_arg)
                                print(value_arg)
                                line = f"{command} {class_name} {id_arguments} {key_arg} {value_arg}"
                                if i == len(arguments_list) - 1:
                                    return cmd.Cmd.onecmd(self, line)
                                else:
                                    cmd.Cmd.onecmd(self, line)
                        else:
                            key_arg , value_arg = arguments.split(", ")
                            line = f"{command} {class_name} {id_arguments} {key_arg} {value_arg}"
                            
        return cmd.Cmd.onecmd(self, line)

    def do_count(self, line):
        """Do counting of instances"""
        # check if class name exists
        # if it does not exist, print '0' and return
        # initialize counter
        # loop through storage.all()
        # extract the class_name
        # compare the class_name with the argument from onecmd
        #       if class_name found:
        #       increment counter
        # print(count)
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

    # def preloop(self):
    #     """checks if console is interacting with a terminal or not
    #     """
    #     if not sys.stdin.isatty():
    #         print()

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
                # add attribute or update its value if it exists
                if type(args_list[3]) not in [str, int, float]:
                    return
                else:
                    attr_name = args_list[2].strip("\"'")
                    attr_value = args_list[3].strip("\"'")
                    # use ID to search for instance
                    # for key, value in storage.all().items():
                    search_key = f"{args_list[0]}.{args_list[1]}"

                    for key, value in storage.all().items():
                        if key == search_key:
                            try:
                                attr = getattr(storage.all()[key], attr_name)
                                if HBNBCommand.is_integer(attr):
                                    # print("____________Is INTEGER___________")
                                    setattr(storage.all()[key], attr_name, int(attr_value))
                                elif HBNBCommand.is_float(attr):
                                    # print("____________Is FLOAT___________")
                                    setattr(storage.all()[key], attr_name, float(attr_value))
                                else:
                                    # print("____________Is STR___________")
                                    setattr(storage.all()[key], attr_name, str(attr_value))
                            except AttributeError:
                                pass
                            # print(f"attr:\t{attr}")
                        else:
                            setattr(storage.all()[key], attr_name,
                                        str(attr_value))
                            # if hasattr(storage.all()[key], attr_name):
                            #     attr_type = type(getattr(storage.all()[key],
                            #                              attr_name)).__name__
                                # print(f"attr:\t{attr}\t type(attr):\t{type(attr)}")
                                # print("isnumberic(attr): {}".format(attr.isnumeric()))
                                # print(f"**************\n\n{attr_type}\n\n***************")
                                # if HBNBCommand.is_integer(attr):
                                #     print("____________Is INTEGER___________")
                                #     setattr(storage.all()[key], attr_name, int(attr_value))
                                # elif HBNBCommand.is_float(attr):
                                #     print("____________Is FLOAT___________")
                                #     setattr(storage.all()[key], attr_name, float(attr_value))
                                # else:
                                #     print("____________Is STR___________")
                                #     setattr(storage.all()[key], attr_name, str(attr_value))
                                    
                                # if attr_type == "int":
                                #     setattr(storage.all()[key], attr_name, int(attr_value))
                                # elif attr_type == "str":
                                #     setattr(storage.all()[key], attr_name,
                                #             str(attr_value))
                                # elif attr_type == "float":
                                #     setattr(storage.all()[key], attr_name,
                                #             float(attr_value))
                                
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
        return s.isdigit() # or (s[0] == '-' and s[1:].isdigit())

    @staticmethod
    def is_float(s):
        """Method to check if a string is a floating number"""
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
