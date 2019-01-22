class StrictClass():
    __slots__ = ['x', 'y']

    def __init__(self, x, y=None):
        self.x = x
        self.y = y


class MoreStrictClass(StrictClass):
    __slots__ = ['a', 'b']

    def __init__(self, a, b, x, y=None):
        super(MoreStrictClass, self).__init__(x=x, y=y)
        self.a = a
        self.b = b


msc = MoreStrictClass(x=1, a=2, b=3)

print(msc.x)
print(msc.a)
print(msc.b)
print(msc.y)


print(msc.__slots__)