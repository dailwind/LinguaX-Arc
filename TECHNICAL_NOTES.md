# Technical Notes

This document describes the algorithms and statistics that LinguaX Arc computes, so that results can be reported, checked and reproduced. All references to code are to `www/index.html`.

## 1. Text input and tokenisation

- **Input formats.** `.txt` is read directly. `.pdf` text is extracted with pdf.js 2.16.105 (page by page, text items joined with spaces). `.docx` raw text is extracted with mammoth.js.
- **Tokeniser.** A word token is a match of:

  ```
  /[A-Za-zÀ-ɏ؀-ۿ']+(?:-[A-Za-zÀ-ɏ]+)*/g
  ```

  That is: runs of Latin letters (including accented Latin), Arabic-script letters (U+0600–U+06FF, which covers Urdu letters) and apostrophes, with optional hyphenated parts. Numbers and punctuation are **not** counted as tokens.
- **Case.** Each token keeps its original form and a lower-cased form. Frequency-based tools count the lower-cased form, so *The* and *the* are one type. KWIC search can optionally be case-sensitive.

## 2. Word list

- Frequency: raw count of each lower-cased type.
- Normalised frequency: per 1,000 tokens.
- Range: number of corpus files in which the type occurs.

## 3. Collocates

For a node word with frequency *f(n)* (number of hits), a span of *L* words left and *R* words right (window size *W = L + R*), corpus size *N* tokens, collocate frequency in the corpus *f(c)* and observed co-occurrence frequency *O* within the span:

| Statistic | Formula |
|---|---|
| Expected co-occurrence | *E = f(n) · f(c) · W / N* |
| Mutual Information | *MI = log₂(O / E)* |
| T-score | *T = (O − E) / √O* |
| Log-Likelihood (single-cell form) | *LL = 2 · [O · ln(O / E) − (O − E)]* |
| Dice | *Dice = 2O / (f(n) + f(c))* |

Collocates below a user-set minimum co-occurrence frequency are dropped. Results can be ranked by frequency, MI, T, LL or Dice. Left and right co-occurrence counts are reported separately.

## 4. Keyness (target vs reference corpus)

For a word with frequency *a* in the target corpus (size *c* tokens) and *b* in the reference corpus (size *d* tokens):

| Statistic | Formula |
|---|---|
| Expected frequencies | *E₁ = c(a + b)/(c + d)*, *E₂ = d(a + b)/(c + d)* |
| Log-Likelihood G² (Rayson & Garside, 2000) | *G² = 2 · [a·ln(a/E₁) + b·ln(b/E₂)]* (a zero term is omitted) |
| Chi-square (2 cells, no Yates correction) | *χ² = (a − E₁)²/E₁ + (b − E₂)²/E₂* |
| Log Ratio effect size (Hardie, 2014) | *LR = log₂[(a/c) / (b/d)]*, with a zero frequency replaced by 0.5 |
| % Difference (Gabrielatos & Marchi, 2012) | *%DIFF = [(a/c − b/d) / (b/d)] · 100* |

Significance labels use G² critical values for 1 degree of freedom: 3.84 (p < 0.05), 6.63 (p < 0.01), 10.83 (p < 0.001), 15.13 (p < 0.0001). Positive keywords have a higher relative frequency in the target corpus, and negative keywords a lower one. Results can be sorted by G², χ² or |LR|. A minimum combined frequency (a + b) filter and optional stopword removal are available.

## 5. N-grams and clusters

- **N-grams:** contiguous token sequences of length *n*, ranked by frequency.
- **Clusters:** contiguous token sequences that contain the search term, ranked by frequency.

## 6. Concordance (KWIC) and concordance plot

- KWIC lines show each hit with a user-defined left and right context. Search supports plain text, wildcards (`*`) and regular expressions.
- The concordance plot marks the token position of each hit within each file as a percentage of file length, and reports hits per file and hits per 1,000 tokens.

## 7. Readability and lexical diversity (in source, not yet in the v6.0 interface)

| Measure | Formula |
|---|---|
| Flesch Reading Ease | *206.835 − 1.015 · (words/sentences) − 84.6 · (syllables/words)*, clamped to 0–100 |
| Flesch–Kincaid Grade | *0.39 · (words/sentences) + 11.8 · (syllables/words) − 15.59*, minimum 1 |
| Type/Token Ratio | *TTR = types / tokens × 100* |
| Standardised TTR | mean TTR over consecutive 100-token segments |
| Root TTR (Guiraud) | *types / √tokens* |
| Hapax / dis legomena | number of types occurring once / twice |

Syllables are estimated with an English vowel-group heuristic, so readability scores are approximate and intended for English text.

## 8. Word-class profiler

Each token is assigned to one of eight coarse classes (Nouns, Verbs, Adjectives, Adverbs, Pronouns, Determiners, Prepositions, Conjunctions) by an ordered set of rules:

1. Closed-class word lists (determiners, pronouns, prepositions, conjunctions).
2. Lists of modals, auxiliaries and common verbs, plus verbal suffixes (*-ing*, *-ed*, *-ize/-ise*, *-ify*, *-ate*).
3. Common adverbs and the *-ly* suffix (with listed exceptions such as *friendly*, *daily*).
4. Common adjectives and adjectival suffixes (*-able*, *-ful*, *-less*, *-ous*, *-ive*, *-al*, …).
5. Everything else is classed as a noun.

This is a context-free, rule-based approximation for profiling a corpus. It does not disambiguate words by context (for example *record* as noun or verb), and it does not lemmatise.

## 9. Corpus overview and punctuation profile

The Corpus view reports, per file and in total: tokens (as defined in §1), sentence units (runs of `.`, `!` or `?`), punctuation marks (period, comma, question mark, exclamation, semicolon, colon, quotes, parentheses, dashes) and word types (distinct lower-cased tokens). It also shows the word-class histogram (§8) and a punctuation-frequency chart.

## 10. Summarizer

Centroid-based extractive summarisation. Each sentence is represented as a TF-IDF vector (IDF = 1 + ln(N / df), where N is the number of sentences and df the number of sentences containing the word). A document centroid is built from the 15 terms with the highest document-wide weight, and each sentence is scored by the cosine similarity between its vector and the centroid. The highest-scoring sentences form the summary.

## 11. Sentiment and tone

Sentiment is lexicon-based. Each word found in a built-in English valence lexicon contributes a score between −4.0 and +4.0. Document and segment scores are aggregated from these word scores, and a separate list flags threat or violence vocabulary. The lexicon is English-only.

## 12. Corpus cleaner (in source, not yet in the v6.0 interface)

Optional steps, applied in order: lower-casing; URL removal; emoji removal (Unicode ranges U+1F300–U+1FAFF and U+2600–U+27BF, plus variation selectors and zero-width joiners); digit removal; punctuation removal; stopword removal (user-editable list); keeping alphabetic tokens only; whitespace normalisation.

## 13. Privacy and networking

The application makes no network requests during analysis. Files are processed in memory and saved only to app-local storage on the device. The only outbound actions are links the user taps explicitly (for example the website, Zenodo or the Play Store page).

## References

- Gabrielatos, C., & Marchi, A. (2012). Keyness: Appropriate metrics and practical issues. *CADS International Conference*, University of Bologna.
- Hardie, A. (2014). Log Ratio: An informal introduction. ESRC Centre for Corpus Approaches to Social Science (CASS), Lancaster University.
- Rayson, P., & Garside, R. (2000). Comparing corpora using frequency profiling. *Proceedings of the Workshop on Comparing Corpora*, ACL 2000, 1–6.
