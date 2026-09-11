# LinguaX Arc

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%207.0%2B-green.svg)]()
[![Version](https://img.shields.io/badge/version-5.0-orange.svg)]()

**A fully offline corpus analysis toolkit for Android.**

LinguaX Arc brings the core methods of corpus linguistics — concordancing, collocation, keyness, and part-of-speech tagging — to a mobile device, with no internet connection, no account, and no server. Every calculation runs on the phone itself, so a corpus never leaves the researcher's device.

A **Dailwind Studio™** project, part of the **LinguaX Software Series**.

---

## Why this exists

Established corpus tools are built for the desktop (AntConc, WordSmith Tools) or for the browser (Sketch Engine, CQPweb). Both assume infrastructure that many researchers do not have: a personal laptop, a stable connection, or permission to upload their data to someone else's server.

LinguaX Arc addresses three specific gaps:

- **Access.** In many institutions, particularly across South Asia and other low-resource settings, a smartphone is the only computing device a student or early-career researcher owns.
- **Connectivity.** Fieldwork and rural research settings often have no reliable internet. Web-based concordancers are unusable there.
- **Privacy.** Legal, clinical, and interview corpora frequently cannot be uploaded to third-party servers. On-device processing removes that obstacle entirely.

---

## Features

| Module | Description |
|---|---|
| **KWIC Concordance** | Keyword-in-context search with adjustable window and sorting |
| **Concordance Plot** | Visual dispersion of a search term across corpus files |
| **Collocates** | Collocation analysis with configurable left/right span |
| **Clusters** | Recurrent multi-word units around a node word |
| **N-Grams** | Contiguous word sequences with frequency ranking |
| **Word List** | Full frequency list with type/token statistics |
| **Keyness Analysis** | Keyword extraction against a reference corpus |
| **POS Tagger & Lemmatizer** | Part-of-speech annotation and lemmatisation |
| **Sentiment & Tone Analyzer** | Document- and segment-level sentiment scoring |
| **Word Cloud** | Frequency-weighted visualisation |
| **Readability & TTR** | Readability indices and lexical diversity measures |
| **Corpus Cleaner** | Normalisation, noise removal, and stopword handling |
| **File Merger** | Combine multiple files into a single corpus unit |
| **Workspace & History** | Saved sessions and analysis history |

**Supported input:** `.txt`, `.pdf`, `.docx`
**Export:** results can be saved and shared from within the app

---

## Installation

### From releases
Download the latest `.apk` from the [Releases](https://github.com/dailwind/LinguaX-Arc/releases) page and install it on any Android 7.0+ device. You may need to allow installation from unknown sources.

### From Google Play
Available on the Google Play Store under **Dailwind Studio**.

---

## Architecture

LinguaX Arc is built as a [Capacitor](https://capacitorjs.com/) application wrapping a self-contained web layer:

```
┌─────────────────────────────────────────┐
│  Android Shell (Capacitor / WebView)    │
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
│  │  n-grams · POS · sentiment        │  │
│  └───────────────┬───────────────────┘  │
│  ┌───────────────▼───────────────────┐  │
│  │  Presentation & Export            │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
         No network. No server. No telemetry.
```

**Dependencies:** [`pdf.js`](https://mozilla.github.io/pdf.js/) (Apache-2.0) for PDF extraction, [`mammoth.js`](https://github.com/mwilliamson/mammoth.js) (BSD-2-Clause) for DOCX extraction. Both are bundled locally.

---

## Repository structure

```
LinguaX-Arc/
├── www/
│   ├── index.html          Application source
│   └── lib/
│       ├── pdf.min.js
│       ├── pdf.worker.min.js
│       └── mammoth.browser.min.js
├── CITATION.cff
├── LICENSE
└── README.md
```

---

## Citation

If you use LinguaX Arc in published research, please cite it:

```bibtex
@software{qureshi_linguax_arc_2026,
  author    = {Qureshi, Arslan Tahir},
  title     = {LinguaX Arc: A Fully Offline Mobile Corpus Analysis Toolkit},
  version   = {5.0},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.XXXXXXX},
  url       = {https://github.com/dailwind/LinguaX-Arc}
}
```

**APA:**
Qureshi, A. T. (2026). *LinguaX Arc: A fully offline mobile corpus analysis toolkit* (Version 5.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

---

## Contributing

Bug reports, feature requests, and validation studies are welcome. Please open an [issue](https://github.com/dailwind/LinguaX-Arc/issues) describing the problem, your device model, and your Android version.

---

## Author

**Arslan Tahir Qureshi**
PhD Scholar in English Linguistics, Emerson University Multan, Pakistan
Founder, Dailwind Studio™ & the LinguaX Software Series

Website: [dailwind.com](https://dailwind.com)
Email: [arslan@dailwind.com](mailto:arslan@dailwind.com)
ORCID: [0009-0007-7681-7972](https://orcid.org/0009-0007-7681-7972)

---

## License

Released under the [MIT License](LICENSE).

Third-party components and their licenses are listed in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

© 2026 Dailwind Studio. LinguaX Arc and Dailwind Studio are trademarks of Arslan Tahir Qureshi.
