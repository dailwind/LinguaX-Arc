# LinguaX Arc: Corpus Toolkit

[![DOI](https://zenodo.org/badge/1365721388.svg)](https://doi.org/10.5281/zenodo.22706551)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%207.0%2B-green.svg)]()
[![Version](https://img.shields.io/badge/version-6.0-orange.svg)](CHANGELOG.md)

**A fully offline corpus analysis toolkit for Android.**

LinguaX Arc brings the core methods of corpus linguistics (concordancing, collocation, keyness and word-class profiling) to a mobile device, with no internet connection, no account and no server. Every calculation runs on the phone itself, so a corpus never leaves the researcher's device.

A **Dailwind App Studio™** project, part of the **LinguaX Software Series**.

---

## Why this exists

Established corpus tools are built for the desktop (AntConc, WordSmith Tools) or for the browser (Sketch Engine, CQPweb). Both assume infrastructure that many researchers do not have: a personal laptop, a stable connection, or permission to upload their data to someone else's server.

LinguaX Arc addresses three specific gaps:

- **Access.** In many institutions, particularly across South Asia and other low-resource settings, a smartphone is the only computing device a student or early-career researcher owns.
- **Connectivity.** Fieldwork and rural research settings often have no reliable internet. Web-based concordancers are unusable there.
- **Privacy.** Legal, clinical and interview corpora frequently cannot be uploaded to third-party servers. On-device processing removes that obstacle.

---

## Features

| Module | Description |
|---|---|
| **Corpus Overview** | Tokens, sentences, punctuation marks and word types per file and for the whole corpus |
| **Word-Class Profile** | Lightweight rule-based part-of-speech histogram (8 coarse word classes) |
| **Punctuation Profile** | Frequency of each punctuation type across the corpus |
| **KWIC Concordance** | Keyword-in-context search with wildcards, regex, case sensitivity and sorting |
| **Concordance Plot** | Visual dispersion of a search term across corpus files |
| **File View** | Read any corpus file with search hits highlighted |
| **Clusters** | Recurrent multi-word units around a node word |
| **N-Grams** | Contiguous word sequences with frequency ranking |
| **Collocates** | Window-based collocation with MI, T-score, Log-Likelihood and Dice |
| **Word List** | Frequency list with normalised frequency and range |
| **Keyness** | Keywords against a reference corpus: Log-Likelihood (G²), Chi-square, Log Ratio, % Difference |
| **Word Cloud** | Frequency-weighted visualisation |
| **Summarizer** | Extractive summary (TF-IDF centroid, cosine similarity) |
| **Sentiment & Tone** | Lexicon-based valence scoring (−4 to +4) at document and segment level |
| **History & Export** | Log of past analyses; results exported as CSV, PDF, Word or text |

**Supported input:** `.txt`, `.pdf`, `.docx`
**Export:** CSV, PDF, Word (.doc), text and images can be saved and shared from within the app.

The statistical formulas used by each module are documented in [TECHNICAL_NOTES.md](TECHNICAL_NOTES.md).

---

## Installation

### From Google Play
Available on the Google Play Store, published by **Dailwind App Studio™**.

### From releases
Download the latest `.apk` from the [Releases](https://github.com/dailwind/LinguaX-Arc/releases) page and install it on any Android 7.0+ device. You may need to allow installation from unknown sources.

### Run from source (any device)
The whole analysis engine is one self-contained web page. Clone the repository and open `www/index.html` in a modern browser (Chrome, Edge or Firefox). No build step and no internet connection are needed.

```bash
git clone https://github.com/dailwind/LinguaX-Arc.git
cd LinguaX-Arc/www
# open index.html in your browser, or serve locally:
python3 -m http.server 8000   # then visit http://localhost:8000
```

---

## Architecture

The Android app is a native WebView shell that loads the bundled web layer from local storage. A small JavaScript bridge handles Android-specific actions such as saving files and opening the Play Store.

```
┌─────────────────────────────────────────┐
│  Android Shell (native WebView)         │
│  ┌───────────────────────────────────┐  │
│  │  Input Layer                      │  │
│  │  .txt  ·  pdf.js  ·  mammoth.js   │  │
│  └───────────────┬───────────────────┘  │
│  ┌───────────────▼───────────────────┐  │
│  │  Tokeniser & Corpus Index         │  │
│  └───────────────┬───────────────────┘  │
│  ┌───────────────▼───────────────────┐  │
│  │  Analysis Engine                  │  │
│  │  KWIC · collocates · keyness ·    │  │
│  │  n-grams · word classes · tone    │  │
│  └───────────────┬───────────────────┘  │
│  ┌───────────────▼───────────────────┐  │
│  │  Presentation & Export            │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
         No network. No server. No telemetry.
```

**Bundled dependencies:** [`pdf.js`](https://mozilla.github.io/pdf.js/) 2.16.105 (Apache-2.0) for PDF text extraction and [`mammoth.js`](https://github.com/mwilliamson/mammoth.js) (BSD-2-Clause) for DOCX extraction. Both are stored locally in `www/lib/`.

---

## Repository structure

```
LinguaX-Arc/
├── www/
│   ├── index.html              Application source (UI + analysis engine)
│   ├── arslan_tahir.jpeg       About-page image
│   ├── adnan_tahir.jpeg        About-page image
│   └── lib/
│       ├── pdf.min.js
│       ├── pdf.worker.min.js
│       └── mammoth.browser.min.js
├── TECHNICAL_NOTES.md          Formulas and algorithms
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSE
├── PRIVACY.md
├── THIRD-PARTY-NOTICES.md
└── README.md
```

---

## Known limitations

- The word-class profiler is rule-based (closed-class word lists plus suffix rules) and gives an approximate profile. It is not a statistical POS tagger and does not lemmatise.
- The sentiment lexicon is English-only.
- The source code also contains a text cleaner, a file merger and a readability / lexical-diversity panel (Flesch, STTR, hapax counts). These are not yet exposed in the v6.0 interface and are planned for a future release.
- The tokeniser recognises Latin and Arabic-script letters. Urdu text is tokenised, but language-specific tools (stopwords, word classes, sentiment) are English-only for now.

---

## Citation

If you use LinguaX Arc in published research, please cite it:

```bibtex
@software{tahir_linguax_arc_2026,
  author    = {Tahir, Arslan},
  title     = {LinguaX Arc: A Fully Offline Mobile Corpus Analysis Toolkit},
  version   = {6.0},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22706551},
  url       = {https://github.com/dailwind/LinguaX-Arc}
}
```

**APA:**
Tahir, A. (2026). *LinguaX Arc: A fully offline mobile corpus analysis toolkit* (Version 6.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22706551

---

## Contributing

Bug reports, feature requests and validation studies are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Author

**Arslan Tahir**
PhD Scholar in English Linguistics, Emerson University Multan, Pakistan
Founder, Dailwind App Studio™ & the LinguaX Software Series

Website: [dailwind.com](https://dailwind.com)
Email: [arslan@dailwind.com](mailto:arslan@dailwind.com)
ORCID: [0009-0007-7681-7972](https://orcid.org/0009-0007-7681-7972)

---

## License

Released under the [MIT License](LICENSE).
Third-party components and their licenses are listed in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

© 2026 Dailwind App Studio™. LinguaX Arc and Dailwind App Studio™ are trademarks of Arslan Tahir.
