#!\usr\bin\python3

class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year
    def say_hi(self):
        if self.name:
            print("Hi, I am {}".format(self.name))
        else:
            print("I am a Robot without a name")
        if self.build_year:
            print("Hi, I made in {}".format(self.build_year))
        else:
            print("I do not know when i was made")
    def set_name(self, name=None):
        self.name = name
    def get_name(self):
        return self.name
    def set_build_year(self, build_year=None):
        self.build_year = by
    def get_build_year(self):
        return build_year


x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()
