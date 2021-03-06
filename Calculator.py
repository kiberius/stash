import math

def CircleCircumference():
	try:
		print('----\nCircle Circumference:')
		r = float(input('Enter radius: '))
		print('\nThe circumference of the circle is {} in lenght.\n'.format(2 * r * math.pi))
		Repeat()
	except:
		print('\nYou must enter a number.\n')
		Repeat()
		
def CircleArea():
	try:
		print('----\nCircle Area:')
		r = float(input('Enter radius: '))
		print('\n- The area of the circle is {} in square units.\n'.format(math.pi * r**2))
		Repeat()
	except:
		print('\nYou must enter a number.\n')
		Repeat()

def Ptheorem():
	try:
		print('----\nPythagorean Theorem:')
		a = float(input('Side A: '))
		b = float(input('Side B: '))
		print('\n- Side C is {} in lenght.\n'.format(math.sqrt(a**2 + b**2)))
		Repeat()
	except:
		print('\nYou must enter a number.\n')
		Repeat()
		

def Repeat(): ## Repeat Function
	answer = input('Would you like to go again? (y/n)\n')
	if answer == 'y':
		Main()
	elif answer == 'n':
		print('\nBYE!\n')
		return
	else:
		print('\nPlease enter Y or N!\n')
		Repeat()

def Main(): ## Main Function
	operation = input('Choose operation (Circumference or Area or Ptheorem)?\n')
	if operation == 'c':
		CircleCircumference()
	elif operation == 'a':
		CircleArea()
	elif operation == 'p':
		Ptheorem()
	else:
		Repeat()

def Authentication(): ## Authentication
	credentials = {'user0':'password0','user1':'password1','user2':'password2','user3':'password3'}
	print('\nEnter credentials!\n')
	user = str(input('Enter user: '))
	pwd = str(input('Enter password: '))
	try:
		if (credentials[user] == pwd):
			print('\nAccess granted!\n')
			Main()
		else:
			print('\nWrong password!\n')
			AuthenticationRepeat()
	except KeyError:
		print('\nWrong username!\n')
		AuthenticationRepeat()

def AuthenticationRepeat():
	again = input('\nEnter credentials again? (y/n)?\n')
	if again == 'y':
		Authentication()
	elif again == 'n':
		print('\nBYE!\n')
		return
	else:
		AuthenticationRepeat()

Authentication()
