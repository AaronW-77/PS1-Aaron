# Ticket scarcity and AI advice: PS1 computational pilot

This is Qianshuo (Aaron) Wang's ticket project. The template's `companion/` folder is an unrelated optional classroom LLM example.

## Run

Python 3.9+; standard library only; no installation, account or API key needed locally.

```sh
python3 research/model.py
python3 -m unittest discover -s research/tests -v
```

The self-contained `ps1_ticket_reliance.ipynb` can be uploaded to Google Colab and run with **Runtime > Run all**. Outputs are already embedded from local cell execution. Hosted Colab verification is pending.

Optional original-game replay (Node.js):

```sh
node research/audit_legacy.js
```

## What is implemented

- Exogenous designed risk `min(.98, N / (N + 8*Q + 1))`; not market-estimated risk.
- One risk-neutral consumer, `V > P > 0`; buy for `V-P`, wait for an available ticket at 10% discount or receive zero after sell-out.
- Symmetric state signal with known conditional accuracy r, not a real AI model or calibrated human belief.
- Exact enumeration of two states and two signals for follow, ignore and posterior-optimal policies.
- A 25-condition grid and a 100,000-round seeded independent numerical check.
- Tests for thresholds, information boundaries, dominance and invalid inputs.

The legacy game in `legacy/index.html` is preserved unchanged and remains the existing online demo. It uses deterministic hashes and retrospective labels. The notebook deliberately makes the probability model explicit and evaluates ex-ante utility. Advice quality is not the same as realized success; the two artifacts address the same question with these documented differences.

## Results

At P=150, V=220, Q=40, N=500, r=.8: exact following payoff 66.1656516443, posterior-optimal payoff 70.0. The stochastic check gives 66.202 for following (seed 206). These are synthetic model outputs, not consumer findings or estimated educational benefits.

## Provenance and AI assistance

See `../records/provenance.json` and Appendix A. Codex assisted with formalization, writing, code and verification on September 12, 2026. Author acceptance and independent rerun are pending. No peer review or handwritten reflection is generated here.

## Reuse

No additional license is granted by this draft. Retain third-party notices. Public access does not itself grant a reuse license; author licensing choice remains pending.
