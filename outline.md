Intro Python as an interpreted language (2 minute)
- Highlevel overview of how Python interpreter works 

Creating Python Bytecode (3 minutes)
- Tokenize the code
- Parse into an AST
- Compile
- Pass bytecode off
- Interpret it!
- Push to the stack

Demo: Create bytecode! (4 minutes)
- Small example: https://github.com/lorenanicole/python-internals-talk/blob/main/script.py
- Use Python's DEBUG build to set the __ltrace__ to see the bytecode created in real time
- Run the script to:
	- Read the tokens
	- Examine the bytecode

Why should you care about Python internals? (1 minute)
- Pitch for starting as a core CPython developer
- More broadly understanding interpreted languages and language design
- It's fun!
