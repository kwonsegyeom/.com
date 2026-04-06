# Calculator

A Python calculator with a clean API and an interactive command-line interface.

## Features

| Category | Operations |
|---|---|
| Basic arithmetic | add, subtract, multiply, divide, modulo, power |
| Scientific | square root, logarithm (any base), factorial, absolute value |
| Trigonometry | sin, cos, tan (degrees) |
| History | full operation history, clear/reset |

## Project layout

```
calculator/
    __init__.py      – public package API
    calculator.py    – Calculator class
    cli.py           – interactive REPL
tests/
    test_calculator.py
main.py              – CLI entry point
requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the CLI

```bash
python3 main.py
```

Example session:

```
Calculator — type 'help' for a list of commands, 'exit' to quit.

calc> add 3 4
7
calc> pow 2 10
1024
calc> sqrt 144
12
calc> sin 90
1
calc> log 1000 10
3
calc> fact 6
720
calc> history
    1. 3 + 4 = 7.0
    2. 2 ** 10 = 1024.0
    3. sqrt(144) = 12.0
    4. sin(90°) = 1.0
    5. log_10(1000) = 3.0
    6. 6! = 720
calc> clear
Cleared.
calc> exit
Bye!
```

## Using the library

```python
from calculator import Calculator

calc = Calculator()

print(calc.add(10, 5))       # 15.0
print(calc.divide(10, 4))    # 2.5
print(calc.sqrt(49))         # 7.0
print(calc.sin(30))          # 0.5
print(calc.factorial(5))     # 120
print(calc.history)          # list of recorded expressions
```

## Running tests

```bash
python3 -m pytest tests/ -v
```

All 54 tests should pass.
