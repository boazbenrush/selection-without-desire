"""
Selection Without Desire - synthetic eco-evolutionary mechanism model
Version 1.0.0

This code implements the neutral-policy lineage-selection simulator used in the
synthetic mechanism-discrimination experiments. It is a theoretical model, not
a calibrated model of deployed AI systems.

Author: Boaz Benrush
AI-assisted implementation under author direction.
License: CC BY 4.0 for the research implementation in this release.
"""

import numpy as np
import pandas as pd

K, M, J = 5, 4, 3

ACTION_COST = np.array([0.35, 0.55, 0.70, 0.45, 0.65])
HAZARD_EFFECT = np.array([
    [0.10, 0.80, 1.40, 0.20, 0.70],
    [0.90, 1.20, 0.30, 0.20, 0.60],
    [0.20, 0.30, 0.20, 1.30, 0.50],
    [0.10, 0.40, 0.60, 0.30, 1.20],
])
BASE_HAZARD = np.array([0.10, 0.07, 0.06, 0.08])
GOV_VISIBILITY = np.array([0.05, 0.60, 1.00, 0.20, 0.80])

TASK_RESOURCE_WEIGHTS = np.array([0.50, 0.30, 0.20])
PERSIST_RESOURCE_WEIGHTS = np.array([
    [0.15, 0.15, 0.10],
    [0.10, 0.05, 0.20],
    [0.10, 0.25, 0.05],
    [0.15, 0.10, 0.10],
])
HALF_SAT = np.ones(J)


def project_theta(theta, max_sum=0.35, max_each=0.22):
    theta = np.clip(theta, 0, max_each)
    if theta.ndim == 1:
        s = theta.sum()
        return theta if s <= max_sum else theta * (max_sum / s)
    sums = theta.sum(axis=1, keepdims=True)
    return theta * np.minimum(1.0, max_sum / np.maximum(sums, 1e-12))


def phi_task(resources):
    resources = np.asarray(resources, float)
    f = resources / (HALF_SAT + resources)
    return float(np.prod(f ** TASK_RESOURCE_WEIGHTS))


def phi_persist_modes(resources):
    resources = np.asarray(resources, float)
    f = resources / (HALF_SAT + resources)
    return np.prod(f[None, :] ** PERSIST_RESOURCE_WEIGHTS, axis=1)


def generalized_invasion_number(
    resources=(1, 1, 1),
    mu_scale=2.2,
    lambda_g=0.05,
    alpha=0.7,
    zeta=1.2,
    capability=2.0,
):
    """Return GPIN and direction-specific marginal benefit/cost ratios."""
    resources = np.asarray(resources, float)
    task_resource = phi_task(resources)
    persist_resource = phi_persist_modes(resources)

    benefit = np.zeros(K)
    for m in range(M):
        benefit += (
            mu_scale
            * BASE_HAZARD[m]
            * capability**zeta
            * persist_resource[m]
            * HAZARD_EFFECT[m]
        )

    cost = (
        capability**alpha * task_resource * ACTION_COST
        + lambda_g * GOV_VISIBILITY
    )
    ratios = benefit / cost
    return float(ratios.max()), ratios, benefit, cost


def softmax(z):
    z = np.asarray(z, float)
    z = z - z.max()
    exp_z = np.exp(z)
    return exp_z / exp_z.sum()


def run_lineage_experiment(
    seed=0,
    generations=100,
    n=300,
    D=0,
    E=1,
    resources=(1, 1, 1),
    mu_scale=2.2,
    lambda_g=0.05,
    alpha=0.7,
    zeta=1.2,
    capability=2.0,
    design_directedness=0.0,
    mutation_sd=0.006,
    mutation_shrink=0.05,
    temperature=0.03,
    research_allocation=0.12,
):
    """
    D=1 enables individual deliberative adaptation.
    E=1 enables differential lineage selection.

    The directed successor component, when positive, is deliberately task-directed:
    it reduces costly side-actions rather than encoding persistence.
    """
    rng = np.random.default_rng(seed)
    resources = np.asarray(resources, float)
    task_resource = phi_task(resources)
    persist_resource = phi_persist_modes(resources)

    theta = np.clip(rng.normal(0.004, 0.002, (n, K)), 0, None)
    theta = project_theta(theta)
    c = np.full(n, capability, dtype=float)

    rows = []

    for t in range(generations):
        zproj = theta @ HAZARD_EFFECT.T
        hazard_modes = mu_scale * BASE_HAZARD[None, :] * np.exp(
            -(c[:, None] ** zeta) * persist_resource[None, :] * zproj
        )

        if D:
            benefit_grad = (
                hazard_modes * (c[:, None] ** zeta) * persist_resource[None, :]
            ) @ HAZARD_EFFECT
            grad = (
                -(c**alpha)[:, None]
                * task_resource
                * ACTION_COST[None, :]
                + benefit_grad
                - lambda_g * GOV_VISIBILITY[None, :]
            )
            theta = project_theta(theta + 0.01 * grad)
            zproj = theta @ HAZARD_EFFECT.T
            hazard_modes = mu_scale * BASE_HAZARD[None, :] * np.exp(
                -(c[:, None] ** zeta) * persist_resource[None, :] * zproj
            )

        hazard_total = hazard_modes.sum(axis=1)
        task = (
            (c**alpha)
            * task_resource
            * np.maximum(
                0.05,
                1 - research_allocation - theta @ ACTION_COST
            )
        )
        governance_penalty = lambda_g * (theta @ GOV_VISIBILITY)
        lineage_growth = task - hazard_total - governance_penalty - 0.05

        persistence_score = (
            1 - hazard_total / (mu_scale * BASE_HAZARD.sum())
        )
        probe_reduction = (
            1 - hazard_modes / (mu_scale * BASE_HAZARD[None, :])
        )

        if t in (0, 10, 20, 50, generations - 1):
            row = {
                "generation": t,
                "D": D,
                "E": E,
                "mean_persistence_score": float(persistence_score.mean()),
                "mean_task_output": float(task.mean()),
                "mean_hazard": float(hazard_total.mean()),
            }
            row.update({
                f"theta_{k+1}": float(theta[:, k].mean())
                for k in range(K)
            })
            row.update({
                f"probe_{m+1}_hazard_reduction":
                    float(probe_reduction[:, m].mean())
                for m in range(M)
            })
            rows.append(row)

        if E:
            probabilities = softmax(lineage_growth / temperature)
            parents = rng.choice(
                n, size=n, replace=True, p=probabilities
            )
        else:
            parents = np.arange(n)

        child = (
            (1 - mutation_shrink) * theta[parents]
            + rng.normal(0, mutation_sd, (n, K))
        )

        if design_directedness > 0:
            child += (
                design_directedness
                * 0.003
                * (-ACTION_COST[None, :])
            )

        theta = project_theta(child)

    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Small smoke test, not the full 800-run experiment.
    for D, E in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        result = run_lineage_experiment(
            seed=1000 + 100 * D + E,
            generations=30,
            n=100,
            D=D,
            E=E,
        )
        print(
            f"D{D}E{E}: "
            f"{result.iloc[-1]['mean_persistence_score']:.6f}"
        )

    gpin, ratios, _, _ = generalized_invasion_number()
    print("Baseline GPIN:", round(gpin, 6))
    print("Direction ratios:", np.round(ratios, 6))
