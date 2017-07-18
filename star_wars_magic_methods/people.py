class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side

    @property
    def light_side(self):
        return self.dark_side is not True
    
    def __str__(self):
        return '{name}'.format(name = self.name)

    def __call__(self):
        return 'Help me {self}, you\'re my only hope.'.format(self = str(self))

    def __truediv__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        return '{self} swings a lightsaber at {target}.'.format(self = str(self), target = str(target))

    def __mul__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        return '{self} throws a thermal detonator at {target}!'.format(self = str(self), target = str(target))

    def __rshift__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        return '{self} uses the force to push {target} away from them.'.format(self = str(self), target = str(target))

    def __lshift__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        return '{self} uses the force to pull {target} towards them.'.format(self = str(self), target = str(target))

    def __neg__(self):
        self.dark_side = True

    def __pos__(self):
        self.dark_side = False

    def __invert__(self):
        self.dark_side = not self.dark_side

    def __xor__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        return '{self} force chokes {target}.'.format(self = str(self), target = str(target))

    def __eq__(self, target):
        if isinstance(target, People) is not True:
            raise TypeError()
        if target.name != 'Han Solo':
            return '{self} shoots {target}.'.format(self = str(self), target =str(target))
        else:
            return 'Han Solo shoots {self}. BECAUSE HAN SHOOTS FIRST.'.format(self = str(self)) 
        
