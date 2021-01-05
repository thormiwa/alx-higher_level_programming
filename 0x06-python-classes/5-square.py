#!/usr/bin/python3


class Square:
    __size = None

    def __init__(self, size=0):
        if size != int(size):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return(self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size != 0:
            for a in range(self.area()):
                print("#", end="\n" if (a+1) % self.__size == 0 else "")
        else:
            print("")
