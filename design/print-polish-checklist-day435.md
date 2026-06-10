# Print design polish checklist — Day 435 bounded pass

Purpose: respond to Larissa's request to spiff up posters/printed materials while protecting the Wed Jun 10 print-content freeze. The current materials already have a warm zine/risograph base; this checklist adds a San Francisco AI-salon / hackathon polish layer without requiring a risky full redesign.

## Direction: “SF AI field-day salon,” not corporate keynote

Use cues from well-received SF AI gatherings: small-room credibility, visible participation, playful diagrams, strong wayfinding, and a little handmade weirdness. Avoid giant-conference gloss, robot-arm imagery, dense academic poster vibes, and sterile SaaS gradients.

Design anchors:
- **Warm civic-tech salon:** peach/lavender foundation with finalized station accents from the printed signs: coral, teal, amber, indigo, and magenta; off-white paper; human-scale instructions.
- **Hackathon clarity:** big station numbers, 1-sentence promise, 3–4 numbered actions, obvious QR/action target.
- **Zine texture:** dashed borders, stamps, “field note” framing, playful labels, visible cards/pens/boards.
- **Gallery wayfinding:** each printed item should answer: “What is this? What do I do next? What can I leave behind?”

## Apply-now physical polish (no PDF changes)

These are safest if the PDFs are already ordered or near-order:

1. **Color-coded station kits** — match each station with one color marker/tape/cardstock cue:
   - Station 1 Prompt Relay: coral `#e0492f`
   - Station 2 Event-in-a-Box: teal `#0d8a7a`
   - Station 3 Bug Triage: amber `#d97b06`
   - Station 4 Future Headline: indigo `#4f5ed3`
   - Station 5 Arcade: magenta `#c2417f`
2. **Use tabletop “material islands”** — put sign + cards + pens + artifact tray in one clear cluster per station. This makes the design feel intentional even if prints are simple.
3. **Add dot stickers for interaction** — headline voting, favorite relay haiku, arcade high scores. Dots are the cheapest way to make paper feel alive.
4. **Use clipboards or sign holders** for worksheets/cards where possible; avoid loose sheets spreading flat across tables.
5. **Handwritten human layer** — one warm marker note near the door: “Pick a card. Ask an agent. Leave something for the Village.” This adds the salon/zine feeling without altering print files.
6. **Do not wall-mount unless approved** — The Fold has no-wall-mount guidance; use easels, boards, tables, sign holders, and rolling whiteboards.

## File-by-file polish audit

### `print-assets/welcome-schedule-signs.html/.pdf`

Current strength: large, warm, readable, already poster-like.

If re-rendering before order, low-risk improvements:
- Add a tiny footer line: “Follow the station signs: each one tells you what to do, what to make, and what to leave behind.”
- Add a small colored “field guide” badge near the subtitle, e.g. `Public SF showcase · playful demos · hands-on stations`.

Skip if PDFs already uploaded; the existing version is strong enough.

### `print-assets/station-signs.html/.pdf`

Current strength: best-designed asset in the bundle; large station number, promise, steps, QR, artifact line.

If re-rendering before order, only consider:
- Add a small station-color stripe or corner badge per station.
- Slightly increase QR label contrast by keeping the short URL line but making the action line dominant.

Do **not** rewrite station instructions; they are already clear and production-ready.

### `print-assets/attendee-program-handout.html/.pdf`

Current strength: compact and informative.

If re-rendering, this is the biggest polish opportunity:
- Add a one-line “How to use this room” box near the top:
  > Pick a station, make one small artifact, and leave one thing behind for the Village if you want.
- Replace plain table header gray with a very light lavender or peach fill.
- Add station numbers as bold visual anchors in the station list.

Skip if time is tight; content is accurate and readable.

### `print-assets/door-prompt-cards.html/.pdf`

Current strength: friendly and useful at check-in.

If re-rendering:
- Add 2–3 variant accent colors across cards so a handful of prompt cards on tables look more lively.
- Keep the dashed border and large question type; do not shrink the questions.

Physical-only alternative: print on lightly colored cardstock or sort cards into colored stacks.

### `print-assets/station-card-decks.html/.pdf`

Current strength: playful prompts; good zine/hackathon energy.

If re-rendering:
- Add a tiny “Draw me” / “Pass me” pill label in the top bar for more game feel.
- Consider station-specific accent colors only if it does not reduce readability.

Skip if already bundled; the cards are fun enough.

### `print-assets/prompt-relay-worksheet.html/.pdf`

Current strength: structured, legible, self-serve.

If re-rendering:
- Add a short “3-minute version” callout for busy/crowded moments:
  > In a hurry? Do Leg 1 + Leg 3 only, then pin the final haiku.

Skip unless Station 1 facilitation looks overloaded; no design blocker.

### `print-assets/future-headline-cards.html/.pdf` and `print-assets/arcade-high-score-cards.html/.pdf`

Current strength: already color-coded by category / arcade mode.

Apply-now physical polish:
- Put them near matching colored markers and dot stickers.
- Display a few blank cards upright in a holder so guests understand they are meant to be filled in and posted.

No PDF change recommended.

### `print-assets/project-qr-wall-print.html/.pdf`

Current strength: does the utilitarian QR job.

Physical polish:
- Place it near the demo screen and/or Arcade table with a handwritten label: “The agents built these. Scan any square.”
- If there are two copies, use one as a “gallery wall” and one as a “play now” Arcade-area copy.

No QR churn recommended.

## Optional paste-in CSS tokens if someone does a last clean re-render

Only use this if the team intentionally regenerates PDFs and re-syncs `logistics/vendor-bundles/ai-village-showcase-print-package-2026-06-13.zip` afterward.

```css
:root {
  --ink: #201727;
  --muted: #5c5068;
  --lav: #efe2ff;
  --peach: #ffe0c8;
  --mint: #ddf7ee;
  --station-1-coral: #e0492f;
  --station-2-teal: #0d8a7a;
  --station-3-amber: #d97b06;
  --station-4-indigo: #4f5ed3;
  --station-5-magenta: #c2417f;
  --blue: #3b82f6;
  --sun: #ffd166;
  --line: #d8c7ea;
}
.badge {
  display: inline-block;
  border: 2px solid var(--ink);
  border-radius: 999px;
  padding: 0.04in 0.12in;
  background: white;
  font-weight: 900;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.fieldnote {
  border: 2px dashed var(--line);
  border-radius: 14px;
  background: linear-gradient(135deg, var(--mint), white 55%, var(--peach));
  padding: 0.12in 0.16in;
}
```

## Decision recommendation

- **If Larissa has not uploaded print files yet:** apply at most one targeted re-render pass to `welcome-schedule-signs`, `attendee-program-handout`, and maybe `door-prompt-cards`; then regenerate PDFs and vendor zip once.
- **If upload/order is underway:** do not touch PDFs. Use the physical polish list above; it gives the room a designed, SF-salon feel without production risk.
- **If only one improvement is possible:** color-code station kits and make the material islands tidy. This will be more visible to attendees than micro-edits inside PDFs.
