import ply.lex as lex
import ply.yacc as yacc
import sys
import time

#Tokenizing
tokens=[
    'COLOR',
    'CAMBIO',
    'Tiempo'
]

#LEXER
t_CAMBIO = r'A'
t_ignore = r' '
t_COLOR = r'ROJO|VERDE|AMARILLO'
    

def t_error(t):
    print("Illegal Characters")
    t.lexer.skip(1)

lexer = lex.lex()


#PARSING
def p_cambio(i):
    '''
    cambio  : expression
            | empty
    '''
    run(i[1])

def p_empty(i):
    '''
    empty :
    '''
    i[0]= None

def p_expression(i):
    '''
    expression : expression CAMBIO expression
    '''
    i[0]= (i[1],i[2],i[3])
def p_expression_color(i):
    '''
    expression : COLOR
    '''
    i[0]= i[1]

def p_error(i):
    print("Syntax Error")

parser = yacc.yacc()   

def run(i):
    # if type(i)==tuple:
    #     print ('Cambio de Luz de '+ str(run(i[0]))+ ' a'+ str(run(i[2])))
    if i[2] == 'ROJO':
        time.sleep(3)
        print('Luz actual es de color '+ str(i[2]))

    elif i[2] == 'ROJO':
        print('Luz actual es de color '+ str(i[2]))

    elif i[2] == 'VERDE':
        print('Luz actual es de color '+ str(i[2]))
    elif i[2] == 'AMARILLO':
        print('Luz actual es de color '+ str(i[2]))
while True:
    try:
        s= input('>')
    except EOFError:
            break
    parser.parse(s)


#lexer.input("ROJO A VERDE")
#while True:
#   tok = lexer.token()
#    if not tok:
#        break
#    print(tok)
