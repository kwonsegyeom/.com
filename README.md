# Calculator

A Python calculator library with an interactive CLI. Supports basic arithmetic, exponentiation, roots, logarithms, trigonometry, and factorial — with full calculation history.

## Quick Start

```bash
# Run the interactive CLI
python3 -m calculator
```

## Features

| Category      | Operations                                 |
|---------------|--------------------------------------------|
| Arithmetic    | add, subtract, multiply, divide, modulo    |
| Power & Roots | power, square root                         |
| Logarithmic   | log (any base), natural log                |
| Trigonometry   | sin, cos, tan (radians)                    |
| Other         | factorial, absolute value, negate          |
| Utility       | calculation history with clear             |

## CLI Usage

```
calc> 10 + 5
15.0
calc> 3 * 4
12.0
calc> sqrt 144
12.0
calc> log 1000
2.9999999999999996
calc> fact 6
720
calc> history
  1. 10 + 5 = 15.0
  2. 3 * 4 = 12.0
  3. sqrt(144) = 12.0
  4. log_10(1000) = 2.9999999999999996
  5. 6! = 720
calc> quit
```

Type `help` inside the CLI for a full command reference.

## Library Usage

```python
from calculator import Calculator

calc = Calculator()

calc.add(2, 3)          # 5.0
calc.divide(10, 4)      # 2.5
calc.power(2, 8)        # 256.0
calc.square_root(49)    # 7.0
calc.factorial(5)       # 120

print(calc.history)     # list of "expression = result" strings
calc.clear_history()
```

## Running Tests

```bash
pip install pytest
python3 -m pytest tests/ -v
```
