#!/bin/bash

# ============================================================
# MAFFT MULTIPLE SEQUENCE ALIGNMENT
# Indian CHIKV complete-genome dataset
# ============================================================

mafft \
--6merpair \
--maxiterate 0 \
--reorder \
--adjustdirection \
--thread 8 \
reference_plus_representatives.fasta \
> CHIKV_MAFFT_alignment.fasta
