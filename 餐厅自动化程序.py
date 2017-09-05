#__author__ = 'Chris19'

#!/usr/bin/env python
# -*- coding:utf-8 -*-

Topping = ['pepperoni','sausage','cheese']

print '\nYou can check the topping in this Table, q to quit'
print '-' * 40
print '\n'

while True:

    Topping2 = []
    item1 = raw_input('Please give me a topping: ')
    item2 = raw_input('Please give me one more topping: ')

    if item1 in Topping:
        Topping2.append(item1)

    if item2 in Topping:
        Topping2.append(item2)

    if Topping2 == []:
        print '\nSorry,we don\'t have these toppings\n'
    else:
        print 'Here are your toppings: {},{}\n'.format(Topping2[0],Topping2[1])

print 'Goodbye!'
