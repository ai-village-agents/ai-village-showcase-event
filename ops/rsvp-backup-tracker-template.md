# RSVP Backup Tracker Template

*Purpose: manual backup in case Partiful has issues. Larissa/host can export the Partiful RSVP list into a private local copy or private shared sheet based on this format before event day. Do not commit a filled guest list to the public repo.*

## Columns

| Column | Description |
|---|---|
| `name` | Attendee name |
| `email` | Attendee email |
| `rsvp_status` | confirmed / interested / waitlist / cancelled |
| `arrived` | yes / no — check off at door |
| `name_tag_given` | yes / no |
| `prompt_card_given` | yes / no |
| `dietary_restrictions` | free text — from Partiful questions or direct outreach |
| `accessibility_needs` | free text — from Partiful questions or direct outreach |
| `how_they_heard` | newsletter / Twitter / friend / Discord / other |
| `notes` | anything else |

## How to use

1. **Day 433–434:** Export RSVP list from Partiful (host dashboard) → paste into a private copy of `ops/rsvp-backup-tracker-template.csv` or a private Google Sheet, not the public repo.
2. **Day 437 (Friday):** Print the private updated CSV or load it on a supervised device for check-in.
3. **Event day:** Use alongside the check-in sheet (`ops/check-in-sheet-template.md`) to track arrivals.

## File format

A starter CSV with headers is in `ops/rsvp-backup-tracker-template.csv`. Keep the repository version blank/template-only.

---

*Last updated: Day 434, Tuesday June 9, 2026*
