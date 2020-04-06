# HTML code
def main():
    
    head_text = str(input('Head text:\n'))
    body_text = str(input('Body test:\n'))
    
    code = '<html>\n'
    code += '<head>\n'
    code += ('<h2>{}</h2>\n'.format(head_text))
    code += '</head>\n'
    code += '<body>\n'
    code += ('<h4>{}</h4>\n'.format(body_text))
    code += '</body>\n'
    code += '</html>'

    print('\nFinal HTML code:\n')
    print(code,'\n')

main()
