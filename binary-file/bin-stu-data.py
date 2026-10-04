'''
prog 13
AIM : To create a Binary file STUDENT.DAT/.BIN/.TXT with each record having details of
rollnumber ,name,total and perform the operations using a menu driven code.
METHODOLOGY: The binary file is created to store details of ‘N’ students, with input read in the
form of a list. The menu is displayed and the related operations are performed on the binary file
depending on user’s choice. '''

import pickle
def bin(N):
    f=open('student.dat','wb')
    for i in range(N):
        r=int(input('Enter rno:'))
        n=input('enter name of the student:')
        t=int(input('enter total marks:'))
        pickle.dump([r,n,t],f)
    print('Successful')
    f.close()
n=int(input('no of students:'))
bin(n)

def tot():
    with open('student.dat','rb') as f:
        try:
            l=[]
            while True:
                x=pickle.load(f)
                l.append(x)
        except EOFError:
            pass
    t=0
    for i in range(len(l)):
                if l[i][2]>t:
                    t=l[i][2]
                    topper=l[i]
    print('Topper details:',topper)
def incre():
    with open('student.dat','rb') as f:
        try:
            l=[]
            while True:
                x=pickle.load(f)
                l.append(x)
        except EOFError:
            pass
    t=int(input('enter the Rno to increment 3 Marks:'))
    for i in range(len(l)):
                if l[i][0]==t:
                    l[i][2]+=3
                    print('Updated student details:',l[i])
    with open('student.dat','wb') as f:
        for i in range(len(l)):
            pickle.dump(l[i], f)
print('MENU')
print('1. Display topper detail')
print('2. Increment the student’s total by 3 marks for a given rollnumber.')
print('3. Exit')
a=0
while a<3:
    a=int(input('Enter your choice:'))
    if a==1:
        tot()
    if a==2:
        incre()
    if a==3:
        print('EXIT')