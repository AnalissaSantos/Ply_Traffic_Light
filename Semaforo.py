import ply.lex as lex
import ply.yacc as yacc
import sys

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
    cambio  :  expression
            | empty
    '''
    print (i[1])

def p_empty(i):
    '''
    empty :
    '''
    i[0]= None

def p_expression(i):
    '''
    expression : COLOR CAMBIO COLOR
    '''
    i[0]= i[1]

def p_error(i):
    pass

parser = yacc.yacc()   

while True:
    try:
        Input= input('')
    except EOFError:
            break


#lexer.input("ROJO A VERDE")
#while True:
#   tok = lexer.token()
#    if not tok:
#        break
#    print(tok)
