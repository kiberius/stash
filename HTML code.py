def Main(): ## Main function

    head_text = str(input('Head text:\n')) ## Inputs
    head_size = int(input('Head size:\n'))
    body_text = str(input('\nBody text:\n'))
    body_size = int(input('Body size:\n'))

    code = '<html>\n' ## Start of code string
    code += '<head>\n'
    code += ('<h{}>{}</h{}>\n'.format(head_size,head_text,head_size))
    code += '</head>\n'
    code += '<body>\n'
    code += ('<h{}>{}</h{}>\n'.format(body_size,body_text,body_size))
    code += '</body>\n'
    code += '</html>'

    print('\nFinal HTML code:\n')
    print(code,'\n') ## Final code

Main()
