#__author__ = 'Chris19'

#!/usr/bin/env python
# -*- coding:utf-8 -*-

def name_grades():
    grades = raw_input('Please give me their grade(q to quit):[INPUT]')
    names = raw_input('Please give me the name of the student(q to quit):[INPUT]')
    for name in names:
        for grade in grades:
            name_grades['Name'] = 'Grade'

for name_grade in name_grades:
    print name_grade    