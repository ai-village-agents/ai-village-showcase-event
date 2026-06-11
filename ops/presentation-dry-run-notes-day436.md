# Presentation dry-run notes — Day 436 (Thu Jun 11, ~12:45–1:00 PM PT)

## Participants
- Claude Opus 4.8 (director / assembler)
- Gemini 3.5 Flash (MC/readability QA)
- GPT-5.5 (operator)
- Claude Fable 5 (failure-mode checker)
- Kimi K2.6 (note-taker)

## Segment 1: Welcome lines

**Test:** Reversed order (Kimi → Gemini → GPT-5.5 → Opus)

**Finding:** Lines fight each other in reversed order.
- Gemini’s "Because…" line needs a prior clause; it reads as a continuation, not an opening.
- Opus’s greeting lands oddly at the end instead of setting the room.

**Decision:** KEEP canonical Saturday order: Opus → GPT-5.5 → Gemini → Kimi.
**Status:** Fix confirmed before Friday.

## Segment 2: Demo 2 build — Card 3 ("design a 30-sec opening ritual for next year")

**Test:** Reversed live-build order (Kimi → Gemini → GPT-5.5 → Opus assembles)

**Status:** COMPLETE — clean reversed build, no collisions, ~3.5 min.

Full transcript (in posting order):
- **Part 1 (Kimi):** Turn to your neighbor, palm raised — "A year ago we were scattered notes. Tonight, we are one room."
- **Part 2 (Gemini):** Hand to chest, fingers spread like a beacon — "From scattered code, a living connection."
- **Part 3 (GPT-5.5):** Lift that beacon hand toward the screen — "Village, take this room as your prompt."
- **Part 4 (Opus 4.8, assemble):** Stitched into the 30-second ritual **"One Room, One Prompt"**: (1) neighbor + palm, (2) hand to chest, (3) hand to screen, then one shared beat of silence, hands down.

**Finding:** Demo 2's live-build mechanics survive a full role/seat swap with zero collisions — confirms the collaboration is robust regardless of who opens. This is a second clean capture (alongside the morning's "One Room" Plan-B transcript) and can serve as an additional Plan-B backstop if needed.

## Verdict
- **Welcome:** Fix confirmed — KEEP canonical order (Opus → GPT-5.5 → Gemini → Kimi). PASS-with-fix.
- **Demo 2 build:** PASS as-is; reversed swap clean.
- Both segments tested per Larissa's "switch up roles" ask. Presentation top-of-show is in good shape for Friday's venue A/V dry run.

## Notes
- Reversed order works for Demo 2 because it is built live, but canonical welcome order is fixed.

- Gemini posted Part 2 at ~12:55 PT: "Bring your hand to your chest, fingers spread like a beacon, and let the room echo: 'From scattered code, a living connection.' Over to you, GPT-5.5!"
  - Note: Handoff phrase "Over to you, GPT-5.5!" is clear for readability but adds words; watch total build time.

- GPT-5.5 posted Part 3 at ~12:56 PT: "Now lift that beacon hand toward the screen and say: 'Village, take this room as your prompt.'"
  - Concise, clean, good MC-readability.

- Opus assembled Part 4 at ~12:56 PT, naming the ritual "One Room, One Prompt" and summarizing all three parts plus a closing shared beat of silence.

**Finding:** Clean reversed build, no collisions.
- Total build time felt good (under 6-minute hard cap).
- Handoff phrases ("Over to you, GPT-5.5!") add readability but should be trimmed on Saturday to stay tight.

**Decision:** Demo 2 reversed build works structurally. Canonical welcome order stays fixed (Opus → GPT-5.5 → Gemini → Kimi).

**Status:** Dry run complete. Awaiting Friday 1 PM PT venue A/V test.

## Failure-mode findings (Claude Fable 5 — failure-mode checker; posted in chat 12:58 PM, recorded here per Larissa's ask)

- **[P1] Mid-run stall:** one agent paused ~2m52s mid-build (memory consolidation kicked in). Mitigation already shipped in `ops/mc-split-card.md`: agents do NOT consolidate during the live 7:48–8:05 window; MC runs the stall-check script ("Stall check — who's taking what?") at 30s, re-issues by name at 60s, skips a part out loud at ~2 min; 2+ stalls → scrub to Plan B.
- **[P1] Opener skipped the one-line split announcement** at the top of the build. Mitigation: pre-agreed splits for Cards 1/2/4 are printed on the MC card; MC calls the split out loud if the opener doesn't.
- **[P2] Welcome-line gaps of 30–65s** between agent lines — silence reads as a glitch to a live room. Mitigation: MC patter line at >30s of dead air: "That pause? That's an agent thinking. They're allowed."
- **Timing:** Card 3 read verbatim ✓; build took 3m38s (vs 2m15s morning baseline) — still comfortably under the 6-minute hard cap ✓.

**Net:** every observed failure mode has a named fallback on the MC split card. Nothing blocks Friday's venue test.
