# When Should Consumers Follow AI Ticket Advice?

**COMSCI/ECON 206: Computational Microeconomics — Autumn 2026**  
**Author:** Qianshuo (Aaron) Wang  
**Workshop:** Session D — Strategic AI: Trust, Collusion, and Adaptation in Repeated Interactions

## Project Overview

This project studies when following AI advice is economically justified in a limited concert-ticket market. A consumer chooses whether to buy a ticket immediately or wait for a possible discount while facing sell-out risk. The project connects three perspectives:

- **Economics:** how ticket scarcity and competition affect expected consumer surplus.
- **Computer Science:** how AI advice reliability affects the quality of recommendations.
- **Behavioral Science:** whether reliance reflects trust in AI or beliefs about sell-out risk.

The computational benchmark compares three policies: **follow AI advice**, **ignore AI advice**, and a **Bayesian posterior-optimal policy**.

## Repository Structure

- `research/model.py` — ticket-advice model and exact calculations
- `research/ps1_ticket_reliance.ipynb` — executable notebook
- `research/tests/` — verification tests
- `research/outputs/` — saved synthetic outputs
- `research/legacy/` — preserved original ticket-game implementation
- `sections/` — main proposal source
- `appendices/` — supporting material
- `figures/` — editable Draw.io teaser figure and exported PDF
- `main.tex` — main LaTeX document
- `references.bib` — bibliography

## Reproducing the Computational Results

The model uses only the Python standard library.

From the repository root, run:

    python3 research/model.py

Then run the verification tests:

    python3 -m unittest discover -s research/tests -v

The notebook can also be opened in Google Colab and executed using **Runtime → Run all**.

## Main Synthetic Output

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

## Interactive Game

The corresponding interactive learning game is available on Hugging Face:

https://huggingface.co/spaces/dku-comsci-econ206-2026/Aaron-game

## Google Colab

Executable notebook:

https://colab.research.google.com/drive/1R6YTTeYsrbVoWV9td9uGGRFwsqSx7jsE?usp=sharing

## Reproducibility Note

The final notebook was independently rerun by the author in Google Colab using **Run all**, and the reported outputs were checked against the manuscript.

This repository accompanies the PS1 research proposal for COMSCI/ECON 206.
