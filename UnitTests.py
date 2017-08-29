from mock import Mock
from Simplemath import Simplemath
m=Mock()
m.add()
m.add.side_effect=Simplemath
n=m.add.side_effect(5,10)
print n.add()