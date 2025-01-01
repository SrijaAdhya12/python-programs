#hybrid

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass


class Derived3(Derived1, Derived2): #hybrid inheritance
    pass

#example of hierchical inheritance

class Base:
    pass

class D1(Base):
    pass

class D2(Base):
    pass

class D3(D1):
    pass
