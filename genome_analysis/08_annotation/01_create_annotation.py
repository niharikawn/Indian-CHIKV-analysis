# ============================================================
# iTOL TREE ANNOTATION
# Indian CHIKV complete-genome dataset
# ============================================================

import pandas as pd


# ------------------------------------------------------------
# Input
# ------------------------------------------------------------

METADATA_FILE = "Genome_Metadata_Curated_Final.xlsx"


# ------------------------------------------------------------
# Read curated metadata
# ------------------------------------------------------------

df = pd.read_excel(METADATA_FILE)

print("Metadata records:", len(df))


# ------------------------------------------------------------
# Keep records with standardized collection dates
# ------------------------------------------------------------

df = df[df["Standardized_Date"].notna()].copy()


# ------------------------------------------------------------
# Genotype annotation
# ------------------------------------------------------------

genotype_colors = {
    "Asian": "#1f77b4",
    "ECSA": "#ff7f0e",
    "ECSA_IOL": "#2ca02c",
    "West_African": "#d62728"
}


with open("iTOL_Genotype.txt", "w") as f:

    f.write("DATASET_COLORSTRIP\n")
    f.write("SEPARATOR TAB\n")
    f.write("DATASET_LABEL\tCHIKV Genotype\n")
    f.write("COLOR\t#000000\n")
    f.write("LEGEND_TITLE\tGenotype\n")

    f.write(
        "LEGEND_SHAPES\t"
        + "\t".join(["1"] * len(genotype_colors))
        + "\n"
    )

    f.write(
        "LEGEND_COLORS\t"
        + "\t".join(genotype_colors.values())
        + "\n"
    )

    f.write(
        "LEGEND_LABELS\t"
        + "\t".join(genotype_colors.keys())
        + "\n"
    )

    f.write("DATA\n")

    for _, row in df.iterrows():

        seq_id = str(row["Sequence_ID"])
        genotype = str(row["Genotype"])

        if genotype in genotype_colors:

            f.write(
                f"{seq_id}\t{genotype_colors[genotype]}\t{genotype}\n"
            )


print("Genotype annotation created:")
print("  iTOL_Genotype.txt")
