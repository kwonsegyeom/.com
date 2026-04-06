# Calculator Example

This repository now includes a small Python calculator module and command-line
tool.

## Features

- Basic operations via the `Calculator` class
- Safe arithmetic expression evaluation with `evaluate()`
- Command-line usage for quick calculations
- Focused `unittest` coverage

## Run the calculator

```bash
python calculator.py "2 * (3 + 4)"
```

Expected output:

```text
14
```

## Run the tests

```bash
python -m unittest discover -s tests
```
