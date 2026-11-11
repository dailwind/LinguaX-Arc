# LinguaX Arc v6.0.2 — validation against AntConc 4.4.2

Materials for the comparative validation reported in the accompanying paper.

- `corpus/` — public-domain texts (Project Gutenberg). Target: three Austen novels. Reference: six fiction texts. `3_Performance_Test/` holds 10k/100k/1M-word files.
- `antconc_exports/` — AntConc 4.4.2 output (default letter-only token definition): word list, KWIC, collocates, keywords, 2- and 3-grams.
- `run_linguax.py` — runs LinguaX Arc headlessly (Playwright) on the same corpus with its native tokeniser (Condition A).
- `run_linguax_tokctrl.py` — same, with the tokeniser set to `\p{L}+` to match AntConc (Condition B).
- `linguax_outputs/`, `linguax_outputs_aligned_tokeniser/` — JSON outputs from the two runs.
- `compare.py` → `comparison_results.json` — agreement statistics (exact match, Pearson r, Spearman ρ, top-k overlap).
- `VALIDATION_NOTES.md` — how each difference was traced.

Reproduce: `pip install playwright && playwright install chromium`, then `python run_linguax.py`, `python run_linguax_tokctrl.py`, `python compare.py`.
