# .com
Kwonsegyeom

## Calculator

This repository now includes a simple Python calculator with:

- Basic operations: add, subtract, multiply, divide
- Safe expression evaluation using a restricted Python AST
- CLI mode (single expression or interactive prompt)

### Run from command line

Evaluate a single expression:

```bash
python3 calculator.py "2 + 3 * 4"
```

Run interactive mode:

```bash
python3 calculator.py
```

Exit interactive mode with `quit` or `exit`.

### Run tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```
