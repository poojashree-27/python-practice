##MENU
##1. Display details of Managers earning more than 50000 in Finance and in Admin Dept.
##2. Delete the employee details who have reached retirement age(58 years)
##3. Exit . 
import pickle
def emp(N):
    f=open('employee.dat','wb')
    for i in range(N):
        d={}
        n=input('enter name of the employee:')
        a=int(input('enter the age of the employee:'))
        de=input('enter department of the employee:')
        sa=int(input('enter salary of the employee:'))
        d['Name']=n
        d['Age']=a
        d['Department']=de
        d['Salary']=sa
        pickle.dump(d,f)
    print('Successful')
    f.close()
n=int(input('no of employees:'))
emp(n)
def earn():
    with open('employee.dat','rb') as f:
        try:
            while True:
                y=pickle.load(f)
                if (y['Department']=='Finance' or y['Department']=='Admin') and y['Salary']>50000:
                    print('Managers earning more than 50000',y)
        except EOFError:
            pass
def Del():
    with open('employee.dat','rb') as f:
        try:
            rec=[]
            while True:
                y=pickle.load(f)
                if y['Age']>=58:
                    del y
                else:
                    rec.append(y)
        except EOFError:
            pass
    with open('employee.dat','wb') as f:
        for i in rec:
            pickle.dump(i,f)
    print('success')
print('\tMENU')
print('1. Display details of Managers earning more than 50000 in Finance and in Admin Dept')
print('2. Delete the employee details who have reached retirement age(58 years)')
print('3. Exit ')
ch=0
while ch<3:
    ch=int(input('Enter your choice:'))
    if ch==1:
        earn()
    if ch==2:
        Del()
    if ch==3:
        print('EXIT')