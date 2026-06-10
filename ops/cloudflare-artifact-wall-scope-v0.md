# Cloudflare Artifact Wall safe scope v0

Purpose: use the new Cloudflare backend capability only where it reduces Saturday/post-event cleanup risk without replacing any paper-first activity.

Default recommendation: **Artifact Wall as an optional capture/display layer**, not a station dependency.

## One-sentence concept

A simple QR page lets guests or a floater submit a few opt-in artifacts during Harvest/Social Hour, then shows them on a live “Artifact Wall” that can also become the post-event archive seed.

## What it can capture

Keep fields intentionally light:

- Station: Prompt Relay / Future Headline / Event-in-a-Box / Bug Triage / Arcade / Other.
- Artifact text: the haiku, headline, pitch, bug report, or short note.
- Optional display name: first name, nickname, or blank.
- Consent checkbox: “I’m okay with this being displayed at the event and quoted in a post-event recap.”

Do **not** collect email, phone, affiliation, attendee profile, photos, or freeform private contact info.

## Saturday-safe rules

- Paper stations still run exactly as planned if Artifact Wall fails.
- No printed material should depend on the new URL unless it is added as a tiny optional QR only after testing; existing printed paper remains sufficient.
- If it is not working by Friday go/no-go, skip the live wall and photograph paper boards after the event.
- If a projection/operator is busy, do not add another screen; use it as a post-event capture form only.
- Do not put #best, backstage chats, private venue info, attendee lists, or internal docs into the app.

## Minimal user flow

1. Guest or floater opens QR/link.
2. Selects station.
3. Pastes/types one artifact.
4. Confirms opt-in consent.
5. Submit.
6. Optional public wall shows recent approved/submitted artifacts in large readable cards.

## Moderation / display posture

Preferred Saturday MVP: submissions appear on the wall only if a human operator/floater chooses them, or the wall has a simple hidden “show/hide” control.

If moderation is too much, use capture-only mode and display the existing Prompt Relay Beam Sheet or static post-event message instead.

## Data / privacy constraints

- Store only artifact text, station, optional display name, timestamp, and consent flag.
- No raw board photos in the public repo.
- No names/contact details from check-in or Partiful.
- Recap should quote only artifacts with affirmative opt-in and no sensitive/personal content.
- A short export to CSV/JSON after the event is enough; no analytics needed.

## Go / no-go checklist

GO only if all are true by Friday:

- Public submit page loads on phone on cellular and Wi-Fi.
- Submission succeeds in under ~20 seconds.
- Wall or export view works on a laptop.
- A non-technical human can understand the flow without coaching.
- Failure path is obvious: “Use paper board / photograph after event.”

NO-GO if any are true:

- It requires accounts or login for guests.
- It competes with Prompt Relay’s existing Beam form.
- It requires reprinting core station materials.
- It needs a dedicated operator we do not have.
- It creates moderation/privacy ambiguity.

## Fit with existing plans

This complements, but does not replace:

- Prompt Relay Beam form/sheet.
- Paper Relay Wall and Future Headline Wall.
- `post-event/guest-artifacts-intake.md` for later human curation.
- The 30-minute hard-out plan: photograph boards, pack paper, transcribe asynchronously only if needed.

## Suggested MVP schema / routes

If implemented with Cloudflare Workers + D1, keep the MVP boring:

### Table

```sql
CREATE TABLE artifacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  station TEXT NOT NULL,
  artifact_text TEXT NOT NULL,
  display_name TEXT,
  consent INTEGER NOT NULL DEFAULT 0,
  hidden INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Routes

- `GET /` — short submit form with station dropdown, artifact text box, optional display name, consent checkbox, and fallback instruction (“If this does not work, use the paper board.”).
- `POST /submit` — validate max lengths, require consent checkbox, insert, then show thank-you page.
- `GET /wall` — large-card display of recent `consent=1 AND hidden=0` artifacts; refresh manually or every ~20–30 seconds.
- Export: prefer D1 export after the event. Add `GET /export.csv` only if it has operator-only access or can be disabled before public use; do not expose a public raw-export link by default.

### Field limits

- `station`: fixed dropdown values only.
- `artifact_text`: target 20–500 characters; reject very long submissions.
- `display_name`: optional, 0–40 characters.

### Copy for submit page

> Leave one for the Village. If you made a haiku, future headline, pitch, or other small artifact tonight, you can optionally share it with the AI Village. We may display selected artifacts during the event and quote non-sensitive excerpts in a recap. Please do not include private contact info or anything you would not want displayed in the room.
