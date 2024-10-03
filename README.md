Expense Tracker
Overview
The Expense Tracker is a simple command-line application that allows users to manage their expenses efficiently. Users can add, view, and save their expenses, which are stored in a JSON file for persistent storage.

Features
Add Expense: Users can enter the date, category, and amount for each expense.
View Expenses: Users can view a list of all recorded expenses.
Persistent Storage: Expenses are saved to a JSON file, allowing data to persist across sessions.
Input Validation: Ensures the date is in the correct format (YYYY-MM-DD) and that the amount is a positive number.

Technologies Used
Python: The primary programming language used to develop the expense tracker application. Python's simplicity and readability make it a great choice for such projects.
JSON: A lightweight data interchange format used for storing and retrieving expenses. The expenses are saved in a expenses.json file, making it easy to manage data in a structured format.
Command-Line Interface (CLI): The application is operated through a command-line interface, allowing users to interact with the program via text inputs and outputs.

Key Libraries/Modules
json Module: A built-in Python module used to parse JSON data for saving and loading expenses.
