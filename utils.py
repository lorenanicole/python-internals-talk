import tokenize

# Source: https://docs.python.org/3/library/tokenize.html
with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
