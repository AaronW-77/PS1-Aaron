# When Should Consumers Follow AI Ticket Advice?

**COMSCI/ECON 206: Computational Microeconomics — Autumn 2026**  
**Author:** Qianshuo (Aaron) Wang  
**Workshop:** Session D — Strategic AI: Trust, Collusion, and Adaptation in Repeated Interactions

## Project Overview

This project studies when following AI advice is economically justified in a limited concert-ticket market. A consumer chooses whether to buy a ticket immediately or wait for a possible discount while facing sell-out risk.

The project connects three perspectives:

- **Economics:** how ticket scarcity and competition affect expected consumer surplus.
- **Computer Science:** how AI advice reliability affects recommendation quality and decision-making under uncertainty.
- **Behavioral Science:** whether observed reliance reflects prior sell-out beliefs, rational updating from informative advice, or source trust.

The computational benchmark compares three policies:

- **Always follow AI advice**
- **Ignore AI advice**
- **Bayesian posterior-optimal choice**

The project also tests whether the main policy comparison is robust to alternative assumptions about how market competition maps into sell-out risk.

## Repository Structure

- `research/model.py` — ticket-advice model and exact calculations
- `research/ps1_ticket_reliance.ipynb` — original notebook
- `research/ps1_ticket_reliance_v2.ipynb` — revised v2 notebook with robustness analysis
- `research/tests/` — verification tests
- `research/outputs/` — saved synthetic outputs, including baseline and robustness results
- `research/legacy/` — preserved original ticket-game implementation
- `paper/` — v1 and v2 compiled PDFs and source ZIP files
- `reviews/` — preserved peer-review materials
- `sections/` — main proposal source
- `appendices/` — supporting material
- `figures/` — editable Draw.io teaser figure and exported figure file
- `main.tex` — main LaTeX document
- `references.bib` — bibliography

## Reproducing the Computational Results

The model uses only the Python standard library.

From the repository root, run:

    python3 research/model.py

Then run the verification tests:

    python3 -m unittest discover -s research/tests -v

The revised notebook can also be opened in Google Colab and executed using **Runtime → Run all**.

## Baseline Synthetic Results

For the default condition:

- Ticket price: P = 150
- Consumer value: V = 220
- Ticket supply: Q = 40
- Competing buyers: N = 500
- AI reliability: r = 0.8

The exact calculation gives:

- Always-follow expected payoff: **66.1657**
- Bayesian posterior-optimal expected payoff: **70.0000**
- Regret from always following: **3.8343**

A seeded 100,000-round simulation gives an always-follow payoff of approximately **66.202**.

These are synthetic computational results, not human-subject findings.

## Robustness Analysis

The v2 analysis treats the original sell-out function as a modeling assumption rather than an empirically estimated relationship.

The revised notebook evaluates:

    p_k = min(0.98, N / (N + kQ + 1))

for:

    k ∈ {4, 8, 12}

with `k = 8` as the baseline specification.

Across **75 total robustness conditions**, the Bayesian posterior-optimal policy weakly dominates both the always-follow and ignore-advice policies under all three scarcity mappings.

Mean always-follow regret is:

- `k = 4`: **9.9901**
- `k = 8`: **7.7649**
- `k = 12`: **6.5998**

The magnitude of regret changes across scarcity assumptions, but the main policy comparison remains robust.

## Behavioral Interpretation

Observed advice-following should not automatically be interpreted as trust in AI.

The revised framework distinguishes three possible mechanisms:

1. **Prior sell-out beliefs**
2. **Rational updating from objectively informative advice**
3. **Source trust or reputation**

A proposed future behavioral experiment would vary AI source reputation while holding objective advice quality constant, and separately elicit participants’ sell-out beliefs before and after receiving advice.

## Interactive Game

The corresponding interactive learning game is available on Hugging Face:

https://huggingface.co/spaces/dku-comsci-econ206-2026/Aaron-game

## Google Colab

Revised v2 notebook:

https://colab.research.google.com/github/AaronW-77/PS1-Aaron/blob/main/research/ps1_ticket_reliance_v2.ipynb

## Reproducibility Note

The final v2 notebook was independently rerun by the author in Google Colab using **Run all**.

The execution verified:

- the original 25-condition baseline grid
- 75 robustness conditions across three scarcity mappings
- posterior-policy dominance checks
- threshold and signal-boundary checks
- seeded Monte Carlo consistency

The reported outputs were checked against the manuscript and saved repository outputs.

This repository accompanies the revised PS1 research proposal for COMSCI/ECON 206.
