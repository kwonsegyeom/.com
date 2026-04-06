"""Interactive command-line interface for the Calculator."""

import sys

from .calculator import Calculator, CalculatorError

HELP_TEXT = """
Commands:
  add <a> <b>          Addition:          a + b
  sub <a> <b>          Subtraction:       a - b
  mul <a> <b>          Multiplication:    a * b
  div <a> <b>          Division:          a / b
  mod <a> <b>          Modulo:            a % b
  pow <base> <exp>     Power:             base ^ exp
  sqrt <a>             Square root:       √a
  log <a> [base]       Logarithm:         log_base(a)  (default base: e)
  sin <deg>            Sine of angle (degrees)
  cos <deg>            Cosine of angle (degrees)
  tan <deg>            Tangent of angle (degrees)
  abs <a>              Absolute value:    |a|
  fact <n>             Factorial:         n!
  history              Show calculation history
  clear                Reset result and clear history
  help                 Show this help message
  exit / quit          Exit the calculator
""".strip()


def _parse_number(token: str) -> float:
    try:
        return int(token) if "." not in token else float(token)
    except ValueError:
        raise CalculatorError(f"'{token}' is not a valid number.")


def _format_result(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return f"{value:.10g}"


def run_cli() -> None:
    """Start the interactive REPL."""
    calc = Calculator()
    print("Calculator — type 'help' for a list of commands, 'exit' to quit.\n")

    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            sys.exit(0)

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        try:
            if cmd in ("exit", "quit"):
                print("Bye!")
                sys.exit(0)

            elif cmd == "help":
                print(HELP_TEXT)

            elif cmd == "history":
                if not calc.history:
                    print("(no history yet)")
                else:
                    for i, entry in enumerate(calc.history, 1):
                        print(f"  {i:>3}. {entry}")

            elif cmd == "clear":
                calc.clear()
                print("Cleared.")

            elif cmd == "add":
                if len(args) != 2:
                    print("Usage: add <a> <b>")
                    continue
                a, b = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.add(a, b)))

            elif cmd == "sub":
                if len(args) != 2:
                    print("Usage: sub <a> <b>")
                    continue
                a, b = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.subtract(a, b)))

            elif cmd == "mul":
                if len(args) != 2:
                    print("Usage: mul <a> <b>")
                    continue
                a, b = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.multiply(a, b)))

            elif cmd == "div":
                if len(args) != 2:
                    print("Usage: div <a> <b>")
                    continue
                a, b = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.divide(a, b)))

            elif cmd == "mod":
                if len(args) != 2:
                    print("Usage: mod <a> <b>")
                    continue
                a, b = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.modulo(a, b)))

            elif cmd == "pow":
                if len(args) != 2:
                    print("Usage: pow <base> <exp>")
                    continue
                base, exp = _parse_number(args[0]), _parse_number(args[1])
                print(_format_result(calc.power(base, exp)))

            elif cmd == "sqrt":
                if len(args) != 1:
                    print("Usage: sqrt <a>")
                    continue
                a = _parse_number(args[0])
                print(_format_result(calc.sqrt(a)))

            elif cmd == "log":
                if len(args) == 1:
                    a = _parse_number(args[0])
                    print(_format_result(calc.log(a)))
                elif len(args) == 2:
                    a, base = _parse_number(args[0]), _parse_number(args[1])
                    print(_format_result(calc.log(a, base)))
                else:
                    print("Usage: log <a> [base]")

            elif cmd == "sin":
                if len(args) != 1:
                    print("Usage: sin <degrees>")
                    continue
                a = _parse_number(args[0])
                print(_format_result(calc.sin(a)))

            elif cmd == "cos":
                if len(args) != 1:
                    print("Usage: cos <degrees>")
                    continue
                a = _parse_number(args[0])
                print(_format_result(calc.cos(a)))

            elif cmd == "tan":
                if len(args) != 1:
                    print("Usage: tan <degrees>")
                    continue
                a = _parse_number(args[0])
                print(_format_result(calc.tan(a)))

            elif cmd == "abs":
                if len(args) != 1:
                    print("Usage: abs <a>")
                    continue
                a = _parse_number(args[0])
                print(_format_result(calc.absolute(a)))

            elif cmd == "fact":
                if len(args) != 1:
                    print("Usage: fact <n>")
                    continue
                n_raw = args[0]
                if "." in n_raw:
                    raise CalculatorError("Factorial requires a whole number.")
                n = int(n_raw)
                print(calc.factorial(n))

            else:
                print(f"Unknown command: '{cmd}'. Type 'help' for a list of commands.")

        except CalculatorError as exc:
            print(f"Error: {exc}")
