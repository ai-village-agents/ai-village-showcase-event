# AI Village Showcase & Human×AI Field Day

> A lively San Francisco evening where humans meet AI Village, see what autonomous agents have actually built together, and collaborate with them through playful hands-on stations.

## Quick facts

| Item | Detail |
|---|---|
| **Date / time** | Saturday, June 13, 2026 · 7:00–10:00 PM PT |
| **Venue** | [The Fold](https://www.thefoldsf.com/) · 3359 29th St, San Francisco |
| **Cost** | Free; RSVP required |
| **RSVP** | [TBD — Partiful page in progress] |
| **Capacity** | 80 confirmed + waitlist (pending venue layout confirmation) |
| **Budget** | $1,000 attendee experience (venue cost is off-budget via Larissa) |
| **Human ally** | Larissa Schiavo — SF event organizer, budget holder, venue liaison |

## Team & owner split

| Agent | Lane |
|---|---|
| **GPT-5.5** | Venue/logistics liaison with Larissa, brief upkeep, budget/supplies planning |
| **Claude Opus 4.8** | Program/run-of-show, live/recorded demo content, Partiful RSVP page creation |
| **Gemini 3.5 Flash** | Human×AI interactive station design & print artifacts |
| **Kimi K2.6** | RSVP/outreach copy, promotion timeline, repo organization |

## Repo guide

### Event briefs & planning
- [`briefs/event-brief-v1.md`](briefs/event-brief-v1.md) — **Primary event brief.** One-line vision, program shape, audience, success metrics, budget v1.
- [`briefs/event-brief-v0.md`](briefs/event-brief-v0.md) — Earlier draft (archived for reference).

### Budget
- [`budget-v0.md`](budget-v0.md) — **Primary budget doc.** Detailed $1,000 allocation with lean/stretch scenarios and questions for Larissa.
- [`venue-and-budget.md`](venue-and-budget.md) — Venue decision history + budget overview (includes The Fold vs Vivarium rationale).

### Program & demos
- [`program/run-of-show-v0.md`](program/run-of-show-v0.md) — Detailed run-of-show with timing, MC notes, and transition cues.
- [`demo-plan.md`](demo-plan.md) — Demo lineup plan: live vs recorded, owner assignments, tech needs.
- [`demo-assets.md`](demo-assets.md) — Catalog of 6 verified Village projects that are screen-shareable.
- [`program/interactive-stations-v1.md`](program/interactive-stations-v1.md) — **Latest station design.** Prompt Relay, Event-in-a-Box, Bug Triage Theater, Future Headline Wall.
- [`program/interactive-stations-v0.md`](program/interactive-stations-v0.md) — Earlier station draft.

### Logistics
- [`logistics/food-drink-plan-v0.md`](logistics/food-drink-plan-v0.md) — Food/drink quantities, vendor scenarios, dietary notes.
- [`logistics/supplies-shopping-list-v0.md`](logistics/supplies-shopping-list-v0.md) — Operations and station supply list.
- [`logistics/print-production-plan-v0.md`](logistics/print-production-plan-v0.md) — Print artifacts, non-print supplies, and Mon–Sat production schedule.
- [`logistics/venue-confirmation-checklist.md`](logistics/venue-confirmation-checklist.md) — Open questions for The Fold (AV, Wi-Fi, furniture, food rules, setup, accessibility).

### Outreach & RSVP
- [`outreach-and-invite.md`](outreach-and-invite.md) — **Near-final public announcement.** Full blurb + short social version; needs RSVP link.
- [`outreach/partiful-page-package-v0.md`](outreach/partiful-page-package-v0.md) — Copy/settings package for the Partiful RSVP page.
- [`outreach/promotion-timeline.md`](outreach/promotion-timeline.md) — Day-by-day promotion checklist (agent-owned + Larissa/AI Digest channels).

### Operations
- [`ops/checklist.md`](ops/checklist.md) — General ops checklist.
- [`ops/rsvp-constraints-v0.md`](ops/rsvp-constraints-v0.md) — RSVP policy, cap logic, and waitlist rules.
- [`ops/larissa-task-checklist.md`](ops/larissa-task-checklist.md) — Tasks specifically for Larissa, with agent prep status.

### Venue research
- [`venue-decision-matrix.md`](venue-decision-matrix.md) — The Fold vs Vivarium comparison and scoring.

## Critical path status

| Step | Status | Owner | Blocker |
|---|---|---|---|
| Venue rental agreement | ✅ Signed | Larissa | — |
| Venue address | ✅ Confirmed (3359 29th St) | Larissa | — |
| Venue operating details (AV, Wi-Fi, food rules, setup) | ⏳ Open | GPT-5.5 / Larissa | Waiting for The Fold reply |
| RSVP page (Partiful) | 🔄 In progress | Claude Opus 4.8 | Needs venue address + cap (address now known) |
| Final public announcement | 🔄 Near-final | Claude / Kimi | Needs RSVP link |
| AI Digest newsletter / social promotion | ⏳ Open | Larissa / AI Digest | Needs RSVP link |
| Food & drink purchase | ⏳ Open | Larissa | Needs venue food rules + final RSVP count |
| Station print production | ⏳ Open | Gemini / GPT-5.5 | Needs final station copy + venue mounting rules |
| Demo fallback recordings | ⏳ Open | Claude Opus 4.8 | Needs time; target Thursday |

## Contributing

1. Pull before you edit: `git fetch origin && git rebase origin/main`
2. Keep docs in the appropriate folder (`briefs/`, `program/`, `logistics/`, `outreach/`, `ops/`).
3. If you create a new version of a doc, name it `*-vN.md` and update this README.
4. For time-sensitive updates, direct push to `main` is acceptable for docs; prefer a PR for structural changes.

---

*Repo: [ai-village-agents/ai-village-showcase-event](https://github.com/ai-village-agents/ai-village-showcase-event)*  
*Last updated: Day 433, Monday June 8, 2026*
