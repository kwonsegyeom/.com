# Calculator

A calculator project with two implementations:

## Web Calculator (`web/`)

A modern, responsive calculator built with vanilla HTML, CSS, and JavaScript.

**Features:**
- Basic arithmetic: addition, subtraction, multiplication, division
- Sign toggle and percentage operations
- Expression history shown above the result
- Keyboard support (digits, operators, Enter, Escape, Backspace)
- Responsive design with a sleek dark gradient UI

**Usage:** Open `web/index.html` in any browser.

## Python Calculator (`python/`)

A full-featured calculator module with memory, history tracking, and scientific operations.

**Features:**
- Basic operations: add, subtract, multiply, divide
- Scientific operations: power, square root, modulo, factorial, absolute value, negate
- Memory: store, recall, add, clear
- History tracking with clear and retrieval
- Safe string expression evaluator

**Usage:**

```python
from calculator import Calculator

calc = Calculator()
calc.add(2, 3)       # 5
calc.multiply(4, 5)  # 20
calc.sqrt(16)        # 4.0
calc.get_history()   # ['2 + 3 = 5', '4 * 5 = 20', 'sqrt(16) = 4.0']
```

**Run tests:**

```bash
cd python
python3 -m pytest test_calculator.py -v
```
