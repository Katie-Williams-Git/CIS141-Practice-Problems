#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25

for rows in range(1,6):
    for col in range(1,6):
        tabl = rows * col
        print(f"{tabl}" + '\t', end=' ')
        if col == 5:
            print()
