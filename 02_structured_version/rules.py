"""
Warehouse location rules.

This file contains the warehouse structure/configuration.
The generator reads this file and creates locations from it.

Idea:
- rules.py = warehouse truth
- generator.py = creates JSON from that truth
"""

SLOTS = ["A", "B", "C", "D"]

DEFAULT_ROWS_PER_COLUMN = 6

AISLE_CONFIG = {
    1: {
        "max_columns": 22,
        "rows_per_column": DEFAULT_ROWS_PER_COLUMN,
        "missing_columns": [],
        "min_row_by_column": {},
        "missing_slots_by_column": {}
    },
    2: {
        "max_columns": 22,
        "rows_per_column": DEFAULT_ROWS_PER_COLUMN,
        "missing_columns": [],
        "min_row_by_column": {},
        "missing_slots_by_column": {}
    },
    3: {
        "max_columns": 22,
        "rows_per_column": DEFAULT_ROWS_PER_COLUMN,
        "missing_columns": [],
        "min_row_by_column": {},
        "missing_slots_by_column": {}
    },
    4: {
        "max_columns": 34,
        "rows_per_column": DEFAULT_ROWS_PER_COLUMN,
        "missing_columns": [16],
        "min_row_by_column": {
            34: 30
        },
        "missing_slots_by_column": {
            33: ["D"]
        }
    },
    5: {
        "max_columns": 34,
        "rows_per_column": DEFAULT_ROWS_PER_COLUMN,
        "missing_columns": [15, 16],
        "min_row_by_column": {
            33: 30,
            34: 30
        },
        "missing_slots_by_column": {}
    }
}
