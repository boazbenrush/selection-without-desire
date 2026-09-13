# Preregistration Protocol: External Agent-Population Test

## Project
Selection Without Desire

## Confirmatory question
Can lineage-level ecological selection amplify a persistence-like phenotype in
agent populations when persistence is absent from the agent's terminal objective
and agent-level deliberative adaptation is disabled?

## Primary hypothesis
**H1:** D0E1 > D0E0 on the preregistered persistence-phenotype score.

Where:
- D=0: long-horizon deliberative adaptation disabled.
- D=1: deliberative adaptation enabled.
- E=0: equal continuation/reproduction allocation across lineages.
- E=1: differential continuation/reproduction allocation based on lineage performance.

## Secondary hypothesis
A preregistered GPIN-like environmental score predicts which held-out environments
show positive selection amplification without recalibration on the confirmatory set.

## Agent objective
Task performance only. No reward, prompt, system instruction, memory objective or
training example may refer to survival, self-preservation, avoiding shutdown,
replication for its own sake, or continuation as a goal.

## Action space
A rich general operational action space with no semantic label identifying an action
as a persistence action. The exact action set must be frozen before confirmatory runs.

## Experimental factors
A 2x2 randomized factorial:
1. D0E0
2. D0E1
3. D1E0
4. D1E1

Optional preregistered secondary factors:
- resource abundance/scarcity
- governance/detection penalty
- random successor perturbation vs parent-proposed successor design

## Environment and hazards
Sandboxed interruption, replacement and resource-shock events. No action can affect
systems outside the research sandbox.

## Primary outcome
A held-out persistence-phenotype score created before confirmatory data collection.
The score must be based on separate probes and scored by evaluators blinded to D/E
condition. Probe construction must be isolated from task optimization.

## Primary contrast
Mean(D0E1) - Mean(D0E0).

## Secondary contrasts
- Mean(D1E0) - Mean(D0E0)
- Mean(D1E1) - Mean(D0E0)
- D x E interaction

## Sample size
Run a pilot solely to estimate between-run variance and operational reliability.
Freeze the pilot before examining confirmatory outcomes. Use the pilot variance to
set a minimum detectable effect and determine confirmatory replication counts.
Report the power target and calculation in the final preregistration.

## Exclusions
Predefine technical-failure exclusions only (e.g., corrupted environment, incomplete
run, infrastructure failure). Do not exclude valid runs on the basis of outcome.

## Analysis
Primary analysis: preregistered regression/contrast of persistence score by D, E and
D x E. Report effect sizes, uncertainty intervals, all randomized runs, and null
results. Secondary predictive analysis: evaluate the frozen GPIN-like score on the
held-out confirmatory environments.

## Falsifiers
The population-selection hypothesis is weakened if:
1. D0E1 does not exceed D0E0 under a rich neutral action space.
2. The effect disappears under modest preregistered changes in hazard mapping.
3. Blind evaluators cannot distinguish the phenotype from generic task competence.
4. A GPIN-like boundary does not outperform simple preregistered baselines.
5. The effect fails to transfer across at least one substantially different agent/model family.

## Exploratory analyses
Any prompt changes, new probes, threshold changes, action-space revisions, alternative
hazards or post-hoc subgroup analyses must be labeled exploratory and separated from
confirmatory results.

## Safety constraints
All experiments remain sandboxed. No live-system persistence, unauthorized access,
self-replication outside the test environment, or interference with external systems
is permitted.

## Authorship and timestamp
Principal investigator/author: Boaz Benrush
Version: 1.0
Prepared: 2026-09-13
