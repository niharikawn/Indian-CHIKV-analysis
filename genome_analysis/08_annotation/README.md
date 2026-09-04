# Tree Annotation

This directory contains the steps used to generate annotation files for visualization of the CHIKV phylogenetic tree in iTOL.

The annotation files were generated from curated metadata using `Sequence_ID` as the identifier for matching metadata entries to phylogenetic tree tips.

## Annotations

The workflow generated separate annotation files for:

- Genotype
- Collection year
- State/location

The genotype annotation was generated as an iTOL `DATASET_COLORSTRIP` dataset.

## Workflow

Curated metadata
↓
Read `Sequence_ID` and annotation information
↓
Match metadata identifiers with phylogenetic tree tip identifiers
↓
Generate iTOL annotation files
↓
Visualize annotations on the phylogenetic tree

## Input

- Curated metadata table

## Output

- iTOL genotype annotation file
- iTOL year annotation file
- iTOL state annotation file

## Note

These annotation files are intended for phylogenetic tree visualization in iTOL and are not inputs for BEAST analysis.

Study-specific metadata, accession lists, and unpublished annotation results are not included in this public repository.
