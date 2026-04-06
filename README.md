# Calculator Project

This repository now includes a simple Python calculator module.

## Features

- Basic operations:
  - add
  - subtract
  - multiply
  - divide
  - power
  - modulo
- Safe expression evaluator using Python AST
  - Supported operators: `+`, `-`, `*`, `/`, `%`, `**`
  - Supports parentheses and unary `+`/`-`

## Usage

```python
from calculator import Calculator

calc = Calculator()

print(calc.add(2, 3))           # 5
print(calc.divide(10, 2))       # 5.0
print(calc.evaluate("2 + 3*4")) # 14
```

## Running tests

```bash
python -m unittest -v
```
