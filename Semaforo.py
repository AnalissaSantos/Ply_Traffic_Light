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
    
# def t_tiempo(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

def t_error(t):
    print("Illegal Characters")
    t.lexer.skip(1)

lexer = lex.lex()   #creación del lexer



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

parser = yacc.yacc() #construcción del parser

def run(i):
    t_end = time.time() + 5
    t_cambio = time.time() + 10
    if (i[0] == 'VERDE') & (i[2] == 'ROJO'):
        print('Luz actual es de color '+ str(i[0]))
        while time.time() < t_end:
            time.sleep(1)
            print('.')
        print('lUZ DE ADVERTENCIA: AMARILLO')
        while time.time() < t_cambio:
            time.sleep(1)
            print('.')
        print('NUEVA LUZ: '+ str(i[2]))

    else: 
        print('Luz actual es de color '+ str(i[0]))
        while time.time() < t_end:
            time.sleep(1)
            print('.')
        print('NUEVA LUZ: '+ str(i[2]))

while True:
    try:
        s= input('>>')
    except EOFError:
        break
    parser.parse(s)

