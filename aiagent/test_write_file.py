from functions.write_file import write_file
from functions.get_file_content import get_file_content


# Test 1: Overwrite an existing file (lorem.txt)
print("=== Test 1: Overwrite calculator/lorem.txt ===")
result = write_file("calculator", "lorem.txt", "wttttt")
print(result)
# Verify the content was written
content = get_file_content("calculator", "lorem.txt")
print(f"New content: {content}")
print()

# Test 2: Write to a file in an existing subdirectory
print("=== Test 2: Write to calculator/pkg/morelorem.txt ===")
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result)
# Verify the content was written
content = get_file_content("calculator", "pkg/morelorem.txt")
print(f"New content: {content}")
print()

# Test 3: Write to a file that requires creating parent directories
print("=== Test 3: Write to calculator/newdir/newfile.txt (creates parent dir) ===")
result = write_file("calculator", "newdir/newfile.txt", "this is a new file in a new directory")
print(result)
# Verify the content was written
content = get_file_content("calculator", "newdir/newfile.txt")
print(f"New content: {content}")
print()

# Test 4: Try to write outside the working directory (should error)
print("=== Test 4: Write outside working directory ===")
result = write_file("calculator", "/etc/passwd", "hacked!")
print(result)
print()

# Test 5: Try to write to a directory path (should error)
print("=== Test 5: Write to a directory (calculator/pkg) ===")
result = write_file("calculator", "pkg", "can't write to a directory")
print(result)
