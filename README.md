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

- `paper/README.md` — pointer to the DOI-backed canonical manuscript
- `supplement/README.md` — pointer to the DOI-backed analytical workbook
- `code/simulation_model.py` — clean implementation of the synthetic eco-evolutionary model
- `code/REPRODUCIBILITY.md` — evidence levels and reproduction notes
- `code/requirements.txt` — Python dependencies
- `data/` — compact reported summary outputs plus a pointer to the complete DOI-backed raw-data archive
- `PREREGISTRATION_OSF.md` — preregistration-ready external agent-population experiment
- `policy/README.md` — policy-facing interpretation and archive pointer
- `CITATION.cff` — machine-readable citation metadata
- `DEPOSIT_METADATA.json` — public release metadata
- `docs/OUTREACH_PLAN.md` — staged dissemination and credit plan
- `docs/IMPACT_TRACKING.md` — tracking template for citation, reuse, policy uptake, and derivatives

## Reproducibility

The repository distinguishes three evidence levels:

1. **Numerical verification** — checks that implementation and analytical expressions agree.
2. **Synthetic held-out prediction** — evaluates GPIN on unseen synthetic environments generated from the same structural model family.
3. **External empirical validation** — not yet performed.

The supplied Python script includes a smoke test. Compact reported summaries are included directly under `data/`; the complete raw synthetic outputs and supplementary workbook remain frozen in the Zenodo v1.0 publication package so the DOI-backed record is the authoritative snapshot.

## Canonical citation

Benrush, B. (2026). *Selection Without Desire: Eco-Evolutionary Emergence of Persistence in Resource-Constrained Self-Designing AI Populations* (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.22730599

## Attribution and AI assistance

Boaz Benrush is the human author and bears responsibility for the research. Generative AI tools, principally OpenAI ChatGPT, were used under the author's direction for formalization, simulation implementation, drafting, editing, visualization, and document production. The AI system is not an author.

## License

This repository follows the license of the canonical Zenodo v1.0 record: **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See `LICENSE.md`.

## Version integrity

The canonical citable public deposit is the Zenodo record above. Future substantive changes should be released as a new version rather than silently replacing v1.0.0.
