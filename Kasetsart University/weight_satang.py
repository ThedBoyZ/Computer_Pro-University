gender=input('Enter gender : ')
age=int(input('Enter age : '))
weight=float(input('Enter weight : '))
height=float(input('Enter height : '))
if age==0:
    if gender=='male':
        if 2.8<=weight<=3.9 and 47.6<=height<=53.1:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 2.7<=weight<=3.7 and 46.8<=height<=52.9:
            print('Normal')
        else:
            print('Abnormal')
if age==1:
    if gender=='male':
        if 3.4<=weight<=4.7 and 50.4<=height<=56.2:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 3.3<=weight<=4.4 and 49.4<=height<=56.0:
            print('Normal')
        else:
            print('Abnormal')
if age==2:
    if gender=='male':
        if 4.2<=weight<=5.5 and 53.2<=height<=59.1:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 3.8<=weight<=5.2 and 52.0<=height<=59.0:
            print('Normal')
        else:
            print('Abnormal')
if age==3:
    if gender=='male':
        if 4.8<=weight<=6.4 and 55.7<=height<=61.9:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 4.4<=weight<=6.0 and 54.4<=height<=61.8:
            print('Normal')
        else:
            print('Abnormal')
if age==4:
    if gender=='male':
        if 5.3<=weight<=7.1 and 58.1<=height<=64.6:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 4.9<=weight<=6.7 and 56.8<=height<=64.5:
            print('Normal')
        else:
            print('Abnormal')
if age==5:
    if gender=='male':
        if 5.8<=weight<=7.8 and 60.4<=height<=67.1:
            print('Normal')
        else:
            print('Abnormal')
    if gender=='female':
        if 5.3<=weight<=7.3 and 58.9<=height<=66.9:
            print('Normal')
        else:
            print('Abnormal')