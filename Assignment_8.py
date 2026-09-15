with open("input.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)

with open("extracted_lines.txt", "w") as new_file:
    new_file.writelines(lines[:2])

print("Total number of lines:", line_count)
print("First two lines copied to extracted_lines.txt")

# Output 
#Total number of lines: 4
#First two lines copied to extracted_lines.txt
