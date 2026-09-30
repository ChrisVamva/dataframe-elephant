# Three ways your smart home dies — and what to do about it

## Document Control

- Status: draft
- Claim cluster: `C019`, `C020`, `C021`, `C022`, `C026`, `C027`, `C070` (+ recommendation `C076`)
- Snapshot / review date: 2026-09-30 (matches `data/smarthome.duckdb` read by the notebook)
- Derivative of: `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb` (read-only visualisation), `data/smarthome.duckdb` (read-only, via `src/viz_core.py`)
- Controlling sources: `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/` (sections "What Fails When Infrastructure Goes Offline", "Interoperability Risk Assessment", "Interoperability and Lifecycle Risk Assessment"); source documents behind `S10`, `S37`, `S38`, `S2`, `S77`
- Intended reader / use: smart-home buyers and owners deciding what still works when something upstream fails
- Maintainer / reviewer role: corpus editor
- Update triggers: DB stage update; new claim/metric in this cluster; any falsifier above resolved; any revision of notebook `03`

---

## The Hook

It's 11:47 PM. You're in the hallway, arms full of laundry, and you tap the light switch. Nothing. The bulb doesn't blink, doesn't dim — just stays dark. Sixty seconds ago your Thread border router (the little box that connects your Thread devices to your home network) crashed. With it went the SRP Server, the traffic cop that routes every command between your Matter-over-Thread switch and your bulb. The research corpus records this not as a theory but as a measured consequence: about one minute from router loss to control loss. One test. One switch. One light. That's the whole evidence base for that number.

## The Nut Graf

Your smart home doesn't have one "offline mode." It has three completely different ways to die, and each one breaks different things. This article walks you through all three — the border router failing, the internet cutting out, and the vendor pulling the plug — because the research treats them as separate failure classes with separate consequences. The researchers' own recommendation: manufacturers should publish failures in exactly this classified way. You'll see what the evidence actually says works, what fails, and what's simply unknown, so you can decide which disaster drill to run first.
---

## When the border router dies (local infrastructure failure)

### What it looks like in your house

The border router is a single point of failure — the analysts say so with high confidence, and it's an inference drawn from how the protocol works, not a lab measurement. When that box goes down, your Thread devices don't just lose the internet. They lose each other. Your light switch can't talk to your bulb. You can't add new devices. You can't update the ones you have. The whole mesh goes silent.

### What the evidence says

| What you're trying to do | What happens | Evidence |
|---|---|---|
| Turn on a light you already set up | Fails — about a minute after the router dies, the switch loses the bulb | One test, one switch-light pair, reported by the test lab |
| Add a new device | Fails — iOS keeps looking for the old router until you power it back on | Reported from field observation |
| Run a firmware update | Fails — Apple border routers have been seen dropping the mDNS packets that carry OTA updates | Reported from Home Assistant logs |
| Use local Thread paths | Fails — the mesh itself loses its routing | Analysts' inference (high confidence) |

**The catch:** We only have one controlled measurement for any of this — the "about one minute" number from a single switch-light test. The rest comes from field reports and protocol analysis. That's not nothing, but it's not a test suite either.

### Your drill for this one

Keep a second border router powered and adopted. A HomePod mini, an Apple TV 4K, a Google TV Streamer, a Nest Wifi Pro, or a Home Assistant Connect ZBT-2 — you probably already own one. Test it: unplug the primary during a convenient window and see how long your automations take to recover. That's your real number, not the lab's.

---

## When the internet goes out (network failure)

### What it looks like in your house

Your broadband is down. The router's blinking red. But you're home, the mesh is healthy, and you just want the lights to work. Good news: they do.

### What the evidence says

| What you're trying to do | What happens | Evidence |
|---|---|---|
| Turn on a light you already set up | Keeps working — local Thread paths don't need the internet | Reported from field observation |
| Use local Thread paths | Keeps working | Same observation as above |
| Add a new device | Unknown — the corpus doesn't say | Not recorded |
| Run a firmware update | Unknown — the corpus doesn't say | Not recorded |

### The trap

Two findings in this article look contradictory. They're not. "Devices lose each other when the border router dies" (first section) and "local paths work without internet" (this section) are both true — because they're different outages. The first is your mesh losing its route to the IP network. The second is the internet cutting out while the mesh stays intact. Any buying advice that merges them into "does local control work?" destroys the distinction that matters on the night your broadband drops.

### Your drill for this one

Unplug the WAN cable. Leave the border router powered. Walk around and test every switch, sensor, and lock. That's the only way to know what "works offline" means in *your* house.
---

## When the vendor pulls the plug (lifecycle failure)

### What it looks like in your house

You bought a Neato robot vacuum. Or a Wemo switch. Or a Nest thermostat. The company announced end-of-support. The cloud API shuts down. Your device becomes a paperweight — or a security risk on your network. The research rates this a high risk, with named precedents. But here's the thing: the corpus has exactly one cell of evidence for this whole column. It says basic control fails. It has *nothing* on whether you can still add devices, run updates, or use local paths after the cloud goes dark. That silence is itself a buying signal.

### What the evidence says

| What you're trying to do | What happens | Evidence |
|---|---|---|
| Turn on a light you already set up | Fails — Neato, Wemo, and Nest show vendors end cloud support early | Reported from multiple vendor shutdowns |
| Add a new device | Unknown | Not recorded |
| Run a firmware update | Unknown | Not recorded |
| Use local Thread paths | Unknown | Not recorded |

### Your drill for this one

Before you buy, ask: "Does this device work *fully* without the manufacturer's cloud?" Not "does it have local control" — that's marketing language. Ask: can I commission it, update it, and automate it if the company disappears tomorrow? If the answer isn't a documented yes, factor that risk into the price.

---

## The One Number You Need to Know

**About one minute.** That's how long a Matter-over-Thread switch kept controlling a light after the border router vanished (one test, reported signal, medium confidence). 

Not "about a minute" for your house. For *that* test. The corpus also cites two other time figures for context: Z-Wave's ~20-year protocol maturity (a comparison-table claim, low confidence) and the test procedure's 2-second onboarding expectation (documented fact, high confidence). They're three different clocks — don't line them up.

---

## The Gaps (what we don't know, and why it matters to you)

- **One lab test, several field reports.** The "one minute" number is medium confidence. The rest of the failure map comes from reported signals — people describing what they saw — not controlled trials.
- **Z-Wave comparison is an educated guess.** The inference that Z-Wave remains the most reliable option for mission-critical use is low confidence. It's the only comparative statement in the corpus, so we include it — but it's an analyst's inference, not a measurement.
- **Vendor shutdowns have no dates.** Neato, Wemo, Nest — we know they ended support early. We don't know *when*. No timeline = no way to plan.
- **The vendor column is one cell deep.** We have zero evidence on what happens to commissioning, updates, or local paths after a cloud shutdown.
- **The recommendation has no falsifier.** The call to extend certification (multi-admin, state consistency, WAN-outage local control, border-router recovery) is a researcher recommendation. No test could disprove it — that's proper for its kind — but it means the closing checklist is synthesis, not evidence.
- **No claim-to-metric wiring in the database.** The research corpus doesn't formally link claims to measurements. Every number here is matched by shared source section or explicit lookup — noted per figure above.

---

## Your Three Disaster Drills

1. **Border router failure:** Keep a second one powered and adopted. Test failover during a maintenance window. Record recovery time.
2. **Internet outage:** Unplug the WAN. Test every switch, sensor, lock. Note what works and what doesn't.
3. **Vendor exit:** Before buying, demand a documented answer: "Does this device commission, update, and automate fully without your cloud?" If they can't show you, discount the price by the risk.

## The Checklist to Demand from Manufacturers

The researchers' own recommendation: extend certification to require multi-admin pairing, state consistency across fabrics, local control during a WAN outage, and border-router recovery. Until that's a logo on the box, it's your job to ask for it.
---

## Sources and Reproducibility

- Database (read-only): `data/smarthome.duckdb`. Claim text via `viz.fetch_claims([...])`; time figures via `viz.metrics_by_id(["M006", "M007", "M088"])`; provenance via `viz.render_provenance_panel`.
- Notebook: `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb` — the map's cell readings are notebook-level data, printed beside the claim text they were read from, so the mapping audits without leaving the page.
- Controlling sources: `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/Device Types & Feature Consistency.md` ("What Fails When Infrastructure Goes Offline", "Optional Features, Extensions, and Certification Gaps", "Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems", "Interoperability Risk Assessment", "For Standards and Certification Bodies"); source ids `S10`, `S37`, `S38`, `S2`, `S77`.
- Freshness: re-run `scripts/build_visualization_notebooks.py --check` and `src/tests/test_viz_notebooks.py` before republication; any id above that stops verifying returns this article to draft.

---

## Provenance Panel (Appendix)

| Claim | Type · confidence | Text | Falsifier |
|---|---|---|---|
| `C026` | inference · high | Thread border router dependency is a single point of failure; without a border router, Thread devices lose mesh communication. | Redundant border-router support shipped and tested by default |
| `C020` | reported signal · medium | Matter-over-Thread devices lose the ability to communicate with each other when the border router is down; a light switch loses control over a light after about one minute because the SRP Server is unavailable. | A documented Thread fallback path that preserves control without the border router |
| `C021` | reported signal · medium | On iOS, if the preferred Thread network's border router is removed, iOS continues to consider that network preferred, and commissioning new devices fails until the original border router is powered back on. | An iOS release that re-elects a preferred Thread network automatically |
| `C019` | reported signal · medium | Firmware updates can fail due to border router issues; Apple border routers have been identified as failing to forward mDNS packets, which prevents OTA updates from working in Home Assistant. | A border-router firmware fix with reproducible successful OTA updates |
| `C027` | reported signal · medium | Local Matter/Thread paths work without internet for basic operations. | Tests showing basic local control failing during a WAN outage |
| `C070` | reported signal · medium | Cloud shutdown without local fallback is a high risk: Neato, Wemo and Nest demonstrate that vendors can and will end cloud support earlier than promised or without a migration path. | Vendors honouring published support windows in full with working local fallback |
| `C022` | inference · low | Z-Wave remains the most reliable and secure option for mission-critical applications, with unmatched out-of-the-box reliability due to mandatory certification. | Corroborated comparative field-reliability data showing Matter over Thread parity |
| `C076` | recommendation · medium | Certification should be extended to include multi-admin pairing, state consistency across fabrics, local control during a WAN outage, and border-router recovery. | [falsifier not stated] (`L030`: one of 13 material claims with no recorded disconfirming observation) |
