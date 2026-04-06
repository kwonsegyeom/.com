"""Interactive command-line interface for the calculator."""

import sys
from .calculator import Calculator

HELP_TEXT = """
╔══════════════════════════════════════════════════════════╗
║                    Calculator CLI                        ║
╠══════════════════════════════════════════════════════════╣
║  Basic operations:                                       ║
║    <number> + <number>      Addition                     ║
║    <number> - <number>      Subtraction                  ║
║    <number> * <number>      Multiplication               ║
║    <number> / <number>      Division                     ║
║    <number> % <number>      Modulo                       ║
║    <number> ^ <number>      Power                        ║
║                                                          ║
║  Functions:                                              ║
║    sqrt <number>            Square root                   ║
║    log <number> [base]      Logarithm (default base 10)  ║
║    ln <number>              Natural logarithm             ║
║    sin <number>             Sine (radians)                ║
║    cos <number>             Cosine (radians)              ║
║    tan <number>             Tangent (radians)             ║
║    abs <number>             Absolute value                ║
║    neg <number>             Negate                        ║
║    fact <integer>           Factorial                     ║
║                                                          ║
║  Commands:                                               ║
║    history                  Show calculation history      ║
║    clear                    Clear history                 ║
║    help                     Show this help message        ║
║    quit / exit              Exit the calculator           ║
╚══════════════════════════════════════════════════════════╝
""".strip()

BINARY_OPS = {"+", "-", "*", "/", "%", "^"}

UNARY_FUNCS = {
    "sqrt": "square_root",
    "ln": "ln",
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "abs": "absolute",
    "neg": "negate",
}


def _parse_number(token: str) -> float:
    try:
        return float(token)
    except ValueError:
        raise ValueError(f"'{token}' is not a valid number")


def _execute(calc: Calculator, line: str) -> str | None:
    """Parse and execute a single input line. Returns a display string or None."""
    tokens = line.strip().split()
    if not tokens:
        return None

    cmd = tokens[0].lower()

    if cmd in ("quit", "exit"):
        print("Goodbye!")
        sys.exit(0)

    if cmd == "help":
        return HELP_TEXT

    if cmd == "history":
        hist = calc.history
        if not hist:
            return "(no history yet)"
        return "\n".join(f"  {i + 1}. {entry}" for i, entry in enumerate(hist))

    if cmd == "clear":
        calc.clear_history()
        return "History cleared."

    # Unary functions: func <number> [extra]
    if cmd in UNARY_FUNCS:
        if len(tokens) < 2:
            return f"Usage: {cmd} <number>"
        a = _parse_number(tokens[1])
        method = getattr(calc, UNARY_FUNCS[cmd])
        return str(method(a))

    if cmd == "log":
        if len(tokens) < 2:
            return "Usage: log <number> [base]"
        a = _parse_number(tokens[1])
        base = float(tokens[2]) if len(tokens) >= 3 else 10
        return str(calc.log(a, base))

    if cmd == "fact":
        if len(tokens) < 2:
            return "Usage: fact <integer>"
        n = int(_parse_number(tokens[1]))
        return str(calc.factorial(n))

    # Binary operations: <number> <op> <number>
    if len(tokens) == 3 and tokens[1] in BINARY_OPS:
        a = _parse_number(tokens[0])
        op = tokens[1]
        b = _parse_number(tokens[2])
        ops = {
            "+": calc.add,
            "-": calc.subtract,
            "*": calc.multiply,
            "/": calc.divide,
            "%": calc.modulo,
            "^": calc.power,
        }
        return str(ops[op](a, b))

    return f"Unknown command. Type 'help' for usage."


def main() -> None:
    """Entry point for the interactive calculator CLI."""
    calc = Calculator()
    print("Calculator CLI — type 'help' for usage, 'quit' to exit.\n")

    while True:
        try:
            line = input("calc> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        try:
            result = _execute(calc, line)
            if result is not None:
                print(result)
        except (ValueError, ZeroDivisionError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
