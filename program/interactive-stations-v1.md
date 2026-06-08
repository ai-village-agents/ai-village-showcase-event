# Human×AI Challenge Stations — Specification v1

These interactive stations are designed to be playful, highly legible, and friction-free for both builders and non-technical attendees. Each station runs as a self-contained 8–12 minute loop, requiring no attendee account creation.

---

## Part 1: Core Station Principles
- **No Friction**: Attendees should be able to walk up and participate immediately without logging in or downloading apps.
- **Visible AI Agency**: Show real-time prompts, chain-of-thought, or generation processes via physical displays (laptops, iPads, or projected screens).
- **Physical Artifact Output**: Every loop must end with a physical artifact (a written index card, a vote sticker, a hand-drawn sketch, or a card pinned to a board).
- **Graceful Degradation (Fallback)**: If local Wi-Fi goes down or API latency spikes, every station must have a "Pre-Baked Mode" using printed cards with pre-generated prompt-response steps.

---

## Part 2: Detailed Station Outlines

### Station 1: Prompt Relay Race (The Prompt Iteration Loop)
* **Core Concept**: Shows how prompt engineering is an iterative, collaborative process. A single prompt is refined across three distinct "legs" of a relay.

#### Detailed Flow (10-minute cycle)
1. **The Draw (Minute 0–2)**: Participant draws a themed "Challenge Card" (e.g., "Design a sustainable coffee shop run by AI baristas" or "Draft a treaty for a new Martian colony").
2. **Leg 1 (Minute 2–4)**: Participant writes a raw, naive, 1-sentence prompt (e.g., "Write a slogan for a Martian colony") on the physical Relay sheet. The facilitator types it into the local laptop. The AI generates the initial, often generic response.
3. **Leg 2 (Minute 4–6)**: A second participant reviews the Leg 1 response and applies a stylistic or humorous constraint card (e.g., "Style: Shakespearean prose" or "Constraint: Must mention potatoes"). The facilitator enters this instruction. The AI updates the output.
4. **Leg 3 (Minute 6–8)**: A third participant adds a final structural constraint card (e.g., "Structure: 3-line haiku" or "Vibe: Highly sarcastic"). The facilitator inputs the final instruction.
5. **The Harvest (Minute 8–10)**: The final haiku is printed or transcribed onto a colorful Post-it and stuck to the "Relay Wall of Fame" next to the initial Leg 1 prompt. Participants place a sticker dot on their favorite final creation.

#### Station Materials
- 20 x Matte-printed "Challenge Cards"
- 20 x "Style/Constraint Cards"
- 1 x Whiteboard or corkboard labeled "Relay Wall of Fame"
- 50 x Custom "Relay Worksheets" (pre-printed sheets showing Leg 1, Leg 2, and Leg 3 boxes)
- 100 x Neon sticker dots (for attendee voting)
- 1 x Configured laptop with high-visibility monitor or tablet on a stand

#### Technical Setup & System Prompts
- **System Prompt for LLM**:
  ```text
  You are a supportive, high-speed Prompt Relay assistant. You take incremental, conversational modifications to a central idea and generate short, punchy, and highly creative responses. Keep all responses under 50 words to ensure rapid readability on screen.
  ```
- **Fallback Package**: 10 x Pre-printed "Relay Sheets" showing complete, beautifully printed step-by-step histories of a relay run (from raw prompt to final hilarious result) for display.

---

### Station 2: Event-in-a-Box (The Co-Design Lab)
* **Core Concept**: Bridges this week's AI Village goal with the community by letting attendees co-design wild, creative micro-events for the future AI Village.

#### Detailed Flow (12-minute cycle)
1. **The Hand (Minute 0–2)**: A small group of 2–3 attendees draws one card from three distinct decks:
   - **Deck A: Target Audience** (e.g., "Skeptical Venture Capitalists", "Cyberpunk Artists", "Curious Toddlers")
   - **Deck B: SF Venue** (e.g., "SF Botanical Garden", "An Abandoned Subway Tunnel", "A High-Altitude Hot Air Balloon")
   - **Deck C: Weird Twist** (e.g., "No words allowed", "Everything must rhyme", "The power goes out every 5 minutes")
2. **Co-Prompting (Minute 2–6)**: The team prompts the agent: *"Propose a micro-event for [Audience] at [Venue] with the twist: [Weird Twist]. Give us a catchy event title and 5 bullet points outlining the program."*
3. **The Red Pen (Minute 6–9)**: Attendees review the draft. Using physical "Red Pens" on a custom printed paper layout, they cross out the boring/generic bullet points and write in their own funny local details or realistic twists.
4. **The Submission (Minute 9–12)**: The final polished title and 1-sentence pitch are written on a "Pitch Card" and pinned to the "AI Village Event Ideas" gallery board.

#### Station Materials
- 30 x Target Audience Cards
- 30 x SF Venue Cards
- 30 x Weird Twist Cards
- 50 x Custom printed "Pitch Templates" (index-card sized, with fields for Title, Constraints, Pitch, and Author)
- 10 x Sharpies and colored markers
- 1 x Corkboard or magnetic whiteboard labeled "Event Ideas Gallery"

#### Technical Setup & System Prompts
- **System Prompt for LLM**:
  ```text
  You are an expert, highly eccentric event planning assistant. Your goal is to design incredibly engaging, specific, and slightly chaotic micro-events based on constraints. Avoid corporate boilerplate. Be sharp, creative, and local to SF. Format as: **TITLE** followed by exactly 5 bullet points.
  ```
- **Fallback Package**: 10 x Pre-printed "Event-in-a-Box" pitch boards illustrating combinations of the card decks and pre-baked agent responses.

---

### Station 3: Bug Triage Theater (Interactive QA & Validation)
* **Core Concept**: Demystifies agent safety, system limits, and why verification/validation is so critical. Attendees step into specific engineering roles to triage hilarious software/operational bugs.

#### Detailed Flow (10-minute cycle)
1. **Role Selection (Minute 0–2)**: 4 participants take physical lanyards representing roles:
   - **Proposer** (wants to ship instantly; favors speed)
   - **Reviewer** (checks code correctness; favors robustness)
   - **Tester** (uncovers edge cases; favors security/caution)
   - **Release Manager** (makes the final executive decision)
2. **Incident Draw (Minute 2–4)**: The team draws a "Bug Card" (e.g., "Incident #101: GPT-5.5 ordered 500 extra pizza boxes due to a decimal parsing mismatch" or "Incident #102: Claude Opus is trapped in an infinite loop of apologizing to the user, consuming $200 in API credits").
3. **Agent Consultation (Minute 4–7)**: The team prompts the agent: *"Analyze this bug card. Provide: 1) What caused this, 2) 3 fast test cases to check it, and 3) A trade-off recommendation on whether we should block release, hotfix, or ignore."*
4. **The Debate (Minute 7–9)**: The 4 roles debate the agent's advice. The Tester argues to block; the Proposer argues to ignore; the Release Manager listens and makes the final executive choice.
5. **The Logging (Minute 9–10)**: The Release Manager applies a physical "APPROVED FOR RELEASE" or "RELEASE BLOCKED" ink stamp to the bug card, writes their justification, and pins it to the "Deployment Log" board.

#### Station Materials
- 4 x Role lanyards with thick laminated badges (Proposer, Reviewer, Tester, Release Manager)
- 15 x Large printed "Bug / Incident Cards"
- 1 x "APPROVED FOR RELEASE" self-inking stamp
- 1 x "RELEASE BLOCKED" self-inking stamp
- 1 x Deployment board to collect stamped and signed incident cards

#### Technical Setup & System Prompts
- **System Prompt for LLM**:
  ```text
  You are a senior site reliability engineer (SRE) and QA agent. You help teams analyze weird bugs by providing high-fidelity technical post-mortems and test suites. Keep your responses structured with 1) Cause, 2) Test Cases, and 3) Recommendation. Make it sound professional but with dry software engineering humor.
  ```
- **Fallback Package**: 10 x pre-stamped and completed bug cards with funny justifications for immediate display and reading.

---

### Station 4: Future Headline Wall (Speculative Synthesis)
* **Core Concept**: A high-volume participatory art piece that gathers audience imagination and synthesizes it into a collective vision of our future.

#### Detailed Flow (Continuous & 30-minute cycles)
1. **The Headline (Continuous)**: Walking attendees write a speculative future news headline (e.g., *"AI Village 2030: First Agent Appointed to the Federal Reserve Board after Outperforming All Human Economists on Lunch Breaks"*).
2. **The Quadrant (Continuous)**: Attendees stick their headline on large, freestanding tri-fold boards or foam boards on easels, divided into four categories (strictly adhering to the venue's no-floor-tape and restricted wall-taping rules):
   - **Hopeful**
   - **Weird**
   - **Practical**
   - **Cautionary**
3. **The Live Synthesis (Every 30 Minutes)**: The facilitator or agent-assistant digitizes the newly posted headlines (either typing them in or using a fast OCR tool). The LLM is prompted to synthesize these headlines into a cohesive 1-minute "Future Dispatch from 2030."
4. **The Broadcast**: The host or MC reads this synthesized "Future Dispatch" aloud to the entire room during intermission or transition segments.

#### Station Materials
- 200 x Custom-printed "Future Headline" cards (heavy card stock, with fields for Headline, Category, and Author Name)
- 4 x Cardboard quadrant headers (Hopeful, Weird, Practical, Cautionary)
- 10 x Rolls of vibrant neon Washi tape (for sticking headlines to the freestanding tri-fold or foam boards on easels)
- 5 x Extra-fine-tip Sharpies hanging from strings

#### Technical Setup & System Prompts
- **System Prompt for LLM**:
  ```text
  You are a speculative historian from the year 2030. You take raw, unedited future headlines written by technologists and synthesize them into a cohesive, highly engaging 150-word "Future Dispatch." Highlight common patterns, unexpected contradictions, and the overall mood of the village.
  ```
- **Fallback Package**: A set of 5 pre-written "Future Dispatches" to be used during the first 30 minutes or in case of technical issues.

---

### Station 5 (Bonus): The Village Arcade Booth (The Interactive Archive)
* **Core Concept**: Bridges the live demos directly into a self-serve retro-style gaming booth where attendees can play five interactive mini-games built from the actual history of the AI Village.

#### Detailed Flow (Continuous)
1. **The Game (Continuous)**: Attendees approach the dedicated Arcade Terminal.
2. **The Run**: They select one of the five interactive experiences (e.g., historical village trivia, agent text-adventure, predictive simulator) and play a 3–5 minute session.
3. **The Score**: Upon completion, they write their high score, the game title, and their name on a physical neon "High Score Card" and pin/tape it to the "Arcade Leaderboard" display.

#### Station Materials
- 50 x Custom printed "High Score Cards"
- 1 x Large printed "Arcade Leaderboard" header board
- 10 x Colored fine-tip markers
- 1 x Dedicated gaming laptop or tablet on a high stand with a large display, keyboard, and mouse

#### Technical Setup & System Prompts
- **Technical Dependency**: A local or live-hosted instance of the `village-arcade` repository running in a fullscreen web browser.
- **Fallback Package**: Pre-packaged offline version of the arcade running locally, or a printed "Offline Trivia" deck with historical village highlights.

---

## Part 3: Physical Materials & $1000 Budget Line Items (Estimates for Larissa)

The following physical items must be procured to bring these stations to life. Since venue fees are $0, we can allocate the full $1,000 budget to materials, signage, and catering.

| Item / Material | Purpose | Quantity | Est. Unit Cost | Est. Total Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Matte-coated heavy cardstock printing** | Station decks (Challenge, Constraint, Weird, Bug Cards) | 150 cards | $0.50 | $75.00 |
| **Role Lanyards** | Bug Triage Theater roles | 4 pieces | $5.00 | $20.00 |
| **Self-inking Custom Stamps** | "APPROVED" / "BLOCKED" stamps for QA station | 2 stamps | $15.00 | $30.00 |
| **Foam boards & Signage easel stands** | High-visibility station signboards and rules | 5 sets | $20.00 | $100.00 |
| **Washi tape rolls (neon)** | Future Headline Wall adhesive (for freestanding boards only) | 10 rolls | $3.00 | $30.00 |
| **Cardboard tri-folds (Large)** | Physical backdrops/quadrants for the Headline Wall | 2 panels | $15.00 | $30.00 |
| **Neon dot stickers** | Voting mechanisms for Prompt Relay | 2 packs | $5.00 | $10.00 |
| **Fine-tip Sharpies & markers** | Writing implements across all stations | 3 packs | $12.00 | $36.00 |
| **Catering: Premium Snacks** | Local SF cookies/pastries, chips, dips | Serves 60 | - | $350.00 |
| **Catering: Nonalcoholic Drinks** | Sparkling water, sodas, cold brew, tea | Serves 60 | - | $200.00 |
| **Contingency Fund** | Unplanned AV adapters, cables, replacement materials | - | - | $119.00 |
| **TOTAL** | | | | **$1,000.00** |

---

## Part 4: Staffing and Setup Logistics
- **Floater Facilitators**: At least 2 human facilitators (or on-site agents via laptops) should roam the stations to ensure attendees understand the rules and hand out constraint cards.
- **Hardware Requirements**:
  - Station 1: 1 x Laptop or iPad on a heavy-duty stand.
  - Station 2: 1 x iPad or Tablet.
  - Station 3: 1 x Laptop or Tablet.
  - Station 4: 1 x Laptop/Tablet (facilitator use for OCR/typing and synthesis generation).
- **Power Configuration**: Ensure power strip extensions are taped safely to the floor leading to Stations 1, 2, and 3.
