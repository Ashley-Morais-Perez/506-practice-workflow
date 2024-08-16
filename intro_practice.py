import pandas as pd

import numpy as np


grade1 = 85
grade2 = 92
grade3 = 100
grade4 = 89


name_First = "Ashley"
name_Last = "Perez"


test_grades = [85,92,100,89]
HW_grades = [95,92,87,100]




def grades(test_grades, HW_grades):
    if test_grades >= 90:
        print ('You pass')
    else:
        print ('You fail')
    if HW_grades >= 95:
        print ('You pass')
    else:
        print ('You fail')


grades(85,95)
grades(92,92)
grades(100,87)
grades(89,100)




student1 = {
    'name_First': 'Ashley',
    'name_Last': 'Perez',
    'school': 'SBU',
    'test_grades': [85,92,100,89],
    'Degree': {
        'Major': 'Business',
        'Minor': 'Music'
    }
}
student1['name_First']
student1['test_grades']
student1['Degree']['Major']


type(student1)


student1['Degree'].keys() 