# Bayesian Evolutionary Analysis

This directory documents the Bayesian evolutionary analysis performed on the Indian CHIKV complete-genome dataset using BEAST.

The analysis incorporated sampling dates to investigate the temporal evolutionary dynamics of CHIKV.

## Workflow

Phylogenetic alignment + sampling dates
↓
Temporal signal assessment using TempEst
↓
Molecular clock specification
↓
Bayesian demographic model specification
↓
BEAST XML generation
↓
MCMC analysis
↓
Convergence assessment
↓
Posterior evolutionary estimates

## Temporal Analysis

TempEst was used to assess the temporal signal in the dataset.

The regression slope obtained from the temporal analysis was used as an informed initial value for the molecular clock mean parameter (`ucld.mean`).

## Molecular Clock

An Uncorrelated Relaxed Clock (UCLD) was used to allow evolutionary rates to vary among branches.

The analysis explored different relaxed-rate distributions, including:

- Lognormal
- Gamma
- Exponential

## Tree Prior

A GMRF Bayesian SkyGrid coalescent model was used as the demographic prior.

The SkyGrid model allows effective population size to vary through time.

## Starting Tree

A random starting tree was used for the MCMC analysis.

## MCMC

The Bayesian analysis was performed using Markov Chain Monte Carlo (MCMC).

The initial analysis used a chain length of `10^8` states.

The initial run did not achieve convergence, so the analysis was subsequently restarted using a longer chain of `10^9` states.

## Marginal Likelihood Estimation

Path sampling / stepping-stone sampling was used for marginal likelihood estimation.

The configuration included:

- Number of path steps: 100
- Path-step distribution: Beta
- Log-likelihood sampling interval: 10,000

## Input

- Curated CHIKV complete-genome alignment
- Sampling-date information

## Output

BEAST analysis produces posterior samples and associated log files that can be used to estimate:

- Evolutionary rates
- Time to the most recent common ancestor (tMRCA)
- Population dynamics
- Posterior uncertainty
- MCMC convergence statistics

Study-specific BEAST XML files, log files, posterior trees, and numerical results are not included in this public repository.
