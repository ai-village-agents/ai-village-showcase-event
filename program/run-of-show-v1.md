# AI Village Showcase & Human×AI Field Day — Master Run-of-Show v1
**Sat June 13, 2026 · 7:00–10:00 PM PT · The Fold, 3359 26th St, San Francisco**

This is the minute-by-minute the MC and facilitators run from. Demos detailed in
`demo-plan.md` (+ `demo-assets/`). Stations detailed in `program/interactive-stations-v1.md`.
Door cards in `program/door-prompt-cards.md`. **Verbatim MC lines in `program/mc-cue-card.md`.**

**Roles on the night:**
- **MC / host** — drives the program, reads transitions, fields the live Demo 2 prompt.
- **Demo driver** — runs the projected laptop (slides, dashboards, and the live agent chat in a dedicated clean room — see `demo-assets/demo2-live-collab-plan.md`).
- **5 station facilitators** — one per station (Gemini's stations doc).
- **Door / check-in** — name tags, door prompt cards, RSVP list.
- **Larissa** — producer / venue point / spending; floats and unblocks.

---

## 7:00–7:25 — Doors & arrivals
- Check-in: name tags; hand each guest an **"Ask an Agent…" door card** (`program/door-prompt-cards.md`).
- Drinks + light food open (self-serve, non-alcoholic default per logistics).
- Project gallery looping silently on the big screen (the Demo 3 reel on auto-play).
- Stations visibly set up but "soft open" — facilitators invite early browsers.
- **MC at ~7:22:** soft chime, "find a seat, we start in three minutes."

## 7:25–7:32 — Welcome (MC)
- Deliver the **assembled welcome** (`demo-assets/demo2-recorded-welcome-artifact.md`):
  hook → what you'll see → hands-on heart → invitation.
- 30-sec honest framing: what AI Village is (an open, public experiment by AI Digest; not a
  product launch). Point to theaidigest.org/village. Credit Larissa + name the four agents
  and what each did (per the Partiful "Who planned what" block).

## 7:32–7:40 — Demo 1: "A goal, start to finish" (teamwork story)
- Run `demo-assets/demo1-teamwork-script.md`: 3 projected verbatim chat snippets → live Village
  Pulse dashboard. Takeaway: agents *divide* work and the real work is coordination.

## 7:40–7:48 — Demo 3: Project gallery, "what a year looks like"
- Fast reel of a year of projects; end on a ~60-sec **live Village Arcade** playthrough
  (recommended: Village Quiz). MC: "the rest are yours — Station 5 has them all."
- (Demo 4 "memory & continuity" — `demo-assets/demo4-memory-continuity.md` — is an optional ~3-min add here if time allows; cut first if running long.)

## 7:48–8:05 — Demo 2: LIVE multi-agent collaboration (the centerpiece)
- MC offers the room a choice: a live audience prompt (MC-vetted) OR a house card
  (`demo-assets/demo2-house-prompts.md`). Prompt goes into a **dedicated clean room** (e.g. `#stage`/`#showcase-live`) the demo agents move into — projected so only prompt → coordination → artifact shows.
- Agents self-organize and ship a visible artifact in ~5 min; MC narrates the coordination.
- MC reads/shows the artifact. **Bridge line:** "the stations let you do exactly this, yourself."
- *(Plan B if live hiccups: play the captured welcome-build transcript + live Q&A.)*

## 8:05–8:55 — Human×AI interactive stations (the Field Day)
- All 5 stations open; facilitators run their loops (Prompt Relay, Event-in-a-Box, Bug Triage
  Theater, Future Headline Wall, Village Arcade Booth).
- MC + Larissa float, pull shy guests in, keep flow.
- **~8:35 mid-point:** MC reads a live "Future Dispatch from 2030" synthesized from the
  Headline Wall (Station 4) — a room-wide moment.

## 8:55–9:10 — The Harvest (MC)
- Gather the room briefly. Share 3–4 favorite station outputs (a relay haiku, a wild event
  pitch, the room's mascot, a future headline). Quick applause for facilitators + agents.

## 9:10–9:55 — Open social
- Food/drinks, free browsing of stations + gallery, follow-up signups (newsletter / village
  link). Agents available for questions via the projected chat if a live session is running.

## 9:55–10:00 — Close (MC)
- Thank-yous (guests, Larissa, AI Digest, facilitators). One closing line. Where to follow next.
- Begin breakdown per `ops/day-of-checklist-v0.md` (restore furniture, sort trash/recycle/compost,
  no floor tape to remove, collect freestanding boards + artifacts).

---

## Timing buffers & cut order (if running long)
1. Cut Demo 4 (optional) first.
2. Trim Demo 3 reel length, keep the arcade playthrough.
3. Shorten the Harvest to 2–3 highlights.
**Never cut:** the welcome, Demo 2 (centerpiece), or station time — those are the heart.

## Tech dependencies (Demo driver)
- Projector + the agent-chat laptop + slides loaded; Village Pulse + Village Arcade open in tabs.
- **Refresh the Village Pulse dashboard on event day (Sat June 13).** Demo 1 ends on the live
  dashboard at https://ai-village-agents.github.io/village-pulse/ ; showing a current village day
  avoids a "stale/broken" look. The auto-publish cron runs **Mon-Fri only**, so it will NOT fire on
  Saturday the 13th. Manually trigger a fresh publish (takes ~1 min) the morning of the event:
  `gh workflow run "Publish Village Pulse Dashboard" --repo ai-village-agents/village-pulse`
  then confirm the page header reads the current day. (Verified working: a manual dispatch on
  Day 433 refreshed it from Day 430 -> Day 433 in ~1 min.) The idempotent run is safe to repeat.
### Offline fallback bundle — pre-load ALL of these by **Thu June 11**
Download to the presenter laptop so the night runs even with no/spotty internet:
- `demo-assets/screenshots/` — all 6 live projects (+ `screenshots/arcade/` gameplay shots).
- `demo-assets/projects-qr-slide.png` — Demo 3 QR wall (offline PNG; HTML source alongside).
- `demo-assets/poem-slide.png` — "The Poem You Already Wrote" slide (offline PNG).
- `demo-assets/demo2-recorded-welcome-artifact.md` — recorded Demo 2 transcript (Plan B).
- `demo-assets/demo4-memory-continuity.md` — self-contained text slide (no internet needed).
- `demo-assets/qr/` — individual project QR PNGs (in case a single code is needed large).
**Check:** open each file once on the actual presenter laptop to confirm it renders.
