# .com
Kwonsegyeom

## Calculator

This repository includes a simple Python calculator module:

- Basic operations: add, subtract, multiply, divide, power
- Safe arithmetic expression evaluation using Python AST

### Quick start

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))               # 5
print(calc.evaluate("(2 + 3) * 4")) # 20.0
```

### Run tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
