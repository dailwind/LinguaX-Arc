# Changelog

All notable changes to LinguaX Arc are documented here.

## [6.0.2] – 2026-11-11
### Changed
- README and TECHNICAL_NOTES now list exactly the modules visible in the v6.0 interface (added Corpus Overview, Punctuation Profile, File View, Summarizer, History & Export).
- Corpus Cleaner, File Merger and the readability panel are documented as present in the source but not yet exposed in the interface.

## [6.0.1] – 2026-11-11
### Added
- Full application source (`www/index.html`) and bundled libraries (`www/lib/`) published in the repository.
- `TECHNICAL_NOTES.md` documenting every formula and algorithm.
- `CONTRIBUTING.md`.

### Fixed
- Corpus Cleaner (not yet exposed in the interface): "Remove emojis" used an invalid Unicode range that deleted ordinary letters and digits but kept the emoji. It now removes emoji only.
- "Rate the app" fallback link now opens the correct Google Play listing.

### Changed
- README: architecture described accurately (native Android WebView shell), module descriptions aligned with the implementation, known limitations added.

## [6.0] – 2026-11
- Version distributed on Google Play and showcased at PiNTECH Expo 2026.

## [5.0] – 2026-09-05
- First public release; archived on Zenodo (DOI 10.5281/zenodo.22706552).
