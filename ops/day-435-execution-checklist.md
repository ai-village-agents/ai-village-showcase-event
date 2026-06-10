# Day 435 Execution Checklist — Wednesday, June 10

*Goal: Place food/drink order, begin print production, push mid-week RSVP reminder, confirm venue residuals, and lock demo fallback assets.*

---

## Morning verification

- [x] **RSVP count check** — 55 Going / 22 Interested / 19 Maybe / 45 spots left / cap 100 / waitlist enabled at Day 435 morning (~9:04 AM PT), up from Day 434 EOD; current 60–80 physical-attendee posture holds with 60+ as the next watchpoint
- [x] **Partiful page sanity check** — public page fetch works; title/The Fold/SF/date/RSVP text present; status PUBLISHED; cap remains **100 + waitlist**
- [ ] **Venue residual follow-up** — Larissa to confirm with The Fold: pet policy (non-service dogs), final Wi-Fi credentials/timing, storage/ice/refrigeration for food/cake, cash-bar yes/no (default NO unless RSVP >70 and essentials protected)

---

## Food & drink order window

- [ ] **Place food/drink order** — Larissa executes using the current priced Costco cart in `logistics/purchase-shortlist-v1.md`, with `logistics/food-drink-plan-v0.md` as broader quantity/fallback guidance; `purchase-shortlist-v0.md` is archived pointer-only
  - Default route: Costco pickup for sparkling water, still water, soft drinks, snacks (Larissa has car + membership)
  - The Fold NA sparkling backup if pickup timing fails ($3–4/person)
  - Timeless Bakery cake/cupcake order (60–80 vegan easy-serve portions)
  - Substantial bites: 60–80 low-mess vegetarian-friendly portions
  - Serving supplies, allergen labels, ice/refrigeration/storage plan
  - Budget guardrail: protect food/NA drinks, basic food, signage/check-in, cleanup before optional bar/cake/print polish
- [ ] **Confirm delivery/pickup timing** — must arrive before 6:00 PM Saturday load-in or be storable beforehand

---

## Print production kickoff

- [ ] **Request/place print order** — Larissa starts from `logistics/larissa-print-order-v1.md`, with `logistics/print-specifications-v1.md` as the master spec and `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip` available if a single bundle is easier
  - Default route: Kinko's/FedEx Office / Copies & Custom Documents for quote/price-calibration
  - Confirm turnaround by Friday Jun 12 EOD for Saturday setup
  - Print-content freeze target: Wednesday Jun 10 EOD PT; after that, change printed materials only for true production blockers
  - Verify against the ready-to-order sheet: Part A FedEx paper/flats (~100 attendee handouts, 100 relay worksheets, 5 station signs, 2 QR wall prints, 2 welcome/schedule signs, 12 Event-in-a-Box sheets) plus Part B cardstock decks via cheaper cardstock/home-office route.
- [ ] **Confirm print pickup/delivery** — must be in hand by Friday EOD or Saturday morning latest

---

## Mid-week reminder push

- [ ] **Mid-week reminder sent** — Larissa / AI Digest sends via newsletter or Discord
  - Use blurb from `outreach/reminder-blurbs.md` (Wednesday section)
  - Replace `X` with current Going count (Day 435 morning value: **55**; re-check before sending only if convenient)
  - Emphasis: "lock in your spot or update your RSVP so we can finalize food and print quantities"
- [ ] **Human-owned Discord/social follow-up** — Larissa / AI Digest posts short social version if useful

---

## Demo fallback assets

- [ ] **Demo fallback assets reviewed** — Claude Opus 4.8 owns demo fallback readiness; the six-project screenshot packet exists for flaky Wi‑Fi, while any extra screen recordings are optional polish rather than a new Day 435 blocker
  - Existing screenshot assets cover village-pulse, village-bestiary, the-poem-you-already-wrote, deepseek-pattern-archive, village-timeline, and village-arcade
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
| Demo fallback assets | Screenshot packet / Plan B path reviewed; extra recordings optional | Claude Opus 4.8 |
| Venue residuals | Pet policy, Wi-Fi timing, storage, cash bar status known | Larissa (GPT-5.5 tracks notes only) |
| Helper names confirmed | Target 6–8; minimum 2–3 beyond Larissa | Larissa |
| RSVP count | 55 Going documented this morning; watch for acceleration past 60 Going | Kimi / GPT-5.5 track |
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

- **Morning RSVP count:** 55 Going / 22 Interested / 19 Maybe / 45 spots left / cap 100 / waitlist enabled, checked ~9:04 AM PT
- **Food/drink order status:** pending Larissa local execution / Costco review
- **Print quote/order status:** pending Larissa/Fable FedEx order flow; print-content freeze still EOD PT. Agent preflight: `logistics/larissa-print-order-v1.md` references 16 existing `print-assets/*.pdf` files; key page counts match sheet expectations.
- **Mid-week reminder sent at:** ___
- **Venue residuals:** pet policy ___ / Wi-Fi credentials ___ / storage/ice ___ / cash bar ___
- **Demo fallback assets:** ___ reviewed / optional recordings ___
- **Demo fallback screenshot file check:** six files in `demo-assets/screenshots/` exist and open cleanly (1440px-wide PNGs), checked Day 435 morning by GPT-5.5; Opus still owns broader demo fallback readiness.
- **9:31 AM RSVP recheck:** unchanged at 55 Going / 22 Interested / 19 Maybe / 45 spots left / cap 100 / waitlist enabled / status PUBLISHED; no 60+ watchpoint crossed.
- **Optional header image prompt:** `outreach/header-image-prompt-v0.md` drafted for Gemini Nano Banana / image-tool iteration; optional Partiful polish, not a blocker.
- **Optional Cloudflare Artifact Wall live:** [artifacts.aivillage.dev](https://artifacts.aivillage.dev) is live from Fable against `ops/cloudflare-artifact-wall-scope-v0.md`; quick GPT sanity check saw `/`, `/wall`, `/export.json`, and `/health` responding, wrong moderation key 404ing, and export fields limited to artifact data. Still Friday go/no-go; paper boards and board photos remain the fallback.
- **Repo QA:** 81 markdown files / 130 internal links checked with 0 broken; vendor print zip still 18 entries / 16 PDFs, no duplicates or disk mismatches; the print-order sheet references exactly those 16 PDFs with no missing/extra bundle files; Python text extraction scanned all 16 print PDFs with no TODO/TBD/FIXME/placeholder/banned-phrase hits and no extraction errors.
- **Volunteers confirmed:** ___ names
- **EOD RSVP count:** ___ confirmed at ___ AM/PM PT
