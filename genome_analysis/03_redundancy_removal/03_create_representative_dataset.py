# ============================================================
# CREATE CD-HIT REPRESENTATIVE DATASET
# Indian CHIKV complete-genome dataset
# ============================================================

import pandas as pd
from Bio import SeqIO


# ============================================================
# INPUT FILES
# ============================================================

EXCEL_FILE = "metadata.xlsx"
FASTA_FILE = "genomes.fasta"
CLSTR_FILE = "CHIKV_CDHIT.clstr"


# ============================================================
# OUTPUT FILES
# ============================================================

FASTA_OUTPUT = "CHIKV_CDHIT_representatives.fasta"
EXCEL_OUTPUT = "CHIKV_CDHIT_representatives.xlsx"
HISTORY_OUTPUT = "CDHIT_redundancy_history.xlsx"


# ============================================================
# READ ORIGINAL EXCEL AND FASTA
# ============================================================

df = pd.read_excel(EXCEL_FILE)

records = list(
    SeqIO.parse(FASTA_FILE, "fasta")
)


# ============================================================
# READ CD-HIT CLUSTER FILE
# ============================================================

clusters = {}
current_cluster = None

with open(CLSTR_FILE, "r") as f:

    for line in f:

        line = line.strip()

        if line.startswith(">Cluster"):

            current_cluster = int(
                line.split()[1]
            )

            clusters[current_cluster] = []

        elif line and ">" in line:

            header = line.split(">", 1)[1]

            header = header.split("...", 1)[0]

            clusters[current_cluster].append(header)


# ============================================================
# IDENTIFY REPRESENTATIVES
# AND REDUNDANT SEQUENCES
# ============================================================

representative_headers = []

redundancy_history = []

for cluster_id, members in clusters.items():

    # CD-HIT places the representative first
    representative = members[0]

    representative_headers.append(
        representative
    )

    # Remaining sequences are redundant
    for redundant in members[1:]:

        redundancy_history.append({
            "Cluster": cluster_id,

            "Removed_Accession":
                redundant.split("|")[0].rsplit("_", 1)[0],

            "Removed_Header":
                redundant,

            "Representative_Accession":
                representative.split("|")[0].rsplit("_", 1)[0],

            "Representative_Header":
                representative,

            "Reason":
                "100% sequence identity by CD-HIT-EST"
        })


# ============================================================
# ACCESSION EXTRACTION
# ============================================================

def get_accession(header):

    accession = header.split("|")[0]

    accession = accession.rsplit("_", 1)[0]

    accession = accession.split(".")[0]

    return accession


representative_accessions = {
    get_accession(header)
    for header in representative_headers
}


# ============================================================
# NORMALIZE EXCEL ACCESSIONS
# ============================================================

df["_Accession_Normalized"] = (
    df["Accession"]
    .astype(str)
    .str.strip()
    .str.replace(
        r"\.\d+$",
        "",
        regex=True
    )
)


# ============================================================
# CREATE REPRESENTATIVE METADATA
# ============================================================

df_representatives = df[
    df["_Accession_Normalized"].isin(
        representative_accessions
    )
].copy()


df_representatives.drop(
    columns=["_Accession_Normalized"],
    inplace=True
)


# ============================================================
# CREATE REPRESENTATIVE FASTA
# ============================================================

records_representatives = []

for record in records:

    accession = record.id.split("|")[0]

    accession = accession.rsplit("_", 1)[0]

    accession = accession.split(".")[0]

    if accession in representative_accessions:

        records_representatives.append(record)


# ============================================================
# WRITE REPRESENTATIVE FASTA
# ============================================================

SeqIO.write(
    records_representatives,
    FASTA_OUTPUT,
    "fasta"
)


# ============================================================
# WRITE REPRESENTATIVE METADATA
# ============================================================

df_representatives.to_excel(
    EXCEL_OUTPUT,
    index=False
)


# ============================================================
# WRITE REDUNDANCY HISTORY
# ============================================================

pd.DataFrame(
    redundancy_history
).to_excel(
    HISTORY_OUTPUT,
    index=False
)


# ============================================================
# FINAL CHECK
# ============================================================

print("=" * 70)
print("CD-HIT REPRESENTATIVE DATASET")
print("=" * 70)

print(
    "Original FASTA records :",
    len(records)
)

print(
    "Original metadata records :",
    len(df)
)

print(
    "\nCD-HIT clusters :",
    len(clusters)
)

print(
    "Representative sequences :",
    len(representative_headers)
)

print(
    "Redundant sequences :",
    len(redundancy_history)
)

print(
    "\nRepresentative FASTA records :",
    len(records_representatives)
)

print(
    "Representative Excel records :",
    len(df_representatives)
)


print("\n" + "=" * 70)
print("OUTPUT FILES")
print("=" * 70)

print(FASTA_OUTPUT)
print(EXCEL_OUTPUT)
print(HISTORY_OUTPUT)


print("\n" + "=" * 70)
print("FINAL CHECK")
print("=" * 70)

if (
    len(records_representatives)
    == len(df_representatives)
    == len(representative_headers)
):

    print(
        "✅ Representative FASTA and metadata "
        "records are consistent."
    )

else:

    print(
        "⚠️ Record-count mismatch — "
        "check the input files and CD-HIT clusters."
    )

print("=" * 70)
