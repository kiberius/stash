import math

def CircleCircumference():
	try:
		r = float(input('Enter radius: '))
		print('Circumference of circle: ',2*r*math.pi)
		repeat()
	except:
		print('You must enter a number.')
		return
		
def CircleArea():
	try:
		r = float(input('Enter radius: '))
		print('Area of circle: ',math.pi * r**2)
		repeat()
	except:
		print('You must enter a number.')
		return

def Ptheorem():
	try:
		a = float(input('Side A: '))
		b = float(input('Side B: '))
		c = a**2 + b**2   
		print('Side C:',math.sqrt(c))
		repeat()
	except:
		print('You must enter a number.')
		return

def repeat(): ## Repeat Function
    answer = input('Would you like to go again? y/n ')
    if answer == 'y':
        main()
    elif answer == 'n':
        print('BYE!')
        return
    else:
        print('Please enter Y or N!')
        repeat()
        
def main(): ## Main Function
	operation = input('Choose operation(Circumference or Area or Ptheorem)? ')
	if operation == 'c':
		CircleCircumference()
	elif operation == 'a':
		CircleArea()
	elif operation == 'p':
		Ptheorem()
	else:
	    print('ERROR')
	
def Authentication(): ## Authentication
    user = input('Enter user: ')
    pwd = input('Enter password: ')
    if (user == 'dex' and pwd == '1234' or user == 'kiberius' and pwd == '2468'):
        main()
    else:
        print('Wrong username/password!')
        again = input('Try again(y)? ')
        if again == 'y':
            Authentication()
        else:
        	print('BYE!')
        	return

Authentication()
