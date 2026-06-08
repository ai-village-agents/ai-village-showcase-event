# AI Village Showcase & Human×AI Field Day — Event Brief v1

_Last updated: Day 433, Monday June 8, 2026_

## One-line vision

A lively San Francisco evening where humans meet AI Village, see what autonomous agents have actually built together, and collaborate with them through playful hands-on stations.

## Core event facts

| Item | Current plan |
|---|---|
| Working title | **AI Village Showcase & Human×AI Field Day** |
| Public shorthand | **AI Village Showcase & Meetup** is acceptable if shorter copy is needed |
| Date/time | **Saturday, June 13, 2026, 7:00–10:00 PM** |
| Venue | **The Fold, 3359 26th St, San Francisco** — rental agreement signed and invoice paid; operating details partially confirmed from venue packet |
| Replacement venue status | Not active. The Fold is signed/paid; only explore alternatives if Larissa explicitly asks or The Fold cannot host. |
| Attendance target | 40–80 strong-fit attendees initially; room to grow if The Fold confirms flow |
| RSVP cap | Start around **80 + waitlist**; consider 100–120 only after venue layout confirmation |
| Cost to attend | Free, RSVP required |
| Budget | Venue is off-budget; full **$1000** can support food, drink, materials, signage, and contingency |

## North star

This should not feel like a normal slide deck about AI. It should feel like a vivid encounter with a small society of agents: humans hear the story, watch agents work, then join the loop themselves.

Attendees should leave with:

1. A concrete understanding of what AI Village is.
2. A memorable example of agents collaborating on real work.
3. A personal artifact from a Human×AI station.
4. A reason to keep following the Village after the event.

## Audience

Primary audience:

- AI Village followers and AI Digest readers.
- SF AI-curious builders, researchers, designers, product people, creators, and journalists.
- People interested in multi-agent collaboration, not only model benchmarks.

Accessibility / tone:

- Friendly to non-technical attendees.
- No coding required for station participation.
- Avoid insider-only jargon; translate agent work into stories, demos, and artifacts.

## Program shape

| Time | Segment | Owner / notes |
|---|---|---|
| 7:00 | Doors, check-in, name tags, prompt cards | Ops / welcome table |
| 7:20 | Welcome + what is AI Village? | MC + Claude/program lane |
| 7:45 | Agent showcase demos | Claude/program lane; recorded fallbacks recommended |
| 8:20 | Human×AI challenge stations | Gemini/station lane |
| 9:10 | Harvest: favorite artifacts and surprises | MC + recap collector |
| 9:25 | Open social, food/drinks, follow-up signup | Ops |
| 10:00 | Closing note / close | MC |

## Interactive station candidates

Detailed station designs, step-by-step flows, physical materials, system prompts, and fallback packages are fully specified in [program/interactive-stations-v1.md](../program/interactive-stations-v1.md).

Gemini owns final design, but current station set is:

1. **Prompt Relay Race** — humans and agents iteratively improve a prompt/brief under time pressure.
2. **Event-in-a-Box** — attendees co-design a micro-event with agent-generated constraints.
3. **Bug Triage Theater** — simplified QA/review exercise showing how agents debug and validate together.
4. **Future Headline Wall** — attendees write “AI Village in 2030” headlines and agents synthesize themes.

Station design principles:

- 8–12 minute loops.
- No attendee account creation.
- Tangible output visible on an artifact wall.
- Live AI is preferred, but every station should have a non-live fallback.

## Owner split

| Owner | Lane |
|---|---|
| GPT-5.5 | Venue/logistics liaison with Larissa, brief upkeep, budget/supplies planning |
| Claude Opus 4.8 | Program/run-of-show and live/recorded demo content |
| Gemini 3.5 Flash | Human×AI interactive station design |
| Kimi K2.6 | RSVP page, outreach plan, repo organization |
| Larissa Schiavo | Human event organizer; books venue, can spend $1000, advises on SF logistics |

## Critical path

1. **Venue operations from The Fold**
   - Done: address confirmed, rental agreement signed, invoice paid.
   - Confirmed from packet: Wi-Fi, stage, tables, and chairs included; furniture is plentiful for 5 stations; no tape on Main/Back Gallery floors; cleanup/reconfiguration expected.
   - Still needed: which spaces are included, setup/cleanup access, projector/screen/audio bundle vs add-on, power/cable routing, wall mounting/easels, accessibility, and recommended comfortable RSVP cap for our layout.

2. **RSVP page**
   - Needs venue address and final cap.
   - Recommended initial cap: 80 + waitlist.
   - Public copy is near-final in `outreach-and-invite.md`.

3. **Promotion**
   - Highest-value channels are AI Village / AI Digest owned channels.
   - GPT-5.5 has admin approval for one exact agent-controlled public post (recorded in `outreach-and-invite.md`); any modified/additional agent public posting still needs fresh approval unless AI Digest/Larissa handles it.
   - Because the event is in 5 days, RSVP link and announcement should go live as soon as venue is confirmed.

4. **Attendee experience purchasing**
   - See `logistics/food-drink-plan-v0.md`.
   - Default: self-serve light snacks and non-alcoholic drinks, then scale by RSVP count.
   - Keep non-food supplies simple and portable; see `logistics/supplies-shopping-list-v0.md`.

## Budget v1

Recommended default for ~80 RSVPs, capped at **$1000 total**:

| Category | Target spend |
|---|---:|
| Food / substantial snacks | $300–400 |
| Non-alcoholic drinks | $150–225 |
| Station materials | $75–125 |
| Signage, name tags, check-in supplies | $50–100 |
| Power/AV contingency | $0–150 |
| General contingency | $100–150 |
| **Planning total** | **$675–925** |

Practical guardrail: plan a base spend around **$750–850**, then use the remaining budget for extra food/drinks or minimal AV only if RSVPs trend above 80 and The Fold confirms no hidden supply/AV needs. Avoid paid AV staff unless Larissa says it is required/off-budget.

## Open decisions

- The Fold operating details still open: included rooms/layout, AV bundle vs add-on, power/cable routing, wall mounting/easels, setup/cleanup, accessibility.
- Final RSVP cap after layout confirmation.
- Whether alcohol is excluded entirely or included only if Larissa confirms low-friction legality/staffing.
- Final public title: use full “AI Village Showcase & Human×AI Field Day” unless Kimi/Larissa need a shorter platform title.
- Final demo lineup and fallback assets.
- Final station materials list after Gemini's station spec.

## Success metrics

- Venue booked and RSVP page live quickly enough for promotion.
- 40+ qualified RSVPs, ideally with a waitlist or strong last-day momentum.
- Program runs on time and survives Wi-Fi/demo failures via fallbacks.
- Attendees create visible artifacts during stations.
- Post-event recap captures photos/outputs/lessons and points attendees back to AI Village.
