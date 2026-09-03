# Data recovery and organization
# Indian CHIKV complete-genome dataset

# Required libraries
import pandas as pd
from Bio import SeqIO

# Input files
metadata_file = "metadata.csv"
sequence_file = "sequences.fasta"

# Read metadata
metadata = pd.read_csv(metadata_file)

# Read recovered genome sequences
sequences = list(SeqIO.parse(sequence_file, "fasta"))

# Display basic information
print("Number of metadata records:", len(metadata))
print("Number of genome sequences:", len(sequences))

# Display sequence identifiers
sequence_ids = [record.id for record in sequences]

print("Data recovery completed.")
