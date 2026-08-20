# 1. Create a file, write initial content, and close it manually
file = open("sample.txt", "w")

lines = [
    "First Line: Python\n",
    "Second Line: File Handling\n",
    "Third Line: Unit 3\n"
]

file.writelines(lines)
file.close()


# 2. Read file information and content using try...finally
try:
    file = open("sample.txt", "r")

    print("Filename:", file.name)
    print("Mode:", file.mode)
    print("Is Closed?:", file.closed)

    data = file.read()
    print("\n--- File Content ---\n" + data)

finally:
    file.close()


# 3. Add new content to the existing file using 'with'
with open("sample.txt", "a") as f:
    f.write("Fourth Line: Appended Content\n")


# 4. Demonstrate file pointer using tell() and seek()
with open("sample.txt", "r") as f:

    print("Initial Pointer Position:", f.tell())

    # Read the first line from the file
    print("Line 1:", f.readline().strip())
    print("Pointer Position after line 1:", f.tell())

    # Move the pointer back to the beginning
    f.seek(0)

    # Read all lines
    all_lines = f.readlines()


# 5. Store the first two lines in a separate output file
total_lines = len(all_lines)
first_two_lines = all_lines[:2]

with open("output.txt", "w") as f_out:
    f_out.writelines(first_two_lines)

print("\nTotal lines in file:", total_lines)
print("First two lines copied to output.txt successfully.")


# OUTPUT 
# Filename: sample.txt
# Mode: r
# Is Closed?: False

# --- File Content ---
# First Line: Python
# Second Line: File Handling
# Third Line: Unit 3

# Initial Pointer Position: 0
# Line 1: First Line: Python
# Pointer Position after line 1: 20

# Total lines in file: 4
# First two lines copied to output.txt successfully.