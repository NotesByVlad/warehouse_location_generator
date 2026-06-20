import json

print("Location Generator")

# Data
slots = ["A", "B", "C", "D"]

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


def generate_warehouse(start_aisle, end_aisle, columns, rows, slots):
    warehouse = {"aisles": {}}

    for aisle in range(start_aisle, end_aisle + 1):

        rules = aisle_rules.get(aisle, {})
        missing_columns = rules.get("missing_columns", [])
        min_row_by_column = rules.get("min_row_by_column", {})
        missing_slots_by_column = rules.get("missing_slots_by_column", {})

        aisle_key = f"{aisle:02d}"

        warehouse["aisles"][aisle_key] = {
            "columns": {}
        }

        for column in range(1, columns + 1):

            if column in missing_columns:
                continue

            column_key = f"{column:02d}"

            warehouse["aisles"][aisle_key]["columns"][column_key] = {
                "rows": {}
            }

            start_row = min_row_by_column.get(column, 0)
            missing_slots = missing_slots_by_column.get(column, [])

            for row in range(start_row, rows * 10, 10):

                row_key = f"{row:02d}"

                warehouse["aisles"][aisle_key]["columns"][column_key]["rows"][row_key] = {
                    "locations": {}
                }

                for slot in slots:

                    if slot in missing_slots:
                        continue

                    location_code = f"{aisle:02d}-{column:02d}-{row:02d}-{slot}"

                    warehouse["aisles"][aisle_key]["columns"][column_key]["rows"][row_key]["locations"][slot] = {
                        "location_code": location_code,
                        "status": "available"
                    }

    return warehouse


start_aisle = int(input("Start aisle: "))
end_aisle = int(input("End aisle: "))
columns = int(input("Columns per aisle: "))
rows = int(input("Rows per column: "))

warehouse = generate_warehouse(
    start_aisle,
    end_aisle,
    columns,
    rows,
    slots
)

with open("location_nested.json", "w") as file:
    json.dump(warehouse, file, indent=4)

print("Saved to locations_nested.json")
