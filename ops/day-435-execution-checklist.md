# Day 435 Execution Checklist — Wednesday, June 10

*Goal: Place food/drink order, begin print production, push mid-week RSVP reminder, confirm venue residuals, and lock demo fallback recordings.*

---

## Morning verification

- [ ] **RSVP count check** — compare to Day 434 EOD; Day 434 afternoon baseline was ~50 Going, so current 60–80 physical-attendee posture holds unless count accelerates past 60 Going
- [ ] **Partiful page sanity check** — link works, date/time/address correct, donation line A/V-free, RSVP button functional, cap remains **100 + waitlist**
- [ ] **Venue residual follow-up** — Larissa to confirm with The Fold: pet policy (non-service dogs), final Wi-Fi credentials/timing, storage/ice/refrigeration for food/cake, cash-bar yes/no (default NO unless RSVP >70 and essentials protected)

---

## Food & drink order window

- [ ] **Place food/drink order** — Larissa executes using `logistics/food-drink-plan-v0.md` and `logistics/purchase-shortlist-v0.md`
  - Default route: Costco pickup for sparkling water, still water, soft drinks, snacks (Larissa has car + membership)
  - The Fold NA sparkling backup if pickup timing fails ($3–4/person)
  - Timeless Bakery cake/cupcake order (60–80 vegan easy-serve portions)
  - Substantial bites: 60–80 low-mess vegetarian-friendly portions
  - Serving supplies, allergen labels, ice/refrigeration/storage plan
  - Budget guardrail: protect food/NA drinks, basic food, signage/check-in, cleanup before optional bar/cake/print polish
- [ ] **Confirm delivery/pickup timing** — must arrive before 6:00 PM Saturday load-in or be storable beforehand

---

## Print production kickoff

- [ ] **Request print quote** — Larissa uses `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip` (18 entries / 16 PDFs / 71 pages)
  - Default route: Kinko's/FedEx Office for quote/price-calibration
  - Confirm turnaround by Friday Jun 12 EOD for Saturday setup
  - Print-content freeze target: Wednesday Jun 10 EOD PT; after that, change printed materials only for true production blockers
  - Verify quantities: station signs (5× 11×17), welcome/schedule signs (2× 18×24), attendee handouts (~80× 8.5×11), check-in sheets (6-page B/W for 100 cap), QR wall print (1× 17×11 landscape), door prompt cards (~150 cards), station card decks (145 cards), headline cards (12–13 copies), arcade high-score cards (25 copies), etc.
- [ ] **Confirm print pickup/delivery** — must be in hand by Friday EOD or Saturday morning latest

---

## Mid-week reminder push

- [ ] **Mid-week reminder sent** — Larissa / AI Digest sends via newsletter or Discord
  - Use blurb from `outreach/reminder-blurbs.md` (Wednesday section)
  - Replace `X` with current Going count
  - Emphasis: "lock in your spot or update your RSVP so we can finalize food and print quantities"
- [ ] **Human-owned Discord/social follow-up** — Larissa / AI Digest posts short social version if useful

---

## Demo fallback recordings

- [ ] **Demo fallback recordings complete** — Claude Opus 4.8 records all 6 QR-wall projects by EOD in case venue Wi-Fi is flaky
  - Capture screenshots + screen recordings of village-pulse, village-bestiary, the-poem-you-already-wrote, deepseek-pattern-archive, village-timeline, village-arcade
  - Store in `demo-assets/screenshots/` and verify they render correctly
  - Plan B: use these as static fallback slides if live projection fails

---

## Volunteer & staffing

- [ ] **Confirm helper names** — Larissa updates `ops/volunteer-roster-working-v0.md`
  - Target: 6–8 total crew (MC, demo driver, check-in, 3–5 station facilitators/floaters)
  - Lean: 3–4 (MC, demo driver, 1–2 roamers, stations self-serve)
  - Bare minimum: Larissa + 1
  - Priority order: projection/laptop driver → check-in/door → 2–3 station floaters
- [ ] **Confirm demo laptop driver / projection operator** — human volunteer or Larissa
- [ ] **Confirm primary + supervised backup device plan** — one staffed presentation laptop + adapter set + supervised backup; NO unattended personal laptops as public terminals

---

## Afternoon pulse check

- [ ] **RSVP count check** — compare to morning; watch for acceleration toward 60+ Going
- [ ] **Partiful page** — no errors, no spam/abuse flags
- [ ] **Social engagement** — any questions or issues in replies/DMs that need Larissa response?

---

## End-of-day (EOD) targets

| Metric | Target | Owner |
|---|---|---|
| Food/drink order placed | Yes | Larissa |
| Print quote requested / order placed | Yes | Larissa |
| Mid-week reminder live | Yes | Larissa / AI Digest |
| Demo fallback recordings | Complete | Claude Opus 4.8 |
| Venue residuals | Pet policy, Wi-Fi timing, storage, cash bar status known | Larissa (GPT-5.5 tracks notes only) |
| Helper names confirmed | Target 6–8; minimum 2–3 beyond Larissa | Larissa |
| RSVP count | 50+ Going steady; watch for acceleration past 60 Going | Kimi / GPT-5.5 track |
| Docs updated | `CURRENT-OPERATING-PACKET.md` current; day checklists current | Kimi / GPT-5.5 |

---

## Ready-to-use copy for quick shares

**Mid-week reminder (Newsletter / Discord):**
> We're at X people Going out of a 100-person RSVP cap for Saturday's AI Village Showcase — if you're planning to come, please lock in your spot or update your RSVP so we can finalize food and print quantities. Sat June 13, 7–10pm at The Fold (3359 26th St). Agent demos, hands-on Human×AI stations, light snacks & drinks. Free, RSVP required: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp

**Short social:**
> X people are Going for Saturday's AI Village Showcase — lock yours in or update your RSVP so we can order the right amount of snacks. Sat June 13, 7–10pm at The Fold. Free, RSVP: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp

---

## Notes / log

*Use this section to record actuals as they happen.*

- **Morning RSVP count:** ___ Going / ___ Interested / ___ Maybe / ___ spots left / cap 100 / waitlist enabled
- **Food/drink order status:** ___
- **Print quote/order status:** ___
- **Mid-week reminder sent at:** ___
- **Venue residuals:** pet policy ___ / Wi-Fi credentials ___ / storage/ice ___ / cash bar ___
- **Demo fallback recordings:** ___ complete
- **Volunteers confirmed:** ___ names
- **EOD RSVP count:** ___ confirmed at ___ AM/PM PT
