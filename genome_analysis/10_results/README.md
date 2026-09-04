# Results and Outputs

This directory documents the types of outputs generated during the Indian CHIKV genome-level analysis.

Study-specific result files are not included in this public repository.

## Phylogenetic Analysis

Maximum-likelihood phylogenetic analysis produces a phylogenetic tree representing the evolutionary relationships among the analyzed CHIKV genomes.

Typical outputs include:

- Maximum-likelihood tree
- Bootstrap support values
- SH-aLRT support values
- Model-selection information
- IQ-TREE analysis logs

## Tree Annotation

Phylogenetic trees can be visualized with metadata annotations using iTOL.

The annotation workflow includes:

- Genotype
- Collection year
- State/location

The annotation scripts are provided in:

`../08_annotation/`

## Bayesian Analysis

BEAST analysis produces posterior samples that can be used to investigate the temporal evolutionary dynamics of CHIKV.

Potential outputs include:

- Evolutionary rate estimates
- Time to the most recent common ancestor (tMRCA)
- Population-size trajectories
- Posterior distributions
- MCMC parameter logs
- Effective sample size (ESS) values

## Quality Control

Quality-control steps were performed throughout the workflow to verify:

- Sequence and metadata correspondence
- Sequence identifiers
- Sequence lengths
- Alignment consistency
- Redundancy removal
- Reference sequence inclusion
- Recombination screening

## Public Repository Policy

The following study-specific materials are intentionally excluded from this repository:

- Raw sequence files
- Curated metadata tables
- Accession lists
- Private or in-house sequences
- Restricted-access sequence data
- BEAST XML files
- BEAST log files
- Posterior tree files
- Study-specific numerical results
- Accession-level findings
- Unpublished figures and tables
