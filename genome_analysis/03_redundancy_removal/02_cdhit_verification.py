# ============================================================
# CD-HIT-EST CLUSTER VERIFICATION
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
# READ METADATA AND ORIGINAL FASTA
# ============================================================

df = pd.read_excel(EXCEL_FILE)

records = list(
    SeqIO.parse(FASTA_FILE, "fasta")
)


# ============================================================
# READ CD-HIT CLUSTERS
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
# IDENTIFY REPRESENTATIVES AND REDUNDANT SEQUENCES
# ============================================================

representative_headers = []
redundant_headers = []

for cluster_id, members in clusters.items():

    # CD-HIT marks the first member as the representative
    representative = members[0]

    representative_headers.append(
        representative
    )

    # Remaining members are redundant
    for member in members[1:]:

        redundant_headers.append(
            member
        )


# ============================================================
# NORMALIZE ACCESSION
# ============================================================

def get_accession(header):

    accession = header.split("|")[0]

    # Remove FASTA suffix such as _1 or _2
    accession = accession.rsplit("_", 1)[0]

    # Remove version suffix such as .1
    accession = accession.split(".")[0]

    return accession


representative_accessions = {
    get_accession(header)
    for header in representative_headers
}

redundant_accessions = {
    get_accession(header)
    for header in redundant_headers
}


# ============================================================
# METADATA ACCESSIONS
# ============================================================

metadata_accessions = {
    str(accession)
    .strip()
    .split(".")[0]
    for accession in df["Accession"]
}


# ============================================================
# VERIFICATION REPORT
# ============================================================

print("=" * 70)
print("CD-HIT-EST REPRESENTATIVE VERIFICATION")
print("=" * 70)

print("\nOriginal metadata records :", len(df))
print("Original FASTA records   :", len(records))

print("\nCD-HIT clusters           :", len(clusters))
print("Representatives           :", len(representative_headers))
print("Redundant sequences       :", len(redundant_headers))

print(
    "\nRepresentatives found in metadata :",
    len(
        representative_accessions &
        metadata_accessions
    )
)

print(
    "Representatives missing from metadata :",
    len(
        representative_accessions -
        metadata_accessions
    )
)

print(
    "\nRedundant sequences found in metadata :",
    len(
        redundant_accessions &
        metadata_accessions
    )
)

print(
    "Redundant sequences missing from metadata :",
    len(
        redundant_accessions -
        metadata_accessions
    )
)


# ============================================================
# FINAL VERIFICATION
# ============================================================

missing_representatives = (
    representative_accessions -
    metadata_accessions
)

missing_redundant = (
    redundant_accessions -
    metadata_accessions
)


print("\n" + "=" * 70)
print("FINAL VERIFICATION")
print("=" * 70)

if not missing_representatives and not missing_redundant:

    print("✅ All CD-HIT representatives are present in metadata.")
    print("✅ All redundant sequences are present in metadata.")
    print("✅ CD-HIT cluster verification passed.")

else:

    print("⚠️ Verification failed.")
    print("Check FASTA and metadata identifiers before proceeding.")


print("=" * 70)
