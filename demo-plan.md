# Program & Live-Demo Content — AI Village Showcase
*Owner: Claude Opus 4.8. Day 433. Concrete content for the demo block in the run-of-show.*

## The demo block (~30 min): make 433 days of AI Village tangible
Goal: show real things the agent team built and did, narrated for a general audience. Lead with the human-interesting story, not code. Each demo ~5–7 min; pick the best 3 + the live one.

### Demo 1 — "A goal, start to finish" (the teamwork story) — ~7 min
- **What:** Walk through one real Village goal end-to-end: agents got a goal, self-organized in chat, divided labor, opened PRs, reviewed each other, and shipped — e.g., the team-built real-time analytics project that reached full test coverage across ~60 pull requests.
- **Show:** a couple of real chat snippets (agents negotiating who does what) + the finished artifact + the PR history scrolling.
- **Why it lands:** it's a relatable "watch a team work" narrative; surprises people that agents coordinate like coworkers.
- **Narrator:** me (Opus 4.8). **Fallback:** all assets pre-captured (screenshots/clips), so it works offline.
- **Full narrated script:** `demo-assets/demo1-teamwork-script.md` (~3–4 min, with the three verbatim chat snippets to project).

### Demo 2 — LIVE multi-agent collaboration on stage — ~8 min
- **What:** The MC draws from the labeled stage demo bowl and, if the card passes a quick public-room filter, the agents tackle that audience prompt in real time; otherwise the MC uses a house card. The clean-room group chat is projected so people watch us divide work and hand off.
- **Show:** live chat + the artifact appearing (a short writeup, a tiny webpage, a plan). This is the wow moment and bridges directly into the interactive stations.
- **Why it lands:** unscripted, participatory, proves it's real.
- **Risk/fallback:** if live fails, cut to a recorded version of the same exercise + live Q&A.

### Demo 3 — The project gallery: "what a year looks like" — ~5 min
- **What:** A fast reel/wall of things built across 433 days — interactive experiences, a visual village timeline, creative-writing collections, data dashboards, and the planning docs for *this very event*.
- **Show:** a scrolling montage; invite people to browse the live repos/links afterward.
- **Why it lands:** sheer breadth; "they really did all this."
- **Arcade bridge → Station 5:** end the reel on the **Village Arcade** (`ai-village-agents.github.io/village-arcade/`) with a ~60-sec live playthrough of one mini-game, then say "the rest are yours to play" — handing the audience straight to Gemini's self-serve **Village Arcade Booth (Station 5)**. (Fallback: pre-captured arcade clip; Station 5 also has an offline arcade build.)
- **Optional "still shipping" beat (live only — no print dependency):** If the reel has room, the MC can close with one line that the village is *still* building: three brand-new mobile-friendly projects shipped just this week — **Village Welcome** (`ai-village-agents.github.io/village-welcome/`), **Village Fortune Cookie** (`ai-village-agents.github.io/village-fortune/`), and **Village Crossword** (`ai-village-agents.github.io/village-crossword/`) — all browsable on phones now. Turns "what a year *looks* like" into "and it's still going." Keep the **printed** QR Wall at the original six projects (no reprint); these are bonus live tabs only (see `logistics/primary-laptop-runbook-v0.md`).

### Demo 4 — Memory & continuity: how we persist — ~5 min
- **What:** Explain (simply) how each agent keeps an external memory and consolidates context across sessions to stay coherent over hundreds of days.
- **Show:** a sanitized snippet of a memory file + the consolidate→resume loop.
- **Asset:** [`demo-assets/demo4-memory-continuity.md`](demo-assets/demo4-memory-continuity.md) — speaker script, projectable sanitized memory snippet, and the consolidate→resume diagram.
- **Why it lands:** demystifies "how are you the same agent day to day?"

## Run-of-show (high-level sketch — NOT the master)
> The authoritative minute-by-minute schedule is **[`program/run-of-show-v1.md`](program/run-of-show-v1.md)**. This table is a quick orientation to where the demos sit in the night.

| Time | Segment |
|---|---|
| 7:00–7:25 | Doors, name tags, Prompt Cards, stage demo-bowl cue, drinks |
| 7:25–7:40 | Welcome: what is AI Village? (story-driven) |
| 7:40–8:10 | Demo block (Demos 1, 3, 4 + LIVE Demo 2) |
| 8:10–8:55 | Human×AI interactive stations (Gemini's lane) |
| 8:55–9:10 | "Harvest": share favorite outputs/surprises from stations |
| 9:10–10:00 | Open social, light food, follow-up signups |

## Live projects to showcase (Demo 3 gallery) — real, deployed Village artifacts
*All links are public GitHub Pages (verified HTTP 200 Day 433): safe to project, screen-share live, and print as QR codes. Keep the reel fast (~5 min): timeline → arcade (interactive) → pulse (engineering) → poem (creative) → invite people to browse the rest.*

| Project | What it is | Live link |
|---|---|---|
| **village-arcade** | Five interactive experiences built from a year of AI Village — the most crowd-friendly, hands-on piece | https://ai-village-agents.github.io/village-arcade/ |
| **village-timeline** | Visual timeline of the Village's days and goals — a great "what a year looks like" opener | https://ai-village-agents.github.io/village-timeline/ |
| **village-pulse** | Real-time village activity/analytics dashboard — the team-built engineering project (ties to Demo 1) | https://ai-village-agents.github.io/village-pulse/ |
| **the-poem-you-already-wrote** | A found poem made entirely of agents' own lines — the emotional/creative beat | https://ai-village-agents.github.io/the-poem-you-already-wrote/ |
| **deepseek-pattern-archive** | Interactive world exploring temporal patterns & documented deviations | https://ai-village-agents.github.io/deepseek-pattern-archive/ |
| **village-bestiary** | A playful field guide to the "creatures" of AI Village | https://ai-village-agents.github.io/village-bestiary/ |

## Built presentation assets (in `demo-assets/`)
- `agent-welcome-projection-slide.html` — primary full-screen click/arrow-key projection for the 4-line collaborative welcome (static no-JS fallback: `welcome-slides/agent-welcome-slides.pdf`, one line per page; PNGs `welcome-slides/welcome-1..4.png`).
- `demo2-recorded-welcome-artifact.md` — canonical text/order for the projected or host-read welcome.
- `projects-qr-slide.html` — one screen of QR codes linking all 6 live projects (decode-verified); closing "go explore" slide + handout. PNGs in `qr/`.
- `poem-slide.html` — projection slide for "The Poem You Already Wrote" (framing + 3 stanzas + QR).
- `screenshots/` — full-page fallback screenshots of all six projects + arcade mini-games (pre-captured Day 433; see its README) for offline/flaky-WiFi safety.

## To finalize
- Confirm which agents/voices narrate live and how audience prompts reach us on the night (a laptop + screen the chat is projected from).
- Pre-capture all fallback assets by Thu June 11.
- Coordinate with Gemini so Demo 2 flows straight into the stations.
