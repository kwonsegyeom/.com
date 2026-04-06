class Calculator {
  constructor(expressionEl, resultEl) {
    this.expressionEl = expressionEl;
    this.resultEl = resultEl;
    this.reset();
  }

  reset() {
    this.currentOperand = "0";
    this.previousOperand = "";
    this.operator = null;
    this.shouldResetScreen = false;
    this.lastResult = null;
  }

  clear() {
    this.reset();
    this.updateDisplay();
  }

  appendDigit(digit) {
    if (this.shouldResetScreen) {
      this.currentOperand = "";
      this.shouldResetScreen = false;
    }
    if (this.currentOperand === "0" && digit !== ".") {
      this.currentOperand = digit;
    } else {
      this.currentOperand += digit;
    }
    this.updateDisplay();
  }

  appendDecimal() {
    if (this.shouldResetScreen) {
      this.currentOperand = "0";
      this.shouldResetScreen = false;
    }
    if (!this.currentOperand.includes(".")) {
      this.currentOperand += ".";
    }
    this.updateDisplay();
  }

  toggleSign() {
    if (this.currentOperand === "0") return;
    if (this.currentOperand.startsWith("-")) {
      this.currentOperand = this.currentOperand.slice(1);
    } else {
      this.currentOperand = "-" + this.currentOperand;
    }
    this.updateDisplay();
  }

  percent() {
    const value = parseFloat(this.currentOperand);
    if (isNaN(value)) return;
    this.currentOperand = String(value / 100);
    this.updateDisplay();
  }

  chooseOperator(op) {
    if (this.operator && !this.shouldResetScreen) {
      this.evaluate();
    }
    this.operator = op;
    this.previousOperand = this.currentOperand;
    this.shouldResetScreen = true;
    this.updateDisplay();
  }

  evaluate() {
    const prev = parseFloat(this.previousOperand);
    const current = parseFloat(this.currentOperand);
    if (isNaN(prev) || isNaN(current)) return;

    let result;
    switch (this.operator) {
      case "add":
        result = prev + current;
        break;
      case "subtract":
        result = prev - current;
        break;
      case "multiply":
        result = prev * current;
        break;
      case "divide":
        if (current === 0) {
          this.resultEl.textContent = "Error";
          this.reset();
          return;
        }
        result = prev / current;
        break;
      default:
        return;
    }

    result = Math.round(result * 1e12) / 1e12;
    const expression = `${this.formatNumber(prev)} ${this.operatorSymbol(this.operator)} ${this.formatNumber(current)}`;
    this.expressionEl.textContent = expression;
    this.currentOperand = String(result);
    this.operator = null;
    this.previousOperand = "";
    this.shouldResetScreen = true;
    this.lastResult = result;
    this.updateDisplay();
  }

  operatorSymbol(op) {
    const symbols = { add: "+", subtract: "−", multiply: "×", divide: "÷" };
    return symbols[op] || op;
  }

  formatNumber(num) {
    const str = String(num);
    if (str.includes(".")) {
      const [integer, decimal] = str.split(".");
      return `${Number(integer).toLocaleString("en-US")}.${decimal}`;
    }
    return Number(num).toLocaleString("en-US");
  }

  updateDisplay() {
    const displayValue = this.currentOperand || "0";
    const num = parseFloat(displayValue);

    if (displayValue.endsWith(".") || displayValue.endsWith(".0")) {
      this.resultEl.textContent = displayValue;
    } else if (!isNaN(num)) {
      this.resultEl.textContent = this.formatNumber(num);
    } else {
      this.resultEl.textContent = displayValue;
    }

    if (this.operator && this.previousOperand) {
      this.expressionEl.textContent = `${this.formatNumber(parseFloat(this.previousOperand))} ${this.operatorSymbol(this.operator)}`;
    } else if (!this.lastResult) {
      this.expressionEl.textContent = "";
    }

    const len = this.resultEl.textContent.length;
    if (len > 12) {
      this.resultEl.style.fontSize = "1.8rem";
    } else if (len > 9) {
      this.resultEl.style.fontSize = "2.1rem";
    } else {
      this.resultEl.style.fontSize = "";
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const expressionEl = document.getElementById("expression");
  const resultEl = document.getElementById("result");
  const calc = new Calculator(expressionEl, resultEl);

  document.querySelectorAll(".btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const { value, action } = btn.dataset;

      if (value !== undefined) {
        calc.appendDigit(value);
      } else {
        switch (action) {
          case "clear":
            calc.clear();
            break;
          case "toggle-sign":
            calc.toggleSign();
            break;
          case "percent":
            calc.percent();
            break;
          case "decimal":
            calc.appendDecimal();
            break;
          case "equals":
            calc.evaluate();
            break;
          case "add":
          case "subtract":
          case "multiply":
          case "divide":
            calc.chooseOperator(action);
            document.querySelectorAll(".operator").forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            break;
        }
      }
    });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key >= "0" && e.key <= "9") calc.appendDigit(e.key);
    else if (e.key === ".") calc.appendDecimal();
    else if (e.key === "+" || e.key === "=") {
      if (e.shiftKey || e.key === "+") calc.chooseOperator("add");
      else calc.evaluate();
    }
    else if (e.key === "-") calc.chooseOperator("subtract");
    else if (e.key === "*") calc.chooseOperator("multiply");
    else if (e.key === "/") { e.preventDefault(); calc.chooseOperator("divide"); }
    else if (e.key === "Enter") calc.evaluate();
    else if (e.key === "Escape" || e.key === "Delete") calc.clear();
    else if (e.key === "Backspace") {
      if (calc.currentOperand.length > 1) {
        calc.currentOperand = calc.currentOperand.slice(0, -1);
      } else {
        calc.currentOperand = "0";
      }
      calc.updateDisplay();
    }
  });
});
