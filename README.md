# Selection Without Desire

**Eco-Evolutionary Emergence of Persistence in Resource-Constrained Self-Designing AI Populations**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22730599.svg)](https://doi.org/10.5281/zenodo.22730599)

**Author:** Boaz Benrush  
**Affiliation:** Independent Researcher  
**ORCID:** [0009-0008-6200-1523](https://orcid.org/0009-0008-6200-1523)  
**Version:** 1.0.0  
**Release date:** 2026-09-13  
**Zenodo DOI:** [10.5281/zenodo.22730599](https://doi.org/10.5281/zenodo.22730599)

## Overview

This repository accompanies the research manuscript **Selection Without Desire**. The work studies a population-level mechanism distinct from agent-level instrumental self-preservation:

> Lineage-level selection can, in principle, amplify a costly persistence phenotype even when persistence is absent from the agent's terminal objective.

The framework introduces the **Generalized Persistence Invasion Number (GPIN)** and a mechanism-discrimination design separating:

- **D:** agent-level deliberative adaptation
- **E:** lineage-level ecological selection

The primary future empirical hypothesis is **D0E1 > D0E0** under a neutral action space and held-out persistence probes.

## What the work does not claim

This release does **not** claim that present-day frontier AI systems already exhibit population-level self-preservation, does not estimate the probability of loss of control, and does not interpret synthetic simulation frequencies as probabilities about the real world.

The reported simulations are **internal model evidence**. External empirical validation remains to be performed.

## Repository structure

- `paper/Selection_Without_Desire_v1.0.pdf` — canonical manuscript matching the Zenodo v1.0 deposit
- `paper/Selection_Without_Desire_v1.0.docx` — editable manuscript source
- `supplement/Selection_Without_Desire_Supplementary_Model_v1.0.xlsx` — analytical model and synthetic results workbook
- `code/simulation_model.py` — clean implementation of the synthetic eco-evolutionary model
- `code/REPRODUCIBILITY.md` — evidence levels and reproduction notes
- `code/requirements.txt` — Python dependencies
- `data/` — canonical synthetic outputs reported in the manuscript
- `PREREGISTRATION_OSF.md` — preregistration-ready external agent-population experiment
- `policy/` — policy-facing interpretation
- `CITATION.cff` — machine-readable citation metadata
- `DEPOSIT_METADATA.json` — release metadata
- `SHA256SUMS.txt` — SHA-256 fingerprints for provenance
- `docs/` — dissemination and impact-tracking materials

## Reproducibility

The repository distinguishes three evidence levels:

1. **Numerical verification** — checks that implementation and analytical expressions agree.
2. **Synthetic held-out prediction** — evaluates GPIN on unseen synthetic environments generated from the same structural model family.
3. **External empirical validation** — not yet performed.

The supplied Python script includes a smoke test. The canonical CSV outputs under `data/` contain the reported synthetic experiment outputs, including the 2×2 mechanism-discrimination experiment and the 300-environment GPIN holdout evaluation.

## Canonical citation

Benrush, B. (2026). *Selection Without Desire: Eco-Evolutionary Emergence of Persistence in Resource-Constrained Self-Designing AI Populations* (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.22730599

## Attribution and AI assistance

Boaz Benrush is the human author and bears responsibility for the research. Generative AI tools, principally OpenAI ChatGPT, were used under the author's direction for formalization, simulation implementation, drafting, editing, visualization, and document production. The AI system is not an author.

## License

Except where otherwise noted, the manuscript, explanatory research materials, data, and research implementation in this v1.0 repository are released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See `LICENSE_CC_BY_4.0.txt`.

## Version integrity

The canonical citable public deposit is the Zenodo record above. Future substantive changes should be released as a new version rather than silently replacing v1.0.0.
