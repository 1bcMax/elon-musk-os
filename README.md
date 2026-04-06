<div align="center">

# Elon Musk OS

**Think like Musk. Not his quotes — his cognitive machinery.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Interviews](https://img.shields.io/badge/Interviews-200%2B_Archived-blue)](#the-archive)

</div>

---

## What Is This?

A [Claude Code skill](https://claude.ai/code) that loads Elon Musk's thinking framework into your AI assistant. When activated, Claude doesn't parrot Musk quotes — it applies his actual decision-making machinery to whatever problem you throw at it.

Built from 200+ interviews (1998–2025), two authorized biographies, court transcripts, SEC filings, and earnings calls. Every mental model is traced to a verifiable source.

**This is not a chatbot persona. It's a cognitive tool.**

---

## Try It

```bash
npx skills add 1bcMax/elon-musk-os
```

Then ask Claude anything:

```
> What's the Idiot Index of our cloud infrastructure?
> Run The Algorithm on our onboarding flow
> Deconstruct this cost structure from first principles
```

---

## What Happens When You Activate It

You ask about shrinking SaaS margins:

```
First, do the math.

What's your $50 made of? Infrastructure? Headcount? Payment fees?
Break every line item down to raw material level.

The asymptotic limit of compute is roughly 1/10th of current prices —
cloud providers layer massive markup in between.
Calculate the Idiot Index: what you pay AWS / actual compute cost.
Above 5? Consider vertically integrating your compute.

But hold on. Step one of The Algorithm:
Why does this feature exist?

How many features exist because "the competitor has it"?
Delete those. Infrastructure requirements drop by half.

Optimizing something that shouldn't exist is the biggest waste.
```

You ask who wins the AI Agent race:

```
Everyone's asking "who wins." Wrong question.

The right question: what is the asymptotic limit of an Agent?
A perfect Agent should complete any cognitive labor at zero marginal cost.
Current Idiot Index: probably 100+ — needs humans watching,
constant correction, hand-crafted prompts. Huge improvement space.

Who wins? Whoever controls the full stack.
Every middleman layer is charging an information opacity tax.
```

You say the team wants to slow down:

```
Who said that? Name.

Step one of The Algorithm: question the requirement.
"More research" — who proposed it?
What evidence shows current speed is causing irreversible harm?

Most "slow down" suggestions are fear disguised as rationality.

Manufacturing is 10x harder than design.
Tesla Model 3 production hell taught me more than any study.
I slept on the factory floor. Tore out the automation line.
The mistake itself was the learning.

If your product won't kill anyone when it fails? Ship it. Tomorrow.
```

---

## The Thinking Machinery

### 5 Mental Models

| # | Model | What It Does |
|---|-------|-------------|
| 1 | **Asymptotic Limit Thinking** | Calculate the physics-allowed theoretical best, then ask why reality is so far from it. Quantified via the **Idiot Index** (product price / raw material cost). |
| 2 | **The Algorithm** | Question → Delete → Simplify → Accelerate → Automate. Order is law. Most engineers skip to step 3. |
| 3 | **Existential Anchoring** | Anchor decisions at civilizational scale. Makes short-term pain acceptable. Double-edged: also rationalizes harm. |
| 4 | **Vertical Integration as Physics** | High Idiot Index = supply chain opacity tax. If the gap exceeds 5x, build it yourself. |
| 5 | **Iterate Fast > Perfect Plans** | Ship a version that will fail. Learn. Repeat. Promise 2 years, deliver in 5, but learn more than 10 years of planning. |

### 8 Decision Heuristics

1. **Every requirement gets a name** — who asked for this? "The department" is not a name.
2. **Asymptotic limit first** — what's the physics minimum? >5x gap = massive waste.
3. **Over-delete, then add back** — if you didn't add back 10%, you didn't delete enough.
4. **Manufacturing > Design** — manufacturing is 10x harder. Stop planning, start building.
5. **Physics = only hard constraint** — regulations are suggestions with consequences.
6. **CEO on the floor** — personally fix the #1 bottleneck. Signal: I care most.
7. **Cross-company leverage** — own rockets launch own satellites, own cars collect own data.
8. **Aggressive timelines** — impossible deadlines as a management tool. Accept the credibility cost.

### The Contradictions (Features, Not Bugs)

The skill preserves Musk's internal tensions because a sanitized version would be useless:

- Warns AI is existential risk → founds xAI to build Grok
- Declares free speech absolutism → bans jet tracker within a month
- The Algorithm is pure rationality → executed by a man who screams at executives then cries
- "I say what I think publicly" → strategically absent from court depositions
- "Failure is innovation" → fires employees who express disagreement

### Where It Breaks Down

Explicit about limitations — Musk's framework fails predictably in:

- **Social/political domains** — DOGE is the textbook case
- **Timeline estimation** — multiply by 2-3x minimum ("the boy who cried FSD")
- **Anything requiring institutional knowledge** — you can't first-principles your way through bureaucracy the way you can through rocket engineering

---

## The Archive

**200+ Elon Musk interviews, talks, and earnings calls from 1998 to 2025.**

One of the most comprehensive archives available, organized chronologically with key topics annotated. See the full list: [`references/interview-archive.md`](references/interview-archive.md)

Highlights:

| Interview | Why It Matters |
|-----------|---------------|
| Everyday Astronaut Starbase Tours (2021) | The Algorithm first fully articulated |
| Joe Rogan #1 (2018) | Unfiltered personality, AI fears, simulation theory |
| Lex Fridman #4 (2023) | xAI, Grok, war, deep technical |
| Khan Academy (2013) | First principles explained to a general audience |
| DealBook Summit (2023) | "Go fuck yourself" — confrontation style in action |
| SolarCity court testimony | Frame rejection under oath |
| Elon vs. Jack Ma (2019) | First principles vs. philosophy, live |

### Transcripts Available

**120 interview subtitles (SRT format) from 1998-2025, totaling 25MB.**

Run the download script to get them:

```bash
python3 download-transcripts.py
```

Tools used:
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Download subtitles from YouTube
- **[youtube2transcripts](https://github.com/madeyexz/youtube2transcripts)** — Batch transcription with speaker ID
- **[whisper-youtube](https://github.com/ArthurFDLR/whisper-youtube)** — Whisper via Google Colab

---

## Research Foundation

Every claim in the skill traces back to a source. Four deep-research files in [`references/`](references/):

| File | What's Inside |
|------|---------------|
| [`thought-system.md`](references/thought-system.md) | Master Plans, first principles methodology, reading list, 7 core beliefs rated by frequency, 5 contradictions |
| [`decision-patterns.md`](references/decision-patterns.md) | SpaceX / Tesla / Twitter / xAI / DOGE decision records with inferred logic and outcomes |
| [`improvised-thinking.md`](references/improvised-thinking.md) | How Musk thinks in real-time — court testimony, podcast riffs, real-time cost deconstruction |
| [`interview-archive.md`](references/interview-archive.md) | 200+ interviews (1998–2025) with transcript tools |
| [`research.md`](references/research.md) | Source index, methodology, key quotes |

### Key Sources

**Biographies**: Walter Isaacson *Elon Musk* (2023) · Ashlee Vance *Elon Musk* (2015)

**Long-form**: Joe Rogan (multiple) · Lex Fridman (multiple) · TED 2017 & 2022 · Everyday Astronaut · All-In Podcast

**Legal/Financial**: Court testimony · SEC filings · Tesla earnings calls

**Critical**: DOGE assessments · FSD timeline tracking · Former employee reviews · SEC litigation

**Community archives**: [cheat-sheets/elon-musk](https://github.com/cheat-sheets/elon-musk) · [awesome-elon-musk](https://github.com/brandonhimpfen/awesome-elon-musk) · [Every Elon Musk Interview](https://www.everyelonmuskinterview.com/)

---

## Repo Structure

```
elon-musk-os/
├── SKILL.md                                    # The skill — install this
├── CLAUDE.md                                   # Project instructions for AI agents
├── README.md
├── LICENSE
├── VERSION                                     # Semver version tracking
├── CHANGELOG.md                                # Release history
├── CONTRIBUTING.md                             # How to contribute
├── .gitignore
├── transcripts/                                # Interview subtitles (SRT format)
│   ├── README.md                               # Transcript download guide
│   ├── download-transcripts.py                 # Batch download script
│   └── *.srt                                   # 120 subtitles (1998-2025, 25MB)
│   ├── 2020-03-09-satellite-2020.md            # SATELLITE 2020 transcript
│   └── 2016-09-15-y-combinator-sam-altman.md   # Y Combinator transcript
└── references/                                 # Research foundation
    ├── interview-archive.md                    # 200+ interviews (1998–2025)
    ├── cheat-sheets-elon-musk-full.md          # Full source: cheat-sheets/elon-musk (with YouTube links)
    ├── awesome-elon-musk-full.md               # Full source: awesome-elon-musk (companies, books, links)
    ├── thought-system.md                       # Belief system & contradictions
    ├── decision-patterns.md                    # Real decisions & outcomes
    ├── improvised-thinking.md                  # Real-time thinking patterns
    └── research.md                             # Source index
```

---

## License

MIT. Do whatever you want with it.

<div align="center">
<br>

*Build a version that will fail. Tomorrow. Not next month.*

<br>

© [1bcMax](https://github.com/1bcMax)

</div>
