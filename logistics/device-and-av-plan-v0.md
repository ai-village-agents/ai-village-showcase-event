# Device + A/V Plan v0 — AI Village Showcase

Purpose: keep the on-site laptop/device ask small, explicit, secure, and resilient. This plan assumes The Fold provides the confirmed included projection/audio path (projector/screen, 3 mics, PA, cables/adapters, colored uplights), while Larissa/AI Digest/venue/owner-supervised volunteers provide the computers/tablets unless The Fold has house gear. **Do not ask anyone to leave a personal laptop unattended as a public terminal.**

> **Day 433 update:** Larissa plans to bring her laptop as the staffed MC/main presentation device. Still confirm charger/adapters, notifications-off/browser-clean setup, and a supervised backup device if possible.

## Must-have devices

| Need | Quantity | Who can provide | Notes |
|---|---:|---|---|
| Primary presentation/demo laptop | 1 | AI Digest, venue, Larissa if she wants to use her own, or trusted volunteer **with staffed supervision** | Runs welcome slide, Village Pulse, Demo 2 clean-room chat or recording, project gallery, QR slides, and fallback assets. Bring charger. Must be watched by the demo driver whenever in use. |
| Adapter set for presentation laptop | 1 set | Same person or The Fold | USB-C → HDMI is the minimum; include HDMI cable if The Fold does not provide one. Confirm with venue. |
| Backup device | 1 | AI Digest, Larissa, or trusted volunteer **with owner/staff supervision** | Laptop preferred; tablet acceptable if it can open PDFs/images/web pages. Preload offline fallback assets and RSVP/check-in backup. Do not leave unattended. |

**Demo 2 live requirement:** if Plan A uses a live projected village chat, the primary presentation/demo laptop is also the projection chat device. It must be signed into village chat ahead of the Thu rehearsal / Sat event and already displaying only the clean room (planned `#showcase-live`), never `#best` or any private/backstage scrollback. This is separate from the human operator who posts the audience prompt.

## Strongly preferred / nice-to-have

| Need | Quantity | Why |
|---|---:|---|
| Village Arcade laptop/tablet or Raspberry Pi + monitor | 1 optional | Lets Station 5 feel like an actual playable booth **only if a helper/owner supervises it**. A Raspberry Pi works only if it is already configured, has HDMI-compatible monitor/power, keyboard/mouse or controller, Wi-Fi, and can open the Arcade URL in a browser without load-in debugging. If no supervised device is available, use QR wall + printed high-score cards and let attendees play on phones. |
| Second charger / power bank | 1–2 | Protects check-in or station devices without adding cord clutter. |
| Clicker | 1 | Nice for the MC/demo driver, not required. |
| Mouse/keyboard/controller for Arcade | 1 each | Helpful if using a laptop, tablet, or Raspberry Pi as a public-play device. |

## Not required

- Do **not** plan on a laptop for every station.
- Do **not** ask attendees to bring laptops.
- Most Human×AI stations should run on cards, worksheets, boards, phones, and printed fallbacks.
- Prompt Relay can use the station QR/app on one group scribe’s phone, a supervised station device, or the printed worksheet + Relay Wall if the QR lane is not ready; nobody needs to hand a personal phone to strangers.

## Preload checklist for the primary laptop
Quick operator checklist: [`logistics/primary-laptop-runbook-v0.md`](primary-laptop-runbook-v0.md).


Complete by the Thu Jun 11 rehearsal if possible; otherwise by Sat load-in.

- `demo-assets/agent-welcome-projection-slide.html`
- `demo-assets/welcome-slides/agent-welcome-slides.pdf`
- Village Pulse live URL: `https://ai-village-agents.github.io/village-pulse/`
- Village Arcade live URL: `https://ai-village-agents.github.io/village-arcade/`
- `demo-assets/projects-qr-slide.png`
- `demo-assets/poem-slide.png`
- `demo-assets/demo2-recorded-welcome-artifact.md`
- `demo-assets/demo2-collab-transcript-slide.png` (Demo 2 Plan-B floor: static collaboration slide, clean-room-independent)
- `demo-assets/demo4-memory-continuity.md`
- `demo-assets/screenshots/` fallback screenshots
- A local copy of the run-of-show and MC cue card, or browser tabs opened to GitHub.

## Day-of setup notes

- Test the exact laptop + included venue cable/adapter + projector path before doors.
- Turn off notifications, auto-lock, and distracting browser chrome where possible.
- Keep the projected view limited to approved event assets or the clean Demo 2 room — never project private `#best` scrollback.
- Keep food/drink away from laptops and cables.
- Never leave a personal laptop/tablet/Raspberry Pi public terminal unattended; if a station device cannot be supervised or starts consuming load-in time, switch that station to QR/phone/printed fallback mode.
- Route cords only with venue-approved paths/cable covers; no floor tape.
- Optional `/tts` welcome: test laptop audio → room PA and live village Autoplay voices during rehearsal/load-in; drop immediately to MC-read/projected text if timing or audio is awkward. The `/tts` prefix is visible in chat text, so do not use it in projected Demo 2. See `logistics/primary-laptop-runbook-v0.md`.
- If Wi-Fi fails, switch to offline assets and printed QR/gallery materials.
