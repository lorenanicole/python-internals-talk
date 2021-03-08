# Python Internals: PyLadies IWD Lightning Talk

This code is for the `What happens when you type print(‘Hello PyLadies’)? A look at Python internals!` for [PyLadies International Women's Day 2021](https://iwd.pyladies.com).

## Install Python from source

We'll be installing [Python in debug mode](https://pythonextensionpatterns.readthedocs.io/en/latest/debugging/debug_python.html) which will allow us to see Python's bytecode that is generated when we use the Python interpreter:

```
wget http://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
tar xzvf Python-3.9.2.tgz
cd Python-3.9.2
../configure --with-pydebug
make EXTRA_CFLAGS="-DPy_REF_DEBUG"   # Build Python in debug mode to get the bytecode output
make install
```

From the terminal try `python` to see the version is set correctly:

```
$ python 
Python 3.9.2 (default, Mar  8 2021, 14:54:05)
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

## How can I see the bytecode?

Now we'll see the `__ltrace__ = None` to see the Python bytecode in the terminal:

```
>>> __ltrace__ = None
>>> print('Hello PyLadies')
0: 101, 0
push <built-in function print>
2: 100, 0
push 'Hello PyLadies'
4: 131, 1
Hello PyLadies
ext_pop 'Hello PyLadies'
ext_pop <built-in function print>
push None
6: 70
pop None
8: 100, 1
push None
10: 83
pop None
```

What is all this output? The bytecode! Let's start by looking at the Python lexer.
