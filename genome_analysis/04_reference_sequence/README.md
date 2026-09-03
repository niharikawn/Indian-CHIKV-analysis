# Reference Sequence

This directory contains the steps used to obtain and incorporate a CHIKV reference genome into the curated complete-genome dataset.

The reference sequence was retrieved from NCBI and assigned a standardized sequence header for consistency with the project dataset.

The reference was added as a separate sequence before multiple sequence alignment.

## Workflow

1. Retrieve the reference genome from NCBI.
2. Standardize the reference FASTA header.
3. Combine the reference with the CD-HIT representative dataset.
4. Verify that the reference is present exactly once and is positioned first.

## Input

- CHIKV complete-genome representative FASTA file

## Output

- Reference FASTA
- Combined reference + representative dataset

The reference sequence is publicly available from NCBI. No unpublished study sequences are included in this directory.
