# Three ways your smart home dies

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

## 1. Claim Summary (with IDs)

Your smart home does not have one "offline mode". The corpus distinguishes three different failure classes with different consequences: the Thread border router disappearing, the internet (WAN) link going down, and the vendor retiring a cloud service. Each section below follows one failure class, and every statement carries its claim id so it can be checked in the provenance panel.

---

## 2. Provenance Panel

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
---

## 3. Evidence and Metrics

### Lede

The hallway goes dark. You tap the switch — nothing. Sixty seconds ago the Thread border router crashed, and with it went the SRP Server that routes every command between your Matter-over-Thread light switch and your bulb. The corpus records this not as a theory but as a measured consequence: about one minute from router loss to control loss (`M006`, reported signal, medium confidence; scope: a Matter-over-Thread switch-and-light pair when the SRP Server is unavailable).

### Nut graf

This article walks you through the three distinct ways your smart home dies — local infrastructure failure (the border router), network failure (the WAN link), and lifecycle failure (the vendor cloud) — because the corpus treats them as three different failure classes with different consequences, and its own recommendation (`C076`) argues manufacturers should publish failures in exactly this classified way. You will see exactly what the evidence says works, what fails, and what is simply not recorded, so you can decide which disaster drill to run first.

---

### Death 1 — the border router goes away (local infrastructure failure)

**What the evidence says:** the border router is a single point of failure (`C026`, inference, high confidence). When it goes down, Thread devices lose mesh communication with each other, not just with the internet. Concretely: a light switch loses control of a light after about one minute because the SRP Server is unavailable (`C020`, reported signal, medium). You cannot add new devices (`C021`, reported signal, medium — iOS keeps treating the removed network as preferred until the original router is powered back on). You cannot patch the ones you have (`C019`, reported signal, medium — Apple border routers failing to forward mDNS packets blocks OTA updates in Home Assistant). Local Matter/Thread paths themselves fail (`C026` again).

| Capability | Border router removed / replaced | Governing claim | Evidence class · confidence |
|---|---|---|---|
| Basic control of commissioned devices | fails | `C020` | reported signal · medium |
| Commissioning new devices | fails | `C021` | reported signal · medium |
| Firmware updates | fails | `C019` | reported signal · medium |
| Local Matter/Thread paths | fails | `C026` | inference · high |

Blank cells in the corpus's failure map mean "no claim in this cluster records this combination" — blank is not the same as working.

### Death 2 — the internet goes down (network failure)

**What the evidence says:** local Matter/Thread paths keep working without internet for basic operations (`C027`, reported signal, medium). This covers both basic control of commissioned devices and the local paths themselves. Two claims in this article look contradictory and are not: `C020` says devices lose each other when the border router is down; `C027` says local paths work without internet. Both hold because they describe different outages — `C027` is an internet outage on a working mesh, `C020` is the mesh losing its route to the IP network. Any buying advice that merges them into one "does local control work?" verdict destroys exactly the distinction that matters on the night your broadband drops.

| Capability | Internet (WAN) down | Governing claim | Evidence class · confidence |
|---|---|---|---|
| Basic control of commissioned devices | keeps working | `C027` | reported signal · medium |
| Local Matter/Thread paths | keeps working | `C027` | reported signal · medium |
| Commissioning new devices | not recorded | — | — |
| Firmware updates | not recorded | — | — |
### Death 3 — the vendor goes away (lifecycle failure)

**What the evidence says:** cloud shutdown without local fallback is rated a high risk, with named precedents: Neato, Wemo and Nest demonstrate that vendors can and will end cloud support earlier than promised or without a migration path (`C070`, reported signal, medium). The vendor-lifecycle column in the corpus's failure map is one cell deep — only basic control is claimed against a retired cloud; commissioning, firmware and local-path behaviour after a cloud shutdown are simply not recorded. That silence is itself a buying signal.

| Capability | Vendor cloud retired | Governing claim | Evidence class · confidence |
|---|---|---|---|
| Basic control of commissioned devices | fails | `C070` | reported signal · medium |
| Commissioning new devices | not recorded | — | — |
| Firmware updates | not recorded | — | — |
| Local Matter/Thread paths | not recorded | — | — |

### The one quantity, and two figures that are not comparable with it

`M006` is the only recorded measurement of how quickly control is lost: "about 1" minute (reported signal, medium confidence; scope: a Matter-over-Thread light switch losing a light when the SRP Server is unavailable). The corpus also records two other time figures; they are shown here so the reader sees the scale of the corpus's time language — they are not three points on one axis.

| Metric | Stated value | Unit | What it actually measures | Class · confidence |
|---|---|---|---|---|
| `M006` — time to lose device control after border router removal | about 1 | minute | Measured consequence: switch loses light, SRP Server unavailable | reported signal · medium |
| `M007` — Z-Wave protocol maturity | about 20 | years | Comparison-table entry ("rock-solid"), not a measurement | reported signal · low |
| `M088` — onboarding response expectation | 2 | seconds | The corpus's own test procedure (Test T1: device responds to on/off within 2 s after commissioning) | documented fact · high |

Linkage note: `M006` reaches this article by shared source id (`S10`, "What Fails When Infrastructure Goes Offline"); `M007` and `M088` are read by explicit metric id for context, not as cluster measurements.
---

## 4. Visualization / Reference

- Failure-state × capability heatmap (one claim per cell; blank = no claim in this cluster): `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb`, evidence cell (states: "Border router removed / replaced", "Internet (WAN) down", "Vendor cloud retired"; capabilities: basic control, commissioning, firmware updates, local paths).
- Coverage bar ("how much of the failure map the corpus fills", four capabilities per state): same notebook, evidence cell — shows the vendor-lifecycle column one cell deep.
- Three time figures, each in its own unit (minutes / years / seconds): same notebook, context cell (`M006`, `M007`, `M088` via `viz.metrics_by_id`, parsed with `viz.numeric_value`).
- Claim-wording audit table ("the claims the map is read from", claim text printed beside each reading): same notebook, uncertainty cell.
- All figures interactive (Plotly, `plotly_mimetype+notebook`); reproduce headless via the notebook or `src/tests/test_viz_notebooks.py`.

---

## 5. Uncertainty, Gaps, and Limitations

- **One measurement, several relayed observations.** `M006` is medium confidence; the map's cell readings come from reported-signal claims (`C019`, `C020`, `C021`, `C027`) rather than controlled trials.
- **`C022` is a low-confidence inference** that Z-Wave remains the most reliable option for mission-critical use. It is kept because it is the corpus's only comparative reliability statement, and it is labelled as an inference wherever it appears — including here.
- **`C070` names vendors without dates.** Neato, Wemo and Nest are recorded as having ended cloud support earlier than promised, but the corpus records no shutdown dates, so no timeline is drawn in this article.
- **The vendor-lifecycle column is one cell deep** (see the table in Death 3): post-shutdown commissioning, firmware and local-path behaviour are not recorded.
- **`C076` carries no falsifier** (`L030`): as a recommendation it has no recorded observation that would disconfirm it, which is proper for its kind — but it means the closing ask below is synthesis, not evidence.
- **No foreign key** joins claims to metrics (`schemas/stage2.sql`); linkage here is heuristic (section-first, then source id) and the rule is stated per metric above.

---

## 6. Interpretation / Synthesis (explicit label)

*Everything in this section is editorial synthesis, not corpus evidence.* If you buy Matter-over-Thread today, plan as if three separate disaster drills apply: keep a second border router powered and adopted (Death 1 is total — control, commissioning and updates all fail); test what "works offline" means with the WAN unplugged while the mesh is healthy, because that is the only outage `C027` covers (Death 2); and prefer devices with documented local fallback, because vendors have ended clouds early before and the corpus cannot tell you what happens the day after (Death 3). The corpus's own recommendation — extend certification to multi-admin pairing, state consistency across fabrics, local control during a WAN outage, and border-router recovery (`C076`) — is the checklist to demand from manufacturers until then.

---

## 7. Sources and Reproducibility

- Database (read-only): `data/smarthome.duckdb`. Claim text via `viz.fetch_claims([...])`; time figures via `viz.metrics_by_id(["M006", "M007", "M088"])`; provenance via `viz.render_provenance_panel`.
- Notebook: `notebooks/2/03_offline_failure_and_cloud_dependency.ipynb` — the map's cell readings are notebook-level data, printed beside the claim text they were read from, so the mapping audits without leaving the page.
- Controlling sources: `schemas/stage2.sql`; `research/raw/Stage 2/Extraction 1/Device Types & Feature Consistency.md` ("What Fails When Infrastructure Goes Offline", "Optional Features, Extensions, and Certification Gaps", "Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems", "Interoperability Risk Assessment", "For Standards and Certification Bodies"); source ids `S10`, `S37`, `S38`, `S2`, `S77`.
- Freshness: re-run `scripts/build_visualization_notebooks.py --check` and `src/tests/test_viz_notebooks.py` before republication; any id above that stops verifying returns this article to draft.
