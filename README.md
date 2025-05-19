# freepbx-dialplan-generator
This script generates a structured CSV file containing phone number prefixes and match patterns, useful for telecom configurations such as SIM assignments, call routing, or PBX setups.

## How It Works
1. **Define Prefix Range** – Set `min_prefix` and `max_prefix` to specify the range of prefixes (e.g., SIM card allocations).
2. **Adjust Prepend Values** – Custom mappings (e.g., `10 → 97`) simplify number formatting.
3. **Generate Entries** – Creates multiple variations of phone numbers based on predefined match patterns.
4. **Export to CSV** – Saves the output as `generated_dialplan.csv` for easy import into telecom systems.

## Example Use Case

A telecom operator assigns SIM cards based on specific prefixes:

| Prefix | Phone Number  | SIM Assignment |
|--------|-------------|---------------|
| 541    | 098 1231231 | SIM 1         |
| 542    | 098 1231232 | SIM 2         |
| 543    | 098 1231233 | SIM 3         |
| 544    | 098 1231234 | SIM 4         |

To configure this setup, adjust the following settings in the script:

```python
# IMPORTANT: min_prefix must be one number LESS than the actual starting prefix!
min_prefix = 540  # This will generate prefixes starting from 541
max_prefix = 544  # This is the last prefix in the range
