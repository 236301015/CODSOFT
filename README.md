
# Simple Command-Line Calculator

A brief description of what this project does and who it's for


## 🔧 Features

- Supports basic arithmetic operations:  
  ➕ Addition  
  ➖ Subtraction  
  ✖️ Multiplication  
  ➗ Division (with zero-check)  
  ➗ Modulo (with zero-check)
- Input validation for non-numeric entries
- Loop continues until user types `"exit"`

## 📂 File

- `Calculator.py` — Main script

## ▶️ Usage

```bash
python Calculator.py
```

## ❗ Notes



* Division and modulo operations check for zero to prevent runtime errors.

* The calculator works with integers only.

* Only the symbols +, -, *, /, and % are supported.


## License



This project is open-source and free to use.
## Appendix

Any additional information goes here

Enter first number: 10
Enter a number or "exit" to exit the loop: 5
Enter a symbol: +
Enter a number or "exit" to exit the loop: 2
Enter a symbol: *
Enter a number or "exit" to exit the loop: exit
Result: 30


## Documentation

📝 Documentation: Calculator.py
📌 Overview

This script implements a basic command-line calculator in Python. It performs a series of arithmetic operations on a number entered initially by the user and continues until the user types "exit". Each iteration allows the user to input a new number and an operator to apply to the running total.
🔄 Workflow

    Initial Input:
    The script starts by prompting the user to enter the first number, which is stored as num1.

    Loop for Continuous Calculation:
    A while True loop is used to keep requesting:

        Another number (num2)

        An operation symbol (sym)

    The loop runs until the user types "exit".

    Input Validation:

        If the user types anything non-numeric (excluding "exit"), an error is shown.

        For / and % operations, division/modulo by zero is handled.

    Operations:
    Based on the symbol entered, the calculator performs:

        + Addition

        - Subtraction

        * Multiplication

        / Division (with zero-check)

        % Modulo (with zero-check)

    Result Display:
    Once the user types "exit", the final result (num1) is printed.

🔣 Functions/Variables

    num1 (int):
    Stores the running total/result.

    num2 (int / str):
    Temporarily holds the next input number. Initially a string to allow checking for "exit" and validation.

    sym (str):
    The arithmetic operator to apply.

⚠️ Error Handling

    Checks for:

        Invalid number inputs

        Division or modulo by zero

        Invalid operation symbols

Each of these shows an appropriate error message and continues the loop without crashing the program.
🧼 Limitations

    Only works with integers.

    Doesn’t support floating-point numbers.

    Doesn’t support chained operations (e.g., 10 + 5 * 2 in a single line).

    No function modularization — all code is in the global scope.

✅ Suggestions for Improvement

    Wrap logic in functions (e.g., get_input(), perform_operation())

    Add support for float inputs.

    Enhance symbol handling with a dictionary.

    Add unit tests or error logging.

    Optional: build a GUI or web version.
