# Open and read the POSCAR file
with open('POSCAR', 'r') as file:
    lines = file.readlines()

# Print information from line 5
print("Line 5:")
print(lines[4])

# Print information from line 6
print("Line 6:")
print(lines[5])

# Print information from line 7
print("Line 7:")
print(lines[6])