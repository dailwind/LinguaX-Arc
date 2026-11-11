LinguaX Arc - Validation Corpus
================================

SOURCE
Project Gutenberg Selections, distributed with NLTK Data:
https://github.com/nltk/nltk_data  (packages/corpora/gutenberg.zip)
Public-domain texts. Converted to UTF-8; text otherwise unchanged.

Cite as: Bird, S., Klein, E., & Loper, E. (2009). Natural Language
Processing with Python. O'Reilly Media. (NLTK Gutenberg corpus)

FOLDERS
1_Target_Austen       3 novels by Jane Austen            ~363,000 tokens
2_Reference_Fiction   6 works of 19th/20th-c. fiction    ~620,000 tokens
                      (Chesterton x3, Melville, Carroll, Edgeworth)
3_Performance_Test    10k / 100k / 1M-token files built from all
                      18 Gutenberg texts, for phone speed tests

WHAT TO RUN IN ANTCONC 4 (load 1_Target_Austen as the corpus)
Settings to match LinguaX Arc:
 - Token definition: letters; also allow apostrophe (') and hyphen (-)
 - Treat all data as lowercase: ON
 - No stoplist

 1. Word List  -> export CSV
 2. KWIC hit counts for: time, love, said, never, house  (note the numbers)
 3. Collocates of "time": window 5L-5R, min. collocate freq 5
    -> export with MI, and again with Log-Likelihood
 4. Keyword List: Target = 1_Target_Austen, Reference = 2_Reference_Fiction,
    statistic = Log-Likelihood (4-term), effect size = Log Ratio
    -> export CSV
 5. N-grams: size 2 and size 3, min freq 5 -> export CSV each

Send all CSV files plus your AntConc version number (Help > About).
