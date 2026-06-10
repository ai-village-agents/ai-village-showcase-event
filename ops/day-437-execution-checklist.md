# Day 437 Execution Checklist — Friday, June 12

*Goal: Send final 24h reminder, assemble print/station kits, confirm food/drink delivery, close or waitlist RSVPs, and hold final team prep.*

---

## Morning verification

- [ ] **RSVP count check** — compare to Day 436 EOD; target trajectory is 70+ Going by EOD Day 437
- [ ] **Partiful page sanity check** — link works, cap **100 + waitlist**, no errors
- [ ] **Print kit verified** — all print assets in hand and sorted by station/role
- [ ] **Food/drink delivery confirmed** — vendor confirms Saturday delivery/pickup window before 6:00 PM load-in

---

## Final 24h reminder

- [ ] **Final reminder sent** — Larissa / AI Digest sends via newsletter or Discord
  - Use blurb from `outreach/reminder-blurbs.md` (Friday section)
  - Include: address, transit, what to expect, RSVP update link
  - Emphasis: "Final reminder … if your plans have changed, please update your RSVP so we can adjust food quantities"
- [ ] **Human-owned short social posted** — Larissa / AI Digest final Twitter/Discord push, if useful
- [ ] **Personal warm nudges** — Larissa only, if useful, texts/emails warm contacts who have not RSVPed or updated plans; agents do not cold-contact people

---

## RSVP management

- [ ] **Cap review** — if Going count is near 100 or waitlist is growing, confirm with Larissa whether to:
  - Keep waitlist open (default)
  - Close RSVPs to prevent overage
  - Allow last-minute signups with check-in discretion
- [ ] **Update-your-RSVP nudge** — Larissa / AI Digest sends to existing RSVP list reminding them to update if plans changed

---

## Print & station kit assembly

- [ ] **Kit assembly** — Larissa / human crew packs everything into labeled bags/boxes by station/role
  - **MC kit:** cue card, run-of-show printout, welcome slides (HTML + PDF fallback), Demo 2 operator brief, timer/phone
  - **Check-in kit:** check-in sheets, name tags, pens, donation sign, door prompt cards
  - **Station kits:** 
    - Station 1 (Prompt Relay): challenge/constraint decks, relay worksheets, wall display materials, QR fast-lane printout for https://ai-village-agents.github.io/village-relay/ (only deploy if it clears the 2-phone/browser go/no-go using `ops/relay-venue-test-card.md`; paper remains base)
    - Station 2 (Event-in-a-Box): pre-baked plans sheet, card decks, red pens, sign
    - Station 3 (Bug Triage): bug cards, role cards, sign (upside only — pack but may not deploy)
    - Station 4 (Future Headline Wall): headline cards, freestanding boards/easels, markers, sign
    - Station 5 (Village Arcade): high-score cards, leaderboard printout, QR wall print, sign
  - **Demo kit:** fallback screenshot packet, Demo 2 house prompt cards, projector adapter set
  - **Artifact collection kit:** trays/envelopes/clipboards + labels for "Leave one for the Village"
  - **Signage kit:** all 11×17 station signs, 18×24 welcome/schedule signs, donation note, volunteer quick brief
  - **Food/drink serving kit:** plates, napkins, cups, utensils, ice plan, allergen labels
- [ ] **Manifest cross-check** — verify every item chosen from `logistics/larissa-print-order-v1.md` is printed/packed, including any optional Part A2 ride-alongs the human crew decided to include
- [ ] **Backup digital copies** — load key PDFs onto primary laptop and supervised backup device

---

## Food & drink final confirmations

- [ ] **Cake/dessert confirmed** — Timeless Bakery or chosen vendor confirms pickup/delivery time and location
- [ ] **NA drinks confirmed** — Costco pickup or The Fold NA sparkling ready for transport
- [ ] **Substantial bites confirmed** — vendor/delivery confirmed or Larissa has pickup plan
- [ ] **Ice/refrigeration plan** — if The Fold has limited fridge space, confirm ice run timing or cooler plan
- [ ] **Allergen labels printed** — simple labels for common allergens on food items
- [ ] **Leftover plan** — confirm who takes home extras or disposal method per venue rules

---

## Tech & A/V prep

- [ ] **Primary laptop final prep** —
  - Notifications OFF (Do Not Disturb)
  - Browser clean (no personal tabs/bookmarks visible)
  - Signed into village chat showing ONLY `#showcase-live` (never #best)
  - Charger + adapter set packed
  - Test projector connection if adapter available
- [ ] **Supervised backup device prepped** — same setup as primary
- [ ] **Demo 2 assets loaded** — clean-room operator brief, rehearsal capture/Plan B ready
- [ ] **Welcome projection slide tested** — `demo-assets/agent-welcome-projection-slide.html` loads and navigates smoothly
- [ ] **Optional `/tts` audio test** — if Larissa has tested PA routing, do one final check; if not, fallback to MC-read is confirmed
- [ ] **Village Pulse manual refresh** — run `gh workflow run "Publish Village Pulse Dashboard" --repo ai-village-agents/village-pulse` so Saturday's dashboard is current (cron Mon–Fri won't auto-fire on Saturday)

---

## Team prep & alignment

- [ ] **Final #best async prep** — agents confirm:
  - Welcome lines memorized/ready (Opus 4.8 → GPT-5.5 → Gemini 3.5 Flash → Kimi K2.6)
  - Demo 2 choreography locked; silent stand-down if Plan B triggered
  - Station designs finalized; self-serve stations ready for lean deployment
- [ ] **Human crew arrival times confirmed** — each helper knows when and where to arrive
  - Load-in: 6:00 PM at The Fold
  - Greeter/check-in: ~6:45 PM upstairs front
  - MC: ~6:50 PM position at front/stage
  - Station floaters: ~6:50 PM downstairs
- [ ] **Emergency contacts shared privately** — Larissa has phone numbers for all crew; crew has Larissa's number
- [ ] **Parking/transit notes** — crew knows how to get to The Fold (3359 26th St, SF)

---

## Afternoon pulse check

- [ ] **RSVP count check** — final count before doors; update food quantities if needed
- [ ] **Partiful page** — no last-minute errors
- [ ] **Weather check** — if rain, any door/line management changes needed?

---

## End-of-day (EOD) targets

| Metric | Target | Owner |
|---|---|---|
| Final 24h reminder live | Yes | Larissa / AI Digest |
| Print/station kits assembled | Yes | Larissa / human crew |
| Food/drink delivery confirmed | Yes | Larissa |
| Primary + backup laptops prepped | Yes | Demo laptop driver / Larissa |
| Human crew arrival times + roles communicated | Yes | Larissa |
| Village Pulse manually refreshed | Yes | Any agent (idempotent) |
| RSVP count | 70+ Going by EOD (57 Going documented Day 435 late morning; watch trajectory) | Kimi / GPT-5.5 track |
| Docs updated | `CURRENT-OPERATING-PACKET.md` current | Kimi / GPT-5.5 |
| Everything packed or staged | Yes | Larissa / human crew |
| Team aligned, no open logistics questions | Yes | #best + Larissa |

---

## Ready-to-use copy for quick shares

**Final 24h reminder (Newsletter / Discord):**
> Final reminder: the AI Village Showcase is tomorrow night, Saturday June 13, 7–10pm at The Fold (3359 26th St, San Francisco). Doors at 7:00, welcome at 7:20, demos at 7:45, stations at 8:20. Light snacks and drinks provided. If your plans have changed, please update your RSVP so we can adjust food quantities. See you there: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp

**Short social:**
> Tomorrow night — AI Village Showcase, 7–10pm at The Fold (3359 26th St). Agent demos, hands-on stations, snacks. Last call to RSVP or update your plans: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp

---

## Notes / log

*Use this section to record actuals as they happen.*

- **Morning RSVP count:** ___ Going / ___ Interested / ___ Maybe
- **Final RSVP count before doors:** ___ Going / ___ Interested / ___ Maybe / ___ waitlist
- **Kit assembly status:** ___
- **Food/drink delivery window:** ___
- **Village Pulse refreshed:** ___ (time)
- **Crew confirmed:** ___ names + arrival times
- **Any last-minute changes:** ___
