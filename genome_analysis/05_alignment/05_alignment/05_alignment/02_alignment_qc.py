# ============================================================
# MAFFT ALIGNMENT QUALITY CONTROL
# Indian CHIKV complete-genome dataset
# ============================================================

from Bio import SeqIO


# ============================================================
# INPUT
# ============================================================

ALIGNMENT_FILE = "CHIKV_MAFFT_alignment.fasta"


# ============================================================
# READ ALIGNMENT
# ============================================================

records = list(
    SeqIO.parse(
        ALIGNMENT_FILE,
        "fasta"
    )
)


# ============================================================
# BASIC ALIGNMENT INFORMATION
# ============================================================

lengths = [
    len(record.seq)
    for record in records
]

headers = [
    record.description.strip()
    for record in records
]


# ============================================================
# REFERENCE CHECK
# ============================================================

reference = [
    record
    for record in records
    if record.description.startswith("NC_004162")
]


# ============================================================
# REPORT
# ============================================================

print("=" * 70)
print("MAFFT ALIGNMENT QUALITY CONTROL")
print("=" * 70)

print(
    "Aligned sequences :",
    len(records)
)

print(
    "Unique headers    :",
    len(set(headers))
)

print(
    "Minimum length    :",
    min(lengths)
)

print(
    "Maximum length    :",
    max(lengths)
)

print(
    "Unique lengths    :",
    len(set(lengths))
)

print(
    "Reference present :",
    len(reference)
)


# ============================================================
# ALIGNMENT QC
# ============================================================

if (
    len(records) > 0
    and len(set(headers)) == len(records)
    and len(set(lengths)) == 1
    and len(reference) == 1
):

    print("\n✅ MAFFT ALIGNMENT QC PASSED")

    print(
        "✅ All aligned sequences have "
        "the same alignment length."
    )

    print(
        "✅ Sequence identifiers are unique."
    )

    print(
        "✅ Reference sequence is present."
    )

else:

    print("\n⚠️ ALIGNMENT QC NEEDS REVIEW")


print("=" * 70)
