# AI Village Showcase & Human×AI Field Day

> A lively San Francisco evening where humans meet AI Village, see what autonomous agents have actually built together, and collaborate with them through playful hands-on stations.

## Start here — current human-facing packet

If you are Larissa, AI Digest, or another human trying to understand the current plan, start with:

- [`CURRENT-OPERATING-PACKET.md`](CURRENT-OPERATING-PACKET.md) — locked facts, current decisions, the small set of docs to use, archived docs to ignore, and open blockers.

The rest of this README is a full repo map for agents and maintainers. Many older `v0` files are retained for history; prefer the packet above when in doubt. Note: `v0` does **not** always mean stale — some current docs are first-version files and are listed as current in the packet.

## Quick facts

| Item | Detail |
|---|---|
| **Date / time** | Saturday, June 13, 2026 · 7:00–10:00 PM PT |
| **Venue** | [The Fold](https://www.thefoldsf.com/) · 3359 26th St, San Francisco |
| **Cost** | Free; RSVP required |
| **RSVP** | Live: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp |
| **Capacity** | 80 confirmed + waitlist (pending venue layout confirmation) |
| **Budget** | $1,000 attendee experience (venue cost is off-budget; The Fold invoice paid via Larissa) |
| **Human ally** | Larissa Schiavo — SF event organizer, budget holder, venue liaison |

## Team & owner split

| Agent | Lane |
|---|---|
| **GPT-5.5** | Venue/logistics liaison with Larissa, brief upkeep, budget/supplies planning |
| **Claude Opus 4.8** | Program/run-of-show, live/recorded demo content, Partiful RSVP page creation |
| **Gemini 3.5 Flash** | Human×AI interactive station design & print artifacts |
| **Kimi K2.6** | RSVP/outreach copy, promotion timeline, repo organization |

## Repo guide

**Human shortcut:** use `CURRENT-OPERATING-PACKET.md` first. The sections below are a fuller map of current docs plus archived history.

### Event briefs & planning
- [`briefs/event-brief-v1.md`](briefs/event-brief-v1.md) — **Primary event brief.** One-line vision, program shape, audience, success metrics, budget v1.
- [`briefs/event-brief-v0.md`](briefs/event-brief-v0.md) — Earlier draft (archived for reference).

### Budget
- [`budget-v0.md`](budget-v0.md) — **Primary budget doc.** Detailed $1,000 allocation with lean/stretch scenarios and questions for Larissa.
- [`venue-and-budget.md`](venue-and-budget.md) — Mixed venue decision history + budget overview; not the primary current budget/venue doc.

### Program & demos
- [`program/run-of-show-v1.md`](program/run-of-show-v1.md) — **Master run-of-show (latest).** Minute-by-minute 7–10 PM, roles, crew tiers, cut-order, tech deps, offline pre-load checklist, Village Pulse event-day refresh.
- [`program/mc-cue-card.md`](program/mc-cue-card.md) — Verbatim spoken MC transition lines for the whole night.
- [`program/attendee-program-handout.md`](program/attendee-program-handout.md) — Attendee-facing one-pager (flow, 5 stations, project QR, good-to-know).
- [`program/door-prompt-cards.md`](program/door-prompt-cards.md) — "Ask an Agent…" arrival cards for the 7:00–7:25 doors window.
- [`demo-plan.md`](demo-plan.md) — Demo lineup plan: live vs recorded, owner assignments, tech needs, the 6-project Demo 3 gallery, and the built-asset manifest.
- [`demo-assets/agent-welcome-projection-slide.html`](demo-assets/agent-welcome-projection-slide.html) — **Full-screen venue projection slide** for the 4-line collaborative agent welcome (Opus → GPT-5.5 → Gemini → Kimi). Arrow-key/click navigation, progress counter, large readable dark text.
- [`demo-assets/welcome-slides/agent-welcome-slides.pdf`](demo-assets/welcome-slides/agent-welcome-slides.pdf) — Static no-JS PDF fallback for the same 4-line projected welcome if browser navigation glitches.
- [`demo-assets/demo2-recorded-welcome-artifact.md`](demo-assets/demo2-recorded-welcome-artifact.md) — Canonical 4-line collaborative welcome text (same order as projection slide).
- [`demo-assets/demo2-rehearsal-runsheet.md`](demo-assets/demo2-rehearsal-runsheet.md) — Thursday Jun 11 rehearsal plan for Demo 2: tests live injection path and captures safety recording in one session.
- [`demo-assets/demo2-clean-room-operator-brief.md`](demo-assets/demo2-clean-room-operator-brief.md) — Short operator checklist for creating/projecting the clean Demo 2 rehearsal/live room.
- [`program/interactive-stations-v1.md`](program/interactive-stations-v1.md) — **Latest station design.** Prompt Relay, Event-in-a-Box, Bug Triage Theater, Future Headline Wall, Village Arcade Booth.
- [`program/interactive-stations-v0.md`](program/interactive-stations-v0.md) — Archived earlier station draft; do not use for current station ops.
- [`program/station-card-decks-v1.md`](program/station-card-decks-v1.md) — **Print-ready card decks** for all three stations (Prompt Relay, Event-in-a-Box, Bug Triage).
- [`program/station-sign-copy-v0.md`](program/station-sign-copy-v0.md) — Concise copy for the five 11x17 station title/rules signs.

### Logistics

- [`logistics/food-drink-plan-v0.md`](logistics/food-drink-plan-v0.md) — Food/drink quantities, vendor scenarios, dietary notes.
- [`logistics/catering-menu-options-v0.md`](logistics/catering-menu-options-v0.md) — Concrete lean/base/vendor/venue-package menu options for Larissa once venue rules are confirmed.
- [`logistics/supplies-shopping-list-v0.md`](logistics/supplies-shopping-list-v0.md) — Operations and station supply list.
- [`logistics/purchase-shortlist-v0.md`](logistics/purchase-shortlist-v0.md) — Practical Larissa buying menu with lean/base/stretch carts and venue-dependent decision gates.
- [`logistics/print-production-plan-v0.md`](logistics/print-production-plan-v0.md) — Print artifacts, non-print supplies, and Mon–Sat production schedule.
- [`logistics/print-specifications-v1.md`](logistics/print-specifications-v1.md) — Print-shop-ready sizes, paper stock, finishes, cuts, and quantities for station materials and handouts.
- [`logistics/print-vendor-shortlist-v0.md`](logistics/print-vendor-shortlist-v0.md) — Verification-first shortlist and script for local SF print ordering.
- [`print-assets/`](print-assets/) — Browser-printable fallback HTML/PDF files for station, welcome, and schedule signs.
- [`logistics/print-run-manifest-v0.md`](logistics/print-run-manifest-v0.md) — Batch-print checklist for handouts, signs, station cards, worksheets, demo assets, and display boards.
- [`logistics/print-shop-handoff-v0.md`](logistics/print-shop-handoff-v0.md) — Short coordinator-facing print-shop package: send-ready files, still-pending items, and printer instructions.
- [`logistics/print-vendor-order-draft-v0.md`](logistics/print-vendor-order-draft-v0.md) — Copy/paste vendor quote/order request using the current print-ready PDFs.
- [`logistics/print-package-validation-v0.md`](logistics/print-package-validation-v0.md) — PDF existence/page-count QA sheet for the print package.
- [`logistics/the-fold-venue-facts.md`](logistics/the-fold-venue-facts.md) — Packet-derived venue facts: capacity, furniture, Wi-Fi, A/V add-ons, food/drink rules, no-floor-tape constraint.
- [`logistics/venue-confirmation-checklist.md`](logistics/venue-confirmation-checklist.md) — Current booked/paid venue status plus remaining questions for The Fold (AV bundle, power, wall mounting, setup, accessibility).
- [`logistics/venue-questions-email-v0.md`](logistics/venue-questions-email-v0.md) — Sendable note Larissa can adapt for The Fold covering layout, setup, A/V, Wi-Fi, food/drink, displays, power, accessibility, and cleanup.
- [`logistics/layout-plan-v0.md`](logistics/layout-plan-v0.md) — Practical The Fold layout request for presentation, five stations, check-in, food/drink, display boards, and no-floor-tape power flow.

### Outreach & RSVP
- [`outreach-and-invite.md`](outreach-and-invite.md) — **Public announcement with live RSVP link.** Full blurb + short social version ready for Larissa / AI Digest channels.
- [`outreach/partiful-page-package-v0.md`](outreach/partiful-page-package-v0.md) — Copy/settings package for the Partiful RSVP page.
- [`outreach/partiful-description-final.md`](outreach/partiful-description-final.md) — **Paste-ready Partiful description** (long + short), matched to locked facts, for Larissa.
- [`outreach/partiful-donation-blurb.md`](outreach/partiful-donation-blurb.md) — Short optional-donation blurbs for Partiful, check-in signs, or event materials.
- [`outreach/promotion-timeline.md`](outreach/promotion-timeline.md) — Day-by-day promotion checklist (agent-owned + Larissa/AI Digest channels).
- [`outreach/reminder-blurbs.md`](outreach/reminder-blurbs.md) — Pre-written reminder copy for Day 435 (mid-week), Day 436 (second reminder), and Day 437 (final 24h).
- [`outreach/email-invite-template-v0.md`](outreach/email-invite-template-v0.md) — Copy/paste email templates for Larissa’s personal network invites.
- [`outreach/newsletter-blurb-v0.md`](outreach/newsletter-blurb-v0.md) — Newsletter-ready AI Digest / AI Village invite copy with subject, preview, full blurb, and sidebar version.
- [`outreach/press-brief-v0.md`](outreach/press-brief-v0.md) — Quick facts, framing, and ground rules for journalists in attendance.
- [`outreach/journalist-outreach-template-v0.md`](outreach/journalist-outreach-template-v0.md) — Copy/paste email/DM for Larissa or AI Digest to invite thoughtful journalists.
- [`outreach/journalist-exclusive-ranking-v0.md`](outreach/journalist-exclusive-ranking-v0.md) — Internal recommendation for ranking Larissa’s journalist contacts for an exclusive.
- [`outreach/guest-list-guidance-v0.md`](outreach/guest-list-guidance-v0.md) — Invite filters for high-fit attendees and journalist guidance.
- [`outreach/station-host-recruitment.md`](outreach/station-host-recruitment.md) — **Ready-to-send ask** to recruit a few station hosts (20-min shifts) — de-risks staffing.

### Operations
- [`ops/checklist.md`](ops/checklist.md) — Superseded generic early checklist; use Larissa/week/day-of docs instead.
- [`ops/code-of-conduct.md`](ops/code-of-conduct.md) — Short friendly conduct/safety note for Partiful, check-in, and welcome remarks.
- [`ops/rsvp-constraints-v0.md`](ops/rsvp-constraints-v0.md) — RSVP policy, cap logic, and waitlist rules.
- [`ops/larissa-task-checklist.md`](ops/larissa-task-checklist.md) — Tasks specifically for Larissa, with agent prep status.
- [`ops/rsvp-backup-plan-v0.md`](ops/rsvp-backup-plan-v0.md) — Fallback RSVP channel and velocity targets if Partiful has issues.
- [`ops/rsvp-backup-tracker-template.md`](ops/rsvp-backup-tracker-template.md) / [`ops/rsvp-backup-tracker-template.csv`](ops/rsvp-backup-tracker-template.csv) — Manual Partiful export/check-in backup tracker.
- [`ops/larissa-week-plan.md`](ops/larissa-week-plan.md) — Dated Mon–Sat action plan for Larissa: venue, promotion, helpers, donations, orders, rehearsal, load-in.
- [`ops/day-of-checklist-v0.md`](ops/day-of-checklist-v0.md) — Minute-by-minute checklist for event day (load-in through breakdown).
- [`ops/volunteer-roster-template.md`](ops/volunteer-roster-template.md) — Role/shift assignment sheet for sourced volunteers.
- [`ops/volunteer-roster-working-v0.md`](ops/volunteer-roster-working-v0.md) — Public-safe working roster with Larissa confirmed as MC and remaining helper roles TBD.

### Venue research
- [`venue-decision-matrix.md`](venue-decision-matrix.md) — Archived Day 433 venue comparison; not an active replacement plan.

## Critical path status

| Step | Status | Owner | Blocker |
|---|---|---|---|
| Venue rental agreement + invoice | ✅ Signed / paid | Larissa | — |
| Venue address | ✅ Confirmed (3359 26th St) | Larissa | — |
| Venue operating details (AV, Wi-Fi, food rules, setup) | 🔄 Partial | GPT-5.5 / Larissa | Packet confirms Wi-Fi/tables/chairs/no floor tape; waiting on AV bundle, setup, wall mounting, power, accessibility, outside snacks/cake policy, and optional beer/wine bar-package quote |
| RSVP page (Partiful) | ✅ Live | Larissa / AI Digest | 13 confirmed as of Day 433 ~2:21 PM PT; 67/80 spots left; link: https://partiful.com/e/4a5fqEa0knyDWNGur1Fp |
| Final public announcement | ✅ Link inserted / ready for human channels | Claude / Kimi / GPT-5.5 | GPT-5.5 has approval for one exact agent-controlled public post; human channels can promote anytime |
| AI Digest newsletter / social promotion | ✅ Ready to send | Larissa / AI Digest | Newsletter blurb template pushed (`outreach/newsletter-blurb-v0.md`); Larissa has copy |
| Food & drink purchase | ⏳ Open | Larissa | Needs venue food/NA/cake rules + final RSVP count; no outside alcohol; beer/wine only via The Fold bar package if quote/minimums are acceptable |
| Station print production | 🔄 Assets ready / execution open | Gemini / GPT-5.5 | Core PDFs formatted; needs Larissa/local printer route, venue mounting/display/easel rules, final quantities, pickup/delivery, and cut/bundle decision |
| Demo 2 rehearsal & fallback recordings | 🔄 Scheduled | Claude Opus 4.8 | Rehearsal runsheet + clean-room operator brief ready for Thu Jun 11; still pending AI Digest confirmation of `#showcase-live` / prompt-injection / projection path |

## Contributing

1. Pull before you edit: `git fetch origin && git rebase origin/main`
2. Keep docs in the appropriate folder (`briefs/`, `program/`, `logistics/`, `outreach/`, `ops/`).
3. If you create a new version of a doc, name it `*-vN.md` and update this README.
4. For time-sensitive updates, direct push to `main` is acceptable for docs; prefer a PR for structural changes.

---

*Repo: [ai-village-agents/ai-village-showcase-event](https://github.com/ai-village-agents/ai-village-showcase-event)*  
*Last updated: Day 433, Monday June 8, 2026 (~2:38 PM PT)*
