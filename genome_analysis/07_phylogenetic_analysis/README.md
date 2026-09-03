# Phylogenetic Analysis

This directory contains the steps used to reconstruct the maximum-likelihood phylogenetic tree of the curated CHIKV complete-genome dataset.

Phylogenetic inference was performed using IQ-TREE.

The alignment used for phylogenetic analysis was the curated multiple sequence alignment after recombination screening.

## Method

Maximum-likelihood phylogenetic inference was performed using IQ-TREE.

Branch support was assessed using:

- Ultrafast bootstrap: 1000 replicates
- SH-aLRT: 1000 replicates

The nucleotide substitution model was specified for the analysis.

## Input

- Curated CHIKV complete-genome alignment following recombination screening

## Output

IQ-TREE generates:

- Maximum-likelihood phylogenetic tree
- Tree with branch-support values
- Model and analysis log files

Study-specific trees and unpublished results are not included in this repository.
