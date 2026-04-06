# Calculator Demo

Small, dependency-free calculator code that runs directly in the browser.

## What is included

- `index.html` - the calculator UI
- `styles.css` - the app styling
- `script.js` - expression parsing, evaluation, and UI behavior

The evaluator supports:

- addition, subtraction, multiplication, and division
- parentheses for grouping
- decimal numbers
- unary `+` and `-` (for example `-5 * (2 + 3)`)
- a simple calculation history stored in the browser

## Running it

Open `index.html` in a browser, or serve the repository directory with any static
file server.

## Keyboard shortcuts

- `Enter` - calculate the current expression
- `Escape` - clear the current expression

## Notes

The implementation intentionally avoids `eval()` and instead tokenizes and
evaluates expressions with a small parser.
