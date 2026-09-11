# LinguaX Arc

[![DOI](https://zenodo.org/badge/1365721388.svg)](https://doi.org/10.5281/zenodo.22706552)
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
