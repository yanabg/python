# result is 0.300000, instead of 0.3 (judge will accept it)
# a = 0.1
# b = 0.1
# c = 0.1
#
# print(a + b + c)

# to baipass it:

from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.1')
c = Decimal('0.1')

print(a + b + c)