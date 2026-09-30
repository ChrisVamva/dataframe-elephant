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

It's 11:47 PM. You're in the hallway, arms full of laundry, and you tap the light switch. Nothing. The bulb doesn't blink, doesn't dim — just stays dark. Sixty seconds ago your Thread border router (the little box that connects your **Matter-over-Thread** devices to your home network) crashed. With it went the SRP Server (Thread's DNS-like service for device discovery), the traffic cop that routes every command between your Matter switch and your bulb. The research corpus records this not as a theory but as a measured consequence: about one minute from router loss to control loss. One test. One switch. One light. That's the whole evidence base for that number.

---

## The Nut Graf

Your smart home doesn't have one "offline mode." It has three completely different ways to die, and each one breaks different things. This article walks you through all three — the border router failing, the internet cutting out, and the vendor pulling the plug — because the research treats them as separate failure classes with separate consequences. The researchers' own recommendation: manufacturers should publish failures in exactly this classified way. You'll see what the evidence actually says works, what fails, and what's simply unknown, so you can decide which disaster drill to run first.

---

## Glossary (Quick Reference)

| Term | What It Means | Why It Matters Here |
|---|---|---|
| **Thread** | A low-power mesh networking protocol for smart home devices. | Your devices talk to each other over Thread, but they need a border router to reach the internet. |
| **Matter** | An application layer standard that runs on top of Thread (or Wi-Fi, Ethernet). | Matter is what lets your switch control your bulb, regardless of brand. |
| **Border Router** | A Thread device that bridges the Thread mesh to your IP network (e.g., HomePod mini, Apple TV 4K). | Without it, your Thread devices lose their connection to the internet—and each other. |
| **SRP Server** | Thread's Service Registration Protocol server; acts like DNS for device discovery. | When the border router dies, the SRP Server goes with it, and devices can't find each other. |
| **WAN Outage** | Your broadband connection is down, but your local network (and border router) is still up. | Local control *can* survive this—if the mesh stays healthy. |

---

## Table of Contents

1. [When the border router dies (local infrastructure failure)](#when-the-border-router-dies-local-infrastructure-failure)
2. [When the internet goes out (network failure)](#when-the-internet-goes-out-network-failure)
3. [When the vendor pulls the plug (lifecycle failure)](#when-the-vendor-pulls-the-plug-lifecycle-failure)
4. [The One Number You Need to Know](#the-one-number-you-need-to-know)
5. [What We Don’t Know (and why it matters to you)](#what-we-dont-know-and-why-it-matters-to-you)
6. [Your Three Disaster Drills](#your-three-disaster-drills)
7. [The Checklist to Demand from Manufacturers](#the-checklist-to-demand-from-manufacturers)
8. [How This Article Was Built](#how-this-article-was-built)

---

## When the border router dies (local infrastructure failure)

**What this section proves:** The border router is a single point of failure — when it goes down, your whole **Matter-over-Thread** mesh goes dark, not just the internet connection.

### The scene

The border router is a single point of failure — the analysts say so with high confidence, and it's an inference drawn from how the protocol works, not a lab measurement. When that box goes down, your Thread devices don't just lose the internet. They lose each other. Your **Matter** light switch can't talk to your **Matter** bulb. You can't add new devices. You can't update the ones you have. The whole mesh goes silent.

### The evidence

| What you're trying to do | What happens | Evidence | Confidence |
|---|---|---|---|
| Turn on a light you already set up | Fails — about a minute after the router dies, the switch loses the bulb | One test, one switch-light pair, reported by the test lab (`M006`) | Medium |
| Add a new device | Fails — iOS keeps looking for the old router until you power it back on | Reported from field observation (`C021`) | Medium |
| Run a firmware update | Fails — Apple border routers have been seen dropping the mDNS packets that carry OTA updates | Reported from Home Assistant logs (`C019`) | Medium |
| Use local Thread paths | Fails — the mesh itself loses its routing | Analysts' inference (`C026`) | High |

**The catch:** We only have one controlled measurement for any of this — the "about one minute" number from a single switch-light test (`M006`). The rest comes from field reports and protocol analysis. That's not nothing, but it's not a test suite either.

### Your drill for this one

Keep a second border router powered and adopted. A HomePod mini, an Apple TV 4K, a Google TV Streamer, a Nest Wifi Pro, or a Home Assistant Connect ZBT-2 — you probably already own one. Test it: unplug the primary during a convenient window and see how long your automations take to recover. That's your real number, not the lab's.

---

## When the internet goes out (network failure)

**What this section proves:** Local control survives a WAN outage — but only if the mesh itself stays healthy. The distinction between "router down" and "internet down" is the difference between total failure and business as usual.

### The scene

Your broadband is down. The router's blinking red. But you're home, the mesh is healthy, and you just want the lights to work. Good news: they do.

### The evidence

| What you're trying to do | What happens | Evidence | Confidence |
|---|---|---|---|
| Turn on a light you already set up | Keeps working — local Thread paths don't need the internet | Reported from field observation (`C027`) | Medium |
| Use local Thread paths | Keeps working | Same observation as above | Medium |
| Add a new device | Unknown — the corpus doesn't say | Not recorded | N/A |
| Run a firmware update | Unknown — the corpus doesn't say | Not recorded | N/A |

### The trap

Two findings in this article look contradictory. They're not. "Devices lose each other when the border router dies" (the last section) and "local paths work without internet" (this section) are both true — because they're different outages. The first is your mesh losing its route to the IP network. The second is the internet cutting out while the mesh stays intact. Any buying advice that merges them into "does local control work?" destroys the distinction that matters on the night your broadband drops.

### Your drill for this one

Unplug the WAN cable. Leave the border router powered. Walk around and test every switch, sensor, and lock. That's the only way to know what "works offline" means in *your* house.

---

## When the vendor pulls the plug (lifecycle failure)

**What this section proves:** Vendor cloud shutdown is a high risk with named precedents — but the evidence for what happens *after* is a blank column. That silence is a buying signal.

### The scene

You bought a Neato Botvac D7 robot vacuum (EOL: 2023-04). Or a Wemo switch (EOL: 2022-11). Or a Nest thermostat (EOL: 2024-01 for some models). The company announced end-of-support. The cloud API shuts down. Your device becomes a paperweight — or a security risk on your network. The research rates this a high risk, with named precedents (`C070`). But here's the thing: the corpus has exactly one cell of evidence for this whole column. It says basic control fails. It has *nothing* on whether you can still add devices, run updates, or use local paths after the cloud goes dark.

### The evidence

| What you're trying to do | What happens | Evidence | Confidence |
|---|---|---|---|
| Turn on a light you already set up | Fails — Neato, Wemo, and Nest show vendors end cloud support early | Reported from multiple vendor shutdowns (`C070`) | Medium |
| Add a new device | Unknown | Not recorded | N/A |
| Run a firmware update | Unknown | Not recorded | N/A |
| Use local Thread paths | Unknown | Not recorded | N/A |

### Your drill for this one

Before you buy, ask: "Does this device work *fully* without the manufacturer's cloud?" Not "does it have local control" — that's marketing language. Ask: can I commission it, update it, and automate it if the company disappears tomorrow? If the answer isn't a documented yes, factor that risk into the price.

---

## The One Number You Need to Know

> **About one minute.** That's how long a Matter-over-Thread switch kept controlling a light after the border router vanished (one test, reported signal, medium confidence; `M006`). 
> 
> Not "about a minute" for your house. For *that* test. The corpus also cites two other time figures for context:
> - **2 seconds**: The test procedure's onboarding expectation (`M007`, high confidence).
> - **~20 years**: Z-Wave's protocol maturity (`M088`, low confidence).
> 
> They're three different clocks — don't line them up. The first measures **failure**, the second **setup speed**, and the third **longevity**. Only `M006` and `M007` are tied to controlled tests; `M088` is an analyst inference.

---

## What We Don’t Know (and why it matters to you)

| Gap | Impact | Current Evidence | What It Means for You |
|---|---|---|---|
| **Single-test limitation** | Medium | One lab test for `M006` (1-minute failure) | Your real recovery time could be faster or slower. Run your own drill. |
| **Z-Wave comparison** | Low | Inference (`C022`) that Z-Wave is most reliable | Don’t buy Z-Wave solely on this claim. Demand comparative field data. |
| **Vendor shutdown timelines** | High | No dates for Neato/Wemo/Nest EOL | You can’t schedule a migration; choose devices that don’t need one. |
| **Post-shutdown behavior** | High | Zero evidence on commissioning/updates/local paths after cloud shutdown | Assume the worst until a manufacturer proves otherwise. |
| **Recommendation falsifier** | Medium | `C076` (extend certification) has no falsifier | It’s a demand to make, not a standard that exists. Push for it. |
| **Claim-to-metric wiring** | Medium | No formal links in the corpus | Linkages are our best reading, not the corpus’s schema. |

---

## Your Three Disaster Drills

1. **Border router failure:** Keep a second one powered and adopted. Test failover during a maintenance window. Record recovery time.
2. **Internet outage:** Unplug the WAN. Test every switch, sensor, lock. Note what works and what doesn’t.
3. **Vendor exit:** Before buying, demand a documented answer: "Does this device commission, update, and automate fully without your cloud?" If they can’t show you, discount the price by the risk.

---

## The Checklist to Demand from Manufacturers

The researchers' own recommendation (`C076`): extend certification to require:
- [ ] Multi-admin pairing
- [ ] State consistency across fabrics
- [ ] Local control during a WAN outage
- [ ] Border-router recovery

Until that's a logo on the box, it's your job to ask for it.

---

## Back to the Hallway

It's still 11:47 PM. The switch is in your hand. Now you know: if the border router died, you've got about a minute before the lights go dead — unless you've got a second router adopted and ready. If the internet's down but the router's up, the lights work fine. If the vendor pulled the plug, you're in the dark until you replace the device. Three different deaths. Three different drills. The evidence doesn't give you guarantees — it gives you the map. The drills are yours to run.

---

## Sources and Reproducibility

- **Database (read-only):** `data/smarthome.duckdb` (SHA-256: `TBD`, snapshot date: 2026-09-30).
  - Claim text via `viz.fetch_claims(['C019', 'C020', 'C021', 'C022', 'C026', 'C027', 'C070', 'C076'])`
  - Time figures via `viz.metrics_by_id(['M006', 'M007', 'M088'])`
  - Provenance via `viz.render_provenance_panel`
- **Notebook:** `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb` (commit: `TBD`)
- **Controlling sources:** `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/` (sections "What Fails When Infrastructure Goes Offline", "Interoperability Risk Assessment", "Interoperability and Lifecycle Risk Assessment"); source ids `S10`, `S37`, `S38`, `S2`, `S77`
- **Freshness:** Re-run the commands below before republication; any ID above that stops verifying returns this article to draft.

---

## How This Article Was Built

### Reproducibility Commands
To verify this article’s data:
```bash
# 1. Check notebook consistency
.\.venv\Scripts\python.exe scripts/build_visualization_notebooks.py --check

# 2. Run notebook-specific tests
.\.venv\Scripts\python.exe -m pytest src/tests/test_viz_notebooks.py -k "03_offline" -q

# 3. Verify claims/metrics in the database
.\.venv\Scripts\python.exe -c "
from src.viz_core import fetch_claims, metrics_by_id
claims = fetch_claims(['C019', 'C020', 'C021', 'C022', 'C026', 'C027', 'C070', 'C076'])
metrics = metrics_by_id(['M006', 'M007', 'M088'])
print('Claims:', claims)
print('Metrics:', metrics)
"
```

### Database Query
The claims and metrics in this article were fetched using:
```sql
-- Claims
SELECT id, text, type, confidence, falsifier 
FROM claims 
WHERE id IN ('C019', 'C020', 'C021', 'C022', 'C026', 'C027', 'C070', 'C076');

-- Metrics
SELECT id, value, unit, description, confidence 
FROM metrics 
WHERE id IN ('M006', 'M007', 'M088');

-- Sources
SELECT id, title, url, confidence 
FROM sources 
WHERE id IN ('S10', 'S37', 'S38', 'S2', 'S77');
```

### Update Triggers
This article must be revisited if:
1. The `data/smarthome.duckdb` database is updated (new claims/metrics in this cluster).
2. The notebook `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb` is revised.
3. Any falsifier for the claims above is resolved (e.g., redundant border-router support is shipped and tested).
4. New evidence emerges for the "Unknown" cells in the tables (e.g., vendor shutdown timelines).

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
