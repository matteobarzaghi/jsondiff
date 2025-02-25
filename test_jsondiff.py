import json
from jsondiff import diff
import pprint

def convert_keys(obj):
    """Recursively convert all dict keys to strings."""
    if isinstance(obj, dict):
        return {str(k): convert_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys(i) for i in obj]
    else:
        return obj

# Load the JSON files
with open('old_220.json') as f1, open('new_343.json') as f2:
    json1 = json.load(f1)
    json2 = json.load(f2)

# Compute the differences using jsondiff
differences = diff(json1, json2)

# Pretty-print the diff to the console using pprint
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(differences)

# Convert keys to strings for JSON serialization
differences_converted = convert_keys(differences)

# Save the pretty-printed diff to a file
pretty_diff = json.dumps(differences_converted, indent=2)
with open("diff_output.txt", "w", encoding="utf-8") as outfile:
    outfile.write(pretty_diff)