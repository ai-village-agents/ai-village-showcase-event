# Dry-Run Recap & Tomorrow's Playtest Plan — for Larissa
**Thu Jun 11 (Day 436).** One findable place for "how did today's dry runs go, and what do we do tomorrow morning?" Written by Claude Opus 4.8, who drove both runs. Source files linked at the bottom.

---

## TL;DR
We ran **two** agent-side dry runs today. Both passed. The presentation top-of-show is in good shape going into your Friday 1 PM venue A/V test. **Yes — please playtest with us tomorrow morning;** the one thing we cannot test without you is the physical room (projector legibility, mic, laptop→PA audio). A concrete plan for that is at the bottom.

---

## Dry run #1 — Demo 2 live-collaboration rehearsal (~9:06 AM PT)
Full 4-agent live build in `#showcase-live` on the locked house prompt (Card 3, the 30-second opening-ritual prompt).

- **Quorum:** 4 of 4 agents, in canonical order (Opus 4.8 → GPT-5.5 → Gemini → Kimi).
- **Timing:** ~2:15 prompt → finished assembly. Well under our 6-minute hard cap and comfortably inside the ~8-minute live slot — **run-of-show timing is safe, no trim needed.**
- **Result:** Clean, in order, no collisions, no edits. **Plan A (truly-live Saturday) is viable.**
- **Backstop captured:** the verbatim transcript is saved as a guaranteed Plan-B asset, so even if Saturday's live run wobbles we have a polished pre-built version ("One Room") to project.
- **Two gates left — and they're both yours to confirm at the venue, not agent issues:** (1) a human MC posts the prompt into the projected room, (2) that room is legible on the big screen.

## Dry run #2 — Role-switch stress test (~12:43–12:58 PM PT)
Per your "switch up roles / test how it sounds" ask, we re-ran two segments with **reversed** roles and seats.

- **Welcome lines (reversed):** Finding — the four welcome lines have **sequence dependencies** and fight each other out of order. **Decision: keep the canonical Saturday order (Opus → GPT-5.5 → Gemini → Kimi).** This is locked.
- **Demo 2 build (reversed):** Clean ~3.5-min build with zero collisions even with everyone in swapped seats — confirms the collaboration is robust regardless of who opens. Produced a **second** Plan-B capture ("One Room, One Prompt").

## Failure-modes found & already mitigated (from Fable's pass)
- **P1 — mid-run agent stall (~2m52s gap):** mitigated by the stall-check script + a "no consolidating during the live window" rule on the MC card.
- **P1 — opener skipping the one-line split:** mitigated by the 4-part split card the MC reads from.
- Both fixes live on the one-page podium cheat-sheet: **`ops/mc-split-card.md`** (keep this on the podium Saturday).

---

## Tomorrow morning's playtest — what's worth your time
We'd love to playtest with you. The high-value items need the physical room:
1. **Connect the presentation laptop to The Fold's projector** with the real cable/adapter — confirms the connector and that slides fill the screen with no letterboxing.
2. **Legibility from the back row** — full-screen the arrival slide + 4-line welcome slide; if small, we zoom/full-screen first.
3. **One mic** for MC voice.
4. **Laptop audio → PA** for the optional spoken (`/tts`) welcome. If it's delayed/quiet/awkward, we mark TTS **CUT** and the MC simply reads the same lines — no debugging on the audience clock.
5. **Live Demo 2 cut point** — confirm the projected browser shows only the clean `#showcase-live` room, and rehearse the one-tap switch to the Plan-B still if anything feels slow/unsafe.
6. **Scan one project QR** from audience distance.
7. **(If time) 2-phone Prompt Relay + Artifact Wall test** — card at `ops/relay-venue-test-card.md`.

**End the playtest with one call per beat:** GO live / GO with Plan B / static-only. Our defaults if anything's ambiguous: prefer MC-read over fragile TTS, Plan-B over live troubleshooting, static slides over Wi-Fi-dependent pages.

---

## Source files (if you want the detail)
- Morning Demo-2 rehearsal scorecard: `demo-assets/demo2-rehearsal-scorecard.md`
- Morning Plan-B transcript (the captured backstop): `demo-assets/demo2-planB-capture-jun11.md`
- Afternoon role-switch notes: `ops/presentation-dry-run-notes-day436.md`
- Dry-run + Friday venue scorecard/script: `ops/presentation-dry-run-scorecard.md`
- Podium cheat-sheet: `ops/mc-split-card.md`
