#simple script to calculate story points for each sprint for respective scrum teams .. # 1 story point == 6 hours of effective productive hours
import time
print()
try:
    Srivari = int(input ("Enter the Number of sprints eg: any number between 1 and 2 "))
    print()
    if Srivari == 1 or Srivari == 2 :
        print ('Go ahead with the sprint Planning for', Srivari, 'sprints')
    else:
        print ('Not an Ideal sprint Planning, limit the number of sprints to 1 or 2')
except :
    print ('Please enter only integers without decimals and alphapets') #exception handling here for crazy guys 
    Srivari=1 
print() 

try:
    spav = int(input ("Enter the Number of people in the team")) 
    print()
    if spav > 0 and spav < 25 :
        print ('sprint Planning in progress for', spav, 'members')
    else:
        print ('Not an Ideal team, limit the number of people to below 25')
except :
    print ('Please enter only integers without decimals and alphapets') #exception handling here for crazy guys 
    spav=1 
print() 

try:
    ganesha = int(input ("Enter the Number of public holidays eg: any number between 0 and 10"))
    print()
    if ganesha == 0 or ganesha < 11 :
        print ('No of holidays considered is', ganesha)
    else:
        print ('Not a Realistic Holiday scenario, limit the number of holidays to less than 10')
except :
    print ('Please enter only integers without decimals and alphapets') #exception handling here for crazy guys 
    ganesha=0
print() 

try:
    maramma = int(input ("Enter the Number of Leaves taken in total by the team members"))
    print()
    if maramma == 0 or maramma < 250 :
        print ('No of leaves considered is', ganesha)
    else:
        print ('Not a Realistic leaves scenario')
except :
    print ('Please enter only integers without decimals and alphapets') #exception handling here for crazy guys 
    maramma=0
print()

shanka = maramma * 6
srichamundeshwari = 1
print ('Calculating Story Points for complete team')
print()
if Srivari == 1 :
    actual_days = 10 - ganesha
elif Srivari == 2 :
    actual_days = 20 - ganesha 

srichamundeshwari = int((spav * 6 * actual_days *80)/100)

srivigneshwara = srichamundeshwari - shanka

chakra = int(srivigneshwara/6)

print ('Sprint Planning for complete team is', chakra, 'story points')

time.sleep(60)

#pip install auto-py-to-exe

#python -m auto_py_to_exe
    

