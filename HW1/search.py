
rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []


positions = {}


for r in range(rows):
    row_data = []
    print(f"\nRow {r+1}")
    for c in range(cols):
        value = float(input(f"Enter number{c+1}: ")) 
        row_data.append(value)

    
        if value not in positions:
            positions[value] = []
        positions[value].append((r, c))  

    matrix.append(row_data)


print("\nThe numbers are:\n")
for row in matrix:
    print(" ".join(str(x) for x in row))


search_val = float(input("\nSearch: "))

if search_val in positions:
    found_pos = positions[search_val]
    print(f"\nNumber {search_val} found at:", end=" ")
    for pos in found_pos:
        print(f"Row {pos[0]}, Col {pos[1]}", end="  ")
else:
    print(f"\nNumber {search_val} not found in the matrix.")
