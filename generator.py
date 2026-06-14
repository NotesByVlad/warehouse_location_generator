print("Location Generator")

# Data
slots = ["A","B","C","D"]
aisle_rules = {
    4: {
        "missing_columns": [16],
        "min_row_by_column": {34: 30},
        "missing_slots_by_column": {33: ["D"]}
    },
    5: {
        "missing_columns": [15, 16],
        "min_row_by_column": {
            33: 30,
            34: 30
        },
        "missing_slots_by_column": {}
    }
}

# Function
def generate_simple_aisle(aisle, columns, rows, slots):
    rules = aisle_rules.get(aisle, {})
    missing_columns = rules.get("missing_columns", [])
    min_row_by_column = rules.get("min_row_by_column", {})
    missing_slots_by_column = rules.get("missing_slots_by_column", {})

    for column in range(1, columns + 1):
        if column in missing_columns:
            continue

        start_row = min_row_by_column.get(column, 0)
        missing_slots = missing_slots_by_column.get(column, [])

        for row in range(start_row, rows * 10, 10):
            
            for slot in slots:        
                if slot in missing_slots:
                    continue
                    
                print(f"{aisle:02d}-{column:02d}-{row:02d}-{slot}")

# User Input
start_aisle = int(input("Start aisle: "))
end_aisle = int(input("End aisle: "))
columns = int(input("Columns per aisle: "))
rows = int(input("Rows per column: "))

# Run function
for aisle in range(start_aisle, end_aisle + 1):
    generate_simple_aisle(aisle, columns, rows, slots)