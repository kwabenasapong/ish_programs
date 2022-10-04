#!/usr/bin/python3
if __name__ == '__main__':
    #Calc = __import__('calc').Calc
    from calc import Calc

    c = Calc(2, 3)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
