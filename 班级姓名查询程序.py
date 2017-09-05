#!/usr/bin/python
# vim: set fileencoding=utf-8 :

Students = ['Bill','Chris','Floyd','Kelly']

def check (Student):
    if Student in Students:
        print 'Yes,that student is enrolled in the class!'
    elif Student == 'q':
        print ''
    else:
        print 'No,that student is not in the class.'

while True:
    print '-' * 60
    Student = raw_input('Please give me the name of a student (enter \'q\' to quit): ')
    check(Student)
    if Student == 'q':
        break

print 'Bye'
