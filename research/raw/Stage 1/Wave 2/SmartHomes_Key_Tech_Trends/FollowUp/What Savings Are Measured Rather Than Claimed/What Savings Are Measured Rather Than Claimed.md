---
modified: 2026-09-28T20:27:12+03:00
---
The evidence base for coordinated smart-home energy systems has matured significantly, but it remains uneven across device types, control strategies, and geographies. Field trials and utility programs now provide hard numbers for peak reduction, cost savings, and comfort impacts—yet the gap between modelled potential and measured outcomes persists, often by a factor of two or more. Below, I assess what is actually verified, what fails in practice, and where the value flows.

---

## 📊 What Savings Are Measured Rather Than Claimed?

**Heat pump water heaters (HPWHs)** have the strongest field evidence. A 2025 LBNL field demonstration across 10 homes using CTA-2045 controls and five different California pricing profiles found that **29–54% of load was shifted away from peak periods**, reducing HPWH electricity costs by **8–46%** depending on the price profile. Simulations showed that adopting CTA-2045-B with the Advanced Load Up feature would increase cost savings by **21 percentage points** and peak reduction by **31 percentage points**. A separate European field test with 16 autonomous smart water heaters confirmed feasible cost reduction and efficiency gains under real-time pricing, but found **strong dependency on utilization rates**—households with low hot water demand saw negligible benefit.

**HVAC and heat pumps** show meaningful but variable results. A UK field trial of third-party control on air-source heat pumps achieved an **average power reduction of 88.2% during DR events** (maximum demand reduction of 1.581 kW across a building cluster), with override requests in only **2.7%** of cases and events lasting 30–120 minutes. Supervisory predictive control of an air-to-air heat pump in field demonstration reduced total heating energy costs by **19% on average** (95% confidence interval). However, a controlled test-room study found that a "smart" controller solely focused on precise indoor temperature control **did not guarantee energy savings and potentially jeopardized equipment** due to frequent cycling, with efficiency actually decreasing at part load—contradicting both literature and manufacturer claims.

**EV charging** is the most automation-sensitive load. Analysis of 558 charging stations in Korea found that stations with **automatic controls achieved an average 11.8% reduction during DR event hours**, while **manual adjustments yielded only 0.4%**—underscoring the limitations of voluntary compliance. Station occupancy rate mattered: facilities with 25–63% occupancy showed the largest reductions. A nationwide UK demand flexibility program (2.6 million customers, 16 winter events) reduced **overall peak grid demand by 23.1% among compliers** at an average household remuneration of £2,900 per MWh; adoption of solar, batteries, heat pumps, and EVs all increased demand response participation.

**Batteries and solar** deliver reliable but context-dependent value. A Greek simulation study found that residential buildings achieve **40–60% self-consumption** with balanced PV-to-battery ratios (≈4 kW PV / 10 kWh battery) under net-billing; transitioning from flat to time-of-use tariffs increased self-consumption by **up to 20 percentage points**. Offices performed worst (5–30% self-consumption) due to limited operation hours. Payback periods remained within **6–8 years** across scenarios. However, a Japanese randomized controlled trial on households with rooftop PV found that critical peak pricing induced only **3–4% usage reductions**—a quarter of the effect seen in households without solar, suggesting PV owners have less incentive to respond to peak pricing.

**Whole-home coordination** produces the largest aggregate effects. A nationwide UK field experiment reduced peak grid demand by **28.1% among all program participants**. A Dutch trial with 1,000 households shifting consumption to sunny hours achieved **0.24 kW per household per test moment**. But a critical caveat: current estimates suggest that only **50% of projected savings from demand flexibility resources are actually realized** due to regulatory, technological, and social barriers.

---

## 🔗 Which Device Combinations Provide the Greatest Flexibility?

| Combination | Flexibility Mechanism | Measured Flexibility | Key Constraint |
|---|---|---|---|
| **HPWH + TOU tariff** | Thermal storage in 50–80 gal tank | 29–54% peak load shift | Depends on household hot water usage; low-utilization homes see minimal benefit |
| **Heat pump + battery + solar** | Thermal + electrical storage, PV self-consumption | 88.2% average power reduction during events | Requires third-party control; override requests low (2.7%) but comfort-sensitive users may disengage |
| **EV charger + automatic control** | Deferrable charging load | 11.8% DR event reduction (automatic) vs. 0.4% (manual) | Occupancy rate matters; 25–63% is optimal range |
| **Battery + solar + TOU** | Arbitrage + self-consumption | 40–60% residential self-consumption | Building usage is dominant factor; offices perform poorly (5–30%) |
| **Whole-home (HP + battery + solar + EV)** | Multi-asset optimization | 28.1% nationwide peak reduction among participants | Coordination complexity; regulatory barriers to aggregation |

The evidence consistently shows that **thermal storage devices (HPWHs, heat pumps) paired with batteries and EVs** offer the greatest aggregate flexibility, but the marginal value of each additional device diminishes. A UK field trial explicitly tested combinations—heat pump alone, + solar, + battery, + EV—and found that coordination was essential; uncoordinated assets provided minimal flexibility.

---

## 🌡️ What Comfort and Equipment-Life Penalties Occur?

**Comfort impacts are real but often tolerable.** A Ghent heat pump field experiment with nine well-insulated homes found indoor temperatures **0.38°C lower on average during interventions**, with moderate comfort impacts. A UCL study of three heat pump homes found air temperature drops of **0.3–1.1°C over 3 hours** during DR events; participants either did not perceive the change, noticed but tolerated it, or refused it and adjusted the heat pump. Critically, the study challenged conventional modelling assumptions that DR is unnoticed if temperatures stay within steady-state comfort bounds—**occupants negotiate and incorporate DR into daily practices**, meaning comfort is not purely a physical variable.

A PNNL study in Cordova, Alaska, found that **household-level thermal comfort is more sensitive to the duration of the DR event than to the degree of temperature offset**. Setpoint offsets maintaining indoor operative temperatures between **18–22°C (65–71°F)** may be preferred in cold climates. A Stockholm field study using a personalized DSM app found that **about 25% of events were cancelled** by users, indicating that even with control, comfort preferences frequently override flexibility goals.

**Equipment-life penalties are documented but poorly quantified in consumer settings.** A controlled test-room study found that a smart controller focused on precise temperature control caused **frequent cycling**, potentially reducing system efficiency by **over 10%** and shortening compressor lifespan due to mechanical stress. The same study noted that **efficiency decreased at part load**, contradicting manufacturer claims. Optimal dead-band control research confirms that frequent on/off switching leads to **excessive wear and tear**, and that dynamic adjustment of the dead band can achieve up to **10% energy reduction without degrading regulation performance**—but only if the control strategy explicitly accounts for equipment health. A DTU study warned that cost-driven control algorithms may compromise device lifetime compared to thermostats optimized for reduced wear and tear.

In practice, **the equipment-life penalty is a design choice, not an inevitability**. Systems that enforce minimum on/off times (60 min on, 30 min off) and avoid short-cycling can deliver flexibility without accelerated wear. But many commercial "smart" controllers prioritize temperature precision or cost savings over equipment health, and the field evidence suggests this trade-off is not always transparent to consumers.

---

## ⚡ Which Tariffs, Aggregators, and Regulations Make Flexibility Financially Attractive?

**Tariff structures that work:**
- **Time-of-use (TOU) with a high peak-to-off-peak ratio** is the most reliable driver. HPWH field demonstrations using California TOU rates achieved 8–46% cost savings, with **greater impacts when the price difference between low and high periods was larger**.
- **Real-time pricing (RTP)** enlarges storage capacity requirements (up to 18 kWh for PV-battery systems) but yields **only marginal self-consumption gains** compared to TOU. The Greek study concluded that moderate temporal differentiation—refined TOU aligned with demand profiles—offers a **balanced pathway** without RTP's operational complexity.
- **Capacity-based tariffs** are emerging as an alternative that encourages peak reduction without requiring direct DSO control. A Dutch randomized field experiment is testing static and TOU variants of capacity-based tariffs, with grid charges expected to **rise threefold** if demand response is not adopted.

**Aggregators** are essential for residential participation. Small-scale distributed resources can only participate in markets if aggregated. EU regulations (Articles 13, 15, 17 of the Electricity Directive) mandate **non-discriminatory access to all electricity markets for consumers and aggregators**, and require member states to establish mechanisms that properly value flexibility. The forthcoming **network code on demand response** and **Implementing Act on data interoperability** are expected to further support uptake.

**Compensation structures that work:** A Harvard analysis of 46,822 EV drivers and 6.87 million charging sessions found that **programs offering both upfront enrollment payments and ongoing static participation incentives consistently outperformed all other designs**. A UK nationwide program paid consumers **£2,900 per MWh** of demand reduction, achieving 23.1% peak reduction among compliers. E.ON's flexibility trial in the UK reported **bill savings of up to £360/year per household** from a guaranteed £30/month payment.

**Regulatory barriers persist.** Demand response services are **not always remunerated in the same way as generation**, and remuneration should be compliant with the Electricity Balancing Guideline (EBGL) without distinctions. Conflicts can arise between consumers and suppliers over **accounting of energy flows and compensation** when participating in explicit demand-side flexibility schemes. Transparency regarding **control strategies, event duration, frequency, comfort impacts, and financial compensation** is essential for sustained user engagement.

---

## 🔌 Can Matter-Based Controls Interoperate with Utilities and Home-Energy-Management Systems?

**The specification foundation exists; deployment is nascent.** Matter 1.5 (November 2025) introduced clusters for **tariff and pricing information** and **electrical grid condition signalling**, enabling devices to receive and act upon external economic and grid-state signals. However, grid communication is currently **limited to providing carbon intensity information** to devices. Additional device types include **Electrical Meter and Electrical Utility Meter**.

**Matter alone is insufficient for utility coordination.** A 2026 ACEEE analysis concluded that Matter **"currently lacks native mechanisms for coordinating directly with external utility or aggregator platforms"**. The recommended architecture is a **two-protocol pathway**: Matter handles in-home communication between appliances and an energy gateway; **OpenADR 3** handles communication between that gateway and utilities or grid operators.

The Connectivity Standards Alliance and OpenADR Alliance announced a **liaison agreement in May 2026** to formalize this collaboration, intended to provide an **end-to-end communications pathway from grid operators to individual devices in the home**. The partnership aims to make it easier for manufacturers to develop products capable of working with DR programs and for utilities to have a **"standardized, scalable mechanism for demand response"**.

**Practical limitations remain.** A test integration of Matter into a DataWallet system found that **"the Matter specification is far ahead of the actual device adoption; none of the aforementioned device types is available as a Matter compliant device yet"**—the researchers had to build a **simulator for a solar inverter** to test the integration. The system polled the Matter device's ActivePower attribute every **five seconds**, converted milliwatts to watts, and published to an MQTT topic for the DataWallet's data model. Security was maintained through Matter's commissioning and operational credentials, with internal data access governed by the DataWallet's MQTT access controls and consent policies.

**CTA-2045** remains the most widely deployed communication protocol for demand response in North America, and the LBNL HPWH field demonstrations used it successfully across 10 homes and five pricing profiles. OpenADR 3, IEEE 2030.5, OCPP, and HCA each address specific segments of the ecosystem. The emerging consensus is that **no single protocol will serve all needs**; interoperability requires a layered approach where Matter handles local device control and OpenADR handles grid signals.

---

## 📅 Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems for Energy Flexibility

| Aspect | Matter/Thread | Zigbee | Z-Wave | Proprietary (e.g., Nest, Ecobee) |
|---|---|---|---|---|
| **Energy management device types** | Spec includes solar PV, battery, EV charging, heat pump, HVAC, water heater (Matter 1.3+) | Limited; mostly sensors and switches | Limited; some thermostats and energy meters | Device-specific; deep integration within vendor ecosystem |
| **Tariff/pricing signals** | Matter 1.5 clusters for tariff and grid condition | Not standardized | Not standardized | Vendor-specific; often cloud-dependent |
| **Utility/aggregator coordination** | Requires OpenADR 3 bridge | Requires proprietary gateway | Requires proprietary gateway | Vendor cloud APIs |
| **Local control** | Yes (if border router present) | Yes (via hub) | Yes (via hub) | Often cloud-dependent for advanced features |
| **Multi-admin / cross-ecosystem** | Supported but inconsistent | Not supported | Not supported | Not supported |
| **Field-proven flexibility** | Early; simulators used for testing | Mature but limited to device-level control | Mature but limited | Proven within walled gardens (e.g., Nest Rush Hour Rewards) |

**Key takeaway:** Matter/Thread offers the most credible path to **open, multi-vendor energy management**, but it is **not yet field-proven at scale for utility coordination**. Zigbee and Z-Wave are mature for device control but lack the data models and grid-signal support needed for demand response. Proprietary systems deliver reliable flexibility within their ecosystems (e.g., Nest thermostat DR programs) but lock users into a single vendor and cannot participate in open aggregation markets.

---

## 🚨 Interoperability Risk Assessment

**High Risk:**
- **Utility-to-device pathway immaturity.** Matter lacks native utility coordination; OpenADR integration is announced but not deployed. The Matter PV inverter device type did not exist as a commercial product as of 2026. Any product claiming "Matter-ready demand response" today is likely relying on proprietary middleware.
- **Equipment-life trade-offs are hidden.** Field evidence shows smart controllers can cause frequent cycling, reduce part-load efficiency by over 10%, and shorten compressor lifespan. Consumers and even some manufacturers may not be aware of these penalties.
- **Comfort-driven disengagement.** 25% of DR events were cancelled by users in a Stockholm field study. If override rates scale with broader deployment, program savings estimates will be systematically overstated.
- **Remuneration inequality.** DR services are not consistently remunerated like generation, and compensation conflicts between consumers, suppliers, and aggregators remain unresolved.

**Medium Risk:**
- **Building-type dependency.** Offices achieve only 5–30% self-consumption versus 40–60% for residential buildings. Flexibility programs designed for residential may fail in commercial settings.
- **Solar owners respond less to peak pricing.** Japanese RCT data shows 3–4% reductions for PV households versus ~12–16% for non-PV households. As solar penetration grows, the pool of responsive customers shrinks.
- **Battery availability ≠ battery flexibility.** A home battery's presence does not guarantee it will participate in demand response; homeowner preferences and warranty constraints may limit cycling.

**Low Risk:**
- **Basic load shifting with HPWHs and EV chargers.** These are proven, repeatable, and low-comfort-impact when properly controlled.
- **TOU tariff response for thermal loads.** Well-established across multiple field trials.
- **Local device control.** Matter/Thread devices continue to operate locally when the internet is down.

---

## 🛠️ Who Receives the Value?

| Stakeholder | Share of Value | Evidence |
|---|---|---|
| **Utilities / grid operators** | Highest: avoided peaking generation, deferred T&D investment | DSR could reduce distribution network investment by ~15%, saving up to £7.9 billion by 2050 |
| **Aggregators** | High: revenue from market arbitrage and ancillary services | Aggregators earn through arbitrage trading or ancillary service markets |
| **Consumers** | Moderate: bill savings of 8–46% for HPWHs, up to £360/year for UK flexibility participants | HPWH field data; E.ON trial |
| **Manufacturers** | Variable: revenue from smart devices, but margin pressure from commoditization | Matter specification ahead of device adoption; simulators required for testing |
| **Society** | Long-term: emissions reduction, grid reliability, lower system cost | Nationwide UK program reduced peak demand 23.1% |

The distribution is **asymmetric**: utilities and aggregators capture the largest and most certain value, while consumers bear the comfort, equipment-life, and administrative burdens with uncertain and variable compensation. This asymmetry is the central political economy challenge for residential demand flexibility.

---

## 🛠️ Product-Design Implications

1. **Design for equipment health explicitly.** Enforce minimum on/off times (60 min on / 30 min off is a reasonable starting point) and monitor cycling frequency. Do not assume that cost-optimizing algorithms will protect equipment—the field evidence shows they often do not.

2. **Treat comfort as a negotiated variable, not a constraint.** The UCL study shows that occupants sense and interpret temperature changes differently. Provide granular override controls, learn individual comfort preferences, and design for **reversible, short-duration events** rather than deep setbacks.

3. **Build for the two-protocol architecture.** Matter for in-home device control; OpenADR 3 for utility signals. Do not claim "Matter-native demand response" until the OpenADR bridge is commercially available and tested.

4. **Prioritize HPWHs and EV chargers for flexibility programs.** These have the strongest field evidence, lowest comfort impact, and highest automation responsiveness (11.8% vs. 0.4% for manual EV control). HVAC is more comfort-sensitive; batteries are valuable but homeowner-constrained.

5. **Publish measured performance, not modelled potential.** The 50% realization gap between projected and actual savings is a credibility problem for the entire category. Report field trial results with transparent baselines, uncertainty ranges, and who received the value.

6. **Design for tariff diversity.** TOU is the workhorse; RTP adds complexity without proportional benefit for most households. Build controllers that can adapt to any price signal—flat, TOU, RTP, or capacity-based—without requiring firmware updates.

7. **Plan for aggregator integration.** Even if your device does not directly connect to a utility, provide a standardized API (CTA-2045, OpenADR, or Matter clusters) so that aggregators can incorporate it into their portfolios without custom integration work.

The state of coordinated smart-home energy systems in 2026 is one of **proven device-level flexibility, emerging system-level coordination, and unresolved questions about who bears the cost and who captures the value**. The field evidence is strongest for HPWHs and EV charging, moderate for heat pumps and batteries, and weakest for solar self-consumption as a demand-response resource. Matter and OpenADR provide the architectural foundation for open utility-to-device coordination, but that foundation is not yet built at scale. Product design must bridge the gap with transparent performance reporting, equipment-protective control strategies, and flexible compensation models that fairly distribute the value created.

[

pdf.sciencedirectassets.com

In [55] an agent based BEMS is designed controlling heat pump, washing machine, dryer, and dishwasher considering PV generation,...

[55] an agent based BEMS is designed controlling heat pump, washing machine, dryer, and dishwasher considering PV generation, building load model, and hourly dynamic pricing. ... In [57] a building energy management solution is introduced controlling air conditioner, water heater, and electric vehicle using MPC. ... BEMS in [3] is designed to control thermal and electrical load using HVAC, EV, and appliances considering demand response signal (TOU)...



](https://pdf.sciencedirectassets.com/craft/capi/cfts/init?s=1800&p=%2F280276%2F1-s2.0-S2210670717X00103%2F1-s2.0-S221067071731435X%2Fam.pdf&q=X-Amz-Security-Token%3DIQoJb3JpZ2luX2VjEMH%252F%252F%252F%252F%252F%252F%252F%252F%252F%252FwEaCXVzLWVhc3QtMSJGMEQCICAQqKQvPPMCFYsvn0Flrtne1TqN3G8n87AA8miuiRnlAiAlA8nzVkicoBihJynFbi3NM8OztGCFRQSCMVqUOgGuTSq7BQiJ%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAUaDDA1OTAwMzU0Njg2NSIM27%252BptKPp%252Bf421htyKo8FkA9LFxoN1bls4vVvBikryxfhuUrnE%252FHEosAISireJJN4Syu7u3jWaXZRZxh%252F5EfC2%252BmcUihG6J8810wAcNdyatb%252Fy60v2267PgGHI6VLlpzC8W3UX%252FOya%252F8wgQxmFoD57De2tYDl9Pg3E4uqNhrmfquKcpQsDU%252FHFRUT34ktBbvtDfV%252FQgGKbr6X%252FPhlHufNjfiA0Krt6WDYBeHGD7PedMdXXNuquyzqes9WUJA2eC%252FKUCq2MKhJ866weyuQNmaEcFgsgrePbUs7qRYPogF4%252BUhJbvfNPAX6hsv%252FysGvNQo5ZzxW7F7Hi7JmYT4SZ5Jcpkhr89CvGxTs%252ByRMgqCKs%252BBMBDqmjRSqf0Egh%252Ffo6mOB%252F%252BerI9fHeY7QKWrSbQJnLUnRIyvEbqtOCJjnq1B5zwrz2GU%252FtI0Ei0J3GKqR9MOJ0qsOulM2qbsHcO4scupSNkrNTOxfMA1aGVr%252BKeUQNc19zYCrSVLe3%252FEOJPI%252FkWdoO4Z5qH43m83Vb6pbJQMb0oJG4xmSgyFpGVANQDh7iKFF2F%252Fd%252BNl6aWEzGOl9P3J%252FTHg20Ju6LLm6CBTtW8XYasTIGWhl9iX1%252F39uhh7Fav4ogBLIii55F6ceXa1UOBJWk3B%252Bp1RZ%252B4Tpkj%252BFpVbhfrUrunFSTtrQMaSRNb65PACN3yxjFIXAYoQmD9YAxSbKydLhqFsooGWvOCMr6jPaTjByPavNwCWqdPgh5I9Zq8sxfXAdIFQcQI%252Bply4c9RUrZwUWe3ptoSdpKh2BAeA%252BlJOrOzOqOgwyQ2PRBacNDx9oz297Z5LjMq6jXY5UwjhKLN%252FulJNMmrn%252BpBYjAMZQa%252BrNCOcK%252BFtm%252F1B8aSvQeZ76Cb9tveDvwVVur7SHRjCzqofOBjqyATYIOLX%252FqugHouhcy%252BwHhSsosSHnxQrHg4GfnoyKXphU23cjqm0GDSYWxwYJwLIERfiy1bAteU4fgYXEue%252F2QjQ3HGdJN0bV7ff5jlDIIRL3F0PJfXS8C4f5q1AOt3EbbFO%252B72hsaYF03yZY0dCQcK4gdIRfV1fOofKHzeID%252BjCu7G0oCAuvtjssf0VjvSCWqrQ6%252FLx4v9W1Y%252BLBhwxc63%252FiiysmBd7RY8W81nfxanKA1Yg%253D%26X-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Date%3D20260324T002832Z%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Expires%3D300%26X-Amz-Credential%3DASIAQ3PHCVTYT5HWKD4Z%252F20260324%252Fus-east-1%252Fs3%252Faws4_request%26X-Amz-Signature%3D77eaad0119921f974a84be76f13d36d5df294e74e63ebfe60607e53318954c7b%26hash%3D5190b18893c5de19dc5e929c009b5cf44094b9a49f0dad0d479e09212ccf4e7e%26host%3D68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61%26pii%3DS221067071731435X%26tid%3Dpdf-291a18a9-7221-4c52-8450-aa9500ae2f6b%26sid%3D95363bc248f755453088e85-5a22a0d5ff13gxrqa%26type%3Dclient&i=2026-03-24T00%3A28%3A34.273Z&c=challenge-cn&r=9e118e797aac135e&u=aHR0cHM6Ly93d3cuc2NpZW5jZWRpcmVjdC5jb20vc2NpZW5jZS9hcnRpY2xlL3BpaS9TMjIxMDY3MDcxNzMxNDM1WA%3D%3D&w=interactive&h=eyJrZXkiOiJVOVFMWVp6RStJenRva2swVVBvRm9VeTFuRkl2ck5udi9lNE9nV0JITXVWcnZiM2N1TTlDUXlFK3lHQTI4TDFnRXRkYVZncmtBRmJJLzhBYUlyQkpQR3ZzKzJORlBvTE5BTDFweXU5blpYaz0iLCJpdiI6IjE2NDA3ZjdiYTNhZjhiNzA1OWJmNjY1YjlhMDk1ZjZmIn0%3D#5#2)[

![](https://cdn.deepseek.com/site-icons/nationalgrid.co.uk)

commercial.nationalgrid.co.uk

<center>Figure 2-1: Example MADE Project Smart App Controls </center>

<center>Figure 2-1 ... A 5- home technology trial is in progress ... <table><tr><td>Home</td><td>Heat pump</td><td>Fossil boiler</td><td>PV array</td><td>Battery</td><td>EV Charger ... Combi</td><td>4.41kWp</td><td>Sonnen hybrid 5kWh</td><td>New Motion 32A</td><td>Nissan ... - Hybrid heating system ... - Hybrid heating system...



](https://commercial.nationalgrid.co.uk/downloads-view-reciteme/112243?__cf_chl_tk=5izM5oyDVjfFn3k.kNIQths9VGRdHGhgCAF6uQ9yRfg-1768839524-1.0.1.1-3mDuCb3oVG.oz_6a1ZIioje8OuIgnaTdF1d3xVCt3.E#3#2)[

permanent.fdlp.gov

When the HEMS control was applied to the homes, the operating schedules were adjusted to find an optimal trade- off between elec...

the operating schedules were adjusted to find an optimal trade- off between electricity cost savings and occupant discomfort (within prescribed comfort bounds) [12]. ... The A/C and ... For the house represented in hardware, these controls resulted in \(4.6\mathrm{kWh}\) or \(8\%\) energy savings during two days and \(14\%\) cost savings; however...



](https://permanent.fdlp.gov/gpo109816/70409.pdf?__cf_chl_tk=MUTYbFk.jUzZ_XX6JCraCIonqbb6lEuU8R30pBmCWss-1767449602-1.0.1.1-FfxMguZpvPtK2MxXSvfm5AuhHKFBQzTbrrxfik1LeY4#2#2)[

![](https://cdn.deepseek.com/site-icons/nationalgrid.co.uk)

commercial.nationalgrid.co.uk

- Phase 1: Baseline - The focus was on gathering baseline data about household and asset electrical demand with the assets large...

Baseline - The focus was on gathering baseline data ... the assets largely uncoordinated ... 2: In-home asset coordination - This phase involved automatic coordination of the operation of the hybrid heat pump with the battery and solar generation. ... (1) heat pump + solar (2) + battery (3) +EV</td></tr><tr><td>EV</td><td>Electric vehicle.



](https://commercial.nationalgrid.co.uk/downloads-view-reciteme/231490?__cf_chl_tk=ENs6o0kJpCmKW_jzTmdBE4W6IZ2T4mTDmMZuBNM5ecQ-1769032573-1.0.1.1-DjusHCVWxiKMkgZfeoLq6f.C.UckcfaQnf6TT8zJyMM#10#2)[

![](https://cdn.deepseek.com/site-icons/purdue.edu)

hammer.purdue.edu

7.5 The full model's one- step- ahead predictions (blue curves) of the indoor temperature (left) and the HVAC thermal power (rig...

Supervisory predictive control of residential building heating ... The first field demonstration involved supervisory predictive control of an air- to- air heat pump with backup electric resistance heat. ... During these tests, the control system reduced total heating energy costs by \(19\%\) on average (95% confidence interval...



](https://hammer.purdue.edu/articles/thesis/FIELD_DEMONSTRATION_OF_PREDICTIVE_HOME_ENERGY_MANAGEMENT/28031546/1/files/51215966.pdf#18#2)[

![](https://cdn.deepseek.com/site-icons/tib.eu)

oa.tib.eu

Im Zeitraum von 2022 bis 2025 konnten im Rahmen erster Modellprojekte, regionaler Pilot- vorhaben und wissenschaftlicher Begleit...

Zeitraum von 2022 bis 2025 konnten im Rahmen erster Modellprojekte ... Es wurden in [29] Haushalte mit Wärmepumpen untersucht, wobei die Smart-Meter-Daten dazu genutzt wurden, die Haushalte zu ermitteln, die ein hohes Einspar- und Optimierungspotential zeigten.



](https://oa.tib.eu/renate/server/api/core/bitstreams/c540f727-b5f1-4294-923e-f6ea394523ca/content#17#11)[

![](https://cdn.deepseek.com/site-icons/torontomu.ca)

Toronto Metropolitan University (TMU)

2026/07/19

Co-Optimization of Electrical and Thermal Loads in Smart Homes with Integrated Power-to-Heat Systems

The system consists of photovoltaic (PV) panels, 32 residential users and their 32 EVs, a heat pump (HP), and two thermal storage tanks. ... The developed optimization approach aims to maximize the use of PV production for self-consumption and increase economic efficiency by charging and discharging EV batteries based on dynamic electricity prices.



](https://journals.library.torontomu.ca/index.php/ictea/article/view/2871)[

![](https://cdn.deepseek.com/site-icons/nedo.go.jp)

nedo.go.jp

<table><tr><td>年度</td><td>2021年度</td><td>2022年度</td><td>2023年度</td><td>2024年度</td></tr><tr><td>計画</td><td>実証前<br/>調査</td><td>★<b...

需要家ごとに異なる好み・快適性等を、センサー等でリアルタイムに把握・学習し、電力の需給バランスにあわせて、家庭内の太陽光・蓄電池・EV、空調・給湯器などの家電機器を最適制御する → Energykit という ... Systems</td><td>None</td><td>Solar and EV charger</td>



](https://www.nedo.go.jp/content/800021954.pdf#4#3)[

![](https://cdn.deepseek.com/site-icons/service.gov.uk)

assets.publishing.service.gov.uk

Project Case Study: Total Home Optimisation Management (THOM)

Increase the uptake of heat pumps by providing bespoke information to homeowners about the suitability of heat pumps for their specific homes based on data from smart meters and other household data. ... Minimise the running costs of heat pumps in operation by automatically optimising their performance and integrating them with solar photovoltaic (PV) panels, battery storage, time of use (ToU) tariffs...



](https://assets.publishing.service.gov.uk/media/68834c792f4f3f3c34bbeb70/GenGame.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/service.gov.uk)

assets.publishing.service.gov.uk

Project case study: Intelligent Air-Sourcing to Zet Zero

Minimise the running costs of heat pumps in operation by automatically optimising their performance and integrating them with solar photovoltaic (PV) panels, battery storage and time of use (ToU) tariffs. ... reducing demand spikes.- Running a trial in 7 homes to validate performance savings over a year, including 3 new builds and 4 retrofit properties. ... This shows an average saving of \(61\%\) compared to the cost of the actual metered energy demand of the heat pump and other electricity uses of the homes being met through grid- imported electricity alone on a flat p/kWh tariff.



](https://assets.publishing.service.gov.uk/media/68835393c02b468fa1ae0937/Wondrwall.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/fhv.at)

FHV - Vorarlberg University of Applied Sciences

2025/11/24

Influence of usage and model inaccuracies on the performance of smart hot water heaters: lessons learned from a demand response field test

Influence of usage and model inaccuracies on the performance of smart hot water heaters: lessons learned from a demand response field test - Domestic hot water heaters are considered to be easily integrated as flexible loads for demand response. ... This work reports the findings of a field test with 16



](https://opus.fhv.at/frontdoor/index/index/searchtype/authorsearch/author/Markus+Prei%C3%9Finger/rows/50/start/12/author_facetfq/Kepplinger%2C+Peter/belongs_to_bibliographyfq/true/docId/5400)[

core.ac.uk

Demand Response with Smart Homes and Electric Scooters – An Experimental Study on User Acceptance

Demand Response with Smart Homes and Electric Scooters – An Experimental Study on User Acceptance **_Alexandra-Gwyn Paetz, Thomas Kaschub, Patrick Jochem, Wolf Fichtner_** **_Karlsruhe Institute of Technology (KIT), Chair of Energy Economics_** **ABSTRACT ... dynamic pricing or electric vehicles are conducted, hardly any consumer has



](https://core.ac.uk/download/197532133.pdf#2#1)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

cordis.europa.eu

7. EBox records information received from the additional metering device during the day (5' slots);

EBox records information from smart plugs and smart loads during the day (5' slots) ... 4.1.3. Requests from aggregation system and consumer response The use of Active Demand to provide services to the Electricity System players was tested, namely ... Figure 12 ... The ADDRESS field trials installed an innovative EBox to control appliances in consumers' homes. Before the trial...



](https://www.cordis.europa.eu/docs/results/207643/final1-final-report-address.pdf#5#3)[

proceedings.eceee.org

| | Test home | 20 | 102,530 | | 46 | 15 | - | HVAC and heaters |

The project has deployed all necessary IoT equipment and cloud-based platforms at each community member site to enable the project to control and manage the communities collective demand response flexibility. ... ECEEE SUMMER STUDY PROCEEDINGS 627 5-152-22 PATRÃO ET AL ... Demand response has been integrated as a new highly distributed resource of flexibility...



](https://proceedings.eceee.org/papers/proceedings2022/5-152-22_Patrao.pdf#3#2)[

energiforskning.dk

The integrated control: A system where the set points of a thermostat, are controlled by the frequency

*Practical hardware development of the technology for frequency controlled demand (DFR) * *Validate and evaluate the technology's field performance of reserve provision ... The SmartBox is a demand response (DR) device developed for use in smart grid projects with the need of being able to regulate numerous demands while measuring consumption...



](https://energiforskning.dk/files/slutrapporter/dfr_eudp_report_64009-0001_1_11072013_16101.pdf#17#2)[

iflex-project.eu

D7.6 Small-scale pilot deployment and validation

D7.6 Small-scale pilot deployment and validation | KP16c | Increased consumer flexibility for grid stability and RES integration | 15 ... In the Greek pilot, the aim was to address imbalances in a 500 KW PV plant owned by OPTIMUS by demonstrating the interaction between renewable energy sources (RES) and demand response (DR) aggregators.



](https://www.iflex-project.eu/download/d7-6-small-scale-pilot-deployment-and-validation/?refresh=666aafc2f2d471718267842&wpdmdl=2984#10#10)[

![](https://cdn.deepseek.com/site-icons/theigc.org)

theigc.org

Shifting Household Power Demand across Time: Incentives and Automation+

Shifting Household Power Demand across Time: Incentives and Automation+ ... As part of a randomised control trial, we offer urban Indian households simple Wi-Fi-enabled smart switches that control the operation of an appliance. ... we find that switch-off events lead to a 60% reduction in appliance-level electricity usage and an 8.5% reduction in household-level electricity use during the event...



](https://www.theigc.org/sites/default/files/2025-03/Khanna%20et%20al%20Working%20Paper%20September%202024.pdf#5#1)[

![](https://cdn.deepseek.com/site-icons/lbl.gov)

Lawrence Berkeley National Laboratory (.gov)

Field Testing of Telemetry for Demand Response Control of Small Loads

### Publication Type Report ### Date Published 11/2015 ### Authors ### Abstract The electricity system in California, from generation through loads, must be prepared for high renewable penetrati



](https://smartersmallbuildings.lbl.gov/publications/field-testing-telemetry-demand)[

![](https://cdn.deepseek.com/site-icons/kit.edu)

KIT - Karlsruher Institut für Technologie

Demand Response with Smart Homes and Electric Scooters : An Experimental Study on User Acceptance - Demand Response with Smart Homes and Electric Scooters : An Experimental Study on User Acceptance

Paetz, Alexandra-Gwyn; Kaschub, Thomas; Jochem, Patrick; Fichtner, Wolf ## Abstract: Smart technologies and electric vehicles are supposed to efficiently use renewable resources by shifting loads an



](https://publikationen.bibliothek.kit.edu/1000050664#1)[

![](https://cdn.deepseek.com/site-icons/globalenergyprize.org)

The Global Energy Association

2025/01/06

Kenyan experiment shows how refrigerator management reduces grid load - Kenyan experiment shows how refrigerator management reduces grid load

Scientists from Germany and Tanzania have found a way to significantly reduce the energy consumption of refrigeration equipment by optimizing its load management. This result was achieved during a stu



](https://globalenergyprize.org/en/2025/07/01/kenyan-experiment-shows-how-refrigerator-management-reduces-grid-load/#1)[

![](https://cdn.deepseek.com/site-icons/mdpi.com)

mdpi.com

range

Although the \(D_{Group}^{TSV}\) was not maintained below the \(10\%\) comfort target at all times ... The use of a comfort deadband and a \(30\mathrm{min}\) lockout interval also means that the controller intentionally avoids excessive setpoint changes in response to short- term fluctuations.



](https://www.mdpi.com/2079-9292/15/14/3088/pdf?version=1784028962&_x_output_type_b6db407c4_=embedded_pdf#7#6)[

![](https://cdn.deepseek.com/site-icons/dtu.dk)

backend.orbit.dtu.dk

a cost- and comfort-driven control algorithm has on the number of heat pump activations is therefore of interest

a cost- and comfort-driven control algorithm has on the number of heat pump activations is therefore of interest. ... leading to a final version where ... minimum on- and off-times of at least 60 and 30 minutes respectively [58]. ... Furthermore, the lifetime of the device may be compromised compared to a thermostat that optimises for reduced wear and tear, thus lowering the desirability of economic algorithms.



](https://backend.orbit.dtu.dk/ws/files/123506514/Demand_response_in_a_market_environment.pdf#21#5)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dl.acm.org

Control KPIs

We evaluate the control performance using three Key Performance Indicators (KPIs) that balance economy, comfort, and equipment health. First ... potentially reducing system efficiency by over \(10\%\) [4] and shortening compressor lifespan due to mechanical stress [3]. ... To ensure a fair comparison, we adopt the schedule- based comfort constraints defined by the test case for all algorithms...



](https://dl.acm.org/doi/pdf/10.1145/3744256.3812591?download=true&__cf_chl_tk=0759UbVHmwj6bey1G1K0JzKxV1N5EyYPoWTnX4IgjWk-1786118936-1.0.1.1-WYck5v2PGEzYxhonzZjnZx5sa1iGt_l2QO7kNJ7FV_A#3#2)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arxiv.org

<center>Fig

SAC's policy is an inverter controller, learned rather than engineered [3, 1, 2], while PPO's is a thermostat. ... The duty threshold \(\epsilon = 10^{- 3}\) is permissive: a controller need only hold a near- zero capacity to register as "on," lowering the bar for the always- on optimum...



](https://arxiv.org/pdf/2608.09453#2#2)[

![](https://cdn.deepseek.com/site-icons/uca.es)

Universidad de Cádiz

A field experiment was conducted using a radiant floor system in a fully monitored test room to assess the control quality of both an analogue and a commercial smart control system across two different heat pumps. ... The study found that a “smart” controller, solely focused on precise indoor temperature control, did not guarantee energy savings and potentially jeopardized equipment due to frequent cycling.



](https://rodin.uca.es/bibtex/handle/10498/38004)[

![](https://cdn.deepseek.com/site-icons/polimi.it)

Politecnico di Milano

2025/07/22

RE.PUBLIC@POLIMI pubblicazioni di ricerca del Politecnico di Milano

A field experiment was conducted using a radiant floor system in a fully monitored test room to assess the control quality of both an analogue and a commercial smart control system across two different heat pumps. ... particularly in HVAC systems. The study found that a “smart” controller, solely focused on precise indoor temperature control, did not guarantee energy savings and potentially jeopardized equipment due to frequent cycling. This highlights the lack of a clear definition for “smart” controllers, leading to the mislabelling of commercially available ... Surprisingly, efficiency decreased instead of increasing at part load, contradicting both literature and manufacturer claims.



](https://re.public.polimi.it/handle/11311/1294215)[

![](https://cdn.deepseek.com/site-icons/lbl.gov)

eta-publications.lbl.gov

On average, potential savings were \(M = 0.97\) , \(\mathrm{SD} = 0.92\) USD, ranging from 0.00 to 5.75 USD

could justify substantial warmth. ... The daily peak outside temperature, shown on the thermostat ... Mean power load (W) by thermostat mode, showing comfort and eco modes for overall values (left) and by hour of day (right). </center> ... Cost-saving nudges for clothes washers, dryers, and dishwashers



](https://eta-publications.lbl.gov/sites/default/files/2026-08/1-s2.0-s0378778826002318-main.pdf#7#3)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/01/18

Adaptive thermostat preference learning using behaviour nudging and multi-armed bandits: A field implementation - Some differences have been observed between the results in both zones

it is observed that the temperatures ... at night in zone 2 ... The recurring drops in values show the effect of the discomfort penalty term in the reward signal in Eq. ... This study addressed a gap in the literature in using unsolicited occupant thermostat interactions and utilizing behaviour nudging techniques to explore the full range of thermal comfort of occupants. ... The algorithm was able to learn the occupants’ thermal preferences in two months with only eight



](https://www.sciencedirect.com/science/article/pii/S0378778826000903?via%3Dihub#3)[

![](https://cdn.deepseek.com/site-icons/lbl.gov)

MOSILAB: Ein Modelica-Simulationswerkzeug zur energetischen Gebäude- und Anlagensimulation

2025/08/03

Field Demonstration of Cost Minimizing Load Shifting Controls for 120V Heat Pump Water Heaters in Different Pricing Scenarios

The demonstrations showed that these techniques can shift 29-54% of the load away from peak periods, and reduce 120V HPWH electricity costs by 8-46% depending on the electricity price profile. ... would increase the cost savings by 21 percentage points and the peak period consumption reduction by 31 percentage points.



](https://bies.lbl.gov/publications/field-demonstration-cost-minimizing)[

![](https://cdn.deepseek.com/site-icons/osti.gov)

osti.gov

Optimal Operation of Residential High Performance Water Heater for Reduction of Electricity Cost and Peak Demand Through Field V...

Optimal Operation of Residential High Performance Water Heater for Reduction of Electricity Cost and Peak Demand Through Field Validation<sup>1</sup> ... Modern water heaters ... a mixed- integer linear programming model is proposed to minimize the electricity cost of a heat pump water heater while also reducing the peak demand of the residential household under a time- of- use utility rate by dynamically changing the water heater's running mode. Specifically...



](https://www.osti.gov/servlets/purl/3452329#2#1)[

![](https://cdn.deepseek.com/site-icons/lbl.gov)

calflexhub.lbl.gov

CALFLEXHUB SYMPOSIUM NOVEMBER 3 | 8am-4pm PT

Develop and Validate Price- and Load-Responsive Controls for Prototype 120-volt Retrofit-Ready Heat Pump Water Heaters ... Quantitative- 29% cost savings- 75% peak period kWh reduction- 102% mid- day kWh increase ... 12% cost savings



](https://calflexhub.lbl.gov/wp-content/uploads/sites/41/2023/11/CFH-Symposium-2023-Field-Project-Outlook.pdf#1#1)[

iaee2025paris.org

The Proof of the Pudding is in the Heating: A Field Experiment on Household Engagement with Heat Pump Flexibility

We conducted a field experiment during the winter seasons of 2022- 2023 and 2023- 2024 to evaluate the flexibility potential of residential HPs in nine well- insulated households near Ghent, Belgium.



](https://iaee2025paris.org/download/contribution/abstract/140/140_abstract_20250116_225821.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/ebsco.com)

EBSCO

2025/06/30

Field Demonstration of Cost Minimizing Load Shifting Controls for 120V Heat Pump Water Heaters in Different Pricing Scenarios.

Field Demonstration of Cost Minimizing Load Shifting Controls for 120V Heat Pump Water Heaters in Different Pricing Scenarios. ... The demonstrations showed that these techniques can shift 29-54% of the load away from peak periods, and ... would increase the cost savings by 21 percentage points and the peak period consumption reduction by 31 percentage points.



](https://openurl.ebsco.com/EPDB%3Agcd%3A14%3A29674814/detailv2?sid=ebsco%3Aocu_results%3Acache&id=ebsco%3Adoi%3A10.63044%2Fs25fie02&bquery=DE%20%22LAWRENCE%20Berkeley%20National%20Laboratory%22&page=1&link_origin=none&crl=f)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/03/12

Peak reduction via time-variable tariffs and automated load control: Results from a Swiss pilot study

Peak reduction via time-variable tariffs and automated load control ... - •Automated electric water heater, heat pump, and electric vehicle charging control. - •Reinforcement learning-based decision-making with limited information. ... Both schemes consider automated control of electric water heaters, heat pumps, and electric vehicle charging.



](https://www.sciencedirect.com/science/article/pii/S030626192600317X?fr=RR-2&ref=pdf_download&rr=a1fecc9a4cf2ce9a#1)[

![](https://cdn.deepseek.com/site-icons/ucdavis.edu)

Western Cooling Efficiency Center

2026/09/02

Smart Controls Cut Peak Water Heating Costs for Low-Income Households, but Only When the Closet Has Room to Breathe - Western Cooling Efficiency Center - - News

- News # Smart Controls Cut Peak Water Heating Costs for Low-Income Households, but Only When the Closet Has Room to Breathe Heat pump water heaters are one of the most efficient ways to electrify a



](https://wcec.ucdavis.edu/smart-controls-cut-peak-water-heating-costs-for-low-income-households-but-only-when-the-closet-has-room-to-breathe/#1)[

![](https://cdn.deepseek.com/site-icons/energizeinnovation.fund)

Energize Innovation

Optimizing Heat Pump Load Flexibility for Cost, Comfort, and Carbon Emissions

Optimizing heat pump load flexibility for cost, comfort, and carbon emission reductions The Regents of the University of California, on behalf of the Davis Campus Recipient Davis, CA Recipient Loc



](https://www.energizeinnovation.fund/projects/optimizing-heat-pump-load-flexibility-cost-comfort-and-carbon-emissions)[

![](https://cdn.deepseek.com/site-icons/pdx.edu)

pdxscholar.library.pdx.edu

Portland State University

Follow this and additional works at: https://pdxscholar.library.pdx.edu/open_access_etds Let us know how access to this document benefits you. Recommended Citation Murad, Othman A., "Price-Sign



](https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=7938&context=open_access_etds#9#1)[

![](https://cdn.deepseek.com/site-icons/zenodo.org)

Zenodo

2026/02/26

Optimizing photovoltaic-battery systems for net-billing in Greece: Impact of building usage and pricing schemes - Published February 27, 2026 | Version v1

Impact of building usage and pricing schemes ## Description This study investigates the techno-economic performance of photovoltaic–battery (PVB) systems under the Greek net-billing framework. A simulation-based optimization framework evaluates how ... Transitioning from a flat to a ToU tariff increases self-consumption by up to 20 percentage points ... capacities (up to 18



](https://zenodo.org/records/18873142#1)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/02/24

Optimizing photovoltaic-battery systems for net-billing in Greece: Impact of building usage and pricing schemes - Skip to main contentSkip to article

This study investigates the techno-economic performance of photovoltaic–battery (PVB) ... Residential buildings achieve the highest self-consumption (40–60%) with balanced PV-to-battery ratios (≈4 kW/10 kWh) ... Transitioning from a flat to a ToU tariff increases self-consumption by up to 20 percentage points, whereas RTP further enlarges storage capacities (up to 18



](https://www.sciencedirect.com/science/article/pii/S2352710226005395?fr=RR-2&ref=pdf_download&rr=a10f6850884e0884#1)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

sciencedirect.com

Among all parameters, building usage exerts the most significant influence on both energy behavior and optimal system configurat...

Residential buildings display the highest self- consumption levels ... supported by balanced PV- to- battery ratios (approximately \(4\mathrm{kW}\) PV/10 kWh battery under dynamic tariffs). ... The dual- zone ToU tariff increases self- consumption by roughly 15- 20 percentage points compared to the flat tariff...



](https://www.sciencedirect.com/science/article/pii/S2352710226005395/pdfft?crasolve=1&r=a1b0451e4cd53385&ts=1784029409113&rtype=https&vrr=UKN&redir=UKN&redir_fr=UKN&redir_arc=UKN&vhash=UKN&host=d3d3LnNjaWVuY2VkaXJlY3QuY29t&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&re=X2JsYW5rXw%3D%3D&ns_h=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ns_e=X2JsYW5rXw%3D%3D&rh_fd=rrr\)n%5Ed%60i%5E%60_dm%60%5Eo\)%5Ejh&tsoh_fd=rrr\)n%5Ed%60i%5E%60_dm%60%5Eo\)%5Ejh&hc=~rrr\)n%5Ed%60i%5E%60_dm%60%5Eo\)%5Ejhwrrr\)n%5Ed%60i%5E%60_dm%60%5Eo\)%5Ejhwrrr\)n%5Ed%60i%5E%60_dm%60%5Eo\)%5Ejh&iv=24cb837d26e59f36ce5774c50d42326c&token=37353332316433626563313932346162303164343032666365326631663565656262373766623063643463323133356534383736383434313735316666393666613436343730666332313164616438633036633962346265303964353837616630313064373734663a343061323937623261333164613563623964646563636633&text=17c4609feb486a785ba1490269361fd3148c7fb695575e4392f3277a41d8dd310e3577852e31bfa4e2ac1909823c46719d1a120c89ccc7d749af2713a08fd2e64002c7d191c3cc77683e687a162dce30ee9bb166c07ae9f5ad78169b629d759ca4827f5106423132821e787cb0fc33900e6b7c8ac2526d2c5b004c0d8869a5558b4cbd4cf49ac22b9d1b94a8be634b6570828716a0803f711e76ab8f9b659ba1cc39e350d3f55a844485a8f7e69d42e573a0a8eb7e1b76645b475587854cb29c361e8b7a9208b0a39e1a4531f7bdd1e0f66a5614980a051ee8404c5fa1914c87d93ce690fb19b1fef8e67b52eda012f4bd158daeb4bf0e6f9ab10ce52535ddd41b8f23064e5411500aa7f08644c63b532fe4ffdb5d684143bc95a7e5f6ed78640a7c4cc64ad1f33dcbc1e24fcde7dda8&original=3f&chkp=1c&rack=a1b0451e4cd53385#6#5)[

![](https://cdn.deepseek.com/site-icons/mdpi.com)

mdpi.com

Article Evaluation of a Home Energy Management System Using One-Year Data Under Dynamic Tariff Conditions

Article Evaluation of a Home Energy Management System Using One-Year Data Under Dynamic Tariff Conditions ... This paper presents a case study of a Home Energy Management System (HEMS) integrating photovoltaic (PV) generation, battery energy storage (BES), thermal storage, and a heat pump in a single- family household operating under a dynamic electricity tariff.



](https://www.mdpi.com/1996-1073/19/5/1383/pdf#3#1)[

![](https://cdn.deepseek.com/site-icons/mdpi.com)

mdpi.com

The relationship between each strategy and these evaluation objectives is not uniform

Peak shaving acts primarily on grid dependency by reducing grid import during the 19:00- 22:00 evening window ... Self- consumption rises from 31.73 to 35.2 percent, as strategic battery discharge during peak hours enables better photovoltaic utilization.



](https://www.mdpi.com/2071-1050/18/18/9578/pdf#5#3)[

![](https://cdn.deepseek.com/site-icons/semanticscholar.org)

Semantic Scholar

2026/01/30

[PDF] Solar Charging—Lessons Learned from Field Observation | Semantic Scholar - for the household load only

https://doi.org/10.3390/wevj17020069 ... J. 2026, 17, 69 18 of 26 ... price-sensitive ... hours in response to low dynamic tariffs, thereby increasing their energy consumption



](https://www.semanticscholar.org/reader/d9fe1fe6b3bbd09c7eb093c999ece262aa9d9835#4)[

![](https://cdn.deepseek.com/site-icons/polito.it)

webthesis.biblio.polito.it

The second is that timing has become economically decisive

Work on domestic PV- battery systems has shown that time resolution can alter estimated self- consumption, financial outcomes, and even investment conclusions [11]. Likewise ... A third strand studies photovoltaic (PV) self- consumption and battery dispatch under time- dependent tariffs.



](https://webthesis.biblio.polito.it/39818/1/tesi.pdf#15#2)[

![](https://cdn.deepseek.com/site-icons/springerprofessional.de)

springerprofessional.de

Combining grid friendliness with economical goals: optimal battery storage operation under different end-user electricity and fe...

optimal battery storage operation under different end-user electricity and feed-in tariffs Florian Samm  Julia Vopava-Wrienz ... Abstract This work examines the effects of different end-user electricity and feed-in tariff models on the cost-optimal operation of private battery energy stor- age systems.



](https://www.springerprofessional.de/content/pdfId/51589916/10.1007/s00502-025-01374-6#4#1)[

![](https://cdn.deepseek.com/site-icons/mdpi.com)

mdpi.com

_Article_

Real-World Performance and Economic Evaluation of a Residential PV Battery Energy Storage System Under Variable Tariffs: A Polish Case Study ... This paper presents an annual, real-world evaluation of the performance ... a battery energy storage system (BESS) in southern Poland. The system, monitored with 5 min resolution, operated under time-of-use (TOU) electricity tariffs.



](https://www.mdpi.com/1996-1073/18/15/4090/pdf?version=1754052770#6#1)[

![](https://cdn.deepseek.com/site-icons/ntnu.no)

ntnuopen.ntnu.no

Another device is the national hourly net metering scheme, which makes self- consumption attractive

Another device is the national hourly net metering scheme, which makes self- consumption attractive. Most interviewees explicitly referred to this scheme as a reason for time shifting consumption. Three of the interviewed households also had a home battery installed with an automated energy management system controlling the discharging and recharging of the battery to optimise the self- consumption of PV power. Interestingly...



](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2673517/The%2Brole%2Bof%2Bcompetences.pdf?sequence=2#5#3)[

![](https://cdn.deepseek.com/site-icons/nature.com)

nature.com

The schedule efficiency of \(94.8\%\) represents the optimization success rate in achieving suboptimal individual schedules whil...

The schedule efficiency of \(94.8\%\) represents the optimization success rate in achieving suboptimal individual schedules while respecting cluster- level constraints. ... The customer satisfaction index of \(98.7\%\) reflects high acceptance of the optimized charging schedules...



](https://www.nature.com/articles/s41598-026-35457-x_reference.pdf?proof=t%2529#8#5)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2025/09/18

When and where it counts: enhancing demand response in electric vehicle charging - Skip to main contentSkip to article

•Automatic controls ... Results show that EVCSs with automatic controls achieve an average reduction of 11.8 % during event hours, while manual adjustments in charging patterns yield only a 0.4 % reduction ... Analysis reveals that stations ... 63 % demonstrate the most substantial consumption reductions...



](https://www.sciencedirect.com/science/article/abs/pii/S0306261925014692?fr=RR-1&ref=cra_js_challenge#1)[

![](https://cdn.deepseek.com/site-icons/osti.gov)

OSTI.GOV (.gov)

2025/11/29

Scalability and Effectiveness of Smart Charge Management - Scalability and Effectiveness of Smart Charge Management

Some feeders achieve reductions of more than 40% at high enrollment levels, while others show improvements closer to 10–15%. ... Results also highlight trade-offs between shifting load away from peak periods and minimizing secondary demand peaks, offering practical insights for future utility program design.



](https://www.osti.gov/pages/biblio/3374993#1)[

![](https://cdn.deepseek.com/site-icons/harvard.edu)

Harvard DASH

Harvard Division of Continuing Education - Harvard Division of Continuing Education

Real-world charging data from 46,822 EV drivers and 6.87 million residential charging sessions across the United States ... were provided by ev.energy, a smart charging platform that administers ... smart charging programs offering both upfront enrollment payments and ongoing static participation incentives consistently outperformed all other program designs...



](https://dash.harvard.edu/communities/73120379-4b86-6bd4-e053-0100007fdf3b?spc.page=1&f.subject=Sustainability,equals&f.subject=Energy,equals&f.subject=Climate%20change,equals&f.entityType=Publication,equals#1)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2025/11/06

Weather-informed optimal scheduling of electric vehicle charging under extreme conditions: A case study from the Scottish islands - σ|V| drops from 0.0136 to 0.0115 under smart charging and to 0.0109 under V2G (Table 4), a 20 % improvement over the baseline

σ|V| drops from 0.0136 ... 0.0115 under smart charging and to 0.0109 under V2G (Table 4), a 20 % improvement over the baseline. ... These results show that price-aligned smart charging reduces voltage spread and energy cost in routine days, while bidirectional export is mainly valuable during storm-driven deficits. In Great Britain...



](https://www.sciencedirect.com/science/article/pii/S0142061525008774#4)[

![](https://cdn.deepseek.com/site-icons/fleetowner.com)

FleetOwner

2025/10/14

Ford Pro and Southern Company demonstrate dynamic pricing and fleet charging management without impacting vehicle uptime

Demand response events successfully reduced grid load by half a megawatt within minutes, demonstrating effective load management. ... Southern Company was able to reduce its charging demand by half a megawatt during a 30-minute demand response event, and its chargers improved efficiency by approximately 10 kW per charger.



](https://www.fleetowner.com/emissions-efficiency/article/55323503/ford-pro-and-southern-company-demonstrate-dynamic-pricing-and-fleet-charging-management-without-impacting-vehicle-uptime)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/06/22

Evaluating EV Smart Charging Under Emerging Power-based Network Tariffs for PV Prosumers - Moreover, Table 8 presents the CR obtained across EV smart charging scenarios (2–6) for both EBT and PBT schemes, including the ...

When ASs are enabled (scenarios 5–6), the CR increases to 6–32.5% for EBT and 10–41% for PBT ... 17% and 26%. ... PBT attains an average CR of 23.6%, compared with 12% for EBT, indicating that power-based tariffs achieve nearly twice the CR of energy-based tariffs when smart charging strategies are enabled.



](https://www.sciencedirect.com/science/article/pii/S2666792426000211#4)[

![](https://cdn.deepseek.com/site-icons/tdworld.com)

T&D World

2025/09/03

Southern Company and Ford Pro Complete Managed Charging Pilot for EV Fleets

Southern Company reduced total charging demand by 0.5 megawatts (500 kW) during a 30-minute event, averaging about 10 kW of savings per charger. ... The study showed that managed charging could deliver energy savings, support grid efficiency, and maintain reliability for drivers.



](https://www.tdworld.com/electrification/news/55314436/southern-company-and-ford-pro-complete-managed-charging-pilot-for-ev-fleets?o_eid=8715H5136245C9S&rdx.ident%5Bpull%5D=omeda%7C8715H5136245C9S&utm_campaign=CPS250908140)[

![](https://cdn.deepseek.com/site-icons/unece.org)

unece.org

The SCALE Budapest pilot explicitly targets three outcomes: (i) higher PV self- consumption through charge/discharge scheduling ...

The SCALE Budapest pilot explicitly targets three outcomes: (i) higher PV self- consumption through charge/discharge scheduling (V1G/V2G), (ii) lower energy bills by avoiding peak- price periods, and



](https://unece.org/sites/default/files/2026-02/Report%20Tajikistan%20Report%2010012026.pdf?__cf_chl_tk=vL_wexZBO3yA6MiQ2QMLYGS9XPfGH8iM5fNsEFjyHOo-1777829605-1.0.1.1-KSZSe0tFFOW0eXSv1glaP6Q40JVP9qHUiFQLDo3Msg4#5#4)[

E Source

2026/03/21

Mind the mix: How flexible load solutions interact—and why it matters more than ever

As electrification and decarbonization efforts accelerate, utilities and policymakers are deploying an ever-growing toolkit of flexible load solutions: from time-of-use (TOU) rates and demand response



](https://www.esource.com/insights/mind-mix-how-flexible-load-solutions-interact-and-why-it-matters-more-ever)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/05/10

Matter and OpenADR team up to connect smart homes to the grid - Skip to main content

Matter and OpenADR team up to connect smart homes to the grid The two standards bodies are working together to make it easier to connect home appliances to demand response programs. ... Matter will handle in-home communication between a smart, connected electrical appliance, such as an EV charger, heat pump, or solar install, and an energy gateway that collects real-time data.



](https://www.theverge.com/tech/927756/matter-openadr-demand-response-smart-home-energy-management#1)[

theenergyst.com - Latest energy news

2026/05/10

Connectivity Standards Alliance and OpenADR Alliance announce Liaison Agreement to collaborate on grid-connected energy management - theenergyst.com

The Matter smart home protocol, stewarded by the Connectivity Standards Alliance, handles in-home communication between appliances and an energy gateway. The OpenADR 3 protocol, developed by the OpenADR Alliance ... By enabling their devices to respond to grid signals, consumers benefit through bill credits and additional incentives, while utilities gain a standardised, scalable mechanism for demand response. For regulators...



](https://theenergyst.com/connectivity-standards-alliance-and-openadr-alliance-announce-liaison-agreement-to-collaborate-on-grid-connected-energy-management/)[

TelcoNews Australia

2026/05/11

Matter & OpenADR link up for home energy management

Matter, the smart home standard overseen by the Connectivity Standards Alliance, is intended to manage communication inside the home between appliances and an energy gateway. OpenADR 3 is designed to handle communication between that gateway, utilities and grid operators. ... Together, Matter and OpenADR 3 are intended to provide an end-to-end communications pathway from grid operators to individual devices in the home.



](https://telconews.com.au/story/matter-openadr-link-up-for-home-energy-management)[

elemental

2026/05/11

Connectivity groups to collaborate to accelerate grid-connected energy management - elemental

The partners said that the partnership will ‘bridge the gap between smart home innovation and utility demand response.’ ... seamless communication between smart home devices and the energy grid. ... The Matter smart home protocol, stewarded by the Connectivity Standards Alliance, handles in-home communication between appliances and an energy gateway. The OpenADR 3 protocol...



](https://elementallondon.show/news/connectivity-groups-to-collaborate-to-accelerate-grid-connected-energy-management/)[

![](https://cdn.deepseek.com/site-icons/acm.org)

energy.acm.org

Version 1.5 (November 2025) introduced clusters for tariff and pricing information, as well as electrical grid condition signall...

Version 1.5 (November 2025) introduced clusters for tariff and pricing information, as well as electrical grid condition signalling [10]. These extensions provide the specification- level foundation for demand response and flexibility- oriented applications by enabling devices to receive and act upon external economic and grid- state signals. For now...



](https://energy.acm.org/eir/wp-content/plugins/pdfjs-viewer-shortcode/pdfjs/web/viewer.php?file=https://energy.acm.org/eir/wp-content/uploads/2026/09/sigenergy-eir-final230.pdf&attachment_id=1569&dButton=true&pButton=true&oButton=false&sButton=true#zoom=0&pagemode=none&_wpnonce=b3daed07ba#3#2)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/05/12

Your Smart Home Could Soon Help Balance The Grid (and Save You Money) - Advertisement

The organizations behind the Matter smart home standard and the OpenADR energy management protocol are officially teaming up ... The idea is that Matter handles communication inside the home between smart devices and an energy management gateway, while OpenADR 3 manages communication between that gateway and utility companies or grid operators. ... The new agreement is designed ... demand response programs much easier



](https://tech.yahoo.com/articles/smart-home-could-soon-help-084658566.html#1)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2026/05/10

连接标准联盟与 OpenADR 联盟正式签署联络合作协议，携手推进并网能源管理

由连接标准联盟主导维护的Matter 智能家居标准，负责家庭内部各类电器与能源网关之间的通信交互； - 由 OpenADR 联盟制定的OpenADR 3 协议，实现能源网关、公用事业企业与电网运营商之间的通信对接。



](https://matter.cn/5597.html)[

![](https://cdn.deepseek.com/site-icons/engadget.com)

Engadget

2026/05/10

OpenADR and Matter are collaborating to let your smart home talk to the grid - Engadget - OpenADR and Matter are collaborating to let your smart home talk to the grid

OpenADR and Matter are teaming up to make it easier for smart home appliances to talk to the energy grid. This is a big deal ... It all falls down to demand response ... Demand response is also baked into newer smart thermostats, as they can communicate directly with the grid to automatically make adjustments to prevent blackouts and the like.



](https://www.engadget.com/2169973/openadr-and-matter-are-collaborating-to-let-your-smart-home-talk-to-the-grid/#1)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

Smart Grid Component - an overview - Chapters and Articles

Matter in this domain can bring benefits in terms of communication network [63] (by providing a self-organizing ... Fiastri et al. in [65] introduce a solution to tackle the variability of renewable energy generation by leveraging the Matter standard to enable implicit demand-response for privates. The proposal here is to dynamically adapt the behavior of household consumption by taking advantage of Matter’s



](https://www.sciencedirect.com/topics/computer-science/smart-grid-component#1)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

Silicon Labs

2026/08/23

Matter & Energy Management in Smart Home Ecosystem - Silicon Labs - Why Matter Energy Management Matters for Utilities, Device Makers, and Homeowners

For utilities struggling with grid strain and limited visibility "behind the meter," Matter Energy Management offers an interoperable foundation for demand response and load management. Key benefits include better coordination of flexible loads, improved use of dynamic pricing, smoother integration of distributed energy resources (DERs)...



](https://www.silabs.com/blog/matter-and-energy-management-in-smart-home-ecosystem?source=Social&detail=LinkedIn&cid=soc-lin-mat-081426#1)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

energy.ec.europa.eu

price directly to wholesale market price changes, encouraging consumers to shift their use to cleaner, cheaper hours

These provisions are reinforced by Article 13 on aggregation contracts and by Articles 15 and 17, which define the regime for active customers and demand response by means of aggregation, respectively. Member States are obliged to ensure non- discriminatory access to all electricity markets for consumers and aggregators, and to establish suitable market mechanisms that give consumers and aggregators flexibility to participate and be properly valued in all markets. ... aggregation</td><td>Aggregators should be given non-discriminatory access to electricity markets and remunerated for flexibility on the basis of market value.</td></tr><tr><td>Article



](http://energy.ec.europa.eu/document/download/931d4820-7a8f-46c5-a837-e5c2eea15dcf_en?filename=SWD_2026_126_1_EN_autre_document_travail_service_part1_v6.pdf#28#27)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/08/29

The role of controllable household appliances for effective uptake of digital services by consumers and communities in the energy transition - Aggregators have emerged as strategic entities in the digitalised energy ecosystem, acting as management hubs that coordinate, o...

providing financial incentives and feedback to sustain user engagement. ... the ever-evolving rules of the flexibility markets in which they operate, and regulatory frameworks governing their roles and functions. ... transparency regarding control strategies, event duration and frequency, comfort impacts, and financial compensation is essential. ... Independent aggregation has



](https://www.sciencedirect.com/science/article/pii/S2211467X26003226#4)[

![](https://cdn.deepseek.com/site-icons/ual.es)

cde.ual.es

An aggregator can earn revenues through arbitrage trading on the energy market or via the ancillary service markets of service o...

An aggregator can earn revenues through arbitrage trading on the energy market or via the ancillary service markets of service operators (SOs). ... another way to organise the market would be to aggregate customers into a balancing group with compensation for deferred consumption and additional production distributed across that group.



](https://www.cde.ual.es/wp-content/uploads/2023/12/common-european-energy-data-space-MJ0723057ENN.pdf#13#7)[

![](https://cdn.deepseek.com/site-icons/kuleuven.be)

mech.kuleuven.be

The IT infrastructure required for demand- side flexibility is related to three different industries or businesses: the home app...

Conflicts on technical aspects related to the accounting of energy flows and the compensation issue may arise between the consumer and his/her supplier in case he/she participates in explicit demand- side flexibility schemes with an aggregator or a DSO. ... by prosumers.



](https://www.mech.kuleuven.be/en/tme/research/energy-systems-integration-modeling/phd-dissertations/phd-athir-nouicer#24#9)[

future-energy-lab.de

the United Kingdom and Sweden, with potential expansions in Spain and Finland

The profitability of DR aggregators heavily relies on supportive regulations. He stressed the necessity of establishing fair compensation for curtailed loads and ensuring minimum compensatory measures. ... Customers receive all essential devices free of charge in exchange for a commitment to reduce overall consumption by at least 15%. ... As compensation, operators of adjustable consumption devices are granted a standard reimbursement through reduced grid fees. Additionally...



](https://future-energy-lab.de//app/uploads/2024/12/Gesammelte-Berichte.pdf#25#25)[

![](https://cdn.deepseek.com/site-icons/iea-4e.org)

iea-4e.org

Small-scale distributed resources, such as household and commercial assets, can only participate if aggregated

However, it can be facilitated by removing any regulatory obstacles that complicates or hinders the selling or procurement of aggregated flexibility services. ... avoided curtailment) from using households flexibility is reflected in the economic compensation or other benefit to the customer. ... Clear legislation is needed, which allows for non-discriminatory access of aggregated flexibility on the flexibility marked.



](https://www.iea-4e.org/wp-content/uploads/2024/06/Report-Flexibility-platforms-EDNA-01.docx#5#5)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

energy.ec.europa.eu

Allocation of energy volumes and balance responsibility: Clear allocation of energy volumes is not always present

Remuneration: DR services are not always remunerated in the same way as generation ... Remuneration should be compliant with EBGL and no distinctions be made. ... Of course, where demand response leads to an increase of demand, the compensation should go the other way, i.e. to the aggregator/consumer.



](https://energy.ec.europa.eu/system/files/2019-05/eg3_final_report_demand_side_flexiblity_2019.04.15_0.pdf#6#3)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2025/12/22

Exploring demand side flexibility through aggregation of individual devices - The large-scale outcomes demonstrate the value of successful integration and optimization of different electrical loads in vario...

heterogeneous regulatory frameworks, and multifaceted technical requisites for load coordination in varied markets. ... the aggregator functions as a central ... subsequently performs unified optimization scheduling, where users do not independently optimize their device portfolios but rather passively accept the aggregator’s scheduling arrangements and receive corresponding compensation.



](https://www.sciencedirect.com/science/article/pii/S1364032125013280?via%3Dihub#4)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

EUR-Lex

EUR-Lex - 52016PC0863 - EN - Nella maggior parte degli Stati membri i consumatori sono scarsamente o per nulla incentivati a modificare il loro consumo in ri...

sia individualmente che in maniera aggregata, e renderanno più flessibile il sistema ... stanno emergendo nuovi servizi per la domanda mediante i quali nuovi attori del mercato propongono di gestire il consumo di energia elettrica di una serie di consumatori corrispondendo loro un compenso in cambio di flessibilità.



](https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=COM:2016:0863:FIN#2)[

dr4eu.org

European Workshops on Demand Response 2022

Customer entitlement to contract with independent aggregator of their choice, without need for consent or prior agreement of their supplier (Art. 13) - Strict limits to compensation payments (Art 17(4)) ... This problem will be solved when the new smart meter 2G is installed for ... for settlement purposes.



](https://dr4eu.org/wp-content/uploads/2022/06/Italy_DR-Workshop_16June2022.pdf#2#1)[

![](https://cdn.deepseek.com/site-icons/osti.gov)

OSTI.GOV (.gov)

2024/12/05

Assessing thermal comfort and participation in residential demand flexibility programs - Assessing thermal comfort and participation in residential demand flexibility programs

This paper proposes a method to comprehensively assess the thermal comfort implications of DF strategies and presents results of their impacts on DF event participation decisions and demand savings. Here, the proposed method was applied to a heat pump DF field study in Cordova, Alaska. The study’s key findings are ... 2) Household-level thermal comfort is more sensitive to the duration of the DF event than to the degree of temperature offset from baseline conditions...



](https://www.osti.gov/pages/biblio/3016931#1)[

![](https://cdn.deepseek.com/site-icons/energy.gov)

energy.gov

2024 PROJECT

Demand-response with heat-pumps may impact thermal comfort and interfere with daily routines – DFIDR program administrators have limited resources to consider occupant impact in their planning. ... - Testing demand savings potential of common demand response strategies using heat pumps. ... - Demand savings



](https://www.energy.gov/sites/default/files/2024-11/bto-peer-2024-14119a-Load-Flexibility-Heat-Pumps-Nambiar.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/scilit.com)

Scilit

2024/12/22

The Proof of the Pudding is in the Heating: A Field Experiment on Household Engagement with Heat Pump Flexibility

We conducted a field experiment with nine heat pumps in well-insulated homes near Ghent, Belgium. ... This flexibility came with moderate comfort impacts: on average, indoor temperatures were 0.38°C lower during interventions. ... These findings suggest that flexible residential heating can support renewable energy integration with moderate comfort impacts.



](https://www.scilit.com/publications/6444317b2365209fbbf9e2616e9efcaf)[

![](https://cdn.deepseek.com/site-icons/aceee.org)

aceee.org

OpenADR 3.0 field test provides stronger evidence on utility- to- building implementation: it validated reliable price- signal r...

The measured HVAC reductions were meaningful in both absolute and normalized terms, ranging from approximately 0.23 to \(0.59\mathrm{W / ft^2}\) ... results showed minimal comfort- bound violations and no reported comfort complaints, suggesting that dynamic pricing can ... While bill savings were found as modest in daily dollar terms, the observation is a useful program- design finding: utilities cannot rely on short- ... especially when controls



](https://www.aceee.org/wp-content/uploads/2026/08/from-dynamic-prices-to-dispatchable-flexibility-demonstrated.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/sagepub.com)

Sage Journals

2025/10/26

Enhancing demand side management: A field study on flexibility and personal thermal control - Quirin Hamp, Yangzhe Chen, Qian Wang, 2026 - Skip to main content

This paper presents findings from a longitudinal field study (2023–2024 heating season, Stockholm, Sweden) evaluating a personalized DSM approach. Using the ComfortID mobile application, approximately 70 users could accept, or abort DSM events based on individual thermal comfort preference. The results showed that about 25% of events were cancelled.



](https://journals.sagepub.com/doi/full/10.1177/1420326X251378316#1)[

![](https://cdn.deepseek.com/site-icons/repec.org)

EconPapers

2025/08/28

The proof of the pudding is in the heating: A field experiment on household engagement with heat pump flexibility - The proof of the pudding is in the heating: A field experiment on household engagement with heat pump flexibility

Baptiste Rigaux, Sam Hamels and Marten Ovaere Energy Economics, 2025, vol. 148, issue C Abstract: As renewable energy grows, flexible electricity demand becomes essential. We conducted a field exper



](https://econpapers.repec.org/article/eeeeneeco/v_3a148_3ay_3a2025_3ai_3ac_3as0140988325003895.htm#1)[

![](https://cdn.deepseek.com/site-icons/pv-magazine.com)

pv magazine International

2025/11/04

2025 - Page 66 of 439 - pv magazine Global - Advertisement

Advertisement # Field trial shows third-party control of residential heat pumps can provide grid flexibility UK researchers find that smart, centrally controlled air-source heat pumps could slash pe



](https://www.pv-magazine.com/2025/page/66/#1)[

![](https://cdn.deepseek.com/site-icons/canada.ca)

Natural Resources Canada

2016/07/17

The zone saver field trial: Utility controlled demand response with residential zoned cooling

Authors: D. Mountain (McMaster University) T. Strack (Strack and Associates) W. Zhou (McMaster University) B. Lomanawski (NRCan) Publication date: December 2011 The ZoneComfort® (ZC) technology ena



](https://natural-resources.canada.ca/maps-tools-publications/publications/zone-saver-field-trial-utility-controlled-demand-response-residential-zoned-cooling?wbdisable=true)[

ecbcs.org

- Winter and Summer Demand Response: Rebound effects were most noticeable in winter without mitigation

- Winter and Summer Demand Response: Rebound effects were most noticeable in winter without mitigation. Mitigation strategies reduced sharp increases in demand after flexibility periods.- Rebound Effe



](https://www.ecbcs.org/Data/publications/Methodologies%20and%20evaluations%20of%20energy%20flexibility%20for%20clusters%20of%20buildings_Annex%2082%20D1.pdf#14#9)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2025/03/19

Embedding energy flexibility capability in air source heat pumps via third-party control: Insights from a field trial on residential buildings in England - Skip to main contentSkip to article

Embedding energy flexibility capability in air source heat pumps via third-party control ... This research investigates energy flexibility in residential building clusters transitioning from gas boilers to air source heat pumps ... Findings reveal insights into third-party control operation, events duration, override requests, achievable flexibility and user behaviour/comfort preferences. Peak



](https://www.sciencedirect.com/science/article/abs/pii/S0306261925004350#1)[

![](https://cdn.deepseek.com/site-icons/iifiir.org)

Institut International du Froid

2024/07/14

Field test and evaluation of model predictive control in a grid-interactive thermal energy storage integrated heat pump system.

Field test and evaluation of model predictive control in a grid-interactive thermal energy storage integrated heat pump system. ... A model predictive control (MPC) based on the dynamic programming method was then developed to optimize the performance of the HP-TES system, ensuring both reduced electrical costs and sustained human comfort.



](https://iifiir.org/en/fridoc/field-test-and-evaluation-of-model-predictive-control-in-a-149290)[

![](https://cdn.deepseek.com/site-icons/polimi.it)

Politecnico di Milano

2025/06/07

RE.PUBLIC@POLIMI pubblicazioni di ricerca del Politecnico di Milano

This research investigates energy flexibility in residential building clusters transitioning from gas boilers to air source heat pumps, within the broader context of rapid decarbonisation of both building stock and electric grid in the UK. ... Findings reveal insights into third-party control operation, events duration, override requests, achievable flexibility and user behaviour/comfort preferences.



](https://re.public.polimi.it/handle/11311/1292066)[

![](https://cdn.deepseek.com/site-icons/ucl.ac.uk)

UCL Discovery

2022/07/24

Living with demand response: Insights from a field study of DSR using heat pumps - UCL Discovery

Living with demand response: Insights from a field study of DSR using heat pumps ... The analysis of the results revealed that air and surface temperatures dropped during demand response (air temperature dropped 0.3-1.1 degrees in 3 hours). However...



](https://discovery.ucl.ac.uk/id/eprint/10157018/#1)[

![](https://cdn.deepseek.com/site-icons/ugent.be)

vunit.ugent.be

NUMBER 18, 3 FEBRUARY 2025

**We used large-scale surveys and a field experiment to explore households' interest and expectations in schemes that adjust their heat pump to match electricity demand with renewable production. ... where a total of 287 heat pump interventions were conducted during the winters of 2022—2023 and 2023—2024.



](https://www.vunit.ugent.be/eb/economics/en/research/gei/gei18_en#2#1)[

![](https://cdn.deepseek.com/site-icons/tse-fr.eu)

tse-fr.eu

Measuring Large-Scale Energy Demand Flexibility: Evidence from a Nationwide Natural Field Experiment\*

The program reduced overall peak grid demand by \(23.1\%\) among compliers, at an average household remuneration of £2,900 per MWh. We estimate that the reduction among all program participants was \(28.1\%\) . The adoption of solar panels and batteries, heat pumps, and EVs all increased demand response.



](https://www.tse-fr.eu/sites/default/files/TSE/documents/conf/2026/energy/bernard_abstract.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/jst.go.jp)

J-Stage

2026/01/12

蓄電池の外部制御等による家庭部門でのＤＲ実証 ～既存機能を活用した簡易上げＤＲその２

(DR) without increasing costs for households under the Feed-in Tariff (FIT) scheme. ... A field trial involving households on time-of-use (TOU) pricing showed successful load shifting， with particularly significant effects observed among those on the “Denka Jozu” plan. However...



](https://www.jstage.jst.go.jp/article/jjser/47/1/47_21/_article/-char/en)[

elemental

2026/06/21

EDF and Duracell Energy launch battery storage flexibility trial - elemental

have launched a three-month trial that will explore how residential battery storage can support local electricity flexibility. ... According to the National Infrastructure Commission, greater use of demand side response could reduce the investment required in electricity distribution networks by around 15%, delivering savings of up to £7.9 billion by 2050.



](https://elementallondon.show/news/edf-and-duracell-energy-launch-battery-storage-flexibility-trial/)[

![](https://cdn.deepseek.com/site-icons/napstic.cn)

Napstic

Evaluation of residential demand response trials with smart heat pumps and batteries and their effect at the substation feeder - 首页|Evaluation of residential demand response trials with smart heat pumps and batteries and their effect at the substation feede...

A reduction in mean real power up to 21% was observed for turn-down interventions as well as an increase in real mean power up to 307% for turnup interventions。 In general， the trials had little effect on residents in terms of thermal comfort， hot water availability...



](https://search.napstic.cn/literature/periodical/0220231100916009#1)[

Duke Energy | News Center

2026/02/10

Duke Energy Florida launches Residential Battery Storage Pilot in Orlando’s Hunter’s Creek neighborhood

Duke Energy Florida will apply learnings from the pilot to help determine when and how residential battery systems can be most effective in reducing energy use and grid demand ... high-demand periods. The pilot evaluates how home battery systems can be used for demand response by supplying stored energy during times of peak demand. When available...



](https://news.duke-energy.com/releases/duke-energy-florida-launches-residential-battery-storage-pilot-in-orlandos-hunters-creek-neighborhood)[

neso.energy

Home Response22 assessed the business case for different ESO and DSO services that solar PV with home batteries and heating can ...

Home Response22 assessed the business case for different ESO and DSO services that solar PV with home batteries and heating can provide. This included DSO Secure ... The availability of a home battery23 is not the same as an EV ... For heating, Home Response only regarded the Balancing ... Battery revenue stack of different services, Home Response.



](https://www.neso.energy/document/361091/download?__cf_chl_tk=XBMUWmU2VZQSdA.5SFtdYDFnKn8IjQTSoyoCBIIjMAM-1777686516-1.0.1.1-SY3NVOGeog.b8lhgyLEfrCR.d_AD25NYWbauu3uKgO8#4#3)[

EON Energy

2026/02/25

E.ON Next's pioneering flexibility trial showcases how lower bills, a stronger grid and renewables can thrive together | E.ON News

E.ON Next has launched a pioneering new trial designed to demonstrate how lower energy bills ... the second phase of the project will see up ... demand flexibility can unlock lower bills for struggling ... Early data indicates meaningful bill savings of up to £360 a year per household, driven by each customer receiving a guaranteed payment of £30 per month...



](https://news.eonenergy.com/news/e-on-nexts-pioneering-flexibility-trial-showcases-how-lower-bills-a-stronger-grid-and-renewables-can-thrive-together)[

![](https://cdn.deepseek.com/site-icons/aceee.org)

aceee.org

GMP's Resiliency Zones (RZs) target communities most vulnerable to outages, focusing on rural and high- risk areas

GMP's Resiliency Zones (RZs) target communities most vulnerable to outages, focusing on rural and high- risk areas. In these zones, GMP partners with towns to deploy solar and battery storage systems—



](https://www.aceee.org/sites/default/files/pdfs/faster_and_cheaper_-_demand-side_solutions_for_rapid_load_growth.pdf#24#18)[

![](https://cdn.deepseek.com/site-icons/frontiersin.org)

public-pages-files-2025.frontiersin.org

The electricity cost now stands at 42.064 cents

The electricity cost now stands at 42.064 cents. This implies that the larger the capacity of the battery integrated into the system, the more it aids in leveling the peaks and troughs through energy



](https://public-pages-files-2025.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1289641/pdf#4#4)[

![](https://cdn.deepseek.com/site-icons/uky.edu)

sparklab.engr.uky.edu

Distribution System Optimal Operation of Smart Homes with Battery and Equivalent HVAC Energy Storage for Virtual Power Plant Con...

# Distribution System Optimal Operation of Smart Homes with Battery and Equivalent HVAC Energy Storage for Virtual Power Plant Controls Steven B. Poore, Rosemary E. Alden, Evan S. Jones, and Dan M. I



](https://sparklab.engr.uky.edu/sites/spark/files/2023%20IEEE%20ECCE%20UK%20SPARK%20Poore%20Operation%20Distribution%20System%20HVAC%20Battery%20Energy%20Storage%20Virtual%20Power%20Plant.pdf#1#1)[

EEEP

2026/02/03

Electricity demand response in Japan: Experimental evidence from a residential photovoltaic power-generation system - EEEP

Electricity demand response in Japan ... We report on a randomized controlled trial used to examine the effect of dynamic pricing when applied to households with rooftop photovoltaic (PV) power-generation systems. ... we find that critical ... 3-4% among households with PV systems ... This is the first large-scale field experiment evaluating the demand response of households with PV generation capabilities.



](https://eeep.iaee.org/electricity-demand-response-in-japan-experimental-evidence-from-a-residential-photovoltaic-power-generation-system/)[

EEEP

2026/02/03

field experiment Archives - EEEP

Electricity demand response in Japan: Experimental evidence ... We report on a randomized controlled trial used to examine the effect of dynamic pricing when applied to households with rooftop photovoltaic (PV) power-generation systems. ... we find that critical peak pricing induced significant usage reductions of 3-4% among households with PV systems...



](https://eeep.iaee.org/tag/field-experiment/)[

Eneco

2025/10/13

1,000 households in Zeeland province shift electricity consumption to sunny hours to lower the peak demand

1,000 households in Zeeland province shift electricity consumption to sunny hours to lower the peak demand A thousand households on the Dutch municipalities of Walcheren, Schouwen-Duiveland and Tholen are load-shifting: successfully changing their electricity consumption to times with plenty of solar power. ... The trial ran from 1 May to 31 July ... Immediate self-consumption will be cheapest. In other words...



](https://news.eneco.com/1000-households-in-zeeland-province-shift-electricity-consumption-to-sunny-hours-to-lower-the-peak-demand/)[

![](https://cdn.deepseek.com/site-icons/researchmap.jp)

researchmap

依田 高典 (Takanori Ida) - Electricity demand response in Japan: Experimental evidence from a residential photovoltaic power-generation system - 論文

We report on a randomized controlled trial used to examine the effect of dynamic pricing when applied to households with rooftop photovoltaic (PV) power-generation systems. ... This is the first large-scale field experiment evaluating the demand response of households with PV generation capabilities.



](https://researchmap.jp/read0185923/published_papers/14052178)[

![](https://cdn.deepseek.com/site-icons/ox.ac.uk)

ORA - Oxford University Research Archive

2019/01/03

The practice and potential of renewable energy localisation: results from a UK field trial

We describe a UK field trial in 48 homes of an approach to this problem aimed at directly matching local supply and demand. This combined a community-based business model with social engagement and demand response technology employing both thermal and electrical energy storage.



](https://www.ora.ox.ac.uk/objects/uuid:44045cd9-9fc8-4a4f-906c-e0fdaa759b1b)[

icrepq.com

Validation of flexible demand models and strategies in smart grids for small and medium prosumers

This work presents a scalable system for characterizing flexible demand, based on an experimental DC microgrid. The system integrates photovoltaic generation, various energy storage technologies (batteries, supercapacitors, hydrogen), and controllable load profiles. ... flexibility for small and medium prosumers, with focus on self- consumption, grid stability and costs include...



](https://www.icrepq.com/posters/icrepq25/399-25-rengel-poster.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/gulfoilandgas.com)

Gulf Oil and Gas

2025/10/13

1,000 households shift electricity consumption to sunny hours to lower the peak demand - 1,000 households shift electricity consumption to sunny hours to lower the peak demand

1,000 households shift electricity consumption to sunny hours to lower the peak demand ... A thousand households on the Dutch municipalities of Walcheren, Schouwen-Duiveland and Tholen are load-shifting ... of solar power. In a joint trial set up by grid operator Stedin ... participants were asked to make minor changes in their behaviour. ... 0.24 kW per household per test moment. ... Immediate self-consumption will be cheapest.



](https://gulfoilandgas.com/webpro1/main/mainnews.asp?id=1086090#1)[

![](https://cdn.deepseek.com/site-icons/etsmtl.ca)

Trouver des données de recherche

2025/01/05

Model predictive control for demand flexibility: Real-world operation of a commercial building with photovoltaic and battery systems

We tested two types of demand flexibility applications in the field: electricity bill minimization under time-of-use tariffs and responses to grid flexibility events. Results show that the proposed controller achieves 12% of annual electricity cost savings and 34% peak demand reduction against the baseline, while respecting thermal comfort and food safety.



](https://pure.etsmtl.ca/fr/publications/model-predictive-control-for-demand-flexibility-real-world-operat/)[

![](https://cdn.deepseek.com/site-icons/etsmtl.ca)

Trouver des données de recherche

2025/01/05

Model predictive control for demand flexibility: Real-world operation of a commercial building with photovoltaic and battery systems

Model predictive control for demand flexibility ... We tested two types of demand flexibility applications in the field: electricity bill minimization under time-of-use tariffs and responses to grid flexibility events. Results show that the proposed controller achieves 12% ... 34% peak demand reduction against the baseline, while respecting thermal comfort and food safety.



](https://pure.etsmtl.ca/en/publications/model-predictive-control-for-demand-flexibility-real-world-operat/)[

![](https://cdn.deepseek.com/site-icons/bg.ac.rs)

phaidrabg.bg.ac.rs

The rescheduled demand KPI aims to verify if the use case helped to move demand into the event period

The rescheduled demand KPI aims to verify if the use case helped to move demand into the event period. For instance, if the PV production was higher from 15:00 to 17:00 and the user had received a mes



](https://phaidrabg.bg.ac.rs/open/o:30445#3#3)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

2026/05/06

Reducing peak load from electric vehicles through grid tariffs: Evidence from a randomized field experiment - Beyond feedback, appliance ownership and automation technologies play a crucial role in increasing price elasticity

In a recent field experiment, Bailey et al. (2025a) find that financial incentives for charging between 10 p.m. and 6 a.m. significantly increased off-peak charging, while a non-monetary “nudge” had no effect. Bailey et al. ... Our randomized field experiment is designed



](https://www.sciencedirect.com/science/article/pii/S0095069626000744#2)[

search.web.osakagas.co.jp

Osaka Gas and Panasonic to Conduct a Joint Field Test on Demand Response through Automatic Control of EV Charging

Osaka Gas's DR Option will be linked with Panasonic's Home EV Charging Service app ... From August 2024 to March 2025, Osaka Gas Marketing Co. ... and Panasonic conducted a field test to achieve optimal control in each house and implement DR of an entire house by controlling EV chargers, Ene- Farm cogeneration systems...



](https://search.web.osakagas.co.jp/click?url=https%3A%2F%2Fwww.osakagas.co.jp%2Fen%2Fwhatsnew%2F__icsFiles%2Fafieldfile%2F2026%2F03%2F31%2F260317.pdf&query=%83%4B%83%58&charset=windows-31j&site=EVNVO2AG#1#1)[

![](https://cdn.deepseek.com/site-icons/theiet.org)

IET Digital Library

2025/01/19

From theory to reality: WESA trial integrating dynamic EV flexibility with daily life | IET Conference Proceedings - Skip to main content

We report results from an initial real-world trial to investigate such potential. Building on the previously introduced Whole Energy Systems Accelerator (WESA), the reported field trial makes the following novel contributions ... Over the course of the trial ... with over 2000 kWh of energy delivered. The paper highlights novel WESA testing capabilities and identifies the real-world challenges which must be overcome to unlock the potential of smart EV charging.



](https://digital-library.theiet.org/doi/abs/10.1049/icp.2024.4598?download=true#1)[

![](https://cdn.deepseek.com/site-icons/utilitydive.com)

Utility Dive

2026/03/23

Puget Sound’s vehicle-to-home charging pilot combines demand response, peak shaving, resilience

Puget Sound’s vehicle-to-home charging pilot combines demand response, peak shaving, resilience The test will use electric vehicle batteries for demand response and residential peak shaving while also making their storage capacity available during power outages. ... The study relied on a cohort of 58 drivers in Washington.



](https://www.utilitydive.com/news/puget-sound-energy-ev-electric-vehicle-to-home-pilot/815540/)[

![](https://cdn.deepseek.com/site-icons/electrive.com)

Electrive

2026/07/28

Gelderland launches public smart charging pilot - electrive.com

The field trial will run until January 2027 and covers around 12,000 public charging points. It allows ... The project is designed ... One example is delaying EV charging during periods of peak demand, which the pilot is designed to test.



](https://www.electrive.com/2026/07/29/gelderland-launches-public-smart-charging-pilot/)[

Foresight

2026/04/05

Vehicle-to-Grid Field Demonstration in British Columbia - Foresight

and lessons learned from an 18-month ... of Foresight Canada (“Foresight”). ... The project was designed to advance BC Hydro’s exploration of bidirectional demand response and to measure real-world energy export from fleet electric vehicles to the electricity grid through an operational field deployment. ... This project moved beyond concept validation toward a replicable...



](https://foresightcac.com/report/vehicle-to-grid-field-demonstration-in-british-columbia)[

electrive.net

2026/05/28

V2G-Projekt: Hyundai Group und Vattenfall testen E-Autos als rollende Speicher - electrive.net

Im Fokus des Projekts steht die Vehicle-to-Grid-(V2G)-Ladefunktion – also das Rückspeisen von Energie aus der Fahrzeugbatterie in das Stromnetz. ... „Im Rahmen des Pilotprojekts dienen die Fahrzeuge als flexibler Energiespeicher und tragen dazu bei, Angebot und Nachfrage im Stromnetz besser auszugleichen“, präzisiert Vattenfall.



](https://www.electrive.net/2026/05/29/v2g-projekt-hyundai-group-und-vattenfall-testen-e-autos-als-rollende-speicher/?replytocom=415201#comment)[

pv magazine Deutschland

2026/03/19

Startschuss für das innovative Pilotprojekt LadeFlexBW: Intelligentes Laden von Elektrofahrzeugen stabilisiert Stromnetze - pv magazine Deutschland

Mit dem Start des Pilotprojekts „LadeFlexBW“ beginnt in Baden-Württemberg ein neuartiger Feldtest zur intelligenten, markt- und netzdienlichen Steuerung privater Elektrofahrzeuge. ... Der Ansatz folgt der europäischen Entwicklung hin zu mehr Demand Response – also der aktiven Beteiligung von Verbraucherinnen und Verbrauchern am Energiemarkt...



](https://www.pv-magazine.de/unternehmensmeldungen/startschuss-fuer-das-innovative-pilotprojekt-ladeflexbw-intelligentes-laden-von-elektrofahrzeugen-stabilisiert-stromnetze/)[

Charged EVs

2025/09/15

Ford Pro and Southern Company report results of managed EV charging pilot

Ford Pro (the division of the automaker that serves fleet customers) and Atlanta-based utility Southern Company have completed a six-month pilot program to test managed charging for fleet EV operation



](https://chargedevs.com/newswire/ford-pro-and-southern-company-report-results-of-managed-ev-charging-pilot/)[

![](https://cdn.deepseek.com/site-icons/smartcitiesdive.com)

Smart Cities Dive

2026/03/25

Puget Sound Energy is turning to EVs for backup power and grid support

The utility is partnering with Ford and Kia to test whether electric vehicles can keep homes running and support grid resilience during outages. First published on ### Dive Brief: - Puget Sound Ene



](https://www.smartcitiesdive.com/news/puget-sound-energy-ev-electric-vehicle-to-home-pilot/815693/)[

patentimages.storage.googleapis.com

[0300] The total HVAC-cycling frequency within a multi-region building or other thermostat-controlled multi-region environment m...

[0300] The total HVAC-cycling frequency within a multi-region building or other thermostat-controlled multi-region environment may be closely related to the overall cooling or heating efficiency as well as to HVAC-maintenance costs and life cycles. FIGS.



](https://patentimages.storage.googleapis.com/e3/37/3a/fc109c1d2bc539/US20140052300A1.pdf#20#19)[

patentimages.storage.googleapis.com

FIG

Then shortly into this "off" state, the plant is required again to cycle "on", thereby short-cycling the system again. As in the example of FIG. 2, the plant again is subject to short-cycling which decreases the system efficiency and shortens the life of the plant. ... This also increases the life of the plant by not short-cycling it and prevents energy from being wasted.



](https://patentimages.storage.googleapis.com/b8/dc/f3/7ee1c67c3612df/US5192020.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

サーモスタットのメンテナンス バンド

22°C まで上がるまで再び起動しません ... - Google Nest サーモスタットは、時間の経過とともに家の冷暖房の効き具合を学習し、快適さとシステムの寿命とのバランスを取るようにメンテナンス バンドを自動で調整します。



](https://support.google.com/googlenest/answer/9233450?hl=ja&ref_topic=9361874)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2024/10/03

Optimal Dead Band Control of Occupant Thermostats for Grid-Interactive Homes - Optimal Dead Band Control of Occupant Thermostats for Grid-Interactive Homes

Conventional thermostats typically have a built-in temperature dead band ... and HVAC stays at the most recent state (On/Off). The temperature dead band is an important control parameter that can help save energy as well as preventing frequent On/Off switching cycles leading to excessive wear and tear on the equipment. However...



](https://ieeexplore.ieee.org/abstract/document/10694204#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Thermostat maintenance band - Send feedback on

When your heating or cooling turns on and off frequently it can use more energy and may increase wear on your system. To help prevent this, your ... This delay is commonly called the maintenance band, differential, or temperature swing. ... The maintenance band allows the temperature in your home ... system on or off. You may notice a difference...



](https://support.google.com/googlenest/answer/9233450?hl=sk#1)[

jcai.oucreate.com

where \(X^{t}\) is the part load ratio, which is defined as the ratio of the actual load at each time step to the sensible cooli...

Thermostat cycling model ... This study proposes ... The integrated model affords an analytical methodology to evaluate the HVAC system run time and cycling frequency which are the two major determinants of equipment lifetime. ... the effect caused by the actual system run time and the lifetime reduction effect due to cyclic operations.



](http://jcai.oucreate.com/wp-content/uploads/2022/07/Aging_aware_demand__Jerson___clean_revision.pdf#4#2)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Thermostat maintenance band - Enviar comentarios sobre

When your heating or cooling turns on and off frequently it can use more energy and may increase wear on your system. To help prevent this, your Nest thermostat will wait to turn on your system. This



](https://support.google.com/googlenest/answer/9233450?authuser=5&hl=es#1)[

patentimages.storage.googleapis.com

At 604, gateway 102 determines an action to perform with device 106. For example, the action to perform may have been determined...

At 604, gateway 102 determines an action to perform with device 106. For example, the action to perform may have been determined by server 112 and transmitted to gateway 102. In another embodiment, ga



](https://patentimages.storage.googleapis.com/be/be/44/d6c169da5448ab/US9952614.pdf#3#3)[

Abdullah Gül Üniversitesi

Optimal Dead Band Control of Occupant Thermostats for Grid-Interactive Homes

2024 International Conference on Smart Energy Systems and Technologies, SEST 2024, Torino, İtalya, 10 - 12 Eylül 2024, (Tam Metin Bildiri) - Yayın Türü: Bildiri / Tam Metin Bildiri - Doi Numarası: 10



](https://avesis.agu.edu.tr/yayin/48c7664c-7660-4b51-ba87-ef5fbd6605b4/optimal-dead-band-control-of-occupant-thermostats-for-grid-interactive-homes)[

電力中央研究所

オフィスにおけるデマンドレスポンス制御試験Ⅱ:居室内快適性とワーカーの制御キャンセル率の分析 ｜電力中央研究所 報告書 - 報告書「電力中央研究所報告」は当研究所の研究成果を取りまとめた刊行物として、昭和28年より発行されております

2010年夏平日(35日間)のうち ... To study the acceptance of demand response (DR) control for commercial sector, we conducted a field experiment of peak-cutting DR control of air conditioning in two office spaces, named Office-A and Office-B, located in Tokyo during 2010 summer ... experiment in 2009. ... workers were allowed to cancel



](https://criepi.denken.or.jp/hokokusho/pb/reportDetail?reportNoUkCode=Y10040#1)[

core.ac.uk

8-103-22 Martin-Vilaseca

Living with demand response: Insights from a field study of DSR using heat pumps ... This study compares what happened in three homes of early adopters of heat pumps with demand-side response (DSR). ... The analysis of the results revealed that air and surface temperatures dropped during demand response (air temperature dropped 0.3-1.1 degrees in 3 hours). ... The findings challenge conventional modelling assumptions that demand response is unnoticed by people



](https://core.ac.uk/download/541348064.pdf#3#1)[

電力中央研究所

オフィスにおけるデマンドレスポンス制御試験:需要調整効果と居室内快適性の分析 ｜電力中央研究所 報告書 - 報告書「電力中央研究所報告」は当研究所の研究成果を取りまとめた刊行物として、昭和28年より発行されております

系統側から提示されるシグナルに応じて需要家自身が ... DR制御に対する需要家の受容性は重要な要素である ... 本稿では著者らが2009年7-9 ... Experiment results showed that, it is true these two ... 23% of a peak demand of the office space during DR period, respectively; however, the adopted DR control strategies affected worker's comfort and their subjective working efficiency evidently.



](https://criepi.denken.or.jp/hokokusho/pb/reportDetail?reportNoUkCode=Y09014#1)[

![](https://cdn.deepseek.com/site-icons/springerprofessional.de)

springerprofessional.de

Energy Efficiency (2021) 14: 91

A field demand response event was simulated at a leisure center in Ireland to evaluate the suitability of the site to participate in the Irish demand response market ... A study using the IDA Indoor Climate and Energy ... (Alimohammadisagvand et al. ... A field study on air-conditioned offices in California showed that raising the cooling temperature set point by more than 1.7



](https://www.springerprofessional.de/content/pdfId/19928582/10.1007/s12053-021-09965-w#4#1)[

arcomabstracts.com

2025/04/10

Domestic demand-side response with heat pumps: Controls and tariffs

Findings are presented from a field trial of a new control system that aims to optimize heat pump performance, including under time-varying tariff conditions. ... While the system delivered short-term demand reductions successfully, longer-term demand shifting risked causing unacceptable disturbance to occupants.



](https://arcomabstracts.com/id/eprint/5637/)[

![](https://cdn.deepseek.com/site-icons/hkust.edu.hk)

researchportal.hkust.edu.hk

2024/08/31

Field demonstration of priority stack-based controls in an office building for demand response - Field demonstration of priority stack-based controls in an office building for demand response

Field demonstration of priority stack-based controls in an office building for demand response ... This study developed and tested ... The vanilla and modified PSBC strategies was evaluated through a 22-day field test in a real office building, in terms of load tracking and thermal comfort.



](https://researchportal.hkust.edu.hk/en/publications/field-demonstration-of-priority-stack-based-controls-in-an-office/#main-content#1)[

![](https://cdn.deepseek.com/site-icons/pnnl.gov)

Pacific Northwest National Laboratory | PNNL (.gov)

2026/02/06

Assessing Thermal Comfort and Participation in Residential Demand Flexibility Programs

- Research - Scientific Discovery - Energy Resiliency - National Security - Data Science & Computing - Publications & Reports - Featured Research - People - Partner with PNNL - Facilities & Centers



](https://www.pnnl.gov/publications/assessing-thermal-comfort-and-participation-residential-demand-flexibility-programs)[

![](https://cdn.deepseek.com/site-icons/osti.gov)

osti.gov

The validation of both Thermal Frustration Theory and Comfort Zone Theory models revealed several limitations affecting generali...

The validation of both Thermal Frustration Theory and Comfort Zone Theory models revealed several limitations affecting generalizability. While TFT demonstrated marginally higher predictive performanc



](https://www.osti.gov/servlets/purl/2998091#22#13)[

![](https://cdn.deepseek.com/site-icons/osti.gov)

OSTI.GOV (.gov)

2010/05/27

Customer Impact Evaluation for the 2009 Southern California Edison Participating Load Pilot - Attention

Technical Report · DOI:https://doi.org/10.2172/983800· OSTI ID:983800 The 2009 Participating Load Pilot Customer Impact Evaluation provides evidence that short duration demand response events which



](https://www.osti.gov/biblio/983800#1)[

![](https://cdn.deepseek.com/site-icons/aceee.org)

aceee.org

From the cloud to your basement: Can New Communication Protocols Solve the Interoperability Roadblocks in Residential Demand Fle...

Field studies show that demand flexibility in residential buildings can save up to \(20\%\) in energy costs ... Matter ... though the communication to consumer devices is generally handled by other protocols, such as Matter. ... Matter addresses local interoperability across diverse vendor ecosystems within the home; however, it currently lacks native mechanisms for coordinating directly with external utility or aggregator platforms.



](https://www.aceee.org/wp-content/uploads/2026/08/from-the-cloud-to-your-basement-can.pdf#3#1)[

geotogether.com

Open ADR project allows grid to talk directly to the home, aligning with real world use cases being deployed by demand side resp...

geo led the BEIS (now DESNZ) funded Core4Grid trial in which they were able to show how effective use of data generated by smart meters could deliver significant savings in both energy costs and carbon emissions. The trial, which also involved EDF Energy, saw households saving an average of \(49\%\)



](https://geotogether.com/wp-content/uploads/2025/04/250403-OpenADR_Matter_bridging_spec_PR_v2.1.pdf#1#1)[

ssk21.co.jp

東京電力パワーグリッド/CSA/エコーネットコンソーシアム

あげられた「スマートメーターのIoTルート活用」について、2025年7月より「スマートメーターを活用したディマンドリス ... 質疑応答 ... 本講演では、Matterの概要とエネルギーマネジメントへの取り組みを解説しつつ、AIによるパーソナライズやアン



](https://www.ssk21.co.jp/seminarpamphlet/S25479.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/luiss.it)

tesi.luiss.it

LUISS

A solution to tackle the variability of renewable energy generation: using the Matter IoT standard to enable implicit demand response for private consumers ... Variability in electricity markets...... 6 Energy storage...... ... Demand Response ...... 36** Explicit Demand Response...... 36 Implicit Demand Response...... 37 ... Implementing implicit demand response in households ...... ... The Matter Standard ...... ... Why Matter for DR ......



](https://tesi.luiss.it/34687/1/630383_FIASTRI_ALESSANDRO.pdf#8#1)[

geotogether.com

Battery Storage devices typically allow a range of power values to charge or discharging the batteries

OpenADR is an open standard that allows grid operators to communicate Demand Response (DR) actions in an ‘Automated’ way (hence the name OpenADR). ... over a secure IP network. A Utility or Distribution System Operator (DSO) can use the OpenADR protocol to enable its Distributed Energy Resources Management System (DERMS) to request control of 3rd party assets.



](http://geotogether.com/wp-content/uploads/2025/04/Matter_OpenADR3.x_Interworking_Spec_v1.0.pdf#15#5)[

![](https://cdn.deepseek.com/site-icons/aceee.org)

aceee.org

<table><tr><td>Communication Pathway</td><td>Suitable Protocol (s)</td><td>Reason for choice</td></tr><tr><td>Pathway 2, 4: Aggr...

Matter, OCPP</td><td>Supports local hub deployment ... The protocols examined were OpenADR, IEEE 2030.5, Matter, OCPP, CTA- 2045, and HCA, along with proprietary approaches.



](https://www.aceee.org/wp-content/uploads/2026/08/from-the-cloud-to-your-basement-can.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

ses.jrc.ec.europa.eu

Matter 1.3 Specification Released

Appliances (White goods)- Robot vacuum cleaners- Closure Sensors- Environmental Sensing / Controls- Smoke & CO Detectors- Energy management (Solar PV / Battery / EV Charging / Heat pumps / HVAC / Water Heater / Tariffs / Carbon Incentive Tables / DSR)- Access points ... Matter Energy Management (1.3)



](https://ses.jrc.ec.europa.eu/sites/default/files/2024-10/3.2_csa_mapping_new_example_to_saref_in_annex_3_coc_v.1.0_james_harrow.pdf#1#1)[

geotogether.com

In return, the customer may be offered credits on their bill for turning down their energy

In return, the customer may be offered credits on their bill for turning down their energy. The service relies upon the customer having a smart meter, and uses a base-lining methodology to assess if



](http://geotogether.com/wp-content/uploads/2025/04/Matter_OpenADR3.x_Interworking_Spec_v1.0.pdf#15#3)[

geotogether.com

The DSRSP may need to know the historic power readings from the boundary (smart) meter in order to set a baseline

The DSRSP may need to know the historic power readings from the boundary (smart) meter in order to set a baseline. The power readings will allow a DSO



](http://geotogether.com/wp-content/uploads/2025/04/Matter_OpenADR3.x_Interworking_Spec_v1.0.pdf#15#9)