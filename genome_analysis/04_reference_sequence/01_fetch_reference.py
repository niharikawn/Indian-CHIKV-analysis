# ============================================================
# FETCH CHIKV REFERENCE GENOME FROM NCBI
# ============================================================

from Bio import Entrez, SeqIO


# ============================================================
# NCBI SETTINGS
# ============================================================

Entrez.email = "your_email@example.com"

ACCESSION = "NC_004162.2"


# ============================================================
# FETCH REFERENCE
# ============================================================

handle = Entrez.efetch(
    db="nucleotide",
    id=ACCESSION,
    rettype="fasta",
    retmode="text"
)

record = SeqIO.read(
    handle,
    "fasta"
)

handle.close()


# ============================================================
# REPORT
# ============================================================

print("=" * 60)
print("CHIKV REFERENCE SEQUENCE")
print("=" * 60)

print("Accession :", ACCESSION)
print("Length    :", len(record.seq))

print("\nOriginal header:")
print(record.description)

print("=" * 60)
