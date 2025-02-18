import pandas as pd

# Define the starting values
max_prepend = 32  # Goes up to 32, with 10 -> 97, 20 -> 98, 30 -> 99
min_prefix = 540  # Starts from 540
max_prefix = 592  # Goes up to 592
match_patterns = ["00385Z.", "385Z.", "X.", "Z.", "X."]

# Adjust specific prepend values
def adjust_prepend(prepend):
    return {10: 97, 20: 98, 30: 99}.get(prepend, prepend)

# Generate the data
data = []
for original_prepend in range(1, max_prepend + 1):
    prepend = adjust_prepend(original_prepend)
    prefix = min_prefix + prepend  # Start from 541 and go up to 592
    base_number = prepend * 100000 + 385  # Base number for match pattern

    data.append([prepend, prefix, "00385Z.", ""])
    data.append([prepend * 100, prefix, "385Z.", ""])
    data.append([base_number, prefix, "X.", ""])
    data.append([base_number, prefix, "Z.", ""])
    data.append([base_number, prefix * 10, "X.", ""])

# Create DataFrame
df = pd.DataFrame(data, columns=["prepend", "prefix", "match pattern", "callerid"])

# Save the final CSV file
csv_file_path = "generated_dialplan.csv"
df.to_csv(csv_file_path, index=False, header=True)

print(f"CSV file saved: {csv_file_path}")

# Prevent the script from closing immediately
input("Press Enter to exit...")
