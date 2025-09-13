# Broskies_hub-tasks

📌 Task: Build a Calculator CLI App

🎯 Objective

The goal of this task is to create a command-line calculator in Python that supports basic arithmetic operations. This application should allow users to input numbers, select an operation, and display the result. The program should continue running in a loop until the user decides to exit.


⚙️ Tools Used

Python → Programming language chosen because it is beginner-friendly, widely used, and perfect for CLI-based apps.

VS Code / Any Text Editor → For writing and running the script.

Command-line / Terminal → To execute the program interactively.


🛠️ What I Built

I built a Calculator CLI Application (CalculatorCLI.py) with the following features:

1. Supports Addition, Subtraction, Multiplication, Division, and Modulus.


2. Each operation is implemented using separate functions (for clean code and reusability).

3. User input is taken using input().


4. The program runs in a loop so the user can perform multiple calculations without restarting.

5. Includes error handling for:
Division by zero.

Invalid (non-numeric) inputs.

Invalid menu choices.

6. A menu-driven interface for easy navigation.


📝 Why I Built It This Way

Functions: By separating each operation into its own function (add(), subtract(), etc.), the code is modular, easier to read, test, and extend in the future (e.g., adding advanced operations).

Looping mechanism: Using a while True loop ensures the calculator keeps running until the user explicitly chooses to exit.

Error handling: Prevents program crashes and provides a smooth user experience.

CLI interface: Keeps it lightweight, simple, and accessible from any terminal.



🔎 How It Works (Step by Step)

1. The program starts by displaying a menu of available operations.


2. The user selects an operation (choice 1–6).


3. If the user selects Exit (6), the loop breaks, and the program ends.

4. Otherwise: 
The user is prompted to enter two numbers.

The chosen operation is performed by calling the respective function.

The result is displayed on the screen.



5. If invalid input is given, the program shows an error message and restarts the loop.
 
✅ Outcome

A well-structured, menu-driven calculator that works directly in the terminal, meeting all requirements stated in the task.


---

📌 Example Run

--- Calculator Menu ---
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exit
Enter your choice (1-6): 2
Enter first number: 15
Enter second number: 4
Result: 11.0









