"""
Code borrowed from Stephane Writel EuroPython 2016 talk - Exploring our Python Interpreter 
Video: https://www.youtube.com/watch?v=R0lDKw0FQSI
"""

import tokenize
import dis
import ast

if __name__ == '__main__':

    # Source: https://docs.python.org/3/library/tokenize.html
    print('Here are the tokens Python identifies when we type `print("Hello PyLadies")`:')
    with tokenize.open('hello.py') as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            print(token)

    print('To convert the tokens to bytecode we must first compile it.')
    tree = ast.parse('print("Hello PyLadies")')
    compiled_code = compile(tree, 'test.py', mode='exec')

    # Learn more from PEP-0399
    print('Now here is the byte!')
    byte_code = dis.dis(compiled_code)

    # execution = interpreter(byte_code)
