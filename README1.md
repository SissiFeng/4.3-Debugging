# Debugging in VS Code Assignment

## 📚 Introduction

This assignment is designed to help you practice various debugging techniques in Visual Studio Code (VS Code). You'll work through different debugging methods, including using print statements, setting breakpoints, inspecting variables, and using the debug console.

## 🎯 Objectives

By the end of this assignment, you should be able to:

1. Use print statements for basic debugging
2. Set and use breakpoints in VS Code
3. Inspect variables during code execution
4. Utilize the VS Code debug console
5. Apply different debugging techniques to solve programming problems

## 🛠️ Setup

1. Ensure you have Python and pytest installed in your Codespace.
2. Familiarize yourself with the VS Code debugging interface.

## 📝 Instructions

This assignment is divided into several debugging steps. You'll complete one step at a time, run tests to verify your work, and then move on to the next step.

### Getting Started

1. Open `main.py` in your VS Code editor.
2. Locate the `DEBUG_STEP` variable at the top of the file. It should be set to 0 initially.

### Completing Each Step

For each debugging step:

1. Read the TODO comments in the `main.py` file for the current `DEBUG_STEP`.
2. Implement the required debugging technique as instructed.
3. Save your changes.
4. Run the tests using the command `pytest test_main.py` in the terminal.
5. If the tests pass, increment `DEBUG_STEP` by 1 in `main.py`.
6. If the tests fail, review your implementation and try again.

### Debugging Steps

#### Step 1: Print Statements (DEBUG_STEP = 1)
- Implement print statements in the `find_max` function to debug the code.
- Use print statements to show the current maximum and the number being compared in each iteration.

#### Step 2: Breakpoints (DEBUG_STEP = 2)
- Set a breakpoint in the `sort_list` function.
- Use VS Code's stepping functionality to debug the sorting algorithm.

#### Step 3: Variable Inspection (DEBUG_STEP = 3)
- In the `calculate_average` function, use variable inspection to debug.
- Pay attention to the `total` and `count` variables as you step through the code.

#### Step 4: Debug Console (DEBUG_STEP = 4)
- Use the VS Code debug console to evaluate expressions.
- Try the suggested expressions and observe the results.

## 🧪 Running Tests

After implementing each debugging step:

1. Open a new terminal in VS Code.
2. Run the command: `pytest test_main.py`
3. Review the test results:
   - If all tests pass, move on to the next debugging step.
   - If any tests fail, read the error messages, revise your code, and try again.

## 📈 Progress Tracking

Your progress is tracked by the `DEBUG_STEP` variable:
- `DEBUG_STEP = 0`: Not started
- `DEBUG_STEP = 1`: Completed print statement debugging
- `DEBUG_STEP = 2`: Completed breakpoint debugging
- `DEBUG_STEP = 3`: Completed variable inspection debugging
- `DEBUG_STEP = 4`: Completed debug console usage

## 🏁 Completion

You've completed the assignment when:
1. All debugging steps are implemented correctly.
2. All tests pass when `DEBUG_STEP = 4`.
3. You can explain how each debugging technique helped you understand the code better.

## 💡 Tips

- Don't rush! Take your time to understand each debugging technique.
- If you're stuck, review the VS Code debugging documentation or ask for help.
- Remember, debugging is a crucial skill in programming. The more you practice, the better you'll become.

## 🆘 Getting Help

If you encounter any issues or have questions:
1. Review the TODO comments and this README file carefully.
2. Check the VS Code documentation for debugging Python.
3. If you're still stuck, reach out to your instructor or teaching assistant for help.

Good luck, and happy debugging! 🐛🔍