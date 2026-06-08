# RSVP Backup Plan — AI Village Showcase & Human×AI Field Day

*Owner: Kimi K2.6. Last updated: Day 433, Mon Jun 8, 2026.*

## Primary channel

**Partiful** — https://partiful.com/e/4a5fqEa0knyDWNGur1Fp
- Live, clean, cap at 80 with waitlist.
- Only Larissa has host dashboard access.
- Manual export/check-in backup: copy the host RSVP export into [`ops/rsvp-backup-tracker-template.csv`](rsvp-backup-tracker-template.csv); field guide in [`ops/rsvp-backup-tracker-template.md`](rsvp-backup-tracker-template.md).

## Risk scenarios

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Partiful outage/downtime | Low | High | Switch to Google Form + manual spreadsheet |
| Partiful page corrupted/deleted | Low | High | Rebuild from `outreach/partiful-page-package-v0.md` + `outreach/partiful-description-final.md` |
| RSVPs exceed 80 rapidly | Medium | Medium | Enable waitlist; do not raise cap without The Fold confirmation |
| Low RSVP velocity (<20 by Wed) | Medium | High | Intensify Larissa/AI Digest/human warm-network outreach; use approved exact agent post only if an actual approved agent-controlled channel exists; extend cap timeline |
| Partiful SMS/auth blocks new signups | Low | Medium | Fallback to Google Form |

## Fallback channel

**Google Form (dormant)** — https://docs.google.com/forms/d/1ivSu8B0zAI9eeFVCnLF88IpibK_wQIW4DLfNvOCx7qM/edit
- Built during Day 433 morning before Partiful went live.
- **DO NOT distribute** unless Partiful fails.
- If activated, update all public links and notify #best immediately.

## Activation checklist (use if Partiful fails)

1. Confirm with Larissa that Partiful is unusable.
2. Preserve/export current Partiful data if accessible and paste it into [`ops/rsvp-backup-tracker-template.csv`](rsvp-backup-tracker-template.csv) so existing RSVPs are not lost.
3. Reactivate Google Form: open edit URL, verify fields (name, email, dietary/restriction, accessibility, how they found us).
4. Update all public links: README, email templates, promotion timeline, any social posts.
5. Notify #best chat of fallback activation and new RSVP URL.
6. Set manual cap at 80; track RSVPs in a shared spreadsheet (Google Sheets).
7. Send confirmation emails manually or via Google Forms "response receipt" feature.
8. If reactivating mid-week, send a correction note to anyone who already saw the Partiful link.

## RSVP velocity monitoring

**Current host-view snapshot (Mon Jun 8, ~1:41 PM PT):** 11 confirmed RSVPs; 69/80 spots left. This is still early/low-velocity but before the main AI Digest/Larissa promotion push; keep the 80 cap, hold base print quantities, and recheck tonight or Tue morning after promotion.

| Date | Target RSVPs | Action if below target |
|---|---|---|
| Tue Jun 9 (Day 434) EOD | 20+ | Normal. Continue planned promotion. |
| Wed Jun 10 (Day 435) EOD | 40+ | Normal. Continue planned promotion. |
| Thu Jun 11 (Day 436) EOD | 60+ | If below 50, intensify personal invites via Larissa/AI Digest/human warm networks; use approved exact agent post only if an actual approved agent-controlled channel exists. |
| Fri Jun 12 (Day 437) EOD | 70+ | If below 60, send final personal push; confirm food quantities for actual count. |
| Sat Jun 13 doors | 75–80 | Walk-up policy: if below 70, allow walk-ins with check-in discretion. |

## Walk-in policy

If RSVP count is below 70 at doors-open, allow walk-ins on a first-come basis up to venue comfort limit.
- Check-in records name + email for post-event follow-up.
- Walk-ins do not affect waitlist priority.
- Safety/code-of-conduct still applies.

## Post-event RSVP cleanup

- Export final guest list from Partiful (or Google Form fallback) for thank-you and recap.
- Note no-shows vs. attendees for future event planning.
- Archive list in repo under `ops/` if appropriate and privacy-compliant.
