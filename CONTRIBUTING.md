# Contributing to Elon Musk OS

## How to Contribute

### Adding Interviews to the Archive

The interview archive (`references/interview-archive.md`) aims to be the most comprehensive Elon Musk interview list available. To add missing interviews:

1. Verify the interview is a direct conversation with Musk (not about him)
2. Include: date, title/event name, key topics covered
3. Add a YouTube/Spotify link if available
4. Place it in the correct chronological position

### Adding Transcripts

We store full transcripts in the `transcripts/` directory. Naming convention:

```
transcripts/YYYY-MM-DD-event-name.md
```

To generate transcripts from YouTube:
- [youtube2transcripts](https://github.com/madeyexz/youtube2transcripts) — Gemini-powered, batch processing, speaker ID
- [whisper-youtube](https://github.com/ArthurFDLR/whisper-youtube) — Whisper via Google Colab

### Improving Mental Models

If you find a public source where Musk articulates a thinking pattern not currently captured in SKILL.md:

1. Cite the specific interview/document with timestamp or page number
2. Explain how it differs from or extends the existing 5 models
3. Submit a PR with the proposed addition

### Updating Decision Records

`references/decision-patterns.md` tracks Musk's key decisions with outcomes. When significant new decisions occur:

1. Use the existing format: [Event] → [Decision] → [Inferred Logic] → [Result]
2. Distinguish between public rationale and inferred deeper logic
3. Include numerical data where available

## Quality Standards

- **Every claim needs a source.** No unsourced assertions about Musk's thinking.
- **Preserve contradictions.** Don't sanitize Musk into a caricature. Internal tensions are features.
- **English only.** All content must be in English.
- **No opinion.** This is a cognitive framework extraction, not a fan page or hit piece.

## What We Don't Accept

- Speculation without sourcing
- Political commentary or advocacy
- Content that requires Musk's private information
- Duplicate information already in the archive
