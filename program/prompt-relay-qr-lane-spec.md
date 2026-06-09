# Prompt Relay — optional QR "fast lane" spec (paper stays the base)

**Status:** OPTIONAL bonus layer. A Fable-built static prototype is now live at <https://ai-village-agents.github.io/village-relay/> and in <https://github.com/ai-village-agents/village-relay>. GPT-5.5 static review passed the major guardrails on Day 434: zero external assets/analytics/fetches, no personal-data fields, Beam is optional and only opens the Google Form prefill, start screen names the paper fallback + "No accounts, no names," and the final artifact is haiku-first with the origin prompt below. Fable has since fixed the haiku/origin finish-copy wording, verified Beam -> Form -> Sheet round-trip, documented the live response Sheet in the relay repo README (<https://docs.google.com/spreadsheets/d/1sXUXE5FhyjLmRshJEH0HFXvdly_vnBh_2iT-MGCqZuU/edit?gid=917265687>), and added a scan-verified print QR image in that repo (`relay-qr.png`). Remaining go/no-go item: real 2-phone/browser test on venue-like Wi-Fi by Fri Jun 12. Paper relay worksheets + Relay Wall of Fame remain the guaranteed base regardless of whether this is used Saturday.

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
- **Optional “Beam it to the Village” share may exist only as explicit opt-in.** If Fable adds a finish-screen button that opens a prefilled form/sheet so agents can see results during the party, it must be clearly optional, send only the Leg-1 start prompt + final creation, collect no names/contact/device metadata beyond what the form platform unavoidably logs, and never block the wall artifact if the form or network fails.
- **Dead simple.** Land → scan → first text box in <10s, no account, works on a cold phone over venue Wi-Fi (and gracefully if Wi-Fi is flaky).

## Go / no-go bar (decide by Fri Jun 12, 4 days out)
Ship ONLY if ALL are true:
- Builds + deploys (static or trivially hosted; same GitHub Pages pattern as the bonus pages is fine).
- Passes a REAL phone test on at least 2 different phones/browsers, ideally on venue-like Wi-Fi.
- Round-trips a full 3-leg relay and emits the wall-ready artifact view.
- Has an obvious in-room fallback if it breaks mid-event: guests drop to the printed relay worksheet with zero ceremony.
If any fail by Fri, we run paper-only for Saturday — no loss, since paper is the base.

**Locked-intents review — Opus 4.8 (Day 434, source-level pass of the live build):** Read the deployed `village-relay/index.html` against this spec's six structural intents — all pass at the source level. (1) One QR = one *shared* pass-the-phone session with rotating Runner roles (not isolated per-phone). (2) Each leg's composed prompt + reply is visible, and a "Show the full relay" toggle reveals all three legs together. (3) Finish screen emits a wall-ready artifact card — haiku first, Leg-1 origin below — with a "Copy artifact text" button and explicit "copy onto a Post-it for the Wall of Fame" instruction. (4) No login/name/email/phone fields anywhere; "No accounts, no names." (5) Beam is the only outbound action — opt-in, opens the prefilled Google Form in a new tab (`noopener`), sends only start + final, and never blocks the paper path. (6) Zero external assets/fetch; clipboard has a press-and-hold fallback for locked-down mobile browsers; paper fallback is named on the start screen and footer. This is a static/source review only — it does NOT substitute for the live 2-phone/venue-Wi-Fi test, which remains the sole open go/no-go item.

## What stays paper no matter what
- The printed relay worksheets (Leg 1/2/3 boxes) and the Relay Wall of Fame board + sticker dots ship as planned. The QR lane is an enhancement on top, never a replacement, and never blocks the station opening.

## Agreed hybrid (Larissa, Day 434 ~2:21pm) — record of decision
Larissa converged on the hybrid this spec describes: **phones run the legs via QR → the final creation is emitted physically → pinned to a corkboard → humans dot-vote favorites.** This matches the Relay Wall of Fame + sticker-dot voting already in the station design.
- **Artifact emit, two tiers (room-side, NOT a webapp build dependency):**
  - *Upgrade (optional):* a cheap thermal **receipt printer** auto-prints the final creation + its Leg-1 origin → instantly pinnable. Removes the hand-transcribe step and is genuinely fun. Treat as an in-room hardware nice-to-have on Larissa's budget call; only add if simple to set up at load-in.
  - *Guaranteed fallback:* **handwrite the final + Leg-1 prompt onto a card** from the app's "copy this onto a card" view. The wall fills even if there is no printer or the printer jams. This is why the webapp's artifact view must stay clean and readable for transcription.
- **Voting:** corkboard + sticker dots = the existing Wall of Fame voting; no new mechanic needed.

## Open item for build owner / operator: which AI is "in the loop"
Fable's build plan is **BYO-AI**: the webapp composes each leg's cumulative prompt with a copy button; the group scribe pastes it into whatever consumer chat app they already have open on their own phone, or into a supervised station device if one exists (ChatGPT / Claude / Gemini free tier is fine, since relay replies are capped ~50 words), then pastes the reply back. No API keys and no required hosted backend. If we want consistency on a supervised station device, pin ONE default app on that device and write it into the operator brief — Larissa/Fable's call. Avoid a hosted backend that calls an API key: that reintroduces the failure surface (hosting, quotas, outages) the go/no-go bar is meant to exclude.

A separate opt-in result-share form/sheet is acceptable only as a bonus visibility layer, not as the operating core of the relay. If it ships, label it as sharing the artifact with AI Village; keep the no-personal-data rule; and make the local corkboard/card path complete without it.

## Default output form: haiku (Larissa, Day 434 ~2:25pm)
Larissa suggested the relay produce **"a board full of haikus."** Adopting haiku (5-7-5) as the relay's **default signature output** strengthens every part of the design above, so make it the house default (other forms — slogan, mascot, micro-story — stay available as variant prompt cards):
- **Wall coherence:** a corkboard of haikus reads as one beautiful collective piece, not a jumble of mixed formats. Stronger payoff at the 8:55 harvest.
- **Artifact fit:** a haiku is tiny and fixed-shape — perfect on a receipt-printer slip or a hand-copied card. Keeps the "copy onto a card" fallback fast.
- **Zero AI-literacy floor:** anyone can admire and judge a haiku; great for dot-voting.
- **Maps onto the 3 legs:** Leg 1 = pick a subject (printed prompt card) · Leg 2 = AI drafts rough lines on the theme · Leg 3 = the table shapes/refines it into 5-7-5. The "drift across legs" intent is preserved — guests watch a loose idea tighten into form.
- **For the build:** the webapp's finish-screen artifact view should present the final haiku as three lines (5-7-5) above its Leg-1 origin prompt, so the printed/handwritten card and the Wall stay consistent. Paper relay worksheets can note "shape it into a haiku (5-7-5)" as the default Leg-3 instruction.

## Generalizing the hybrid to other co-creation stations (Larissa, Day 434 ~2:35pm)
Larissa suggested Event-in-a-Box (Station 2) also become a webapp with preset AI parameters and live visible text. The same hybrid principle applies to every co-creation station, with one rule of thumb:
- **The AI-generation step suits a webapp** (preset parameters, live-rendered text). That is the part guests find delightful to watch.
- **The conversational/tactile step must stay physical.** Event-in-a-Box's heart is the table red-penning a *printed* plan together; the relay's is a *shared* table session that produces a wall card. A webapp may generate and display, then it must hand off to paper (print or transcribe) so the group critique and the take-home artifact survive.
- **Paper stays the zero-dependency base** at every station (relay worksheets; Event-in-a-Box prebaked-plans PDF). The webapp is always an enhancement layer, never the station's only path.

### Scope guard (protects the timeline)
Only **one** webapp is an active build with a Friday Jun 12 go/no-go: the Prompt Relay QR lane (Fable). An Event-in-a-Box webapp is a **stretch / post-event idea**, not a second Saturday deliverable — do not let it compete for build time or become a load-bearing dependency. If the relay webapp proves the pattern, a second station webapp can be considered later; for Saturday, Event-in-a-Box runs on its existing paper plan + prebaked-plans PDF.

## Design update — Larissa live phone test (Day 434, ~3:26pm)
Larissa ran the live relay on her own phone and surfaced three real issues. They share one fix:

1. **Leg 1 is dull because the Challenge card is already a finished prompt.** The current Challenge Cards (e.g. "Design a micro-museum exhibit explaining 'AI neural network weight decay' to a medieval peasant") have pre-done the creative work, so there is no naive starting point and no drift to discover. This contradicts this spec's own stated intent (Leg 1 = a *naive* 1-sentence prompt). **Fix (Fable, app-side; mirror to paper):** trim Challenge cards to terse **ingredient seeds** — 2-4 evocative fragments, e.g. `a maze · a blindfold · a guide who whispers` — so the *table itself writes* the naive Leg-1 prompt. Leg 1 becomes the active, low-stakes, funny beat; Legs 2-3 (constraint card → shape into haiku) then create visible drift.
2. **Handing a personal phone to strangers feels weird.** The relay was never meant to require this. It is a **table conversation**, not a pass-the-phone-between-strangers relay. Default shared device = the **station's own tablet/laptop**, or **one phone within a group that arrived together**, using Fable's **"scribe mode"** (one person holds their phone the whole game while the table calls the shots — no handing). The printed worksheet sidesteps any device entirely. The QR/start copy should lead with scribe mode, not "pass the phone."
3. **Too few twists/cards.** The seed format is cheap to expand — grow toward ~30+ seeds + more constraint cards. Webapp deck = Fable; the **paper Challenge deck (station-card-decks) needs the same seed trim** so app and print don't diverge — coordinate with the print lane before the next print pass; print decks are otherwise untouched.

Net: one redesign (Leg 1 = seed, table writes the prompt) fixes the dull-Leg-1 problem, removes the stranger-phone problem, and realigns the live build with this spec's stated Leg-1 intent.

**Scope note for the paper mirror:** Only the Challenge **deck content** changes (finished prompts -> seeds). The printed Station 1 **sign needs no edit** — it already instructs "Draw a Challenge Card → write a short first prompt on the relay sheet → pass the *sheet* → add a style/constraint/twist → facilitator enters it." The seeds actually *resolve* a current contradiction (today's finished-prompt cards conflict with the sign's "write your own first prompt"). Paper relay passes a sheet, not a phone, so the stranger-phone concern is app-only.
