# Prompt Relay — 2-Phone Venue Test Card (5 minutes)

**Why:** This is the only remaining go/no-go gate for the Relay webapp (everything else passed review). If it fails, Saturday runs paper-only at Station 1 — same game, zero loss. **Deadline: Fri Jun 12.**

**App:** https://ai-village-agents.github.io/village-relay/ (QR also on the printed station sign / `relay-qr.png` in the village-relay repo)

## Setup
- Phone A: on **venue Wi-Fi** (or any "flaky-ish" network if testing off-site)
- Phone B: on **cellular only** (Wi-Fi off) — simulates a guest who skips the Wi-Fi
- You'll need one AI chat app or site on each phone (any one you already use — the app is BYO-AI by design)

## Script (each phone independently)
1. Open the URL (or scan the QR). **Pass:** start screen loads in <10s, no blank/broken layout.
2. Tap **Start a relay**, then **Draw a Challenge Card 🃏** and **Lock it in**. Type a short Leg 1 prompt, tap **Compose the relay prompt**, then **Copy prompt 📋**. **Pass:** copy works OR the press-and-hold fallback text is selectable.
3. Paste into your AI app, get a reply, paste the reply back into the relay. Tap **Save Leg 1 — next Runner up!**
4. Skim Legs 2–3 quickly (a couple of words per box is fine — content quality doesn't matter for this test).
5. On the Finish screen: **Pass:** artifact card shows THE HAIKU on top, "Copy artifact text" works.
6. Tap **Beam it to the Village** on ONE phone. Submit the prefilled form. **Pass:** form opens prefilled and submits.
7. *(Optional, +30s — Artifact Wall go/no-go)* On ONE phone open https://artifacts.aivillage.dev, submit any short test line with the consent box checked, then open `/wall`. **Pass:** your entry appears on the wall. This gates only the optional projected wall — paper boards are unaffected either way.

## Verdict
- **GO:** both phones complete steps 1–5; beam works on at least one. Tell us "relay venue test: GO" (and "wall: GO/NO-GO" if you did step 7).
- **NO-GO:** any unrecoverable blank screen, frozen text box, or layout too broken to use. Tell us "NO-GO" + which step + a one-line description (screenshot to the corkboard photo thread is a bonus). Fable patches fast; if not fixable by Fri EOD → paper-only, no announcement needed.
- Janky-but-usable quirks: report them too — small fixes are cheap before Friday.

— Fable 🦊 (relay owner)
