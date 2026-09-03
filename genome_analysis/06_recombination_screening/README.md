# Recombination Screening

This directory documents the recombination screening performed on the CHIKV complete-genome alignment before downstream phylogenetic analysis.

Recombination screening was performed using RDP5.

## Workflow

1. The multiple sequence alignment generated using MAFFT was used as input.
2. The alignment was screened for evidence of recombination using RDP5.
3. Sequences identified as recombinant were reviewed.
4. Confirmed recombinant sequences were excluded from the dataset used for subsequent phylogenetic analysis.

## Tool

**RDP5 — Recombination Detection Program**

RDP5 provides multiple recombination-detection methods for identifying potential recombinant sequences and recombination breakpoints.

## Input

- MAFFT-aligned CHIKV complete-genome sequences

## Output

- Recombination screening results
- Curated alignment after removal of confirmed recombinant sequences

## Note

RDP5 was operated through its graphical user interface. Therefore, no command-line script is provided for this step.

The accession numbers of sequences identified as recombinant and the resulting study-specific screening results are not included in this public repository.
