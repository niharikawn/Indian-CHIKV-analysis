# ============================================================
# iTOL YEAR ANNOTATION
# Indian CHIKV complete-genome dataset
# ============================================================

import pandas as pd

# Input metadata file
METADATA_FILE = "Genome_Metadata_Curated_Final.xlsx"

# Read metadata
df = pd.read_excel(METADATA_FILE)

# Keep records with valid collection dates
df = df[df["Standardized_Date"].notna()].copy()

# Create collection year
df["Collection_Year"] = pd.to_datetime(
    df["Standardized_Date"]
).dt.year

# Write iTOL annotation file
with open("iTOL_Year.txt", "w") as f:

    f.write("DATASET_SIMPLEBAR\n")
    f.write("SEPARATOR TAB\n")
    f.write("DATASET_LABEL\tCollection Year\n")
    f.write("COLOR\t#000000\n")
    f.write("DATA\n")

    for _, row in df.iterrows():

        seq_id = str(row["Sequence_ID"])
        year = int(row["Collection_Year"])

        f.write(
            f"{seq_id}\t{year}\n"
        )

print("Year annotation created:")
print("  iTOL_Year.txt")
