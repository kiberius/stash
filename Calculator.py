import math

def CircleCircumference():
	try:
		print('----\nCircle Circumference:')
		r = float(input('Enter radius: '))
		print('\nThe circumference of the circle is {} in lenght.\n'.format(2 * r * math.pi))
		repeat()
	except:
		print('\nYou must enter a number.\n')
		repeat()
		
def CircleArea():
	try:
		print('----\nCircle Area:')
		r = float(input('Enter radius: '))
		print('\n- The area of the circle is {} in square units.\n'.format(math.pi * r**2))
		repeat()
	except:
		print('\nYou must enter a number.\n')
		repeat()

def Ptheorem():
	try:
		print('----\nPythagorean Theorem:')
		a = float(input('Side A: '))
		b = float(input('Side B: ')) 
		print('\n- Side C is {} in lenght.\n'.format(math.sqrt(a**2 + b**2)))
		repeat()
	except:
		print('\nYou must enter a number.\n')
		repeat()
		

def repeat(): ## Repeat Function
	answer = input('Would you like to go again? (y/n)\n')
	if answer == 'y':
		main()
	elif answer == 'n':
		print('\nBye!\n')
		return
	else:
		print('\nPlease enter Y or N!\n')
		repeat()

def main(): ## Main Function
	operation = input('Choose operation(Circumference or Area or Ptheorem)?\n')
	if operation == 'c':
		CircleCircumference()
	elif operation == 'a':
		CircleArea()
	elif operation == 'p':
		Ptheorem()
	else:
		repeat()

def Authentication(): ## Authentication
	credentials = {'user0':'password0','user1':'password1','user2':'password2','user3':'password3'}
	print('\nEnter credentials:\n')
	user = str(input('Enter user: '))
	pwd = str(input('Enter password: '))
	try:
		if (credentials[user] == pwd):
			print('\nAccess granted!\n')
			main()
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
	if again == 'n':
		print('\nBye!\n')
		return
	else:
		AuthenticationRepeat()

Authentication()
