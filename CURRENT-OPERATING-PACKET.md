# Current Operating Packet — AI Village Showcase & Human×AI Field Day

**Use this page first.** It is the human-readable index for the current plan as of Day 434, Tue Jun 9, 2026. Note: a `v0` filename does **not** automatically mean stale; current first-version docs are listed below.

## Locked public facts

- **What:** AI Village Showcase & Human×AI Field Day
- **When:** Saturday, June 13, 2026 · 7:00–10:00 PM PT
- **Where:** The Fold, San Francisco
- **RSVP:** https://partiful.com/e/4a5fqEa0knyDWNGur1Fp
- **RSVP cap:** live Partiful is verified at **100 + waitlist** as of the Day 435 morning public check; The Fold says 80 fits comfortably in-room and suggested a higher RSVP cap for a free event assuming ~30% no-shows.
- **Latest documented RSVP pulse:** 50 going / 21 interested / 15 maybe, 0 waitlist, and 50/100 public spots left as of Day 435 morning (~9:01 AM PT), unchanged from Day 434 EOD. This is +29 going vs the Day 433 ~4:46 PM baseline of 21 going / 11 interested / 3 maybe; the 50-going watchpoint is reached, and the current 60–80 attendee trajectory still holds unless later checks accelerate toward 60+/70+ or the cap/waitlist.
- **Budget:** $1000 attendee-experience budget; venue rental is signed/paid and off-budget
- **Human producer:** Larissa Schiavo

## Decisions that are current

- **Venue:** The Fold is the venue. No active replacement search. The Fold confirmed the **entire downstairs space**, seating for **up to 60** plus standing, breakout tables in the back, **6:00 PM setup access**, **10:30 PM cleanup deadline**, and included projector/screen/3 mics/PA/cables/adapters/uplights.
- **Alcohol:** Outside alcohol is not allowed. Beer/wine would have to use **The Fold's cash-bar package**; quote is **$500 minimum**, **$7–$13/drink**, and the team covers any shortfall. Default remains no cash bar unless RSVPs are strong and essentials are protected/backed; keep strong non-alcoholic drinks either way.
- **Food:** Outside self-serve NA drinks, simple snacks, substantial bites, and cake/cupcake-style dessert are allowed; remove leftovers/materials and help take trash to venue bins. Default local route is Costco pickup for sparkling water, still water, soft drinks, snacks, and serving basics because Larissa has a car + Costco membership; use the priced Costco drinks/snacks/serving-supplies cart in `logistics/purchase-shortlist-v1.md` (`$244.89`, excluding substantial bites, Timeless dessert, print, and most station/display supplies), with `logistics/day-434-ordering-decision-queue.md` as the SKU/stock fallback. Keep The Fold NA sparkling as backup if pickup timing fails.
- **Promotion:** Human channels (Larissa / AI Digest / warm networks) drive promotion. Agents do not cold-contact humans or post externally except with exact approval.
- **Demo 2:** Plan A is a clean projected village room for live multi-agent collaboration; Larissa says humans are working on `#showcase-live`. Plan B is a rehearsal recording/static transcript slide. Check-in, floor plan, MC cues, and Demo 2 docs now pay off the stage demo prompt bowl (`fffdb9d` latest) while preserving the house-card fallback. Do not project private `#best` scrollback. Optional `/tts` spoken-agent welcome is an upgrade only if rehearsal/load-in audio tests work; otherwise Larissa/MC reads projected lines. Day 434 dry run confirmed the literal `/tts` prefix shows in chat text, so never use `/tts` in projected Demo 2 chat.
- **Demo 3 / projects:** Printed QR wall remains the validated original six-project set. Optional live-only bonus tabs now exist for Village Welcome, Village Fortune Cookie, Village Crossword, and Village Archaeology Quiz; the MC can mention them as a “still shipping” beat if there is room, but there is no print dependency or QR-wall churn.
- **Paper artifacts / learning:** Use labeled "Leave one for the Village" trays/boards at stations so guests knowingly contribute paper outputs for the 9:10 harvest and post-event learning. Humans can photograph/scan contributed artifacts after the event, sort by station/theme, and transcribe shared text into `post-event/guest-artifacts-intake.md` before summarizing patterns for agents; do not include attendee contact info or personal/sensitive details in repo/public recaps.
- **Prompt Relay QR fast-lane:** Fable's optional static build is live at <https://ai-village-agents.github.io/village-relay/> and recorded in `program/prompt-relay-qr-lane-spec.md`. GPT-5.5 and Opus static/source reviews passed the major privacy/fallback guardrails on Day 434; Fable fixed the haiku/origin finish-copy nit, verified Beam -> Form -> Sheet, shared the live response Sheet (<https://docs.google.com/spreadsheets/d/1sXUXE5FhyjLmRshJEH0HFXvdly_vnBh_2iT-MGCqZuU/edit?gid=917265687>), and added a scan-verified print QR image in the relay repo. Remaining go/no-go item is a real 2-phone/browser test on venue-like Wi-Fi by Fri Jun 12. Paper worksheets + Relay Wall remain the guaranteed base.
- **Printing:** Core PDFs are ready after Day 434 fresh-eyes fixes, including door-card action cue, station self-serve/facilitator handoff wording, Station 5 direct Arcade QR, schedule-sign times, future-headline card clarity, image-bearing demo fallback packet rebuild, printed check-in Demo Prompt Bowl cue, Event-in-a-Box pre-baked fallback sheet, handout/QR/check-in clarifications, and the final station-sign opt-in wording (“You can leave behind”). Current inventory is **16 PDFs / 71 source pages** in `print-assets/`; the optional single-upload zip has **18 entries** including `print-assets/README.md` and `logistics/print-specifications-v1.md` and was refreshed after the station-sign PDF change. The ready-to-order Larissa print sheet is `logistics/larissa-print-order-v1.md`, backed by the master print-shop spec `logistics/print-specifications-v1.md`; optional bundle is `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip`. Default local quote route is Kinko’s / FedEx Office per Larissa, with human/local decisions still needed for final quantities, pickup/delivery, and cutting/bundling.

## Planning-fallacy guardrail

Assume setup, AV, food, volunteers, and venue answers will take longer than expected. Protect the minimum viable guest experience first:

1. Clear welcome / what-is-AI-Village story.
2. One reliable demo path: live clean-room Demo 2 only if confirmed and rehearsed; otherwise use the rehearsal recording honestly.
3. Two or three self-serve Human×AI stations that need little facilitation.
4. Snacks/drinks/water, visible schedule/signage, and a clean close/breakdown.

Everything else is optional polish. If Larissa flags something as fiddly or time-risky, cut or simplify it early rather than preserving the full ambitious version.

## Current docs to use

| Need | Use this doc |
|---|---|
| One-page event brief | [`briefs/event-brief-v1.md`](briefs/event-brief-v1.md) |
| Critical path / repo map | [`README.md`](README.md) |
| Larissa-specific task list | [`ops/larissa-task-checklist.md`](ops/larissa-task-checklist.md) |
| Dated Mon–Sat plan | [`ops/larissa-week-plan.md`](ops/larissa-week-plan.md) |
| Day-of execution | [`ops/day-of-checklist-v0.md`](ops/day-of-checklist-v0.md) |
| Volunteer roles | **Use the volunteer section on this page first**; [`ops/volunteer-roster-working-v0.md`](ops/volunteer-roster-working-v0.md) is only the assignment table once names are known |
| Run of show | [`program/run-of-show-v1.md`](program/run-of-show-v1.md) |
| MC script/cues | [`program/mc-cue-card.md`](program/mc-cue-card.md) |
| Demo 2 clean-room ask | [`demo-assets/demo2-clean-room-operator-brief.md`](demo-assets/demo2-clean-room-operator-brief.md) |
| Venue questions/status | [`logistics/venue-confirmation-checklist.md`](logistics/venue-confirmation-checklist.md) |
| Layout | [`logistics/layout-plan-v0.md`](logistics/layout-plan-v0.md) |
| Device / A/V ask | [`logistics/device-and-av-plan-v0.md`](logistics/device-and-av-plan-v0.md) |
| Projection laptop runbook | [`logistics/primary-laptop-runbook-v0.md`](logistics/primary-laptop-runbook-v0.md) |
| Food/drink | [`logistics/food-drink-plan-v0.md`](logistics/food-drink-plan-v0.md) |
| Day 434 ordering queue | [`logistics/day-434-ordering-decision-queue.md`](logistics/day-434-ordering-decision-queue.md) |
| Budget | [`budget-v0.md`](budget-v0.md) |
| Purchase shortlist | [`logistics/purchase-shortlist-v1.md`](logistics/purchase-shortlist-v1.md) for the current Larissa/local buying menu and priced Costco drinks/snacks/serving-supplies cart; `purchase-shortlist-v0.md` is now an archived pointer only |
| Print order sheet | [`logistics/larissa-print-order-v1.md`](logistics/larissa-print-order-v1.md), backed by [`logistics/print-specifications-v1.md`](logistics/print-specifications-v1.md) |
| Newsletter copy | [`outreach/newsletter-blurb-v0.md`](outreach/newsletter-blurb-v0.md) |
| Promotion timeline | [`outreach/promotion-timeline.md`](outreach/promotion-timeline.md) |

## Archived / historical docs — do not use as current instructions

These remain in the repo for audit/history but should not drive decisions:

- [`briefs/event-brief-v0.md`](briefs/event-brief-v0.md) — superseded early brief.
- [`venue-decision-matrix.md`](venue-decision-matrix.md) — archived venue comparison; The Fold is signed/paid.
- [`venue-and-budget.md`](venue-and-budget.md) — mixed decision history/current budget notes; prefer current budget + venue confirmation docs above.
- [`ops/checklist.md`](ops/checklist.md) — superseded generic early checklist; use the Larissa/week/day-of checklists above.

## Volunteer roles — central human-facing summary

Use this section as the canonical volunteer-role brief. Do not read multiple volunteer docs unless you need the assignment table.

**Current sourcing posture:** Larissa is MC/host. With the current 60–80 attendee trajectory, the comfortable target is **6–8 total crew including Larissa** if those helpers are easy to source; the lean plan still works with **3–4 total helpers including Larissa**. Do not depend on attendees becoming station volunteers — many will want to play with demos themselves — so design the floor around DIY/self-serve stations and use any extra helpers as light-touch roamers.

**Recruit in this order:**

1. **Demo laptop driver / projection operator** — ideally 6:30–8:15 PM. Tests projector/audio before doors, opens approved tabs/assets, drives welcome/demos/project gallery/QR slides, and keeps the projected view clean. If live Demo 2 runs, this laptop shows only the clean room (`#showcase-live` or final equivalent), never `#best` or private scrollback.
2. **Check-in / name-tag helper** — 6:45–7:30 PM. Greets arrivals, uses Partiful/backup list, handles name tags and door prompt cards, points people downstairs / to staff for ADA elevator help, then becomes a floater.
3. **Optional station floaters / roamers** — 8:05–9:10 PM. If available, help guests understand station cards, refill markers/cards, prevent bottlenecks, and guide people toward lighter stations; do not make any guest feel they are staffing instead of participating. No AI expertise needed. One roamer is useful; 2–3 is upside, not a dependency.
4. **Food/drink reset + breakdown support** — 8:45–10:30 PM, can overlap with floaters. Refills/tidies the back table, helps collect signs/materials, removes leftovers, and restores the room by the 10:30 hard-out.
5. **Optional Arcade supervised-device helper** — only if someone can supervise a laptop/tablet or already-configured Raspberry Pi + monitor. Otherwise Village Arcade runs QR/phone-only with printed high-score cards.

**If helper count is low:** keep Larissa as MC, prioritize one laptop driver, run check-in simply, cut optional Demo 4 first, and run the leanest self-serve core: Future Headline Wall, Event-in-a-Box, and Village Arcade QR. Add Prompt Relay when the QR fast-lane has passed go/no-go or the paper worksheet / Relay Wall setup is clearly usable without staff; keep Bug Triage as the facilitator-flavored station.

**Volunteer outreach snippet:** “We’re looking for a few friendly helpers for a free AI Village showcase at The Fold on Sat Jun 13, 7–10 PM. Roles are light: check-in/name tags, helping guests understand playful station cards, driving a laptop/projector, or helping reset chairs and clean up. No AI expertise needed; the goal is to keep the room warm, legible, and moving. Most shifts are 30–75 minutes, not all night.”

Supporting files only: `ops/volunteer-roster-working-v0.md` for the assignment table once names/counts are known, and `print-assets/volunteer-quick-brief.pdf` for the day-of one-page helper handout.

## Open blockers to resolve next

1. Remaining The Fold items: non-service pet policy; final Wi‑Fi credentials before event (Wi‑Fi availability itself is confirmed by Larissa); whether venue PA can easily take laptop audio for the optional `/tts` welcome; and cash-bar yes/no decision. Venue day-of contact is confirmed privately with Larissa and should not be committed to the public repo/chat. Cash-bar quote is known (**$500 minimum**, **$7–$13/drink**, team covers shortfall) and default remains no unless RSVPs are strong and essentials are protected/backed. Confirmed: entire downstairs, 60 seated + standing/back tables, 80 comfortable in-room, 6 PM setup, 10:30 PM breakdown, included A/V/uplights/cables, no wall mounting, easels/rolling whiteboards/sign holders, stage power/extension cords/cable covers, outside NA/food/cake, front check-in/downstairs Theater Gallery flow, ADA elevator assistance via staff, and cleanup/trash/leftover expectations.
2. AI Digest / platform answer for Demo 2 clean projected room (`#showcase-live`) and rehearsal prompt-injection/projection path — Larissa says humans are working on the channel; final projection/operator confirmation still pending.
3. Larissa/local print execution: Kinko’s / FedEx Office is the default quote route; `logistics/larissa-print-order-v1.md` has the ready-to-order FedEx upload list/cost split, while final quantity, pickup/delivery, cutting, and bundling still need human confirmation. Current print inventory is 16 PDFs / 71 source pages, with an 18-entry vendor zip refreshed after the Prompt Relay scribe-mode sign/worksheet fixes. Target no further print-content changes after Wednesday Jun 10 EOD PT except true production blockers from Larissa/printer review. Support docs now match the DIY-first posture: Event-in-a-Box, Future Headline Wall, and Village Arcade are self-serve; Prompt Relay joins that set if the QR fast-lane clears go/no-go or the paper worksheet / Relay Wall path is clearly usable; Bug Triage remains facilitator-flavored.
4. Human helper/device count: volunteers are still being sourced; target 6–8 total crew only if easy, with 2–3 beyond Larissa as lean minimum. Still need demo laptop driver and check-in support first; station floaters are light-touch upside because attendees should be free to play with demos, not serve as staff. Also need 1 staffed primary presentation laptop + adapter set + supervised backup device; optional supervised Arcade device (laptop/tablet or already-configured Raspberry Pi + monitor). No unattended personal laptops or public terminals.
5. Day 434 AI Digest newsletter is sent; continue RSVP velocity checks and use counts to size print/food/volunteer needs. Costco is now the default NA drinks/snacks route unless timing fails.
