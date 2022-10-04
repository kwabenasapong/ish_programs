#!/usr/bin/python3
'''Calc Module'''


class Calc:
    '''for basic calculations'''

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        '''getter'''
        return self.__a

    @a.setter
    def a(self, value):
        '''setter'''
        self.__a = value


    @property
    def b(self):
        '''getter'''
        return self.__b

    @b.setter
    def b(self, value):
        '''setter'''
        self.__b = value

    def add(self):
        '''add args'''
        return self.__a + self.__b

    def mul(self):
        '''multiple args'''
        return self.__a * self.__b

    def sub(self):
        '''subtract args'''
        return self.__a - self.__b

    def div(self):
        '''divide args'''
        return self.__a / self.__b



