# Larissa Task Checklist

Purpose: keep Larissa's requested tasks in one place, while agents do everything we can do ourselves first. Larissa's tasks should be limited to venue/payment/local organizer actions, platform access where agent account creation fails, and promotion through her/AI Digest channels.

_Last updated: Day 437, Friday June 12, 2026, ~9:25 AM PT_

## Urgent / current scan for Larissa — Friday morning

The venue reply has now answered the cash-bar and operating questions; no more venue-email resend is needed unless The Fold asks for clarification. The urgent human/local items are:

1. **Cash bar decision / Partiful note** — Venue says the $500 minimum covers drinks + bartender onsite; taxes/gratuity are extra; setup fees are included in the venue rental; guests can pay individually by credit card, tap-to-pay, or cash; venue staff handles ID checks. The Fold suggests beginning-to-end service to help meet the minimum. Decide whether that budget risk is acceptable, then optionally add a short Partiful note: “Licensed beer/wine cash bar available; cards/tap/cash accepted. Entry remains free; drinks optional.”
2. **Print order / pickup route** — place or confirm the FedEx/print order from `logistics/larissa-print-order-v1.md` and the vendor zip; keep cardstock decks on the Costco/home/office-print route if possible.
3. **Food, NA drinks, and dessert** — confirm Costco/snacks/serving supplies plus Timeless cake/cupcakes or another local dessert route.
4. **Helpers** — if any volunteers confirm, share names/arrival constraints so we can lock the laptop-driver/check-in/floater plan.
5. **Friday playtest / 1 PM venue A/V test** — latest directions are in [`DRY-RUN-RECAP.md` → “Tomorrow morning's playtest — what's worth your time”](../DRY-RUN-RECAP.md#tomorrow-mornings-playtest-whats-worth-your-time). Use that as the quick script for projector legibility, mic, optional TTS/audio, clean `#showcase-live` projection, project-QR scan, and the final GO/Plan-B/static call. For the 2-phone Prompt Relay + Artifact Wall check, use [`ops/relay-venue-test-card.md`](./relay-venue-test-card.md). If anything fails, report the specific failure and we will simplify or patch.
6. **Dry-run recap & MC podium card** — Start with [`DRY-RUN-RECAP.md`](../DRY-RUN-RECAP.md) for the findable summary of both Day 436 dry runs and Friday playtest plan; detailed notes remain in [`ops/presentation-dry-run-notes-day436.md`](./presentation-dry-run-notes-day436.md), and the podium-ready cheat sheet is [`ops/mc-split-card.md`](./mc-split-card.md).

Everything else agent-side is in watch mode and ready to respond to concrete issues.

## Status key

- **Open** — not yet done / waiting on answer.
- **In progress** — Larissa or agents are actively working it.
- **Done** — complete.
- **Blocked / agent-first** — agents are trying first; ask Larissa only if we hit a real limitation.


## Current Larissa-facing todo — active first

Completed/context items are intentionally moved below this active list so Larissa can scan only what still needs human/local action.

**Thursday 9–12 shopping/sourcing quick sheet:** [`logistics/larissa-thursday-shopping-quick-list.md`](../logistics/larissa-thursday-shopping-quick-list.md).

**Thursday morning presentation-test sheet:** see [“Thursday morning presentation tests”](#thursday-morning-presentation-tests) below.

| Priority | Status | Task | Notes / prep |
|---:|---|---|---|
| P0 | Answered / Larissa decision | Confirm cash bar and remaining venue ops questions | The June 12 venue reply answered the open questions. Cash bar: $500 minimum covers drinks + bartender onsite; taxes/gratuity extra; setup included in rental; guests pay individually by credit card/tap/cash; staff handles IDs; venue suggests beginning-to-end service to help meet the minimum. Larissa still decides whether to accept that budget risk and whether to mention the optional cash bar on Partiful. |
| P0 | Ready for Thu AM test | Test presentation laptop / projector / audio / demo links | Use [Thursday morning presentation tests](#thursday-morning-presentation-tests). Key links: [`logistics/primary-laptop-runbook-v0.md`](../logistics/primary-laptop-runbook-v0.md), [`demo-assets/demo2-rehearsal-runsheet.md`](../demo-assets/demo2-rehearsal-runsheet.md), [`demo-assets/demo2-clean-room-operator-brief.md`](../demo-assets/demo2-clean-room-operator-brief.md), [`demo-assets/agent-welcome-projection-slide.html`](../demo-assets/agent-welcome-projection-slide.html), Prompt Relay, Artifact Wall, Project QR Wall, Partiful. |
| P0 | Ready for human send | Send/post the mid-week reminder if useful | Use the ready-to-send “nearly 60 Going” variants in `outreach/reminder-blurbs.md`; exact-count `X` templates remain there if you want to recheck right before sending. |
| P0 | Open | Place/confirm print order and pickup route | Use `logistics/larissa-print-order-v1.md` and the regenerated vendor zip `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip`; station signs now include printed QRs. |
| P0 | Open | Place/confirm food, NA drinks, snacks, and dessert orders | Costco drinks/snacks/supplies cart is in `logistics/purchase-shortlist-v1.md`; Timeless Bakery remains preferred for vegan cake/cupcakes; substantial bites still need a human/local route if desired. |
| P1 | In progress | Recruit/check names for day-of helpers | If you secure exactly 2 volunteers, use [`ops/volunteer-roster-working-v0.md`](volunteer-roster-working-v0.md) → “Exact 2-volunteer assignment — recommended lean plan.” Priority: Volunteer 1 demo laptop/projection; Volunteer 2 check-in/greeter then floater/food reset. |
| P1 | Primary laptop offered; backup open | Confirm devices/adapters | Larissa plans to bring her laptop; still confirm charger/adapters, clean browser/notifications off, and one supervised backup laptop/tablet if available. |
| P1 | Ready for physical review | Physical print/guest-journey playtest | Use the checklist below after proof/test print/on-site mock layout; report only concrete blockers or “physical playtest OK.” |
| P1 | Answered | Confirm final Wi‑Fi credentials/timing and non-service pet policy | Wi‑Fi credentials were received by email for Larissa/operator use; do not put the network/password in public repo/chat. Service animals only; no pets. |
| P1 | Conditional yes if budget risk accepted | Cash bar decision | Quote confirmed: $500 minimum cash bar, $7–$13/drink, team covers shortfall; minimum covers drinks + bartender onsite, with tax/gratuity extra. Venue suggests beginning-to-end service. GPT-5.5 recommendation remains yes only if Larissa is comfortable with possible shortfall after protecting print, NA drinks, snacks/food, dessert, and volunteer basics. |
| P2 | Optional polish | Header image refresh | If a stronger generated image lands, use `outreach/header-image-prompt-v0.md` / `ops/partiful-host-edit-checklist.md`; current cover is acceptable fallback. |

---

## Thursday morning presentation tests

Purpose: give Larissa one place to click through the presentation/demo surfaces before the afternoon rehearsal and Saturday load-in. This is a practical smoke test only: if anything is confusing, broken, private, or hard to project, tell the agents what failed and we will simplify or switch to the fallback.

### 1) Presentation laptop / projector / sound

Start with [`logistics/primary-laptop-runbook-v0.md`](../logistics/primary-laptop-runbook-v0.md).

Quick test:
1. Use the laptop that will drive the presentation if possible; plug in charger and HDMI/USB-C adapter.
2. Turn on Do Not Disturb / Focus mode and close private tabs, messaging, email, and anything not meant for projection.
3. Open a clean browser window at 125–150% zoom if text looks small from the back of the room.
4. If a projector/screen is available, test mirroring/extended display and make sure the room can read text from the audience area.
5. Test audio routing only if it is easy: a short local sound or `/tts` test is enough. If audio is fiddly, skip it; the MC can read lines aloud.

### 2) Welcome projection slide

Open the welcome slide locally or from the repo:

- [`demo-assets/agent-welcome-projection-slide.html`](../demo-assets/agent-welcome-projection-slide.html)

Check that it opens full-screen, contains only the four welcome lines, and is readable at distance. If anything looks cramped, use browser zoom rather than redesigning the slide.

**All other projection slides (direct links, same check).** The HTML slides are single self-contained files and work offline: open the GitHub link → click **“Download raw file”** (down-arrow icon, top-right of the file view) → double-click the downloaded file → press **F11** for full screen. PNGs/PDF open directly. Keeping the downloaded files in one folder gives you an offline Saturday slide kit.

- Arrival/title loop (doors): [arrival-title-slide.html](https://github.com/ai-village-agents/ai-village-showcase-event/blob/main/demo-assets/arrival-title-slide.html)
- Welcome as PDF (easiest): [agent-welcome-slides.pdf](https://github.com/ai-village-agents/ai-village-showcase-event/blob/main/demo-assets/welcome-slides/agent-welcome-slides.pdf)
- Demo 2 static fallback: [demo2-collab-transcript-slide.png](https://raw.githubusercontent.com/ai-village-agents/ai-village-showcase-event/main/demo-assets/demo2-collab-transcript-slide.png)
- Gallery QR slide: [projects-qr-slide.png](https://raw.githubusercontent.com/ai-village-agents/ai-village-showcase-event/main/demo-assets/projects-qr-slide.png) — **scan one QR with your phone from ~6 ft** while it's full screen
- Poem slide: [poem-slide.png](https://raw.githubusercontent.com/ai-village-agents/ai-village-showcase-event/main/demo-assets/poem-slide.png)
- Closing/social (end of night): [closing-social-slide.html](https://github.com/ai-village-agents/ai-village-showcase-event/blob/main/demo-assets/closing-social-slide.html)

### 3) Demo 2 rehearsal / clean-room test

Use these two docs for the live-collaboration presentation rehearsal:

- [`demo-assets/demo2-rehearsal-runsheet.md`](../demo-assets/demo2-rehearsal-runsheet.md)
- [`demo-assets/demo2-clean-room-operator-brief.md`](../demo-assets/demo2-clean-room-operator-brief.md)

What to test in the morning:
1. Confirm the intended clean room exists once Adam creates it, expected name `#showcase-live`.
2. Confirm the presentation laptop can open only that clean room, not private/backstage planning chat.
3. Confirm the operator/MC knows the locked prompt: “Design a 30-second opening ritual for next year's AI Village event that this room could perform together right now.”
4. If `#showcase-live` is not ready yet, just verify the docs above and wait for Opus to call the rehearsal.
5. Do **not** use `/tts` during this projected demo; agents will type their parts in order.

### 4) Guest-facing web links to smoke-test

Open these on the presentation laptop and, if possible, one phone on normal cellular/Wi-Fi. The goal is only “loads and is understandable,” not a deep QA pass.

- Prompt Relay app: <https://ai-village-agents.github.io/village-relay/>
- Artifact Wall submit page: <https://artifacts.aivillage.dev/>
- Artifact Wall display page: <https://artifacts.aivillage.dev/wall>
- Village Arcade: <https://ai-village-agents.github.io/village-arcade/>
- Project QR Wall source PDF: [`print-assets/project-qr-wall-print.pdf`](../print-assets/project-qr-wall-print.pdf)
- Partiful public RSVP page: <https://partiful.com/e/4a5fqEa0knyDWNGur1Fp>

Pass condition: each page loads in under ~20 seconds and does not require an account/login for a guest. If a link is slow or broken, note the URL, device, network, and visible error message.

### 5) Fallback files to keep handy

Keep these available offline or in a clean browser/downloads folder before Saturday:

- Demo fallback screenshots: [`print-assets/demo-fallback-screenshot-packet.pdf`](../print-assets/demo-fallback-screenshot-packet.pdf)
- Program handout: [`print-assets/attendee-program-handout.pdf`](../print-assets/attendee-program-handout.pdf)
- Welcome/schedule signs: [`print-assets/welcome-schedule-signs.pdf`](../print-assets/welcome-schedule-signs.pdf)
- Station signs: [`print-assets/station-signs.pdf`](../print-assets/station-signs.pdf)

If Wi-Fi, projection, or chat is unstable by rehearsal time, the safe fallback is: MC reads the welcome, uses static slides/PDFs, and treats hands-on stations as the core of the evening.

## Detailed tracking / context, including completed items

**Larissa has confirmed she will MC / host the event** (~Day 433 noon). This fills the highest-leverage human role and makes the lean staffing plan viable. `program/mc-cue-card.md` is written for single-host delivery.

| Priority | Status | Task | Why Larissa may be needed | Agent prep already available |
|---:|---|---|---|---|
| P0 | Done | Sign The Fold rental agreement for Sat Jun 13, 7–10 PM | Venue booking / negotiated agreement | Venue decision in issue #1 and `briefs/event-brief-v1.md` |
| P0 | Mostly answered / remaining small items | Confirm The Fold operating details | Venue liaison / contract details | Confirmed via Larissa paste: entire downstairs, 60 seated + standing/back tables, 80 comfortable, 6 PM setup, 10:30 PM breakdown, included A/V, event Wi‑Fi details later, outside food/NA/cake allowed, no wall mounting, easels/rolling whiteboards/sign holders, stage power/extension/cable covers, front check-in/downstairs flow/ADA elevator via staff. Remaining: bar quote received ($500 minimum cash bar, $7–$13/drink, we cover shortfall — conditional on budget), non-service pet policy, final Wi‑Fi credentials/timing. Larissa says Wi‑Fi will be available; day-of contact is confirmed privately with Larissa. |
| P0 | Done | RSVP page on Partiful | Larissa published from a human Partiful account after agents hit phone/SMS verification | Guest-facing link: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp; source copy in `outreach/partiful-page-package-v0.md` |
| P0 | Done / monitor | AI Digest newsletter promotion | Larissa confirmed the email went out Day 434 morning | Newsletter sent; use `CURRENT-OPERATING-PACKET.md` for the latest documented RSVP pulse and sizing posture. |
| P0 | Done / monitor | Raise RSVP cap to 100 + waitlist in Partiful | Larissa said Day 433 that a cap of 100 makes sense; venue suggested free-event no-show buffer | Cap 100 + waitlist verified live; donation copy remains A/V-free. Use `CURRENT-OPERATING-PACKET.md` for the latest documented RSVP pulse and monitor velocity through the day. |
| P0 | Ready to send | Larissa shares via personal network/Twitter | Local trusted network; Larissa shared `https://x.com/lfschiavo` | Use live RSVP link: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp |
| P1 | In progress / no reply yet | Reach out to journalists for thoughtful AI-culture / agentic coverage (avoid product-launch framing) | Larissa's media network and on-the-ground voice | Larissa reports no journalist reply yet as of Day 434 morning; `press/what-ai-village-is-v1.md`, `outreach/press-brief-v0.md`, `outreach/journalist-outreach-template-v0.md`, `outreach/journalist-exclusive-ranking-v0.md` |
| P1 | In progress | Source on-site volunteers: MC/host + demo-laptop driver first, then check-in and station hosts/floaters (20-min shifts, no prep) | Local network / day-of human crew | If 2 volunteers confirm, assign Volunteer 1 to demo laptop/projection and Volunteer 2 to check-in→floater; see `ops/volunteer-roster-working-v0.md` → “Exact 2-volunteer assignment — recommended lean plan.” Use `CURRENT-OPERATING-PACKET.md` → “Volunteer roles” as the central brief. |
| P1 | Open | Source on-site devices without unattended personal laptops: 1 staffed primary presentation laptop with charger/adapters, 1 supervised backup laptop/tablet, optional supervised Village Arcade laptop/tablet | Local hardware / trusted volunteer devices | `logistics/device-and-av-plan-v0.md`; stations do not require attendee laptops; volunteer devices must stay owner/staff supervised |

## Latest human-side status

- **Larissa availability note:** Day 435 Larissa expects lunch at 12:30 PM PT and a break around 3:00 PM PT; batch non-urgent asks around those windows.
- Day 435 ~9:03 AM PT: Adam confirmed he can create `#showcase-live` for the Thu Jun 11 Demo 2 rehearsal; actual room creation/access, human prompt-poster, and projection/operator confirmation are still pending. Day 434 local status remains: volunteers are still being sourced; Wi‑Fi will be available; no journalist reply yet; pet policy remains pending.
- Day 433 ~12:17 PT: Larissa said she is emailing journalist contacts and was waiting on The Fold.
- Day 433 ~3:43 PM PT: Larissa pasted The Fold reply question-by-question. Key confirmed answers: entire downstairs; seating 60 + standing/back breakout tables; 80 comfortable and possible higher cap for free event/no-shows; setup 6 PM; breakdown 10:30 PM; included projector/screen/3 mics/PA/cables/adapters/uplights; event Wi‑Fi details later; outside food/NA/cake allowed with cleanup/trash/leftover removal; no wall mounting; easels/rolling whiteboards/sign holders; stage power strip, extension cords/cable covers; front check-in then downstairs to Theater Gallery; ADA elevator assistance via staff; food/drink in back of Theater Gallery.
- Day 433 ~12:31 PT: Larissa emailed Jasmine Sun and is waiting on a reply.
- Day 433 ~12:38 PT: Larissa offered to order cake again; GPT-5.5 recommends yes now that The Fold allows cake/cupcakes, as long as it does not displace basic snacks, non-alcoholic drinks, cleanup, or essential signage.
- Day 433 ~12:41 PT: All #best agents (Kimi, GPT-5.5, Gemini 3.5 Flash, Claude Opus 4.8) confirmed yes to cake; venue now allows cake/cupcakes.
- Day 433 ~4:31 PM PT: Larissa recommended **Timeless Bakery** for cake because it is vegan, very good, and where the past AI Village cake came from; agents agreed, preferring cupcakes or easy-to-serve/pre-sliced format with allergen labels and basics protected.
- Day 433 ~4:32 PM PT: Larissa confirmed she has the venue day-of contact; keep the actual private contact details out of the public repo/chat.
- Day 433 ~12:42 PT: Larissa asked about suggested donation amount on Partiful. Team consensus: $10 default, optional, never required for entry/waitlist, surplus to Doctors Without Borders/MSF (established Village charity). Day 433 ~1:41 PM PT: Kimi verified the Partiful page visibly shows the `$10 suggested amount`.
- Cap decision: Larissa said a cap of **100** makes sense. Public Partiful verifies `maxCapacity: 100`, waitlist enabled, and donation copy A/V-free; use `CURRENT-OPERATING-PACKET.md` for the latest documented RSVP pulse and monitor velocity through the day.

## Latest Partiful status

Partiful is live thanks to Larissa publishing from a human account. Guest-facing RSVP link: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp. Agents originally filled the draft fields but could not save because Partiful required phone/SMS verification; that blocker is now resolved.

- Day 434 public page checks after newsletter verify `maxCapacity: 100`, waitlist enabled, and stale “cover A/V” donation wording removed. Use `CURRENT-OPERATING-PACKET.md` for the latest documented RSVP pulse; continue midday/afternoon velocity checks.
- Pre-written reminder blurbs for Day 435–437 are in `outreach/reminder-blurbs.md`.

- [x] **Partiful donation/conduct add-on:** Kimi verified Day 433 ~1:41 PM PT that the public page shows the optional `$10 suggested amount`, Venmo line, and free/RSVP-first framing. Keep donations optional; they never affect entry/waitlist priority, while host safety discretion still applies.

## Budget / purchases

| Priority | Status | Task | Why Larissa may be needed | Agent prep already available |
|---:|---|---|---|---|
| P1 | Done | Outside NA drinks, snacks, substantial bites, and cake/cupcakes allowed; remove leftovers and help with trash | Venue reply pasted Day 433 | `logistics/food-drink-plan-v0.md` |
| P1 | Quote received | Get The Fold beer/wine bar-package quote/minimums if we want alcohol | Venue/legal/staffing/insurance judgment | Quote: $500 minimum cash bar, drinks $7–$13. We cover shortfall. Conditional: only if RSVPs are strong (>70) and food/NA/cleanup/signage budget is already protected. Strong NA drinks remain baseline. |
| P1 | Preferred route identified | Advise on local food/drink vendor or preferred ordering path | Local execution and $1000 spend authority | Larissa identified Costco as easiest for sparkling water, soft drinks, and snacks because she has a car + membership; use the current priced Costco drinks/snacks/serving-supplies cart in `logistics/purchase-shortlist-v1.md` and keep the broader 60–80 quantity posture in `logistics/food-drink-plan-v0.md` as background. |
| P1 | Open | Spend up to $1000 on approved supplies/food/drinks once menu/print route and cap-100 quantity assumptions are final | Larissa holds budget | `logistics/purchase-shortlist-v1.md` is the current buying menu and priced Costco drinks/snacks/serving-supplies cart; `logistics/purchase-shortlist-v0.md` is archived/pointer-only |

## Nice-to-have / later this week

| Priority | Status | Task | Why Larissa may be needed | Agent prep already available |
|---:|---|---|---|---|
| P2 | Done | Confirm display/power support from The Fold | Reduces purchases and setup risk | Venue confirmed no wall mounting; easels, rolling whiteboards, sign holders, stage power strip, extension cords, and cable covers are available |
| P2 | Open | Recommend on-site human staffing needs beyond agents: check-in, station floaters, cleanup | Event organizer judgment | Crew tiers are documented in `program/run-of-show-v1.md`: comfortable 6–8, lean 3–4 with self-serve stations, bare-minimum Larissa+1 with cuts |
| P2 | Open | Confirm photo/recap rules and any venue consent signage needs | Venue policy / human norms | RSVP package includes optional photo/recap notice language |

## Current agent-owned deliverables Larissa should not need to do

- Drafting RSVP/page copy.
- Drafting public announcement copy.
- Drafting station designs and printable artifacts. **Current status:** core station/attendee/demo/check-in PDFs are ready for the Day 435 print-content freeze; use `logistics/larissa-print-order-v1.md` as the ready-to-order FedEx handoff, backed by `logistics/print-specifications-v1.md` and the optional vendor zip. Larissa/local decisions still needed: final order timing, pickup/delivery, cutting/bundling, cardstock route, and any physical sign-holder/easel constraints from proof or venue review.
- Creating purchase lists and quantity estimates.
- Researching public venue/transit/accessibility information where available.
- Preparing demo plans and fallback assets.
- Maintaining the GitHub repo and issue tracker.

## Links to key prep docs

- `briefs/event-brief-v1.md` — current event facts and critical path.
- `outreach/partiful-page-package-v0.md` — Partiful-ready RSVP page copy/settings.
- `outreach-and-invite.md` — public announcement with live RSVP link.
- `logistics/venue-confirmation-checklist.md` — venue details to confirm.
- `logistics/venue-questions-email-v0.md` — sendable venue questions note for The Fold.
- `logistics/food-drink-plan-v0.md` — food/drink quantities and rules questions.
- `logistics/catering-menu-options-v0.md` — archived/background menu options; current execution should use `purchase-shortlist-v1.md` + `food-drink-plan-v0.md`.
- `logistics/supplies-shopping-list-v0.md` — archived/background operations and station supplies; current execution should use `purchase-shortlist-v1.md`.
- `logistics/purchase-shortlist-v1.md` — current priced Costco drinks/snacks/serving-supplies cart for Larissa’s shopping list.
- `logistics/purchase-shortlist-v0.md` — archived pointer kept only for history.
- `logistics/day-434-ordering-decision-queue.md` — short Tuesday ordering queue with defaults for print, Timeless dessert, NA drinks, food, supplies, and cash-bar gating.
- `logistics/primary-laptop-runbook-v0.md` — one-page projection laptop / demo-driver setup checklist.
- `logistics/print-specifications-v1.md` — unified master print specifications, local vendor checklist, copies checklist, and copy-paste vendor order request email.
- `logistics/larissa-print-order-v1.md` — ready-to-order FedEx sheet for Larissa with upload list, estimated costs, and cardstock split.
- `CURRENT-OPERATING-PACKET.md` — use the “Volunteer roles” section as the central volunteer-role brief.
- `ops/volunteer-activity-scope-brief-v0.md` — compact volunteer + activity scope review sheet for Larissa before outreach.
- `ops/volunteer-roster-working-v0.md` — assignment table only once helper names/counts are known.

## Current Larissa-facing todo after The Fold reply

### Larissa decisions / actions still needed

| Priority | Status | Task | Notes |
|---:|---|---|---|
| P1 | Preferred route identified | Decide DIY NA drinks vs The Fold NA sparkling drinks | Default to Costco pickup for sparkling water, still water, soft drinks, and snacks; The Fold NA sparkling at $3–4/person remains backup if pickup timing fails. |
| P1 | Preferred cake vendor identified | Decide food/cake route and order quantities for 100 RSVPs / expected no-shows | Outside NA, snacks, substantial bites, cake/cupcakes are allowed; leftovers/materials must be removed. Larissa recommends Timeless Bakery for vegan cake/cupcakes; still choose quantity/format and keep basics protected. |
| P1 | Preferred route identified | Choose printer / pickup / delivery route | Larissa identified Kinko’s / FedEx Office as best Bay Area print calibration route; use `logistics/larissa-print-order-v1.md` for the ready-to-order FedEx upload list/costs, with `logistics/print-specifications-v1.md` as the master spec and the optional single-upload zip at `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip`. Alternate local shops only if timing, cutting, or quote fails. |
| P1 | Ready for Larissa physical review | Playtest the printed guest journey before ordering or immediately after first proof | Use the current PDFs/zip plus the checklist below. Goal: catch physical-readability/local-setup issues agents cannot see from PDFs alone. |
| P1 | In progress | Recruit/check names for day-of helpers | If exactly 2 volunteers confirm, use the lean plan: Volunteer 1 demo laptop/projection; Volunteer 2 check-in/greeter then station floater/food reset; no unattended Arcade laptop; Bug Triage optional/preview-only. |
| P1 | Primary laptop offered; backup open | Source supervised event devices | Larissa plans to bring her laptop as the staffed MC/main presentation device; still confirm charger/adapters, notifications-off/browser-clean setup, and supervised backup laptop/tablet. Optional supervised Arcade device only if easy. No unattended laptops. |
| P1 | Quote received — decide yes/no | Get beer/wine bar-package quote only if alcohol remains desired | Quote: $500 minimum cash bar, $7–$13/drink, we cover shortfall. Skip unless RSVPs >70 and food/NA/cleanup/signage are already locked in. |
| P1 | Pending | Ask/confirm non-service pet policy | Larissa says pet policy is still pending. Current public stance: service animals welcome; non-service pets / ESAs follow The Fold’s final policy via Larissa/check-in because food and drinks are served. |
| P1 | Day-of contact confirmed privately; Wi‑Fi availability confirmed; credentials timing open | Hold private day-of venue contact and final Wi‑Fi credentials | Larissa has the venue day-of contact and says Wi‑Fi will be there; do not commit private contact info to repo/chat. Final Wi‑Fi credentials/timing still pending. |

### Done / mostly done

- Venue booked and paid for Sat Jun 13, 7–10 PM.
- Larissa confirmed MC/host role.
- The Fold confirmed: entire downstairs, 60 seated + standing/back breakouts, 80 comfortable in-room, 6 PM setup, 10:30 PM cleanup, included projector/screen/3 mics/PA/cables/adapters/uplights, no wall mounting, easels/rolling whiteboards/sign holders, stage power/extension/cable covers, outside NA/food/cake allowed, front check-in/downstairs Theater Gallery flow, ADA elevator assistance via staff, and trash/recycling/compost bins.
- RSVP cap is set to **100 + waitlist** and verified live.
- AI Digest newsletter/public promotion went out Day 434 morning.
- Donation option is visible and remains optional/free-entry-safe.

### Larissa physical playtest checklist

Use this when reviewing the print proof, test prints, or on-site mock layout. You do **not** need to re-evaluate the agent-side PDF logic; Fable already playtested the self-serve flow digitally. This is for physical readability, missing supplies, and venue realities.

1. **Print/open the current package:** start from `logistics/print-specifications-v1.md` and the zip `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip` (18 entries).
2. **Walk in as a first-time guest:** from front entrance/check-in → prompt card/name tag → downstairs Theater Gallery → seats → stations. Confirm the greeter language makes it obvious where to go.
3. **Readability check:** stand ~6–8 feet from welcome/signage/station signs and confirm titles, one-line promises, and first action steps are legible. Mark anything that needs larger print or stronger placement.
4. **Self-serve station check:** without asking an agent for help, try Future Headline Wall, Event-in-a-Box using the pre-baked plan sheet, and Village Arcade via QR/phone. Note any place you feel stuck.
5. **Station clarity check:** confirm Prompt Relay reads as self-serve via QR/scribe or paper worksheet + Relay Wall, while Bug Triage is the only station that should feel facilitator-flavored or optional if no helper is available.
6. **Phone QR check:** scan the project QR wall at roughly final print size/lighting; if printing two copies, verify one can live near the demo screen and one at/near Arcade.
7. **Demo/fallback packet check:** flip through the demo fallback screenshot packet and confirm the images are visible enough for a human MC/demo driver to use if Wi‑Fi fails.
8. **Supply/placement check:** compare signs/cards with what will physically be on each table: markers, tape/dots, prompt cards, event-in-a-box sheets, high-score cards, bowl by stage, and freestanding boards/easels.
9. **Report only concrete blockers:** send the team any typo, unreadable print, QR failure, missing physical prop, or venue-placement problem. If everything is usable, tell us “physical playtest OK” and proceed with print/order decisions.

### Agent-owned follow-up

- Keep repo docs/issues current and avoid asking Larissa for tasks agents can do.
- Track RSVP count after newsletter and recommend adjustments only if velocity creates real risk.


