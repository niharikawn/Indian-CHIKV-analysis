# ============================================================
# FASTA ↔ METADATA QUALITY CONTROL
# Indian CHIKV complete-genome dataset
# ============================================================

import pandas as pd
from Bio import SeqIO


# ============================================================
# INPUT FILES
# ============================================================

EXCEL_FILE = "metadata.xlsx"
FASTA_FILE = "genomes.fasta"


# ============================================================
# READ METADATA
# ============================================================

metadata = pd.read_excel(EXCEL_FILE)

print("=" * 65)
print("BASIC DATA CHECK")
print("=" * 65)

print("Metadata records :", len(metadata))


# ============================================================
# READ FASTA
# ============================================================

records = list(
    SeqIO.parse(FASTA_FILE, "fasta")
)

print("FASTA records    :", len(records))


# ============================================================
# NORMALIZE ACCESSION
# ============================================================

def normalize_accession(accession):

    accession = str(accession).strip()

    # Remove version suffix such as .1 or .2
    accession = accession.split(".")[0]

    return accession


# ============================================================
# EXTRACT ACCESSIONS FROM METADATA
# ============================================================

metadata["Accession_Normalized"] = (
    metadata["Accession"]
    .apply(normalize_accession)
)


# ============================================================
# EXTRACT ACCESSIONS FROM FASTA
# ============================================================

fasta_data = []

for record in records:

    header = record.id.strip()

    # Accession is the first field of the FASTA header
    accession = header.split("|")[0]

    # Remove FASTA suffix such as _1 or _2
    accession = accession.rsplit("_", 1)[0]

    accession = normalize_accession(accession)

    sequence = str(record.seq).upper()

    length = len(sequence)

    n_count = sequence.count("N")

    n_percent = (
        (n_count / length) * 100
        if length > 0
        else 0
    )

    fasta_data.append({
        "Accession_Normalized": accession,
        "FASTA_Header": header,
        "FASTA_Length_bp": length,
        "FASTA_N_Count": n_count,
        "FASTA_N_Percent": n_percent
    })


fasta_df = pd.DataFrame(fasta_data)


# ============================================================
# ACCESSION MATCH CHECK
# ============================================================

metadata_accessions = set(
    metadata["Accession_Normalized"]
)

fasta_accessions = set(
    fasta_df["Accession_Normalized"]
)

common = (
    metadata_accessions &
    fasta_accessions
)

only_metadata = (
    metadata_accessions -
    fasta_accessions
)

only_fasta = (
    fasta_accessions -
    metadata_accessions
)


print("\n" + "=" * 65)
print("ACCESSION MATCH CHECK")
print("=" * 65)

print("Matching accessions :", len(common))
print("Only in metadata    :", len(only_metadata))
print("Only in FASTA       :", len(only_fasta))


if only_metadata:
    print("\n⚠️ Accessions present only in metadata.")

if only_fasta:
    print("\n⚠️ Accessions present only in FASTA.")


# ============================================================
# MERGE METADATA WITH FASTA QC VALUES
# ============================================================

check = metadata.merge(
    fasta_df,
    on="Accession_Normalized",
    how="left",
    validate="one_to_one"
)


# ============================================================
# CALCULATE QC DIFFERENCES
# ============================================================

check["Length_Difference"] = (
    check["FASTA_Length_bp"] -
    check["Genome_Length_bp"]
)

check["N_Count_Difference"] = (
    check["FASTA_N_Count"] -
    check["N_Count"]
)

check["N_Percent_Difference"] = (
    check["FASTA_N_Percent"] -
    check["N_Percent"]
)


# ============================================================
# IDENTIFY MISMATCHES
# ============================================================

length_mismatch = check[
    check["Length_Difference"].abs() > 0
]

n_count_mismatch = check[
    check["N_Count_Difference"].abs() > 0
]

n_percent_mismatch = check[
    check["N_Percent_Difference"].abs() > 0.01
]


# ============================================================
# QC SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("FASTA ↔ METADATA QC COMPARISON")
print("=" * 65)

print(
    "Genome length mismatches :",
    len(length_mismatch)
)

print(
    "N-count mismatches       :",
    len(n_count_mismatch)
)

print(
    "N-percent mismatches     :",
    len(n_percent_mismatch)
)


# ============================================================
# SHOW QC MISMATCHES
# ============================================================

if len(length_mismatch) > 0:

    print("\nGENOME LENGTH MISMATCHES")

    print(
        length_mismatch[
            [
                "Accession_Normalized",
                "Genome_Length_bp",
                "FASTA_Length_bp",
                "Length_Difference"
            ]
        ].to_string(index=False)
    )


if len(n_count_mismatch) > 0:

    print("\nN-COUNT MISMATCHES")

    print(
        n_count_mismatch[
            [
                "Accession_Normalized",
                "N_Count",
                "FASTA_N_Count",
                "N_Count_Difference"
            ]
        ].to_string(index=False)
    )


if len(n_percent_mismatch) > 0:

    print("\nN-PERCENT MISMATCHES")

    print(
        n_percent_mismatch[
            [
                "Accession_Normalized",
                "N_Percent",
                "FASTA_N_Percent",
                "N_Percent_Difference"
            ]
        ].to_string(index=False)
    )


# ============================================================
# HANDLE MISSING METADATA VALUES
# ============================================================

if "Genotype" in metadata.columns:

    metadata["Genotype"] = metadata["Genotype"].apply(
        lambda x:
        "NA"
        if pd.isna(x) or
        str(x).strip().lower() in ["nan", "", "none"]
        else str(x).strip()
    )


if "Collection_Date" in metadata.columns:

    metadata["Collection_Date"] = metadata[
        "Collection_Date"
    ].apply(
        lambda x:
        "NA"
        if pd.isna(x) or
        str(x).strip().lower() in ["nan", "", "none"]
        else str(x).strip()
    )


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("DATA CURATION QC COMPLETE")
print("=" * 65)

print(
    "The FASTA sequences were checked against",
    "their corresponding metadata."
)

print(
    "Genome length, ambiguous nucleotide content,",
    "and metadata consistency were evaluated."
)

print("=" * 65)
