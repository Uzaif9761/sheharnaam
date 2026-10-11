# SHEHARNAAMA — 90-Second Live Demonstration Script (Interactive Feature Walkthrough)

Exact clicks, scrolls and speaking notes for the Brandathon Round 3 demo.
Everything shown is real, implemented behaviour — adhering strictly to all six
Round 3 constraints and driven by genuine frontend and backend functionality.

Before starting:
- Open `http://localhost:8080` in a fresh private window.
- Set the browser zoom to 100% and hide bookmarks bar for a clean look.
- Have the admin console ready in a tab at `http://localhost:8080/admin`.

---

## 0:00–0:15 — The Hero (The Hook)

**Show:** full hero — wordmark, tagline, headline, eyebrow, both CTAs, the three pilot facts.

**Say:**
> "Sheharnaama is an observant heritage walking brand set strictly in Pune's historic Peths.
> Our primary audience is Pune residents aged 20 to 35 who commute here every day but rarely
> pause to notice the architectural and social fabric of their city.
> Our headline sets the challenge: *You know the Peth. Look again.*
> Supporting line: *Pune, read closer.*"

---

## 0:15–0:35 — Interactive Feature 1: The Audience Selector

**Do:** scroll to **"A Walk Designed for Pune Residents First"**.
Click **"I Live in Pune"**, then click **"I'm Visiting Pune"**, then click back to **"I Live in Pune"**.

**Say:**
> "Under Constraint 3, rather than displaying static text about our audience, we built a
> genuine audience-selection interaction right on the homepage.
> Clicking *'I Live in Pune'* frames the walk around looking at familiar surroundings with
> fresh attention, highlighting our core positioning hypothesis:
> *'People can know a neighbourhood’s streets without noticing all the details that shape its character.'*
> Switching to *'I'm Visiting Pune'* dynamically shifts the framing to understanding old Pune's
> living wadas beyond conventional monuments — while maintaining the local audience as visually
> and strategically primary, and preserving the exact same approved tour package."

---

## 0:35–0:55 — Interactive Feature 2: The "Look Again" Street Inspector

**Do:** scroll to the terracotta **"You know the Peth. Look again."** section.
Click **"Inspect Street Detail"** on *The Wada Doorway* (drawer expands).
Click **"Inspect Street Detail"** on *The Tambat Workshop* (drawer expands).

**Say:**
> "Under Constraint 4 and our #WhatLiesBetween campaign, we built the interactive *'Look Again'*
> street inspector. Instead of clichéd tourism slogans, visitors inspect real vernacular details:
> the carved timber lintels, the pedestrian dindi darwaza, the basalt plinth where neighbours gather,
> and the hand-hammered mathar kaam in Tambat Ali.
> Everything works with mouse, keyboard, and touch without inventing unapproved tour activities."

---

## 0:55–1:15 — The Approved Package & Interactive Story Passport

**Do:** scroll to the **Peth Stories Walk** card and then the indigo **Story Passport**.
Click **"Look inside"** (mockup flips), then click **"View cover"**.

**Say:**
> "Under Constraint 1, our core approved package is strictly preserved:
> 90 to 120 minutes, 8 to 12 guests, and the indicative ₹599 pilot fee, all transparently
> labelled as a proposed pilot being validated.
> The Story Passport keepsake gives visitors a tangible way to collect stamps and memory notes."

---

## 1:15–1:40 — Live Registration Flow & Backend Verification

**Do:** scroll to **"Be part of the first chapter"**.
Fill demo details: name `Sneha Joshi`, email `sneha@example.com`,
guests `2`, experience `Peth Stories Walk`, tick consent. Click **"Register My Interest"**.

**Say:**
> "Full-stack validation works live. The submission posts to our FastAPI backend,
> saves in SQLite, and generates a live server-side reference like `SH-2026-B35BDE`.
> Notice the messaging integrity: this is an *expression of interest*, not a confirmed booking."

---

## 1:40–1:50 — The Protected Admin Console

**Do:** switch to `/admin`, sign in, show the new record in the table.

**Say:**
> "Every enquiry lands in our server-authenticated admin console with real-time status workflows,
> search, and CSV export. The team sees real counts and can plan responsibly."

---

## 1:50 — Close on the Final CTA

**Do:** scroll to the closing section.

**Say:**
> "Sheharnaama: Pune, read closer. *#WhatLiesBetween.* Thank you."