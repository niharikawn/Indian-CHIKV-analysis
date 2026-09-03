# ============================================================
# ADD CHIKV REFERENCE TO REPRESENTATIVE DATASET
# ============================================================

from Bio import SeqIO


# ============================================================
# INPUT FILES
# ============================================================

REFERENCE_FILE = "CHIKV_Reference.fasta"
DATASET_FILE = "CHIKV_CDHIT_representatives.fasta"


# ============================================================
# OUTPUT FILE
# ============================================================

OUTPUT_FILE = "CHIKV_reference_plus_representatives.fasta"


# ============================================================
# READ REFERENCE AND DATASET
# ============================================================

reference = list(
    SeqIO.parse(
        REFERENCE_FILE,
        "fasta"
    )
)

dataset = list(
    SeqIO.parse(
        DATASET_FILE,
        "fasta"
    )
)


# ============================================================
# SAFETY CHECKS
# ============================================================

if len(reference) != 1:

    raise ValueError(
        "Reference FASTA must contain exactly one sequence."
    )


reference_accession = (
    reference[0].id.split("|")[0]
)


# Check that the reference is not already present

for record in dataset:

    accession = record.id.split("|")[0]

    if accession == reference_accession:

        raise ValueError(
            "Reference already exists in the dataset."
        )


# ============================================================
# ADD REFERENCE FIRST
# ============================================================

combined = (
    reference +
    dataset
)


# ============================================================
# WRITE COMBINED FASTA
# ============================================================

SeqIO.write(
    combined,
    OUTPUT_FILE,
    "fasta"
)


# ============================================================
# VERIFY OUTPUT
# ============================================================

check = list(
    SeqIO.parse(
        OUTPUT_FILE,
        "fasta"
    )
)


print("=" * 65)
print("REFERENCE + REPRESENTATIVE DATASET")
print("=" * 65)

print(
    "Reference sequences :",
    len(reference)
)

print(
    "Representative sequences :",
    len(dataset)
)

print(
    "Final sequences :",
    len(check)
)

print("\nFirst sequence:")
print(check[0].description)

print("\n" + "=" * 65)


if (
    len(check) == len(dataset) + 1
    and
    check[0].id.split("|")[0]
    == reference_accession
):

    print("✅ REFERENCE SUCCESSFULLY ADDED")
    print("✅ REFERENCE IS FIRST")

else:

    print("⚠️ REFERENCE CHECK FAILED")


print("=" * 65)
