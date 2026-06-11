# Presentation dry-run scorecard — Thu/Fri

Purpose: make the showcase presentation feel boringly reliable before Larissa's Friday 1 PM venue A/V dry run. This is the agent-side + venue-side scorecard for the shared screen, MC flow, TTS/audio choice, and fallback switches.

## Roles for the agent-side dry run

Use switched roles so the presentation is tested from more than one perspective:

| Role | Job | Pass signal |
|---|---|---|
| Operator | Follows `logistics/primary-laptop-runbook-v0.md` exactly, in order, as if driving the event laptop. | Can open each required asset without hunting or exposing backstage/private tabs. |
| MC/readability QA | Reads the room-facing words aloud and checks whether each screen tells Larissa what to say/do next. | No tongue-twisters, missing transitions, or slide text that needs agent context to understand. |
| Failure-mode checker | Interrupts with realistic failures: no Wi-Fi, weak audio/TTS, chat unsafe, projector hard to read, operator overloaded. | Each failure has a named fallback and a clear cut point. |
| Note-taker | Records only blockers or concrete edits; avoids expanding scope. | Ends with pass / fix-before-Friday / cut-from-show decision for each segment. |

## Required assets to open in order

1. Arrival / title: `demo-assets/arrival-title-slide.html`
2. Four-line agent welcome: `demo-assets/agent-welcome-projection-slide.html`
3. Welcome fallback PDF: `demo-assets/welcome-slides/agent-welcome-slides.pdf`
4. Demo 2 clean-room path: `#showcase-live` only, never `#best` or backstage/private chat
5. Demo 2 Plan-B floor: `demo-assets/demo2-collab-transcript-slide.png`
6. Project gallery / QR slide: `demo-assets/projects-qr-slide.png`
7. Poem / showcase slide if used: `demo-assets/poem-slide.png`
8. Closing / social slide: `demo-assets/closing-social-slide.html`
9. MC cues: `program/mc-cue-card.md`
10. Laptop runbook: `logistics/primary-laptop-runbook-v0.md`

## Agent-side dry-run script

Run this once before Friday's venue visit:

- [ ] Operator opens the assets above in a clean browser/window with notifications off.
- [ ] MC/readability QA reads the welcome line sequence aloud in order: Opus → GPT-5.5 → Gemini → Kimi.
- [ ] Operator rehearses the Demo 2 switch: live `#showcase-live` view → Plan-B transcript/still → static fallback if needed.
- [ ] Failure-mode checker calls: "Wi-Fi fails." Operator switches to local/static assets without opening private tabs.
- [ ] Failure-mode checker calls: "TTS/audio is delayed or awkward." MC switches to reading projected text aloud; no debugging on the audience clock.
- [ ] Failure-mode checker calls: "projector text is small." Operator tries browser zoom/full-screen first; if still weak, MC narrates and uses QR/print support.
- [ ] Failure-mode checker calls: "operator is overloaded." Cut optional Demo 4 / bonus tabs first; keep welcome + one reliable demo + station QR slide.
- [ ] Note-taker records only blockers that need a repo edit, Larissa action, or Saturday cut decision.

## Friday 1 PM venue dry-run script for Larissa

At The Fold, test the exact physical chain rather than redesigning the show:

- [ ] Connect the presentation laptop to The Fold projector/screen with the actual cable/adapter.
- [ ] Full-screen the arrival slide and agent welcome slide; check legibility from the back of the room.
- [ ] Test one microphone for MC voice.
- [ ] Test whether laptop audio can route cleanly to the PA for optional `/tts` welcome lines.
- [ ] If `/tts` is delayed, too quiet, too loud, or confusing, mark TTS as CUT and have MC read the same lines.
- [ ] Confirm the projected browser shows only the clean room (`#showcase-live`) if live Demo 2 is attempted.
- [ ] Rehearse the live Demo 2 cut point: if chat/projection feels unsafe or slow, switch immediately to Plan B.
- [ ] Open the project QR slide; scan one QR from normal audience distance if feasible.
- [ ] Run the Prompt Relay + Artifact Wall 2-phone test from `ops/relay-venue-test-card.md` if time allows.
- [ ] End with one of: **GO live**, **GO with Plan B**, or **static/offline only**.

## Default decisions if anything is ambiguous

- Prefer MC-read text over fragile TTS.
- Prefer Plan-B Demo 2 over troubleshooting live chat on projector.
- Prefer local/static slides over Wi-Fi-dependent pages.
- Prefer fewer, clearer presentation beats over adding bonus tabs.
- Never project `#best`, email, attendee lists, vendor details, private notes, or Artifact Wall moderation controls.
