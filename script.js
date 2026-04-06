const PRECEDENCE = {
  "+": 1,
  "-": 1,
  "*": 2,
  "/": 2,
  "u+": 3,
  "u-": 3,
};

const ASSOCIATIVITY = {
  "+": "left",
  "-": "left",
  "*": "left",
  "/": "left",
  "u+": "right",
  "u-": "right",
};

const HISTORY_STORAGE_KEY = "calculator-history";

function isOperator(token) {
  return Object.prototype.hasOwnProperty.call(PRECEDENCE, token);
}

function tokenize(expression) {
  const compact = expression.replace(/\s+/g, "");
  const tokens = [];
  let index = 0;

  while (index < compact.length) {
    const char = compact[index];

    if (/\d|\./.test(char)) {
      let number = char;
      let hasDecimalPoint = char === ".";
      index += 1;

      while (index < compact.length && /[\d.]/.test(compact[index])) {
        if (compact[index] === ".") {
          if (hasDecimalPoint) {
            throw new Error("Invalid number format.");
          }
          hasDecimalPoint = true;
        }

        number += compact[index];
        index += 1;
      }

      if (number === ".") {
        throw new Error("A decimal point must include digits.");
      }

      tokens.push(number);
      continue;
    }

    if ("+-*/()".includes(char)) {
      const previous = tokens[tokens.length - 1];
      const unary =
        (char === "+" || char === "-") &&
        (!previous || isOperator(previous) || previous === "(");

      tokens.push(unary ? `u${char}` : char);
      index += 1;
      continue;
    }

    throw new Error(`Unsupported character: ${char}`);
  }

  return tokens;
}

function toReversePolishNotation(tokens) {
  const output = [];
  const operators = [];

  tokens.forEach((token) => {
    if (!Number.isNaN(Number(token))) {
      output.push(token);
      return;
    }

    if (isOperator(token)) {
      while (operators.length > 0) {
        const top = operators[operators.length - 1];

        if (
          !isOperator(top) ||
          (ASSOCIATIVITY[token] === "left" && PRECEDENCE[token] > PRECEDENCE[top]) ||
          (ASSOCIATIVITY[token] === "right" && PRECEDENCE[token] >= PRECEDENCE[top])
        ) {
          break;
        }

        output.push(operators.pop());
      }

      operators.push(token);
      return;
    }

    if (token === "(") {
      operators.push(token);
      return;
    }

    if (token === ")") {
      while (operators.length > 0 && operators[operators.length - 1] !== "(") {
        output.push(operators.pop());
      }

      if (operators.pop() !== "(") {
        throw new Error("Mismatched parentheses.");
      }
    }
  });

  while (operators.length > 0) {
    const token = operators.pop();

    if (token === "(" || token === ")") {
      throw new Error("Mismatched parentheses.");
    }

    output.push(token);
  }

  return output;
}

function applyOperator(operator, stack) {
  if (operator === "u+" || operator === "u-") {
    const value = stack.pop();

    if (value === undefined) {
      throw new Error("Missing value for unary operator.");
    }

    stack.push(operator === "u-" ? -value : value);
    return;
  }

  const right = stack.pop();
  const left = stack.pop();

  if (left === undefined || right === undefined) {
    throw new Error("Incomplete expression.");
  }

  if (operator === "+") {
    stack.push(left + right);
    return;
  }

  if (operator === "-") {
    stack.push(left - right);
    return;
  }

  if (operator === "*") {
    stack.push(left * right);
    return;
  }

  if (operator === "/") {
    if (right === 0) {
      throw new Error("Division by zero is not allowed.");
    }

    stack.push(left / right);
  }
}

function formatResult(value) {
  const rounded = Math.round((value + Number.EPSILON) * 1e12) / 1e12;

  if (Number.isInteger(rounded)) {
    return String(rounded);
  }

  return rounded.toFixed(12).replace(/\.?0+$/, "");
}

function evaluateExpression(expression) {
  if (!expression || !expression.trim()) {
    throw new Error("Enter an expression first.");
  }

  const tokens = tokenize(expression);
  const rpn = toReversePolishNotation(tokens);
  const stack = [];

  rpn.forEach((token) => {
    if (!Number.isNaN(Number(token))) {
      stack.push(Number(token));
      return;
    }

    applyOperator(token, stack);
  });

  if (stack.length !== 1) {
    throw new Error("Invalid expression.");
  }

  return formatResult(stack[0]);
}

function loadHistory() {
  if (typeof localStorage === "undefined") {
    return [];
  }

  try {
    const stored = localStorage.getItem(HISTORY_STORAGE_KEY);
    return stored ? JSON.parse(stored) : [];
  } catch (_error) {
    return [];
  }
}

function saveHistory(history) {
  if (typeof localStorage === "undefined") {
    return;
  }

  localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(history.slice(0, 10)));
}

function attachCalculatorUi() {
  if (typeof document === "undefined") {
    return;
  }

  const expressionInput = document.querySelector("#expression-input");
  const resultOutput = document.querySelector("#result-output");
  const historyList = document.querySelector("#history-list");
  const historyEmpty = document.querySelector("#history-empty");
  const clearHistoryButton = document.querySelector("#clear-history");
  const buttonGrid = document.querySelector(".button-grid");

  if (
    !expressionInput ||
    !resultOutput ||
    !historyList ||
    !historyEmpty ||
    !clearHistoryButton ||
    !buttonGrid
  ) {
    return;
  }

  let history = loadHistory();

  function insertValue(value) {
    const start = expressionInput.selectionStart ?? expressionInput.value.length;
    const end = expressionInput.selectionEnd ?? expressionInput.value.length;
    const nextValue =
      expressionInput.value.slice(0, start) + value + expressionInput.value.slice(end);

    expressionInput.value = nextValue;
    const cursor = start + value.length;
    expressionInput.focus();
    expressionInput.setSelectionRange(cursor, cursor);
    updatePreview();
  }

  function deleteValue() {
    const start = expressionInput.selectionStart ?? expressionInput.value.length;
    const end = expressionInput.selectionEnd ?? expressionInput.value.length;

    if (start !== end) {
      expressionInput.value =
        expressionInput.value.slice(0, start) + expressionInput.value.slice(end);
      expressionInput.setSelectionRange(start, start);
      updatePreview();
      return;
    }

    if (start === 0) {
      return;
    }

    expressionInput.value =
      expressionInput.value.slice(0, start - 1) + expressionInput.value.slice(end);
    expressionInput.setSelectionRange(start - 1, start - 1);
    updatePreview();
  }

  function renderHistory() {
    historyList.innerHTML = "";
    historyEmpty.hidden = history.length > 0;

    history.forEach((entry, index) => {
      const item = document.createElement("li");
      const reuseButton = document.createElement("button");
      const expression = document.createElement("span");
      const result = document.createElement("strong");

      item.className = "history-item";
      reuseButton.type = "button";
      reuseButton.className = "history-entry";
      reuseButton.dataset.index = String(index);
      expression.className = "history-expression";
      result.className = "history-result";

      expression.textContent = entry.expression;
      result.textContent = `= ${entry.result}`;

      reuseButton.append(expression, result);
      item.appendChild(reuseButton);
      historyList.appendChild(item);
    });
  }

  function updatePreview() {
    const expression = expressionInput.value.trim();

    if (!expression) {
      resultOutput.textContent = "0";
      resultOutput.dataset.state = "idle";
      return;
    }

    try {
      resultOutput.textContent = evaluateExpression(expression);
      resultOutput.dataset.state = "valid";
    } catch (error) {
      resultOutput.textContent = error.message;
      resultOutput.dataset.state = "error";
    }
  }

  function calculate() {
    const expression = expressionInput.value.trim();

    try {
      const result = evaluateExpression(expression);
      resultOutput.textContent = result;
      resultOutput.dataset.state = "valid";

      history = [
        {
          expression,
          result,
        },
        ...history.filter((entry) => entry.expression !== expression || entry.result !== result),
      ].slice(0, 10);

      saveHistory(history);
      renderHistory();
      expressionInput.value = result;
      expressionInput.focus();
      expressionInput.setSelectionRange(result.length, result.length);
    } catch (error) {
      resultOutput.textContent = error.message;
      resultOutput.dataset.state = "error";
    }
  }

  buttonGrid.addEventListener("click", (event) => {
    const button = event.target.closest("button");

    if (!button) {
      return;
    }

    if (button.dataset.value) {
      insertValue(button.dataset.value);
      return;
    }

    if (button.dataset.action === "clear") {
      expressionInput.value = "";
      expressionInput.focus();
      updatePreview();
      return;
    }

    if (button.dataset.action === "backspace") {
      deleteValue();
      return;
    }

    if (button.dataset.action === "calculate") {
      calculate();
    }
  });

  expressionInput.addEventListener("input", updatePreview);
  expressionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      calculate();
      return;
    }

    if (event.key === "Escape") {
      expressionInput.value = "";
      updatePreview();
    }
  });

  historyList.addEventListener("click", (event) => {
    const button = event.target.closest(".history-entry");

    if (!button) {
      return;
    }

    const entry = history[Number(button.dataset.index)];

    if (!entry) {
      return;
    }

    expressionInput.value = entry.expression;
    expressionInput.focus();
    expressionInput.setSelectionRange(
      entry.expression.length,
      entry.expression.length
    );
    updatePreview();
  });

  clearHistoryButton.addEventListener("click", () => {
    history = [];
    saveHistory(history);
    renderHistory();
  });

  renderHistory();
  updatePreview();
}

attachCalculatorUi();

if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    evaluateExpression,
    tokenize,
    toReversePolishNotation,
  };
}
