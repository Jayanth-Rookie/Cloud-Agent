from functions.run_py_file import run_python_file


# Test 1: Run calculator with no args (should print usage)
print("=== Test 1: calculator/main.py (no args) ===")
result = run_python_file("calculator", "main.py")
print(result)
print()

# Test 2: Run calculator with an expression
print('=== Test 2: calculator/main.py "3 + 5" ===')
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)
print()

# Test 3: Run the calculator tests
print("=== Test 3: calculator/test.py ===")
result = run_python_file("calculator", "test.py")
print(result)
print()

# Test 4: Try to run a file outside working directory (should error)
print("=== Test 4: calculator/../main.py (outside working dir) ===")
result = run_python_file("calculator", "../main.py")
print(result)
print()

# Test 5: Try to run a nonexistent file (should error)
print("=== Test 5: calculator/nonexistent.py ===")
result = run_python_file("calculator", "nonexistent.py")
print(result)
print()

# Test 6: Try to run a non-Python file (should error)
print("=== Test 6: calculator/lorem.txt ===")
result = run_python_file("calculator", "lorem.txt")
print(result)
