#!/bin/bash

# ============================================================
# IQ-TREE MAXIMUM-LIKELIHOOD PHYLOGENETIC ANALYSIS
# Indian CHIKV complete-genome dataset
# ============================================================

iqtree2 \
-s curated_alignment.fasta \
-m MFP \
-nt 16 \
-bb 1000 \
-alrt 1000
