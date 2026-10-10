# AI Engineering Journal

## Experiment Information
- Project: AI-Engineering-Lab
- IDE: Visual Studio Code
- AI assistant: GitHub Copilot / ChatGPT
- Date: 10 October 2026

## Interaction 1: Code Generation

**Objective:** Generate a multiplication function in Python.

**Prompt given to AI:**
"Create a Python function multiply(a, b) that returns the product of two numbers."

**AI-generated suggestion:**
```python
def multiply(a, b):
    return a * b
```

**My review:**
The function uses the multiplication operator and returns the product of the two arguments.

**Validation performed:**
Tested the function using the inputs 2 and 3. The output was 6.

**Final engineering decision:**
Accepted the suggestion after reviewing the implementation and verifying its behavior.

**Reason:**
The function meets the requirement and passed the test performed.

## Interaction 2: Explain the function in main.py

**Objective:** Understand the code in the current Python file.

**Prompt given to AI:**
"explain the function"

**Observed code:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**AI explanation:**
The file defines two arithmetic functions: `add` and `subtract`. `add` returns the sum of two values, and `subtract` returns the difference between two values.

**Engineering decision:**
No code change was required; the explanation was accepted as a correct description of the existing functions.

## Interaction 3: Generate unit test cases

**Objective:** Validate the arithmetic behavior with automated tests.

**Prompt given to AI:**
"generate unit test cases"

**Test file created:**
```python
import unittest

from src.main import add, subtract


class TestArithmeticFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(add(-4, 7), 3)

    def test_add_zero(self):
        self.assertEqual(add(0, 9), 9)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_subtract_zero(self):
        self.assertEqual(subtract(8, 0), 8)


if __name__ == "__main__":
    unittest.main()
```

**Validation performed:**
Command run:
```bash
python -m unittest discover -s tests -v
```

**Result:**
- 6 tests ran
- all 6 passed
- status: OK

## Interaction 4: Identify possible edge cases

**Objective:** Review potential failure scenarios in the arithmetic functions.

**Edge cases identified:**
- very large numbers
- very small floating-point values
- negative inputs
- zero inputs
- mixed-type inputs such as strings and numbers
- invalid non-numeric values
- float precision issues such as `0.1 + 0.2`

**Engineering conclusion:**
The functions are simple and work for valid numeric inputs, but they do not currently validate input types. Float precision is the main practical edge case for Python arithmetic.

## Interaction 5: Add power finding function to main.py

**Objective:** Extend the arithmetic module with a power operation.

**Prompt given to AI:**
"add power finding function to main.py"

**Implementation added to main.py:**
```python
def power(base, exponent):
    """Return the base raised to the power of the exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("base and exponent must be numbers.")
    return base ** exponent
```

**Updated test coverage:**
```python
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
```

**Validation performed:**
Command run:
```bash
python -m unittest discover -s tests -v
```

**Result:**
- 7 tests ran
- all 7 passed
- status: OK

## Interaction 6: Project coding instructions review

**Objective:** Check the project rules that govern future code changes.

**Project rules reviewed from copilot-instructions.md:**
- Use Python 3.
- Write simple, readable, modular code.
- Follow PEP 8 naming conventions.
- Use meaningful variable and function names.
- Add docstrings to public functions.
- Handle invalid inputs appropriately.
- Do not introduce unnecessary dependencies.
- Run Ruff checks before completing changes.
- Format code using Ruff.
- Write unit tests for new functionality.
- Explain significant design decisions.
- Do not modify unrelated files.
- Ask before destructive operations.

**Result:**
These rules were followed in the power-function implementation and in the corresponding testing updates.

## Interaction 7: AI error example and human correction

**Objective:** Document a realistic mistake in AI-generated code and how a human corrected it.

**AI suggestion:**
```python
def divide(a, b):
    return a / b
```

**Problem identified:**
Division by zero was not handled. When `b == 0`, Python raises a `ZeroDivisionError` and the function fails.

**Human decision:**
Add input validation to reject division by zero with a clear error message.

**Corrected implementation:**
```python
def divide(a, b):
    """Return a divided by b, raising a clear error for zero division."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
```

**Verification:**
Command executed:
```python
try:
    divide(10, 0)
except ValueError as exc:
    print(type(exc).__name__, exc)
```

**Final outcome:**
The actual test result was:
```text
ValueError Denominator cannot be zero.
```

This confirms the human correction handled the bug correctly and prevented the program from crashing with an unhandled `ZeroDivisionError`.

## Final project status
- Arithmetic functions available: `add`, `subtract`, `power`
- Tests implemented and passing
- Code remains minimal, readable, and aligned with the project instructions
- Ruff was attempted, but the tool was not installed in the active environment at the time of verification
- Documented AI mistake and human correction: division-by-zero issue was identified and fixed with explicit validation
