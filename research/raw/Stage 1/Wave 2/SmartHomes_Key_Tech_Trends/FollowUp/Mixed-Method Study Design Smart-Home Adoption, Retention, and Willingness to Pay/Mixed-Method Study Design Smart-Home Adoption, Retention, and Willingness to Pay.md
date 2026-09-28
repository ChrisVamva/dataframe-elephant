---
modified: 2026-09-28T20:52:14+03:00
---
# Mixed-Method Study Design: Smart-Home Adoption, Retention, and Willingness to Pay

## 1. Study Architecture

This study employs a **sequential explanatory mixed-methods design** in three phases:

| Phase | Method | Sample | Purpose |
|---|---|---|---|
| **Phase 1** | Quantitative survey + conjoint experiment | N = 2,400 (stratified) | Measure adoption, barriers, WTP, segment structure |
| **Phase 2** | Semi-structured interviews | n = 48 (nested from Phase 1) | Explain quantitative patterns; surface mechanisms |
| **Phase 3** | Behavioral validation (diary study + usage data) | n = 120 (subset) | Validate stated preferences against observed behavior |

The design follows established mixed-method smart-home researchand addresses the **intention-behavior gap** documented in Kuwaiti residences, where perceived behavioral control strongly predicted intention but social norms did not predict actual adoption.

---

## 2. Sampling Plan

### Target Population

US internet households (N ≈ 130 million). Eligibility: age 18+, primary or shared responsibility for household technology decisions.

### Stratification Variables

The sampling frame stratifies across eight dimensions identified in the literature as significant moderators of adoption:

| Dimension | Levels | Source |
|---|---|---|
| **Housing type** | Single-family detached, single-family attached, apartment/condo, mobile home | Housing tenure shapes adoption; elderly tenants negatively correlate with thermostat ownership |
| **Tenure** | Owner-occupied, renter, subsidized/public housing | Renters face distinct barriers: inability to modify infrastructure, surveillance concerns |
| **Climate** | Cold (<4,000 HDD), mixed, hot (>2,000 CDD) | Climate determines which smart categories deliver value |
| **Household composition** | Single adult, couple no children, family with children <18, multigenerational, older adult (65+) living alone | Aging populations prioritize health monitoring; families prioritize cameras/locks |
| **Technical confidence** | Low, moderate, high (validated TRI 2.0 scale) | 52% of DIY users report setup issues; non-technical users face greatest barriers |
| **Income** | <$30k, $30–60k, $60–100k, >$100k | Low-income households spend three times more of income on heating/cooling |
| **Energy burden** | Low (<6% income), moderate (6–10%), high (>10%) | Energy-burdened households stand to gain most from smart energy devices but face highest adoption barriers |
| **Privacy preference** | Affordability-oriented, privacy-oriented, reliability-oriented | Consumers segment into three distinct clusters based on smart home considerations |

### Sample Size and Allocation

**Total N = 2,400.** Quota sampling ensures minimum cell sizes:

| Stratum | Minimum n | Rationale |
|---|---|---|
| Owner, single-family, high income | 400 | Primary adopter segment |
| Renter, apartment, low-moderate income | 400 | Underserved segment with distinct barriers |
| Energy-burdened (>10% income) | 300 | Policy-relevant; highest potential benefit |
| Older adults (65+) living alone | 300 | Aging-in-place priority |
| Families with children <18 | 400 | Security and safety priority |
| High privacy preference | 300 | Privacy-oriented cluster |
| Low technical confidence | 300 | Setup failure risk |

**Power analysis:** With n = 2,400, the study detects a 5-percentage-point difference in adoption rates between strata at 80% power (α = 0.05). For conjoint analysis (12 choice tasks per respondent), the design supports estimation of main effects and two-way interactions at the segment level.

### Recruitment

- **Panel provider** with address-based sampling to reach non-internet households via mail-push-to-web
- **Oversample** of renters, low-income, and energy-burdened households via targeted recruitment through utilities, housing authorities, and community organizations
- **Incentive:** $25 gift card for survey completion; $75 for interview; $150 for diary study

---

## 3. Interview Guide (Semi-Structured)

Interviews last 60–75 minutes, conducted remotely via video call. The guide follows a **critical incident technique**—participants describe specific adoption, setup, failure, and abandonment experiences rather than general opinions.

### Opening (10 min)

1. "Walk me through the smart devices you currently have in your home. How did you decide to get each one?"
2. "Which device do you use most? Which do you use least? Why?"

### Adoption Decision (15 min)

3. "Tell me about the last smart device you bought. What triggered the purchase? What alternatives did you consider?"
4. "What almost stopped you from buying it? What would have made the decision easier?"
5. "How did you figure out what it would cost—not just to buy, but to own and maintain?"

### Setup and Failure Experience (15 min)

6. "Describe the setup process for [most recent device]. What went well? What was frustrating?"
7. "Have you ever had a device fail or stop working? What happened? How did you recover?"
8. "Have you ever returned a device or abandoned it? What led to that decision?"

### Trust and Privacy (10 min)

9. "What data do you think your smart devices collect about you? How do you feel about that?"
10. "Have you ever changed a privacy setting or disabled a feature because of privacy concerns?"

### AI Delegation (10 min)

11. "If an AI assistant could manage some parts of your home automatically, what would you be comfortable delegating? What would you never delegate?"
12. "How would you want to be informed when the AI makes a decision on your behalf?"

### Willingness to Pay (10 min)

13. "If a smart device saved you $X per month on energy, what would you be willing to pay upfront for it?"
14. "How do you feel about subscriptions for smart home features? What would justify a monthly fee?"

### Closing (5 min)

15. "If you could change one thing about how smart home products are designed or sold, what would it be?"

**Probes:** "Can you give me a specific example?" / "What did you do next?" / "How did that make you feel?"

**Sample allocation:** 48 interviews stratified as:
- 12 owners, single-family, high technical confidence
- 12 renters, apartment, low-moderate income
- 8 energy-burdened households
- 8 older adults living alone
- 8 families with children

---

## 4. Survey Instrument

The survey comprises 85 items across 10 modules, with a median completion time of 22 minutes.

### Module 1: Household Profile (12 items)

- Housing type, tenure, length of residence
- Household composition (adults, children, older adults)
- Climate zone (ZIP-based)
- Income, energy burden (energy costs as % income)
- Technical confidence (TRI 2.0 short form)

### Module 2: Current Device Ownership and Use (15 items)

- Device categories owned (lighting, security, thermostat, camera, lock, energy, appliance)
- Number of devices per category
- Primary control method (app, voice, hub, automation)
- Frequency of use (daily, weekly, rarely)
- **Behavioral anchor:** "In the last 7 days, how many times did you use a smart device to control something in your home?"

### Module 3: Setup and Maintenance Experience (10 items)

- Self-reported setup difficulty (1–5 scale)
- Setup time (minutes)
- Whether professional installation was used (and why)
- Whether device was returned or abandoned
- Ongoing maintenance burden (updates, troubleshooting, app management)

**Validated item:** "The setup process was more difficult than I expected" (1–5 agree scale). Parks Associates documents 52% setup/connectivity issues.

### Module 4: Trust and Privacy (12 items)

- Concern about data collection (1–5 scale per data type: voice, video, occupancy, energy usage, biometric)
- Comfort sharing data with spouse, children, roommates, platform, third parties
- Actions taken to protect privacy (disabled features, changed settings, avoided devices)
- **Segmentation item:** "When choosing a smart home device, which matters more: price, privacy, or reliability?" (forced choice)

### Module 5: Desired Outcomes and Value (10 items)

- Importance of outcomes (1–5): convenience, safety, comfort, energy savings, aging in place, insurance benefits
- Which outcome would justify a $200+ purchase?
- Which outcome would justify a $10/month subscription?

### Module 6: AI Delegation (8 items)

- Willingness to delegate across 8 use cases: lighting, thermostat, security arming, lock control, energy optimization, appliance scheduling, camera monitoring, grocery ordering
- **Delegation tier:** No delegation / Reactive support / Supervisory alerts / Anticipatory confirmation / Full autonomy
- Trust in AI for home decisions (1–5 scale)

### Module 7: Subscription Tolerance (8 items)

- Number of current smart home subscriptions
- Monthly spend on subscriptions
- Likelihood to cancel within 12 months (1–5 scale)
- Features that would justify a subscription
- **Price sensitivity:** "At what monthly price would you definitely cancel? Probably cancel? Probably keep? Definitely keep?" (van Westendorp)

### Module 8: Total Cost of Ownership (6 items)

- Upfront spend on smart devices (last 24 months)
- Monthly ongoing costs (subscriptions, maintenance, repairs)
- Time spent on setup and troubleshooting (hours per month)
- Replacement/upgrade frequency

**Behavioral validation:** Cross-reference self-reported spend with diary study data.

### Module 9: Conjoint Experiment (12 choice tasks)

See Section 5.

### Module 10: Open-Ended (4 items)

- "What is the biggest frustration with your smart home?"
- "What would make you recommend a smart home product to a friend?"
- "What would you never automate?"

---

## 5. Conjoint and Pricing Design

### Attribute Selection

Based on prior conjoint studies in smart home contexts, five attributes are included, each with 3–4 levels.

| Attribute | Levels | Rationale |
|---|---|---|
| **Price (upfront)** | $50, $100, $200, $350 | Price heavily outweighs other attributes |
| **Subscription cost** | $0/month, $5/month, $10/month, $20/month | 53% of device owners pay no subscription |
| **Data processing** | Cloud-only, Cloud + local, Local-only | Privacy-oriented cluster values local processing |
| **Interoperability** | Works with one ecosystem, Works with two, Works with all major (Matter) | Matter reduces friction; willingness to pay for multi-ecosystem |
| **Setup complexity** | Professional install included, Guided DIY (app), DIY only | 52% report setup issues |
| **Energy savings guarantee** | None, 5% guaranteed, 15% guaranteed | Energy savings top benefit at 46% |

### Experimental Design

**Fractional factorial design:** 6 attributes with 4, 4, 3, 3, 3, 3 levels = 1,296 possible profiles. A **D-optimal design** selects 36 profiles, blocked into 3 versions of 12 choice tasks each. Each choice task presents two product profiles plus a "neither" option.

**Example choice task:**

| Feature | Product A | Product B |
|---|---|---|
| Upfront price | $200 | $100 |
| Subscription | $5/month | $0/month |
| Data processing | Cloud + local | Cloud-only |
| Interoperability | Works with all (Matter) | Works with one ecosystem |
| Setup | Guided DIY app | Professional install included |
| Energy savings | 15% guaranteed | None |
| **Which would you choose?** | ○ | ○ |

### Analysis

- **Hierarchical Bayes (HB)** estimation of individual-level part-worth utilities
- **Willingness to pay (WTP)** calculated as marginal utility of attribute level divided by price coefficient
- **Segment-level models** for each stratum (renter, owner, energy-burdened, privacy-oriented)
- **Latent class analysis** to identify unobserved preference segments

**Key outputs:**
- WTP for Matter interoperability
- WTP for local processing
- WTP for guaranteed energy savings
- Subscription tolerance by segment

---

## 6. Analysis Plan

### Quantitative Analysis (Phase 1)

| Analysis | Method | Purpose |
|---|---|---|
| **Adoption rates** | Weighted descriptive statistics | Compare across strata |
| **Barrier importance** | Rank-order analysis | Identify dominant barriers by segment |
| **WTP estimation** | HB conjoint | Marginal WTP for attributes |
| **Segmentation** | Latent class analysis + k-means clustering | Replicate and refine three-cluster structure (affordability, privacy, reliability) |
| **Drivers of adoption** | Logistic regression | Predict adoption from technical confidence, income, tenure, privacy preference |
| **Subscription tolerance** | Van Westendorp + survival analysis | Price points and churn risk |
| **TCO estimation** | Descriptive + regression | Observed vs. stated costs |

### Qualitative Analysis (Phase 2)

- **Thematic analysis** using NVivo, with deductive codes from survey constructs and inductive codes for emergent themes
- **Framework matrix:** Rows = participants, Columns = themes (adoption trigger, setup experience, failure recovery, trust, delegation)
- **Cross-case comparison** by stratum to identify segment-specific mechanisms

### Integration (Phase 3)

- **Joint display** comparing quantitative survey findings with qualitative themes
- **Behavioral validation:** Diary study data (device usage logs, spending records) compared against survey self-reports
- **Discrepancy analysis:** Where stated preferences diverge from observed behavior, qualitative interviews explain why

**Mixed-methods research questions:**

| Quantitative Finding | Qualitative Explanation | Integration |
|---|---|---|
| Renters report lower adoption | Interview themes: infrastructure constraints, landlord approval, surveillance anxiety | Joint display: renter-specific barriers |
| Privacy-oriented cluster shows higher WTP for local processing | Interviews: "I don't want my camera video in the cloud" | Conjoint WTP for local processing by cluster |
| Energy savings stated as top benefit | Interviews: "I bought it for savings but haven't changed my behavior" | Discrepancy analysis: intention-behavior gap |

---

## 7. Bias Limitations

| Bias | Risk | Mitigation |
|---|---|---|
| **Hypothetical bias** | Stated WTP exceeds actual WTP in conjoint | Include incentivized choice experiment (real choice of one product at stated price) |
| **Social desirability** | Over-reporting privacy concerns, under-reporting convenience prioritization | Use indirect questioning; validate with behavioral data |
| **Panel bias** | Panel participants differ from general population (more tech-savvy, higher income) | Address-based sampling for non-panel households; post-stratification weights |
| **Recall bias** | Inaccurate recall of setup time, spend, failure frequency | Diary study validates survey recall for subset |
| **Attrition bias** | Renters, low-income, non-adopters less likely to complete | Higher incentives; shorter survey; multiple contact attempts |
| **Conjoint attribute framing** | Attribute descriptions influence choice | Pre-test attribute wording with cognitive interviews (n = 20) |
| **Intention-behavior gap** | Stated adoption intention does not predict behavior | Phase 3 behavioral validation; weight quantitative findings by observed behavior |

**Sample limits:** The study is US-only. Findings may not generalize to markets with different housing policies, energy pricing, or privacy regulation. The conjoint design includes six attributes; omitted attributes (brand, design, ecosystem) may influence choice. The diary study (n = 120) is powered for descriptive comparison, not subgroup hypothesis testing.

---

## 8. Anticipated Segments

Based on prior research, the study expects to identify **five to six segments**:

| Segment | Defining Feature | Expected Size | Key Barrier | WTP Driver |
|---|---|---|---|---|
| **Affordability-oriented** | Price dominates decision; minimal feature interest | 30–35% | Upfront cost; subscription aversion | Energy savings with verified payback |
| **Privacy-oriented** | Willing to pay premium for local processing, no cloud | 20–25% | Data collection concerns; cloud distrust | Local control; E2E encryption |
| **Reliability-oriented** | Values stable operation; avoids complexity | 20–25% | Setup complexity; failure risk | Professional install; warranty |
| **Convenience-driven** | Early adopter; values automation and voice control | 15–20% | Ecosystem fragmentation; interoperability | Seamless multi-ecosystem integration |
| **Energy-burdened pragmatist** | High energy costs drive interest; limited budget | 10–15% | Upfront cost; rental status | Guaranteed bill reduction; utility subsidy |
| **Security-focused** | Prioritizes cameras, locks, monitoring | 15–20% | Subscription fatigue; false alarms | Professional monitoring; insurance discount |

The affordability, privacy, and reliability clusters replicate the three-cluster structure documented in a 631-participant US study.

---

## 9. Adoption Barriers (Expected Findings)

Based on the evidence base, the study expects to confirm:

| Barrier | Expected Dominance | Key Evidence |
|---|---|---|
| **Upfront cost** | Top barrier across all segments | 46% of adopters and 52% of non-adopters cite cost【—】 |
| **Setup complexity** | Second barrier, strongest for low technical confidence | 52% of DIY users report setup/connectivity issues |
| **Privacy and security** | Third barrier, segment-specific | ~45% cite privacy and security concerns【—】 |
| **Subscription fatigue** | Growing barrier; 53% pay no subscription | High churn for low-engagement services |
| **Interoperability** | Moderating barrier; Matter reduces friction | Ecosystem fragmentation persists |
| **Reliability** | Underestimated by vendors | 23% of devices abandoned within a year |

**Expected intention-behavior gap:** 40–50% of respondents who state intention to adopt a device within 6 months will not have done so at 12-month follow-up. This gap is documented in Kuwaiti residences, where perceived behavioral control was the strongest predictor of intention but social norms did not predict actual adoption.

---

## 10. Product Implications

| Finding | Implication |
|---|---|
| Price dominates WTP | **Design for affordability first.** Features are secondary to price for 30–35% of the market. |
| Setup failure affects 52% | **Bundle setup support into the purchase price.** The NPS gap between pro-installed (49) and self-installed (41) is a measurable quality signal. |
| Privacy-oriented segment pays premium | **Offer local-processing SKUs.** A privacy-tier product at 20–30% premium can capture 20–25% of the market. |
| Energy-burdened households benefit most but adopt least | **Subsidy and on-bill financing are essential.** Without intervention, the households that would benefit most are the least likely to adopt. |
| Renters face structural barriers | **Design portable, non-invasive devices.** Clip-on, plug-in, and removable products address a large underserved segment. |
| AI delegation follows partial-autonomy preference | **Design for Tier 3 delegation** (anticipatory assistance requiring confirmation). Full autonomy is rarely preferred; no delegation is rare. |
| Subscription tolerance is low | **Charge for intelligence, not access.** Subscriptions that deliver ongoing AI value retain users; access-only subscriptions face churn. |

---

## 11. Deliverables and Timeline

| Phase | Deliverable | Timeline |
|---|---|---|
| **Phase 1** | Survey instrument finalized; cognitive pretest (n = 20) | Month 1–2 |
| **Phase 1** | Survey fielded (n = 2,400) | Month 3–4 |
| **Phase 1** | Conjoint analysis; segment identification | Month 5 |
| **Phase 2** | Interviews conducted (n = 48) | Month 5–7 |
| **Phase 2** | Thematic analysis; joint display | Month 8 |
| **Phase 3** | Diary study (n = 120); behavioral validation | Month 7–10 |
| **All** | Final report: segments, barriers, WTP, product implications | Month 11 |

**Total cost:** $285,000–$340,000 (panel incentives, interview incentives, diary study compensation, analysis software, researcher time).