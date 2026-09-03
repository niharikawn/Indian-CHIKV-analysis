# Multiple Sequence Alignment

This directory contains the steps used to generate and assess multiple sequence alignments of CHIKV complete-genome sequences.

Multiple sequence alignment was performed using MAFFT.

The alignment was subsequently checked for sequence count, unique sequence identifiers, aligned sequence length, and presence of the reference sequence.

## Method

MAFFT was run using:

- `--6merpair`
- `--maxiterate 0`
- `--reorder`
- `--adjustdirection`
- `--thread 8`

## Input

- Reference + representative CHIKV complete-genome FASTA

## Output

- Multiple sequence alignment in FASTA format
- Alignment quality-control report

The alignment files containing study sequences are not included in this repository.
