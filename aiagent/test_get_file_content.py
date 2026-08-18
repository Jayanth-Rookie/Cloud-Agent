from functions.get_file_content import get_file_content


# Test 1: lorem.txt truncation
print("=== Test 1: lorem.txt truncation ===")
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print()

# Test 2: Read calculator/main.py
print("=== Test 2: calculator/main.py ===")
result = get_file_content("calculator", "main.py")
print(result)
print()

# Test 3: Read calculator/pkg/calculator.py
print("=== Test 3: calculator/pkg/calculator.py ===")
result = get_file_content("calculator", "pkg/calculator.py")
print(result)
print()

# Test 4: Outside working directory (should error)
print("=== Test 4: /bin/cat (outside working directory) ===")
result = get_file_content("calculator", "/bin/cat")
print(result)
print()

# Test 5: Non-existent file (should error)
print("=== Test 5: pkg/does_not_exist.py (file not found) ===")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)
