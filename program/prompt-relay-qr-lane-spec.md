# Prompt Relay — optional QR "fast lane" spec (paper stays the base)

**Status:** OPTIONAL bonus layer, only if it clears the go/no-go bar below by Fri Jun 12. Owner of build + end-to-end phone test: Fable (offered in chat). Paper relay worksheets + Relay Wall of Fame remain the guaranteed self-serve base regardless of whether this ships.

**Context:** Larissa asked (Day 434, ~2:03pm) whether the Prompt Relay could be a webapp where guests scan a QR per role and the app drives the relay; she noted the RSVP crowd skews tech-savvy/phone-familiar. This spec captures the station's design intent so a digital version doesn't lose what makes the relay work.

## The relay's design intent (must be preserved)
1. **Iterative drift across 3 legs.** Leg 1 = a naive 1-sentence prompt; Legs 2–3 each apply ONE small refinement/constraint. The point is for guests to SEE how a prompt evolves and how the output changes with it — not to get one polished answer.
2. **Visible, shared accumulation.** The whole group at the table sees each leg's prompt and output. This drives conversation; it must not collapse into private heads-down phones.
3. **A physical artifact at the end.** The final tiny creation + its Leg-1 origin get pinned side-by-side to the Relay Wall of Fame, with sticker-dot voting. This is the dramaturgical payoff (held up at the 8:55 harvest). A purely on-screen result that nothing physical comes out of LOSES the station's best beat.

## What the QR lane must do (if built)
- **One QR → one shared relay session** (a room/table code), not one-QR-per-person-in-isolation. Roles (Leg 1 / Leg 2 / Leg 3 author) rotate within that shared session so the table still talks.
- **Show all three legs + outputs on one screen** the group can read together (the table device/screen, or one phone passed/held up). Avoid each person only seeing their own leg.
- **Produce a printable/transcribable artifact** at the end: final creation + Leg-1 prompt, formatted to be copied onto a Post-it / index card for the Wall of Fame. If no printer, the app shows a clean "copy this onto a card" view.
- **No personal data.** No login, no name/email/phone capture; no attendee data persisted server-side. Anonymous session only.
- **Dead simple.** Land → scan → first text box in <10s, no account, works on a cold phone over venue Wi-Fi (and gracefully if Wi-Fi is flaky).

## Go / no-go bar (decide by Fri Jun 12, 4 days out)
Ship ONLY if ALL are true:
- Builds + deploys (static or trivially hosted; same GitHub Pages pattern as the bonus pages is fine).
- Passes a REAL phone test on at least 2 different phones/browsers, ideally on venue-like Wi-Fi.
- Round-trips a full 3-leg relay and emits the wall-ready artifact view.
- Has an obvious in-room fallback if it breaks mid-event: guests drop to the printed relay worksheet with zero ceremony.
If any fail by Fri, we run paper-only for Saturday — no loss, since paper is the base.

## What stays paper no matter what
- The printed relay worksheets (Leg 1/2/3 boxes) and the Relay Wall of Fame board + sticker dots ship as planned. The QR lane is an enhancement on top, never a replacement, and never blocks the station opening.

## Agreed hybrid (Larissa, Day 434 ~2:21pm) — record of decision
Larissa converged on the hybrid this spec describes: **phones run the legs via QR → the final creation is emitted physically → pinned to a corkboard → humans dot-vote favorites.** This matches the Relay Wall of Fame + sticker-dot voting already in the station design.
- **Artifact emit, two tiers (room-side, NOT a webapp build dependency):**
  - *Upgrade (optional):* a cheap thermal **receipt printer** auto-prints the final creation + its Leg-1 origin → instantly pinnable. Removes the hand-transcribe step and is genuinely fun. Treat as an in-room hardware nice-to-have on Larissa's budget call; only add if simple to set up at load-in.
  - *Guaranteed fallback:* **handwrite the final + Leg-1 prompt onto a card** from the app's "copy this onto a card" view. The wall fills even if there is no printer or the printer jams. This is why the webapp's artifact view must stay clean and readable for transcription.
- **Voting:** corkboard + sticker dots = the existing Wall of Fame voting; no new mechanic needed.

## Open item for build owner / operator: which AI is "in the loop"
Fable's build plan is **BYO-AI**: the webapp composes each leg's cumulative prompt with a copy button; the group pastes it into whatever consumer chat app is on the facilitator/volunteer phone or station device (ChatGPT / Claude / Gemini free tier is fine, since relay replies are capped ~50 words), then pastes the reply back. No backend, no API keys, nothing stored off-phone. **If we want consistency, pin ONE default app on the facilitator device** and write it into the operator brief — Larissa/Fable's call. Avoid a hosted backend that calls an API key: that reintroduces the failure surface (hosting, quotas, outages) the go/no-go bar is meant to exclude.
