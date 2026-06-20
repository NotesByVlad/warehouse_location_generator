import json

from rules import AISLE_CONFIG, SLOTS


OUTPUT_FILE = "warehouse_locations.json"


def create_location_code(aisle, column, row, slot):
    return f"{aisle:02d}-{column:02d}-{row:02d}-{slot}"


def generate_warehouse(aisle_config, slots):
    warehouse = {
        "aisles": {}
    }

    for aisle, config in aisle_config.items():
        aisle_key = f"{aisle:02d}"

        warehouse["aisles"][aisle_key] = {
            "columns": {}
        }

        max_columns = config["max_columns"]
        rows_per_column = config["rows_per_column"]

        missing_columns = config.get("missing_columns", [])
        min_row_by_column = config.get("min_row_by_column", {})
        missing_slots_by_column = config.get("missing_slots_by_column", {})

        for column in range(1, max_columns + 1):
            if column in missing_columns:
                continue

            column_key = f"{column:02d}"

            warehouse["aisles"][aisle_key]["columns"][column_key] = {
                "rows": {}
            }

            start_row = min_row_by_column.get(column, 0)
            missing_slots = missing_slots_by_column.get(column, [])

            for row in range(start_row, rows_per_column * 10, 10):
                row_key = f"{row:02d}"

                warehouse["aisles"][aisle_key]["columns"][column_key]["rows"][row_key] = {
                    "locations": {}
                }

                for slot in slots:
                    if slot in missing_slots:
                        continue

                    location_code = create_location_code(
                        aisle=aisle,
                        column=column,
                        row=row,
                        slot=slot
                    )

                    warehouse["aisles"][aisle_key]["columns"][column_key]["rows"][row_key]["locations"][slot] = {
                        "location_code": location_code,
                        "status": "available"
                    }

    return warehouse


def save_warehouse_to_json(warehouse, output_file):
    with open(output_file, "w") as file:
        json.dump(warehouse, file, indent=4)


def count_locations(warehouse):
    total = 0

    for aisle_data in warehouse["aisles"].values():
        for column_data in aisle_data["columns"].values():
            for row_data in column_data["rows"].values():
                total += len(row_data["locations"])

    return total


def main():
    warehouse = generate_warehouse(AISLE_CONFIG, SLOTS)
    save_warehouse_to_json(warehouse, OUTPUT_FILE)

    total_locations = count_locations(warehouse)

    print(f"Generated {total_locations} locations.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
