# JSON Diff Tool

A simple Python script that compares two large JSON files and outputs their differences in a human-readable, pretty-printed format. It leverages the `jsondiff` library to compute the differences and then uses Python’s built-in modules to format and save the output.

## Features

- **Compare Two JSON Files:**  
  Reads two JSON files (by default `old_220.json` and `new_343.json`) and computes the differences.

- **Pretty-Printed Output:**  
  Uses the `pprint` module and `json.dumps` to display the diff in a clean and readable format.

- **Key Conversion for JSON Serialization:**  
  Converts non-standard dictionary keys to strings to ensure compatibility with JSON serialization.

- **Output to File:**  
  Saves the formatted diff to `diff_output.txt` for easier searching and navigation.

## Requirements

- Python 3.x
- [jsondiff](https://pypi.org/project/jsondiff/) library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

