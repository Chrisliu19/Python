#__author__ = 'Chris19'

#!/usr/bin/env python
# -*- coding:utf-8 -*-

Topping = ['pepperoni','sausage','cheese']

item1 = raw_input('Please give me a topping: ')
item2 = raw_input('Please give me one more topping: ')
Topping2 = []

print '\nYou can check the topping in this Table'
print '-' * 40

if item1 in Topping:
    Topping2.append(item1)

if item2 in Topping:
    Topping2.append(item2)

if Topping2 == []:
    print '\nSorry,we don\'t have these toppings'
else:
    print 'Here are your toppings: {},{}'.format(Topping2[0],Topping2[1])
