import pandas as pd

# Define the starting and ending prefix values
min_prefix = 560  # Set this 1 less than the desired starting prefix to align numbering
max_prefix = 592  # Upper limit of the prefix range
max_prepend = max_prefix - min_prefix  # Automatically calculates the range
#max_prepend = 32  # Uncomment to manually set a fixed range

# Match patterns for different numbering formats
match_patterns = ["00385Z.", "385Z.", "X.", "Z.", "X."]

# Adjust specific prepend values for better readability and easier configuration.
# Instead of using numbers like 10, 20, 30, we map them to 97, 98, 99
# This avoids unnecessary trailing zeros, making it cleaner.
cosmetic_prepend_map = {
    10: 97,
    20: 98,
    30: 99,
}

# Generate the dial plan data
data = []
for original_prepend in range(1, max_prepend + 1):
    prepend = cosmetic_prepend_map.get(original_prepend, original_prepend)  # Use mapped value only for output
    prefix = min_prefix + original_prepend  # Always use original value for prefix math
    base_number = prepend * 100000 + 385  # Construct base number for match pattern variations

    # Append different variations for the dial plan
    data.append([prepend, prefix, "00385Z.", ""])  # Full international format
    data.append([prepend * 100, prefix, "385Z.", ""])  # National format
    data.append([base_number, prefix, "X.", ""])  # Custom pattern with base number
    data.append([base_number, prefix, "Z.", ""])  # Alternative custom pattern
    data.append([base_number, prefix * 10, "X.", ""])  # Variation with multiplied prefix

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=["prepend", "prefix", "match pattern", "callerid"])

# Save the final CSV file
csv_file_path = "generated_dialplan.csv"
df.to_csv(csv_file_path, index=False, header=True)

print(f"CSV file saved: {csv_file_path}")

# Prevent the script from closing immediately (useful for manual execution)
input("Press Enter to exit...")
