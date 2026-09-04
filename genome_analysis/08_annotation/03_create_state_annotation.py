# ============================================================
# iTOL STATE ANNOTATION
# Indian CHIKV complete-genome dataset
# ============================================================

import pandas as pd

# Input metadata file
METADATA_FILE = "Genome_Metadata_Curated_Final.xlsx"

# Read metadata
df = pd.read_excel(METADATA_FILE)

# Remove entries without state information
df = df[df["State"].notna()].copy()

# Convert state values to strings
df["State"] = df["State"].astype(str)

# Generate a color for each unique state
# Replace these with your preferred colors if needed.
base_colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf"
]

states = sorted(df["State"].unique())

state_colors = {
    state: base_colors[i % len(base_colors)]
    for i, state in enumerate(states)
}

# Create iTOL color-strip annotation
with open("iTOL_State.txt", "w") as f:

    f.write("DATASET_COLORSTRIP\n")
    f.write("SEPARATOR TAB\n")
    f.write("DATASET_LABEL\tState\n")
    f.write("COLOR\t#000000\n")
    f.write("LEGEND_TITLE\tState\n")

    f.write(
        "LEGEND_SHAPES\t"
        + "\t".join(["1"] * len(states))
        + "\n"
    )

    f.write(
        "LEGEND_COLORS\t"
        + "\t".join(state_colors[state] for state in states)
        + "\n"
    )

    f.write(
        "LEGEND_LABELS\t"
        + "\t".join(states)
        + "\n"
    )

    f.write("DATA\n")

    for _, row in df.iterrows():

        seq_id = str(row["Sequence_ID"])
        state = row["State"]

        f.write(
            f"{seq_id}\t{state_colors[state]}\t{state}\n"
        )

print("State annotation created:")
print("  iTOL_State.txt")
