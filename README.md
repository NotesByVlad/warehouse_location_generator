# Warehouse Location Generator

A small Python project that generates warehouse location codes.

The project is based on a warehouse structure where locations follow this format:

```text
AA-CC-RR-S
```

Example:

```text
04-33-30-A
```

Where:

* `AA` = aisle number
* `CC` = column number
* `RR` = row level
* `S` = slot letter

## Features

* Generate locations for a range of aisles
* Generate columns starting from `01`
* Generate rows like `00`, `10`, `20`, `30`
* Generate slots `A`, `B`, `C`, `D`
* Support aisle-specific rules:

  * missing columns
  * columns that start from a higher row
  * missing slots in specific columns

## Example Rules

```python
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
```

## How to Run

```bash
python generator.py
```

Then enter:

```text
Start aisle: 1
End aisle: 5
Columns per aisle: 34
Rows per column: 6
```

## Why I Built This

I built this project to practice Python by creating something connected to real warehouse work and location structures.

The goal was not to build a big system, but to finish a small useful project before creating a complex warehouse system.
