# Validation notes (for manuscript)
Corpus: NLTK Gutenberg selection. Target = Austen x3 (AntConc 366,832 tok / LinguaX 363,454); Reference = Chesterton x3, Melville, Carroll, Edgeworth (631,298 / 619,934).
AntConc 4.4.2 defaults; collocates 5L-5R min 5, LL(4-term)+MI, threshold All; keywords LL(4-term), effect Dice, positive only, threshold All; n-grams 2,3 min freq 5; page size All.
LinguaX Arc v6.0.2 engine (www/index.html) run headless in Chromium via Playwright (run_linguax.py). Condition A = native tokeniser; Condition B = tokeniser replaced by \p{L}+ (AntConc-equivalent; reproduces AntConc token/type counts exactly).
AntConc tokenisation = runs of Unicode letters only (verified: exact 366,832 / 10,307 types; 631,298 ref).
Condition A: wordlist exact freq 92.9% of shared types, r=.998, rho=.995, top-100 overlap 98; collocates co-freq exact 81.3%, MI r=.996 MAE .034, top-10 identical; keywords freq exact 89.0%, LL r=.998 rho=.987, top-20 19/20, top-100 95; 2-grams exact 94.2%, 3-grams 96.7%.
Condition B: 100% identical lists, frequencies, ranges, co-frequencies, MI (MAE 0), keyword sets & top-100 identical; LL rho=1.0.
Residual LL differences: keyness LinguaX uses 2-cell G2 (Rayson & Garside 2000), AntConc 4-term contingency G2 (verified: her 4574.59 vs 4616.067 reproduced exactly); max |diff| 41.5 on G2=4616 (0.9%), 231/6389 words differ >0.01, rank order identical. Collocate LL: LinguaX single-cell form; ranking rho=1.0.
KWIC: A 668/234/1054/701/329 vs AntConc 671/236/1054/702/350; all diffs = hyphenated compounds (dinner-time, love-song, never-ending, farm-house...). B identical.
