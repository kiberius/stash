def Input():
    global limit
    try:
        limit = int(input('Define the limit: '))
        Main()
    except:
        print('Please enter an integer.')
        Input()

def Main():

    x = 0
    y = 1

    for i in range(limit):
        print(x)
        z = x + y
        x = y
        y = z
    
    else:
        print('rdy')

Input()
