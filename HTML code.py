def Repeat():
    again = str(input('\nWould you like to go again? (y/n)\n'))
    if again == 'y':
        Main()
    elif again == 'n':
        print('BYE!')
        return
    else:
        print('You must enter Y or N!')
        Repeat()

def Main():
    try:
        head_text = str(input('Head text:\n'))
        head_size = int(input('Head size:\n'))
        body_text = str(input('\nBody text:\n'))
        body_size = int(input('Body size:\n'))
    except ValueError:
        print('\nYou must enter an integer.\n')
        Repeat()
    except:
        Repeat()

    code = '<html>\n'
    code += '<head>\n'
    code += ('<h{}>{}</h{}>\n'.format(head_size,head_text,head_size))
    code += '</head>\n'
    code += '<body>\n'
    code += ('<h{}>{}</h{}>\n'.format(body_size,body_text,body_size))
    code += '</body>\n'
    code += '</html>'

    print('\nFinal HTML code:\n')
    print(code,'\n')

Main()
