
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)

a = 20
a = a + Color.RED.value
print(a)

b = Color.GREEN
print(b.name)
print(type(b.name))
print(b.value)

c = Color()   #error
c.name = "RED"  #error
