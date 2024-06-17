#!/usr/bin/python3
""" The base class of all classes """


import json
import csv


class Base:
    """ the class itself """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                elem = obj.to_dictionary()
                my_list.append(elem)
        with open(filename, "w") as fd:
            json_list = Base.to_json_string(my_list)
            new_list = json.loads(json_list)
            return json.dump(new_list, fd)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string """
        my_list = []
        if json_string is None or len(json_string) == 0:
            return my_list
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ loads list from file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as fd:
                my_list = fd.read()
                inst_list = Base.from_json_string(my_list)
        except Exception:
            return []
        values = []
        for val in inst_list:
            dummy = cls.create(**val)
            values.append(dummy)
        return values

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attributes set """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy_inst = Rectangle(1, 1)
        else:
            dummy_inst = Square(1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves to csv """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as fd:
            write_obj = csv.writer(fd)
            if cls.__name__ == "Rectangle":
                list_objs = [[z.id, z.width, z.height, z.x, z.y]
                             for z in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[z.id, z.size, z.x, z.y]
                             for z in list_objs]
            write_obj.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        result = []
        with open(filename, "r", newline='') as fd:
            read_obj = csv.reader(fd)
            for row in read_obj:
                row = [int(r) for r in row]
                if cls.__name__ == "Rectangle":
                    dict_objs = {"id": row[0], "width": row[1],
                                 "height": row[2], "x": row[3], "y": row[4]}
                elif cls.__name__ == "Square":
                    dict_objs = {"id": row[0], "size": row[1],
                                 "x": row[2], "y": row[3]}
                result.append(cls.create(**dict_objs))
        return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws all rectangles and squares """
        import turtle
        import time
        import random.randrange
        turtle.Screen().colormode(255)
        for objs in list_rectangles + list_squares:
            curs = turtle.Turtle()
            curs.color((randrange(255), randrange(255), randrange(255)))
            curs.pensize(2)
            curs.penup()
            curse.pendown()
            curs.setpos((i.x + curs.pos()[0], i.y - curs.pos()[1]))
            curs.pensize(15)
            curs.forward(i.width)
            curs.left(90)
            curs.forward(i.height)
            curs.left(90)
            curs.forward(i.width)
            curs.left(90)
            curs.forward(i.height
            curs.left(90)
            curs.end_fill()

        time.sleep(4)
