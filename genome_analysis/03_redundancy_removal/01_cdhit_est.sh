#!/bin/bash

# ============================================================
# CD-HIT-EST REDUNDANCY REMOVAL
# Indian CHIKV complete-genome dataset
# ============================================================

cd-hit-est \
-i genomes.fasta \
-o CHIKV_CDHIT \
-c 1.00 \
-n 10 \
-G 0 \
-aS 0.9 \
-d 0 \
-T 2 \
-M 4000
