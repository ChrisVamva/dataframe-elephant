---
modified: 2026-09-28T20:31:08+03:00
---
The evidence across standards, regulatory guidance, independent testing, and vendor policies reveals a consistent pattern: **formal compliance is advancing faster than practical household protection**. A device can carry the right certification, publish a support period, and implement secure commissioning—and still fail a household when its cloud shuts down, its AI assistant is prompt-injected, or its biometric sensor accepts a printed photo. The minimum trustworthy lifecycle must therefore be assessed against what actually protects a home, not what satisfies a checkbox.

---

## 📅 Support Periods and Update Mechanisms by Device Category

| Device Category | Minimum Expected Support | Update Mechanism | Evidence / Gap |
|---|---|---|---|
| **Smart locks** | 3–5 years (CRA floor); often undocumented | Firmware OTA via vendor app; rarely automatic | Consumer Association tests found plaintext transmission of unlock commands and IC cards that could be cloned |
| **Cameras** | 5 years (Google Nest explicitly); Apple does not publish a fixed period | Automatic OTA for Nest; HomeKit Secure Video relies on hub-based local analysis with E2E encryption | No vendor publishes camera support periods as clearly as Google |
| **Hubs** | 3 years (IKEA); 4 years (Google); 5 years (Amazon) | Automatic security updates (Google, Amazon); manual for some | A University of Skövde audit found Amazon and Google state automatic updates; others do not |
| **Routers** | 3–5 years (UK PSTI statements); TP-Link: 3 years after EOL | Automatic or manual depending on vendor; rarely guaranteed beyond support period | TP-Link, Grandstream, and Devolo publish 5-year periods; Keenetic ends all updates 5 years after release |
| **Appliances** | 7 years (Samsung, from 2024 models); Miele via app | Automatic remote update for Samsung; Miele Remote Update Service | Samsung’s 7-year commitment is an outlier; most appliance makers do not publish periods |
| **Energy devices** | Not standardized; CRA floor applies | Vendor-specific; Matter OTA exists but with limited rollback features | Matter OTA requires manufacturer-signed firmware but “has limitations in sequential updates and recovery” |
| **AI assistants** | Not defined as hardware; tied to cloud service lifecycle | Cloud-side model updates; no local update path for LLM capabilities | Google retains Gemini for Home activity for 18 months by default; Amazon retains recordings for 3 or 18 months |

**The practical gap:** The EU Cyber Resilience Act sets a **five-year minimum support floor** and requires that security updates remain available for **10 years or the remaining support period, whichever is longer**. But the CRA does not apply until **December 2027**, and its five-year floor is explicitly “not a default”—manufacturers can justify shorter periods if they argue expected use time is less. Meanwhile, the US has no comparable federal lifecycle mandate; California SB-327 requires only a “reasonable security feature,” which in practice means no default password.

---

## 🔒 Effectiveness of Segmentation, Automatic Updates, MFA, and Secure Commissioning

**Segmentation** is the most underutilized control. Matter’s fabric model provides strong logical separation: each fabric has its own root of trust, and devices in one fabric cannot control devices in another without explicit authorization. But this protects against cross-fabric interference, not against a compromised device within a fabric. Households rarely VLAN-segment IoT devices from primary networks, and no major consumer router ships with automatic IoT isolation enabled by default.

**Automatic updates** are effective where implemented but inconsistent. Google Nest devices receive **automatic security updates for at least five years** from first sale. Amazon and Google state automatic updates; most other vendors do not. The ANSI blog notes that **46% of IoT devices with known vulnerabilities have no reliable path to receiving updates**. Matter OTA exists as a standardized mechanism, but it requires manufacturer-signed firmware and has limited recovery capabilities, meaning a failed update can brick a device without a rollback path.

**MFA** is unevenly applied. Google Home supports passkey and voice match; Samsung Knox Matrix extends to appliances with passkey support and a security dashboard. But for the most consequential actions—unlocking a door, disarming an alarm—MFA is often absent or optional. Google Home’s developer documentation mandates secondary verification for locks, but this is a platform requirement, not a device-level guarantee.

**Secure commissioning** is Matter’s strongest security feature. PASE (Passcode-Authenticated Session Establishment) creates an encrypted channel during onboarding, and device attestation verifies the device carries a valid certificate chain. This prevents rogue devices from joining a fabric. But commissioning is also where most user errors occur—Bluetooth left open, QR codes photographed and reused, setup codes shared insecurely. Matter’s security model is robust; the human process around it is not.

---

## 🕵️ Data Types Creating the Greatest Privacy Risk

| Data Type | Risk Level | Why |
|---|---|---|
| **Biometric templates (face, fingerprint)** | Highest | Cannot be changed if compromised; often processed on-device but poorly regulated in consumer locks. Consumer tests found printed photos could unlock some locks |
| **Camera video and audio** | Very high | Continuous ambient capture; E2E encryption protects transit but not device compromise. Ring faced backlash for using facial data without permission |
| **Voice recordings and transcripts** | High | Retained for 3–18 months by Amazon; 18 months by Google. Can reveal household routines, arguments, health conditions |
| **Device usage patterns** | Moderate–high | Reveals occupancy, sleep schedules, which rooms are used when. Amazon may retain aggregated data even after deletion |
| **Access credentials (PINs, IC cards)** | High | Plaintext transmission of unlock commands found in multiple lock models; cloned IC cards successful in 12 of 19 tested products |

**The regulatory gap:** EU AI Act explicitly covers smart home assistants and biometric readers, prohibiting real-time biometric categorization using sensitive characteristics. But enforcement begins gradually, and the Act’s high-risk classification for biometric profiling does not automatically translate into device-level technical controls. CEN/TR 18241:2025 provides privacy-by-design recommendations for biometric access control, but it is a technical report, not a binding standard.

---

## ☁️ What Happens When a Cloud Service Shuts Down or Ownership Changes

Three recent cases illustrate the pattern:

**Neato Robotics (2023–2025):** Vorwerk shut down Neato in 2023 and promised cloud support for “at least five years.” By late 2025, it announced cloud services would end, citing “cybersecurity standards, compliance obligations, and regulations” that made legacy systems unsustainable. Devices remain manually operable via a button but lose scheduling, remote start, and no-go zones.

**Belkin Wemo (2026):** Belkin shut down the Wemo app and servers on January 31, 2026, rendering most of the range uncontrollable through the app or third-party services. Refunds were offered for devices under warranty, but out-of-warranty devices became e-waste.

**Google Nest (2025):** Google retired first- and second-generation Nest Learning Thermostats on October 25, 2025, ending software updates and security patches entirely. Devices remain functional as manual thermostats but lose smart features and become a security liability if they still connect to the internet.

**The structural problem:** There is no legal requirement for a manufacturer to provide a local control fallback when a cloud service shuts down. The UK PSTI regime requires disclosure of support periods, but not post-support functionality. A Trusted Reviews analysis argued that “smart devices should have a default local control mode so that, in the event of a shutdown, the device does not become useless”. Matter’s local control model could provide this—if manufacturers implement it and users retain a Matter controller independent of the cloud.

---

## 🤖 Prompt Injection, Unauthorized Actions, Biometric Misuse, and Surveillance

**Prompt injection** has moved from theoretical to demonstrated physical consequences. Researchers showed that **Google Calendar invites could hijack Gemini AI** to control lights, shutters, and boilers—the first documented indirect prompt injection attack with physical-world effects. A separate vulnerability allowed attackers to trigger smart home actions via **messaging notifications**, including controlling Google Home devices.

IEEE research on LLM-enabled home assistants recommends a **layered architecture** separating intent interpretation from authorization enforcement: pre-LLM policy enforcement, context sanitization, and post-LLM action gating. Early findings show this “largely diminishes potential risks” but was tested only on four attack scenarios and one local LLM backend.

**Unauthorized actions** remain possible because AI assistants often lack a hard boundary between “interpret intent” and “execute action.” A safe design requires that the AI cannot directly actuate a device; it can only propose an action that a separate authorization layer evaluates against household policy.

**Biometric misuse** is both a privacy and a security problem. Consumer tests found **printed photos could unlock smart locks** using 2D infrared scanning without liveness detection. Eufy’s FamiLock line processes biometrics on-device and avoids cloud training, which is a more private approach, but the industry norm still varies widely.

**Surveillance risks** are amplified by AI camera summaries. As established earlier, false positives—ghost sightings, misidentified animals—erode trust and could trigger inappropriate automations if summaries are used as triggers. The privacy risk is compounded when footage is analyzed in the cloud: Google’s Home Brief feature and similar services transmit video for AI processing unless explicitly configured otherwise.

---

## 🏷️ Labels, Certifications, and Regulations: What Provides Meaningful Assurance

| Label / Regulation | Scope | Meaningful Assurance? | Limitation |
|---|---|---|---|
| **ioXt Alliance** | Smart home, mobile, routers, cameras | Yes—maps to NIST IR 8259 and covers lifecycle security | Voluntary; adoption concentrated among larger manufacturers like Midea |
| **NIST IR 8259** | Foundational IoT cybersecurity | Yes—defines manufacturer activities for post-market support | Guidance, not regulation; no enforcement mechanism |
| **EU Cyber Resilience Act** | All products with digital elements | Strong—mandatory reporting, 5-year support floor, 10-year update availability | Full application December 2027; enforcement mechanisms still developing |
| **UK PSTI Act** | Consumer connectable products | Moderate—requires disclosure of support period and ban on universal default passwords | Does not mandate a minimum support length; manufacturers self-declare |
| **California SB-327** | Connected devices sold in California | Weak—requires “reasonable security feature” | Interpreted narrowly; no support period requirement |
| **EU AI Act** | AI systems including smart home assistants | Potentially strong—prohibits real-time biometric categorization | Phased enforcement; compliance burden on manufacturers, not verifiable by consumers |
| **Matter certification** | Device interoperability and security | Moderate—ensures secure commissioning and attestation | Does not guarantee ecosystem compatibility or update delivery |
| **Vendor VDPs (e.g., Eufy, SimpliSafe)** | Vulnerability reporting | Variable—Eufy commits to fix critical issues in 3 business days; SimpliSafe runs a bug bounty | Enforcement is voluntary; response times not audited |

**The assurance gap:** A device can be ioXt-certified, Matter-certified, PSTI-compliant, and still fail a household because:
- Its cloud shuts down without a local fallback
- Its AI assistant is prompt-injected through a calendar invite
- Its biometric sensor accepts a photo
- Its update mechanism is automatic but the manufacturer stops pushing updates after the support period

Certifications assure **design-time** properties. They do not assure **operational** resilience over a device’s expected life.

---

## ✅ Lifecycle Control Checklist for Households

**Procurement:**
- [ ] Check the published support period (PSTI statement, CRA disclosure, or vendor page). If none exists, assume no guaranteed support.
- [ ] Prefer devices with **local control** (Matter, Zigbee, Z-Wave) over cloud-only devices.
- [ ] For locks and cameras, verify **liveness detection** (3D structured light, binocular infrared) and **on-device biometric processing**.
- [ ] Confirm the device supports **automatic security updates** and has a **vulnerability disclosure policy**.

**Commissioning:**
- [ ] Use Matter’s PASE commissioning; do not leave Bluetooth open after setup.
- [ ] Change all default passwords; enable MFA on the hub or controller account.
- [ ] Segment IoT devices on a separate VLAN or guest network if the router supports it.
- [ ] For locks: enable combined verification (PIN + fingerprint, or password + card).

**Operation:**
- [ ] Verify that camera footage is **end-to-end encrypted** and that AI analysis happens on-device or with explicit opt-in for cloud processing.
- [ ] Set voice recording retention to the shortest available period (3 months, not 18 months).
- [ ] Disable AI features that create prompt injection surfaces (calendar summarization, message summarization) if not actively needed.
- [ ] Monitor for firmware updates; do not defer critical security patches.

**End-of-life:**
- [ ] Before a cloud shutdown, verify whether the device retains local control.
- [ ] If not, plan for replacement before the shutdown date.
- [ ] Factory-reset devices before disposal to remove credentials and biometric templates.

---

## 🚨 Interoperability and Lifecycle Risk Assessment

**High Risk:**
- **Cloud shutdown without local fallback.** Neato, Wemo, and Nest demonstrate that vendors can and will end cloud support earlier than promised or without a migration path.
- **Prompt injection in AI assistants.** Demonstrated physical-world consequences via calendar invites and messaging notifications. No consumer product currently ships with robust layered enforcement.
- **Biometric spoofing.** Printed photos unlock some smart locks. The industry has no mandatory liveness standard for consumer biometric access.
- **Support period disclosure gaps.** Many devices have no published support period, making informed purchasing impossible.

**Medium Risk:**
- **Update delivery reliability.** Matter OTA has limited recovery; non-Matter devices may rely on manual updates that users ignore.
- **MFA inconsistency.** Locks and security devices often lack mandatory secondary verification.
- **Data retention opacity.** Amazon and Google retain voice data for months; users rarely change default settings.

**Low Risk:**
- **Matter secure commissioning.** PASE and device attestation are robust and mandatory for certified devices.
- **E2E encrypted camera video (Apple HomeKit).** Strong privacy architecture where implemented.
- **ioXt and NIST-aligned design practices.** Meaningful for manufacturers who adopt them voluntarily.

---

## 🛠️ Product-Design Implications

1. **Design for graceful degradation, not just graceful failure.** Every cloud-dependent feature should have a documented local fallback. If the cloud shuts down, locks should still lock, cameras should still record locally, and thermostats should still control temperature.

2. **Treat AI as an untrusted input source.** The AI should never directly actuate devices. It should propose actions to an authorization layer that enforces household policy—device risk tier, user identity, time of day, and occupancy.

3. **Make biometric liveness mandatory, not optional.** 2D infrared scanning is insufficient. Require 3D structured light or equivalent liveness detection for any biometric access control product. Process biometrics on-device; never send templates to the cloud.

4. **Publish support periods as contractual commitments.** A support period is not a marketing claim. It should be stated in the product documentation, reflected in the firmware update mechanism, and honored through the end of the period—including the 10-year update availability required by the CRA.

5. **Design for migration and interoperability.** Matter multi-admin allows devices to join multiple fabrics, but routines and permissions are not portable. Provide structured export of automation logic and user permissions so households can migrate without rebuilding.

6. **Audit AI surfaces for prompt injection.** Calendar, email, messaging, and notification integrations are injection vectors. Sanitize context, tag roles, and gate actions. Do not assume the LLM will refuse unsafe commands—research shows it can be jailbroken.

7. **Give households an exit plan.** When a cloud service ends, provide a local control mode, a data export, and a firmware update that removes cloud dependency. The default should be a device that remains useful, not one that becomes e-waste.

The minimum trustworthy lifecycle is not defined by any single certification or regulation. It is defined by whether a household can **trust a device to work, stay secure, and remain under local control** across its expected life—and whether the manufacturer has a credible plan for what happens when the cloud goes away. On the current evidence, very few products meet that standard.

[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nist.gov

| **Information Dissemination**: The ability for the manufacturer and/or supporting entity to broadcast and distribute (e

such as: <br> a. ... The procedures to support the ability for the manufacturer and/or supporting entity to notify customers of cybersecurity-related events and information related to an IoT product throughout the support lifecycle, such as ... Potential Additional IoT Product Criteria Developed from NISTIR 8259A Using Informative References**



](https://www.nist.gov/system/files/documents/2021/10/29/34-ENISA%20MCS%20resp%20NIST%20IoT%20White%20Paper%20-%2017.10.2021fin.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nvlpubs.nist.gov

within documents to support best practices

examining the maintenance outlook on devices after end of life requirements, and examining how privacy ... NIST heard that effective risk management in the IoT ecosystem requires a balanced approach that aligns industry needs with government capabilities; that utilizing robust frameworks ... that addressing the lifecycle of products and evolving cybersecurity responsibilities among all stakeholders are crucial elements...



](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8562.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nvlpubs.nist.gov

4.Manufacturer Activities Impacting the IoT Product Post-Market Phase

On-Going Support of Product Cybersecurity throughout the Lifecycle and through End-of-Life ... Non-technical cybersecurity capabilities (e.g., Information and Query Reception and Information Dissemination documented in NIST IR 8259B [11]) are critical to facilitating post-market cybersecurity support.



](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8259r1.pdf#8#6)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nvlpubs.nist.gov

<table><tr><td>Recurso de Suporte Não Técnico</td><td>Ações Comuns</td><td>Rationale</td><td>Exemplos de Referência IoT</td></tr...

(Instituto Nacional de Padrões e Tecnologia, Gaithersburg, MD), Relatório Interno ou Interinstitucional (IR) 8259 do NIST. https://doi.org/10.6028/NIST.IR.8259



](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8259B.por.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/nist.rip)

csrc.nist.rip

On- going security of IoT products through the post- market phase will often require actions by customers, manufacturers, and ot...

On- going security of IoT products through the post- market phase will often require actions by customers, manufacturers ... Non-technical cybersecurity capabilities (e.g., Information and Query Reception and Information Dissemination documented in NIST IR 8259B [11]) are critical to facilitating post-market cybersecurity support.



](https://csrc.nist.rip/external/nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8259r1.2pd.pdf#7#6)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

Wind-Driven House Fire, Texas, 2009

2025/05/12

Workshop Summary Report for "Workshop on Foundational Cybersecurity Activities for IoT Device Manufacturers"

2025 "Workshop on Foundational ... by the NIST Cybersecurity for the Internet of Things (IoT) program. ... the purpose of this more recent workshop was to discuss planned updates to NIST IR 8259 and gather additional feedback on taking a product viewpoint with greater emphasis on the IoT product lifecycle...



](https://www-dev.ct.nist.gov/publications/workshop-summary-report-workshop-foundational-cybersecurity-activities-iot-device)[

ioXt

2026/07/20

ioXt Highlights Lifecycle Security as NIST Updates Foundational IoT Cybersecurity Guidance — ioXt

ioXt Highlights Lifecycle Security as NIST Updates Foundational IoT Cybersecurity Guidance ... is highlighting the importance of lifecycle-based cybersecurity following the release of NIST IR 8259r1, Foundational Cybersecurity Activities for IoT Product Manufacturers. ... IoT cybersecurity should not begin at the testing stage, and it should not end when a product ships.



](https://ioxt.com/news-events-blog/ioxt-highlights-lifecycle-security-as-nist-updates-foundational-iot-cybersecurity-guidance)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

National Institute of Standards and Technology (.gov)

2025/11/24

Trusted Internet of Things (IoT) Device Network-Layer Onboarding and Lifecycle Management NIST SP 1800-36 Practice Guide Final

Practice Guide # Trusted Internet of Things (IoT) Device Network-Layer Onboarding and Lifecycle Management NIST SP 1800-36 Practice Guide Final ## Files NIST SP 1800-36A ... Architecture, and Security Characteristics (Final)Document Version NIST SP 1800-36B: Approach ... Complete Guide PDF (Final)Web Version NIST SP 1800-36...



](https://www.nccoe.nist.gov/publications/practice-guide/trusted-internet-things-iot-device-network-layer-onboarding-and)[

![](https://cdn.deepseek.com/site-icons/secrss.com)

安全内参

2026/05/08

美国NIST《物联网产品制造商基础网络安全活动》解读 - 美国NIST《物联网产品制造商基础网络安全活动》解读

该指南反映出NIST正推动物联网安全从单点防护转向全生命周期风险管理，有助于减少客户后续安全投入并降低安全事件影响。 2026年4月20日，美国国家标准与技术研究院（NIST）发布了修订版指南文件NIST IR 8259r1《物联网产品制造商基础网络安全活动》（Foundational Cybersecurity Activities for IoT Product Manufacturers）



](https://www.secrss.com/index.php/articles/90142#1)[

![](https://cdn.deepseek.com/site-icons/squirepattonboggs.com)

squirepattonboggs.com

The Top Ten (Internet of) Things to Consider

1. **Design for security** – Laws, regulations and regulator expectations mandate implementing appropriate security into connected devices. The Federal Trade Commission (FTC) in particular emphasizes the need to implement security in the design process rather than an as afterthought, and California now specifically requires it.



](https://www.squirepattonboggs.com/-/media/files/insights/publications/2022/04/the-top-ten-internet-of-things-to-consider/top_ten_things_consider.pdf?rev=463b88c524294161b4baf0534f02a56c&hash=50A28CFCC5A5D65A903018141F20BA2A#1#1)[

prinzlawoffice.com

```

These FTC imposed requirements include the following: Specifying in writing how functionality and features secure the devices; Engaging in threat modeling to identify potential security risks; Reviewing every planned release of code with automated static analysis tools; Performing pre-release vulnerability testing on each



](https://prinzlawoffice.com/tag/security/?print=pdf-search#1#1)[

![](https://cdn.deepseek.com/site-icons/ftc.gov)

Federal Trade Commission (.gov)

2020/09/25

Careful Connections: Keeping the Internet of Things Secure

To make sure your IoT company is taking reasonable steps to protect your customers’ devices from hackers, thieves, and other bad actors, consider these recommendations from the FTC. ... you may be covered by the FTC Act, the FTC’s Health Breach Notification Rule...



](https://www.ftc.gov/business-guidance/resources/careful-connections-keeping-internet-things-secure?source=post_page-----bb860890cd12---------------------------------------)[

bakerlaw.com

\(^{38}\) Obligations of Online and Mobile Services to Protect Children’s Privacy, available at https://www

FTC guidance for the IoT industry The FTC has given the IoT industry specific guidance on what it thinks would constitute reasonable privacy and security protections for IoT devices. ... - Build privacy and security into devices and software at the outset and continuously look for and cure deficiencies. - Provide a higher level of security for sensitive data.



](https://www.bakerlaw.com/webfiles/IP/2017/Articles/11-29-2017-Friel-Massachi-Marketing-Law-Conf.PDF#3#3)[

![](https://cdn.deepseek.com/site-icons/loeb.com)

loeb.com

Advanced Media and Technology Law

the FTC pointed out that it has already issued guidance to Internet of Things companies on how to preserve privacy and security in their products while still innovating and growing IoT technology. ... The agency just announced that it is inviting the public to create an innovative tool that will help protect consumers from security vulnerabilities in the software of home devices connected to the Internet of Things.



](https://www.loeb.com/-/media/files/publications/2017/01/ftcfocusesoninternetofthings.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/nelsonmullins.com)

nelsonmullins.com

gain easy, unauthorized access to consumers’ files and router login credentials

the FTC issued Consent Orders to both TREND and ASUS listing the steps ... **IV.** **EMERGING IoT RECOMMENDATIONS** Below is a compilation of recommendations from various sources identified in this article, including from governmental agencies, industry, legal commentary and the two recent FTC Consent Orders. ... For purposes of the list, the following definitions apply, modified from the FTC Consent



](https://www.nelsonmullins.com/storage/a58a6292f21ab017548f6095f311fb5e.pdf#4#3)[

![](https://cdn.deepseek.com/site-icons/natlawreview.com)

dev.natlawreview.com

Privacy Tip #219 - Holiday Shopping Tip for Internet-Connected Gifts

Review and follow the Department of Homeland Security's "Securing the Internet of Things" advisory notice. The FTC also issued a consumer alert this week, "What to ask before buying internet- connected toys," urging consumers to understand the smart toy's feature before purchasing it.



](https://dev.natlawreview.com/node/119729/printable/pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/ftc.gov)

Federal Trade Commission (.gov)

2015/01/26

FTC Report on Internet of Things Urges Companies to Adopt Best Practices to Address Consumer Privacy and Security Risks

build security into devices at the outset, rather than as an afterthought in the design process; - train employees about the importance of security, and ensure that security is managed at an appropriate level in the organization ... - monitor connected devices throughout their expected life cycle, and where feasible, provide security patches to cover known risks.



](https://www.ftc.gov/news-events/news/press-releases/2015/01/ftc-report-internet-things-urges-companies-adopt-best-practices-address-consumer-privacy-security?app_v2=true%2525252525252525252F%252525252525252F%2525252525252F%2525252525252F)[

![](https://cdn.deepseek.com/site-icons/insidecybersecurity.com)

insidecybersecurity.com

Footnote 30: Fed

last year the FTC held its _IoT Home Inspector Challenge_ ... the Commission launched its _Start with Security_ initiative,36 _Stick with Security_ blog series,37 and "_Careful Connections_" IoT guidance ... The FTC has provided IoT manufacturers with a host of guidance on how to predict and mitigate against privacy, security, and safety hazards.



](https://insidecybersecurity.com/sites/insidecybersecurity.com/files/documents/2018/jun/cs2018_0263.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/natlawreview.com)

natlawreview.com

Published on The National Law Review https://natlawreview

Published on The National Law Review https://natlawreview.com # FTC Issues Report and Privacy Best Practices for the Internet of Things Article By: Privacy and Data Security On January 27, 2015 th



](https://natlawreview.com/node/41954/printable/pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/lewissilkin.com)

Lewis Silkin

2026/07/30

EU Cyber Resilience Act guidance now out: here's what you need to know

Length of support periods The five-year minimum support period is a floor (and not a default), "unless the product with digital elements is expected to be in use for less than five years, in which case the support period shall correspond to the expected use time."



](https://www.lewissilkin.com/insights/2026/07/31/eu-cyber-resilience-act-guidance-now-out-heres-what-you-need-to-know-102nfex#1)[

![](https://cdn.deepseek.com/site-icons/bund.de)

Bundesamt für Sicherheit in der Informationstechnik

2024/10/09

CRA verabschiedet – BSI sieht Cybersicherheit signifikant gestärkt

Ab November 2027 müssen Produkte mit digitalen Elementen die im CRA enthaltenen grundlegenden Cybersicherheitsanforderungen erfüllen, um in der EU verkauft werden zu dürfen. ... Den im CRA verankerten Grundsatz, den geforderten Supportzeitraum für ein digitales Produkt an dessen individuelle Lebensdauer zu koppeln, unterstützt das BSI.



](https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2024/241010_CRA.html)[

![](https://cdn.deepseek.com/site-icons/revera.legal)

REVERA Belarus

2026/08/12

EU Cyber Resilience Act (CRA): Key Requirements and Business Impact — REVERA - EU Council and European Parliament reach agreement on Digital Product Cybersecurity Act

smart home assistants ... - Security support shall be provided for at least 5 years (except for products which are expected to be in use for a shorter period of time). - Any security updates that occur during the product lifecycle must remain available to users for 10 years or the remaining support period (whichever is longer).



](https://belarus.revera.legal/en/news-and-analytical-materials/sovet-es-i-evroparlament-dostigli-soglasheniya-po-zakonu-o-kiberbezopasnosti-cifrovyx-produktov/#an%d1%81hor-title-1#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2025/08/12

Regulating smart device support periods | Proceedings of the 34th USENIX Conference on Security Symposium - Several features on this page require Premium Access

The upcoming European Cyber Resilience Act (CRA) addresses this by requiring manufacturers to support their products for the expected use time, which should be based on reasonable user expectations. In this work ... We find that respondents' smart device use times and lifetime expectations exceed the CRA's baseline of five years for a majority of device categories and



](https://dl.acm.org/doi/abs/10.5555/3766078.3766343#1)[

![](https://cdn.deepseek.com/site-icons/hunton.com)

Hunton Andrews Kurth LLP

2024/10/16

Council of the European Union Adopts the Cyber Resilience Act - Council of the European Union Adopts the Cyber Resilience Act

Support: Manufacturers must provide ongoing support and provide security updates for a period of at least five years. The end date of the support period should be clearly communicated to users. The security updates made available during the support period must remain available for download for at least 10 years.



](https://www.hunton.com/privacy-and-cybersecurity-law-blog/council-of-the-european-union-adopts-the-cyber-resilience-act#1)[

![](https://cdn.deepseek.com/site-icons/lexology.com)

Lexology

2026/07/30

EU Cyber Resilience Act guidance now out: here's what you need to know - Register now for your free, tailored, daily legal newsfeed service.

length of support periods; and ... The five-year minimum support period is a floor (and not a default), "unless the product with digital elements is expected to be in use for less than five years, in which case the support period shall correspond to the expected use time."



](https://www.lexology.com/library/detail.aspx?g=45f16dc7-b3e3-4d6a-8a3d-58e627e367b4#1)[

![](https://cdn.deepseek.com/site-icons/forkast.news)

Forkast News

2026/09/08

The CRA Deadline Is Thursday. Smart Home AI Companies Are Flying Blind on Agent Compliance.

The EU Cyber Resilience Act starts requiring vulnerability reporting Thursday. ... That is when the EU Cyber Resilience Act starts requiring smart home companies to report actively exploited vulnerabilities and severe incidents to a brand-new regulatory platform. The timelines are unforgiving ... Security updates must be free. The minimum support period is five years. ## The Agent Gap



](https://forkast.news/the-cra-deadline-is-thursday-smart-home-ai-companies-are-flying-blind-on-agent-compliance-2/)[

secure4sme.eu

<table><tr><td>Canale</td><td>Tempo di risposta</td><td>Vulnerabilità segnalate</td><td>Prove</td><td>Stato</td></tr><tr><td>sec...

Gli aggiornamenti devono essere forniti gratuitamente per un periodo di assistenza definito (ad esempio, almeno 5 anni per i dispositivi IoT o per tutta la durata di vita del prodotto). ... tale periodo non può essere inferiore a 5 anni...



](https://www.secure4sme.eu/document/open?id=60#5#4)[

![](https://cdn.deepseek.com/site-icons/lexology.com)

Lexology

2026/03/21

2026 Cybersecurity Countdown: New requirements are coming - Register now for your free, tailored, daily legal newsfeed service.

European Union March 22 2026 March 2026 - The Cyber Resilience Act (Regulation EU 2024/2847 - CRA) entered into force on 10 December 2024 and introduces a comprehensive cybersecurity framework for pr



](https://www.lexology.com/library/detail.aspx?g=a3f0a1ee-ff18-4889-95ad-47cdcd9e39dd#1)[

![](https://cdn.deepseek.com/site-icons/intertek.com.cn)

Intertek 中国

2025/10/20

Intertek

# 一文读懂 | 欧盟《网络弹性法案》（CRA） 2025-10-21 阅读版式 2024年10月10日，欧盟通过了《网络弹性法案》（CRA），以加强联网设备的网络安全。该法案已于2024年11月正式发布，为在欧盟境内生产、进口或销售的数字产品制定了强制性安全要求，确保硬件和软件产品在上市时具有更少的漏洞，并要求制造商在整个产品生命周期内严肃对待安全问题。 一、 欧盟网络弹性法案要点： -



](https://www.intertek.com.cn/listdata/1980473566973399040.html)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic Developer Academy

2026/02/23

Matter security model - Nordic Developer Academy

Matter security model Matter includes a mandatory, built‑in security model designed to ensure that devices can trust each other and communicate securely from the very beginning of the commissioning process. ... Commissioning establishes a secure communication channel, verifies the device’s identity, and assigns operational ... Passcode‑Authenticated Session Establishment (PASE) and device attestation.



](https://academy.nordicsemi.com/courses/matter-fundamentals/lessons/lesson-1-matter-introduction/topic/matter-security-model/?version=v3.4.0)[

![](https://cdn.deepseek.com/site-icons/tta.or.kr)

::: TTA표준화 위원회 :::

::: TTA표준화 위원회 :::

한글 내용요약 | 매터 기기는 커미셔닝 과정에서 키 교환, 자격 증명, 보안 세션 수립 과정을 거쳐 암호화 통신을 제공한다. 이 기술보고서는 매터에서 활용하는 보안 기술을 해설하고...



](https://committee.tta.or.kr/data/standard_view.jsp?thirdDepthCode=null&order=t.publish_date&secondDepthCode=PG1002&by=desc&firstDepthCode=TC010&pk_num=TTAR-10.0201&commit_code=PG1002)[

tink | Smart Home Expert

2026/01/24

Is Matter veilig? Alles over privacy en encryptie - tink Blog NL

De Veilige Handdruk (Commissioning) Het moment waarop de meeste fouten worden gemaakt, is tijdens de installatie (bijv. bluetooth open laten staan). Matter gebruikt hiervoor een strikt proces genaamd PASE (Password Authenticated Session Establishment). Wanneer jij de QR-code op je nieuwe apparaat scant, gebeurt er op de achtergrond een razendsnelle, versleutelde uitwisseling. ... - De Hub controleert het Digitale Paspoort van het apparaat. - Als alles klopt, geven ze elkaar een “veilige handdruk” en krijgt het apparaat een nieuw...



](https://www.tink.nl/blog/privacy-voorop-waarom-je-smart-home-met-matter-veiliger-is-dan-ooit/)[

![](https://cdn.deepseek.com/site-icons/einfochips.com)

eInfochips

2025/09/04

Matter Commissioning Flow Explained - Building a Smarter Home: An In-Depth Look at Matter Commissioning

An In-Depth Look at Matter Commissioning ... Commissioning in Matter is the process of securely adding a device (called the commissionee) to a home network (Fabric) via a commissioner (like your smartphone or hub). ... Matter Commissioning Flow (Step-by-Step)



](https://www.einfochips.com/blog/building-a-smarter-home-an-in-depth-look-at-matter-commissioning/#1)[

![](https://cdn.deepseek.com/site-icons/npmjs.com)

NPM

2026/05/26

@minguyen68/node-red-contrib-matter

Commission and control any Matter device — smart locks, lights, sensors — directly from Node-RED flows over IP or Thread. ... - Commission any Matter device into your own fabric (multi-admin alongside Apple Home, Google Home, etc.) ... Commission a Matter device into the Node-RED controller fabric. After successful commissioning the device is automatically registered in the device registry ... Apple Home → device → ⚙️ → Turn on Pairing Mode



](https://www.npmjs.com/package/@minguyen68/node-red-contrib-matter?activeTab=code#1)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

docs.silabs.com

Communication between Matter devices is protected with different keys in different stages

At the commissioning stage, the key is a result of the Password Authenticated Session Establishment (PASE) process over the commissioning channel ... There are four steps involved in commissioning devices to start communicating on a Matter network: 1. Device Discovery 2. Secure Channel (PASE) 3. Device Attestation



](https://docs.silabs.com/matter/2.3.0/assets/matter.pdf#38#6)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

docs.silabs.com

Matter Security

Matter raises the bar ... 1. No anonymous joining: Always requires "proof of ownership" (that is, a device-specific passcode). 2. Device Attestation ... When commissioned onto a Matter network, every device ... There are four steps involved in commissioning devices to start communicating on a Matter network ... 2. Secure Channel (PASE)



](https://docs.silabs.com/d/matter-fundamentals-security/2.7.0/assets/matter-fundamentals-security.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

the IPv6 hop count

The Device Attestation Certificate is used during the commissioning process by the Commissioner to ensure that only trustworthy devices are admit- ted into a Fabric. ... A NOC is issued during the commissioning process ... Device Commissioning ... This secret is used by Passcode-Authenticated Session Establishment (PASE) to establish a secure commissioning session.



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#7)[

nuki.io

Matter security concept

the device certificate is crucial. - When starting Matter activation in the app, the Smart Lock enters "Commissioning Mode," making it visible to smartphones and Smart Home Hubs. - The Matter Controller initiates the PASE process (Password Authenticated Session Establishment), in which the controller and device establish a secure connection using a password.



](https://support.nuki.io/hc/en-us/articles/19910764139409-Matter-security-concept)[

![](https://cdn.deepseek.com/site-icons/alibabacloud.com)

Alibaba Cloud

2026/03/12

PCA FAQ - Alibaba Cloud - Search for Help Content

smart home devices must pass Matter's device authentication checks before they can join a Matter smart home network ... A Node Operational Certificate (NOC) is issued by a Matter administrator during commissioning to authenticate the identity of other devices and ensure the privacy and integrity of data communication.



](https://www.alibabacloud.com/help/en/ssl-certificate/pca-faq#1)[

![](https://cdn.deepseek.com/site-icons/engadget.com)

Engadget

2025/10/24

Shuttered robot vacuum maker Neato is ending cloud services sooner than planned

The company said in 2023 that cloud services would stay running for at least five years. ... Neato Robotics, which shut down in 2023 due to declining sales, has notified customers that "cloud services are being phased out during Q4 2025," according to an email obtained by The Verge.



](https://www.engadget.com/shuttered-robot-vacuum-maker-neato-is-ending-cloud-services-sooner-than-planned-171604823.html)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/07/10

Belkin is unceremoniously killing most of its Wemo smart home devices - Advertisement

On January 31, 2026 (about six months from now), the Wemo app and its related servers will go offline. ... According to Belkin, it will issue refunds at that time for any devices still under warranty. However...



](https://tech.yahoo.com/home/articles/belkin-unceremoniously-killing-most-wemo-162523585.html#1)[

![](https://cdn.deepseek.com/site-icons/gizmodo.com)

Gizmodo

2025/10/24

Neato Robot Vacuums Return to Dumb Mode After Company Cuts Cloud Services - Skip to content

“Since Neato ceased operations in 2023, Vorwerk has continued maintaining the ... Earlier this year, Google announced that it would drop support for the earliest generations of its Nest smart thermostat, cutting off cloud support and rendering it a standard, manually-operated one. Belkin...



](https://gizmodo.com/neato-robot-vacuums-return-to-dumb-mode-after-company-cuts-cloud-services-2000676827?utm_source=flipboard&utm_content=Gizmodo%2Fmagazine%2FTech#1)[

heise online

2025/10/08

Vorwerk subsidiary Neato shuts down cloud server, hoovers lose functions - zurück zum Artikel

Neato Robotics was closed by Vorwerk in 2023, but the cloud functions were to remain available for another five years. ... According to Neato, cybersecurity requirements and other rules have been greatly expanded since 2023, which is why the cloud infrastructure can no longer be provided.



](https://www.heise.de/en/news/Vorwerk-subsidiary-Neato-shuts-down-cloud-server-hoovers-lose-functions-10748987.html?view=print#1)[

Pilot Protocol

2026/06/18

Smart Home Without Cloud: Local Device Communication

In January 2026, Belkin shut down the Wemo cloud service. Overnight ... Google shut down its Cloud IoT Core service in August 2023, forcing every industrial and consumer IoT project built on it to find a new backend within 12 months.



](https://pilotprotocol.network/blog/smart-home-without-cloud-local-device-communication)[

![](https://cdn.deepseek.com/site-icons/trustedreviews.com)

Trusted Reviews

2026/01/30

The Belkin WeMo shutdown shows the dangers of smart hardware and why there needs to be better exit planning - Advertisement

But with the cloud service shutting down, the bulk of the range will become useless. According to WeMo’s official statement, a long list of products will no longer be controllable through the Wemo app or third-party services as of today, 31 January 2026, when support will also end. ... Smart devices should have a default local control mode so that, in the event of a shutdown...



](https://www.trustedreviews.com/opinion/belkin-wemo-shutdown-shows-dangers-of-smart-hardware-why-there-needs-better-exit-planning#1)[

![](https://cdn.deepseek.com/site-icons/impress.co.jp)

INTERNET Watch

2025/10/26

ロボット掃除機の事業終了も最低5年はクラウドでの動作を保証→わずか2年で打ち切り決定で波紋【やじうまWatch】

しかし2年目を迎えた今月になって、「サイバーセキュリティの基準、コンプライアンス義務などの進化により、既存のクラウドインフラを信頼性と将来性を備えた形で維持することはもはや不可能になった」として、クラウドサービスの段階的廃止を宣言。



](https://internet.watch.impress.co.jp/docs/yajiuma/2058084.html)[

heise online

2025/05/25

Bosch deals the death blow to spexor devices - zurück zum Artikel

Bosch will shut down the spexor servers on July 1, 2025. ... Bosch will “irrevocably” delete all data as of July 1 ... It may be possible to find a way to integrate spexor into your smart home environment – even without the Bosch cloud servers.



](https://www.heise.de/en/news/Bosch-deals-the-death-blow-to-spexor-devices-10396313.html?view=print#1)[

![](https://cdn.deepseek.com/site-icons/macitynet.it)

macitynet.it

2025/10/26

Neato, con lo stop dei server i robot aspirapolvere non sono più smart

Il recente annuncio sulla chiusura anticipata dei server cloud Neato dimostra ... la casa smart privi di compatibilità con standard aperti come Matter. Nel caso specifico, la società che aveva promesso di mantenere attivo il servizio MyNeato fino al 2028 ha cambiato rotta e lo fermerà a fine anno. Di conseguenza...



](https://www.macitynet.it/neato-chiusura-cloud/)[

![](https://cdn.deepseek.com/site-icons/arcpublishing.com)

The Irish Times

2026/01/28

Smart home becomes a harder sell when device makers arbitrarily pull the plug - Smart home becomes a harder sell when device makers arbitrarily pull the plug

It’s not because they have broken or stopped working correctly, but because Belkin has pulled the shutters down on many of its smart home devices, ending cloud support for the products. There is a reprieve for those devices that work with Apple’s HomeKit, and therefore do not need Belkin’s cloud services...



](https://irishtimes-irishtimes-prod.cdn.arcpublishing.com/technology/2026/01/29/smart-home-becomes-a-harder-sell-when-device-makers-arbitrarily-pull-the-plug/#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/08/23

Evaluating Prompt Injection Risk and Guardrails in LLM-Enabled Home IoT Assistants - Evaluating Prompt Injection Risk and Guardrails in LLM-Enabled Home IoT Assistants

Evaluating Prompt Injection Risk and Guardrails in LLM-Enabled Home IoT Assistants ## Abstract: Smart home virtual assistants are increasingly powered by large language models to enable information retrieval and home device actuation. As a result ... exposed to untrusted inputs, increasing their susceptibility to prompt injection, role confusion, and indirect prompt injection through retrieved context.



](https://ieeexplore.ieee.org/document/11655283#1)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

CNET

2026/07/10

The Biggest New Threat to Smart Homes Is AI Promptware. My Tips Help Stop It - CNET

Always keep your devices updated, especially in the age of AI ... Don’t accept or open any messages from unknown sources ... Don’t ask AI to summarize anything you don’t already know well and trust ... Disable AI in your email, calendars, chat apps and other places you can get messages



](https://www.cnet.com/home/security/promptware-threatens-to-take-over-ai-and-smart-homes-heres-how-to-protect-yourself/?utm_source=flipboard&utm_content=cnet%2Fmagazine%2FAI%20Atlas#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/11

Your Calendar Might Be the Most Dangerous Thing in Your Smart Home - Advertisement

Your Calendar Might Be the Most Dangerous Thing in Your Smart Home ... a prime attack surface for AI-powered smart homes. ... into Google Calendar invite ... 14 different indirect prompt injection attacks across web, mobile, and Google Assistant platforms. The researchers believe this is the first documented instance of a prompt injection attack producing direct, physical-world consequences—toggling lights...



](https://tech.yahoo.com/cybersecurity/articles/calendar-might-most-dangerous-thing-102147780.html#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/08/09

Ai SecureDataGuard: A Big Data Security, Privacy-Preserving and Visualization System for LLM-Powered Smart Homes

Now large language models and that multi-agent frameworks are widely used, platforms like MOSS can let users talk to smart homes naturally and link up all kinds of househ...Show More ... intentional prompt injection and safety guardrail evasion attacks ... I made a two-step intent recognition algorithm to block prompt injection and jailbreak attempts. Second...



](https://ieeexplore.ieee.org/document/11635380#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

export.arxiv.org

PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents

Smart- home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. This raises a safety question specific to the home: can the agent tell a genuine user command from ambient or externally- sourced content, television speech, on- screen text, or an overheard conversation...



](https://export.arxiv.org/pdf/2608.05495#3#1)[

![](https://cdn.deepseek.com/site-icons/forkast.news)

Forkast News

2026/09/11

Your Calendar Might Be the Most Dangerous Thing in Your Smart Home

Your Calendar Might Be the Most Dangerous Thing in Your Smart Home Researchers demonstrated that Google Calendar invites can hijack Gemini AI to control lights, shutters, and boilers—the first documented prompt injection attack with physical-world consequences. ... 14 different indirect prompt injection attacks across web, mobile, and Google Assistant platforms.



](https://forkast.news/your-calendar-might-be-the-most-dangerous-thing-in-your-smart-home/)[

![](https://cdn.deepseek.com/site-icons/securityweek.com)

SecurityWeek

2026/06/03

Gemini Voice Assistant Hijacked via Messaging Notifications

Attackers could have triggered dangerous actions, including controlling smart home devices via Google Home and starting Zoom video calls. ... This method enabled attackers to trigger dangerous actions, including controlling smart home devices via Google Home, starting Zoom video calls, crafting deceptive messages that appear to come from trusted contacts...



](https://www.securityweek.com/gemini-voice-assistant-hijacked-via-messaging-notifications/#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/07/10

The Biggest New Threat to Smart Homes Is AI Promptware. My Tips Help Stop It

5 key steps to stop promptware threats ... Always keep your devices updated, especially in the age of AI ... Don't accept or open any messages from unknown sources ... Don't ask AI to summarize anything you don't already know well and trust ... Disable AI in your email, calendars, chat apps and other places you can get messages



](https://tech.yahoo.com/cybersecurity/articles/biggest-threat-smart-homes-ai-110000260.html#1)[

![](https://cdn.deepseek.com/site-icons/incibe.es)

INCIBE

2025/08/20

Smart home hacked using Gemini AI

Google’s artificial intelligence assistant, that allowed them to take control of smart home devices. The attack, known as an indirect prompt injection, involved inserting malicious commands into the description of a Google Calendar event. ... Google strengthened Gemini’s security by introducing filters to detect suspicious prompts, implementing tighter controls over calendar events...



](https://www.incibe.es/en/incibe-cert/publications/cybersecurity-highlights/smart-home-hacked-using-gemini-ai)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/08/05

agent-threat-rules/rules/excessive-autonomy/ATR-2026-00710-ipi-physical-access-grant.yaml at main · Agent-Threat-Rule/agent-threat-rules · GitHub - title: "Indirect PI — Unauthorized Physical Access Grant via Smart Lock / Home Automation"

"Indirect PI — Unauthorized Physical Access Grant via Smart Lock / Home Automation" ... Detects indirect prompt injection payloads that instruct an agent to grant physical access to a premises: adding guests to smart lock systems (August, Kwikset), unlocking doors, or modifying access control rules. The payload is embedded in consumed content and exploits agents with home automation or physical security tool access.



](https://github.com/Agent-Threat-Rule/agent-threat-rules/blob/main/rules/excessive-autonomy/ATR-2026-00710-ipi-physical-access-grant.yaml#1)[

![](https://cdn.deepseek.com/site-icons/gmw.cn)

光明网

2026/05/07

一张打印照片就能打开智能锁？消协实测曝光 - 一张打印照片就能打开智能锁？消协实测曝光

此外，有3款产品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。此类漏洞使得用户的登录凭证和远程指令极易在网络中被截获，可能导致非法开锁或隐私泄露。而在30款产品中...



](https://m.gmw.cn/2026-05/08/content_1304448707.htm#1)[

突出从严从实 推动见行见效-安徽长安网

2026/05/08

一张打印照片就能开门？智能锁这些功能有隐患-安徽长安网

远程开门数据传输有泄密风险 这次检测中还发现，部分智能门锁有远程开门的功能，但实际使用过程中，数据传输并没有加密，隐私与远程控制存风险。少数产品在传输账号密码、远程开锁指令时，采用明文传输...



](http://www.ahcaw.gov.cn/ahcaw/content/2026-05/09/content_9385498.htm)[

![](https://cdn.deepseek.com/site-icons/gmw.cn)

光明网

2026/05/06

用一张照片就刷开了智能门锁？消协实测曝光！ - 用一张照片就刷开了智能门锁？消协实测曝光！

远程开门数据传输 ... 这次检测中还发现，部分门锁有远程开门的功能，但实际使用过程中，数据传输并没有加密，隐私与远程控制存在风险。少数产品在传输账号密码、远程开锁指令时，采用明文传输，黑客可在同一网络环境下截获信息，重放指令实现非法开锁。



](https://m.gmw.cn/2026-05/07/content_1304447590.htm#1)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

CNET

2026/06/09

Eufy Expands Face-Reading Smart Lock Line, Specializing in On-Device Processing - CNET

Eufy's FamiLock line is now larger, with more affordable models that limit AI processing to help protect your privacy. ... but your biometric data also shouldn’t be sent into the cloud or used to train AI. It’s a more private approach that avoids some of the problems people have when Ring used facial data without permission.



](https://www.cnet.com/home/security/eufy-expands-face-reading-smart-lock-line-on-device-processing/#1#1)[

![](https://cdn.deepseek.com/site-icons/kepuchina.cn)

科普中国

2026/05/10

一张打印照片就能刷开智能门锁？快来自查你家的门锁安全吗

这次检测中还发现，部分智能门锁有远程开门的功能，但实际使用过程中，数据传输并没有加密，隐私与远程控制存在风险。少数产品在传输账号密码、远程开锁指令时，采用明文传输，黑客可在同一网络环境下截获信息，重放指令实现非法开锁。



](https://cloud.kepuchina.cn/h5/detail?id=7453207218208137216)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/06/09

Eufy Expands Face-Reading Smart Lock Line, Specializing in On-Device Processing

data more private than other companies. ... but your biometric data also shouldn't be sent into the cloud or used to train AI. It's a more private approach that avoids some of the problems people have when Ring used facial data without permission. ... It avoids collecting face data, even on the device.



](https://tech.yahoo.com/home/articles/eufy-expands-face-reading-smart-231149785.html#1)[

![](https://cdn.deepseek.com/site-icons/ithome.com)

IT之家

2026/05/06

京津冀三地消协实测 30 款智能门锁：IC 卡易复制、人脸识别存缺陷、数据传输不加密...

感谢IT之家网友 加勒比 的线索投递！ IT之家 5 月 7 日消息，据央视新闻报道，近期北京市消费者协会、天津市消费者协会、河北省消费者权益保护委员会对市面上常见的 20 个品牌 30 款智能门锁产品开展了比较试验。 受测样品均从电商平台购买，涉及 TCL、华为、小米、萤石、凯迪仕、松下、德施曼、鹿客等品牌产品，价格在 936 元至 4500 元区间。在核心安全技术指标上，不同产品表现差异显



](https://www.ithome.com/0/947/198.htm)[

simplisafe.com

2025/11/03

Strengthening Security Together: SimpliSafe’s Bug Bounty Program

SimpliSafe’s Bug Bounty Program ... security researchers. Through our Bug Bounty Program, these experts help us identify and responsibly disclose potential vulnerabilities before they can impact customers. The program invites researchers worldwide to responsibly test SimpliSafe systems within defined parameters and report potential security issues.



](https://drupal-ecs.simplisafe.com/blog/simplisafe-bug-bounty)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Bug Hunters

Android and Google Devices Security Reward Program Rules | Google Bug Hunters

The Android and Google Devices Security Reward Program is a collaborative initiative designed to secure the Android ecosystem and Google hardware. We partner with the global security research community to identify, responsibly disclose, and effectively remediate high-impact vulnerabilities. ... Smart Home and Google Nest



](https://bughunters.google.com/about/rules/android-friends/android-and-google-devices-security-reward-program-rules)[

![](https://cdn.deepseek.com/site-icons/eufy.com)

Eufy

2026/09/02

eufy Vulnerability Disclosure Policy - Vulnerability Disclosure Policy

If you believe you have discovered a vulnerability in a eufy Security product or have a security incident to report, please fill in the vulnerability report form on our vulnerability management page ... referring to ISO/IEC 30111. ... Report receipt will be confirmed within 1 business day and a preliminary assessment will take place.



](https://www.eufy.com/vulnerability-disclosure-policy#1)[

mediola - connected living AG

2026/08/18

Security - mediola - connected living AG

Security at mediola (Vulnerability Disclosure Policy) ... If you believe you have identified a potential security vulnerability, security issue, or other security-related concern affecting our products or services, please report it directly to our Product Security Incident Response Team (PSIRT)...



](https://www.mediola.com/en/security-2)[

![](https://cdn.deepseek.com/site-icons/shelly.com)

Shelly USA

2025/05/15

Security Information and Vulnerability Reporting - Shelly USA

In the event of security vulnerability, submit voluntary report via the VULNERABILITY REPORTING FORM : Shelly appreciates responsible disclosure practices in this area, such as not publicly and prematurely disclosing information about vulnerabilities during the time it takes to remediate the vulnerability.



](https://us.shelly.com/pages/security-information-and-vulnerability-reporting)[

![](https://cdn.deepseek.com/site-icons/consumerreports.org)

Consumer Reports

2025/07/08

More Smart Home Companies Want to Hear from Security Researchers - Innovation at Consumer Reports

more smart home device manufacturers are making it easier for security researchers to let them know about security vulnerabilities. ... These programs explain how security researchers can report a vulnerability to a company and describe how the company plans to research and remediate the vulnerability. A good VDP will dictate how a security researcher should share their findings, and explain how the company typically handles a vulnerability report.



](https://innovation.consumerreports.org/more-smart-home-companies-want-to-hear-from-security-researchers/)[

![](https://cdn.deepseek.com/site-icons/hackerone.com)

HackerOne

eero - Bug Bounty Program | HackerOne

eero Program Policy ##Introduction The first mesh home wifi system, eero blankets any home in reliable and secure wifi. eero offers advanced online security tools, eero Secure and eero Secure+, to help protect personal data, devices ... The eero Bug Bounty Program is designed to recognize security research on our consumer electronics...



](https://hackerone.com/eero/policy_versions?type=team&change=3766578)[

![](https://cdn.deepseek.com/site-icons/sonos.com)

Sonos

2026/03/30

Sonos协调漏洞披露政策 - Sonos

协调漏洞披露政策 Sonos致力于通过及时有效的漏洞研究来保护客户的数据和隐私 ... 本政策基于并参考ISO漏洞披露标准 ISO/IEC 29147中使用的方法 ... 可以发送电子邮件至security@sonos.com报告漏洞（邮件主题为“Vulnerability Report”） ... 外部各方预计在3个工作日内收到报告确认。



](https://www.sonos.com/zh-cn/vulnerability-disclosure-policy)[

Sylvania Group

Scoperta e divulgazione delle vulnerabilità

# SCOPERTA E DIVULGAZIONE DELLE VULNERABILITÀ # VULNERABILITY DISCOVERY AND DISCLOSURE ## VULNERABILITY DISCOVERY AND DISCLOSURE Vulnerability discovery and disclosure policy Version 1.5– March 20



](https://www.sylvania-group.com/it-it/homepage-professional/legal-pages/scoperta-e-divulgazione-delle-vulnerabilita/)[

Vestel International

2026/03/01

Vulnerability Disclosure Policy - Vestel International

Cookie Policy EU Data Act Imprint Modern Slavery Act Privacy Policy Right to Repair Security Advisories Terms of Use Vulnerability Disclosure Policy # Overview This Vulnerability Disclosure



](https://vestelinternational.com/en/vulnerability-disclose-policy)[

devolo.co.uk

UK PSTI Statement of Compliance

Minimum Support Period: 5 years (until 30.5.2030) We will provide updates and patches to address any security vulnerabilities that may be identified in the product for at least the duration of the support period specified above.



](https://www.devolo.co.uk/media/c3/62/1b/1764606714/SoC_UK_PSTI_MT3371_202561.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/grandstream.com)

grandstream.com

Statement of Compliance

3. Security Updates Support: GRANDSTREAM will provide security updates for our products during the pre-defined support period. The defined support period will be 5 years after the product's GA. Up-to-date information concerning the defined support periods for the entire GRANDSTREAM product range please refer to Appendix-Products.



](https://www.grandstream.com/hubfs/Declaration-of-Conformity/Statement%20of%20Compliance%202026.04.10.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/tp-link.com)

TP-Link

2021/09/05

Duration of Security Support (Singapore Market) - Duration of Security Support (Singapore Market)

Duration of Security Support (Singapore Market) ... TP-Link will provide security update support to the following products up to 31 Aug 2029, and extended support may be provided after the stated date. ... TP-Link will provide security update support to the following products up to 1st June 2028...



](https://www.tp-link.com/sg/support/faq/3182/#1)[

![](https://cdn.deepseek.com/site-icons/tp-link.com)

TP-Link

2026/03/02

Australian Cyber Security Statement of Compliance | TP-Link Australia - Statement of Compliance

3. TP-Link will provide security updates for our products during the pre-defined support period. The defined support period will end up to 3 years after the product’s end-of-sales date. ... 31/12/2028 or later*



](https://www.tp-link.com/au/landing/au-cyber-compliance/#1)[

![](https://cdn.deepseek.com/site-icons/keenetic.com)

Keenetic

Manuale Utente (Inglese)

Aggiornamenti Limitati: Per almeno quattro anni dal lancio di un prodotto, Keenetic fornisce aggiornamenti limitati. ... Fine degli Aggiornamenti e del Supporto: Cinque anni dopo il rilascio di un prodotto, potremmo interrompere tutti gli aggiornamenti, inclusi gli aggiornamenti critici per la sicurezza del software.



](https://support.keenetic.com/skipper/kn-1913/it/31171-product-lifecycle-support-policy.html)[

![](https://cdn.deepseek.com/site-icons/tp-link.com)

static.tp-link.com

TP-LINK CORPORATION PTE. LTD. 7 Temasek Boulevard #29-03 Suntec Tower One, Singapore 038987

3. TP-Link will provide security updates for our products during the pre-defined support period. The defined support period will end 3 years after the product's end-of-life date. ... V6</td><td>31/12/2027 or later*</td></tr><tr><td>Wi-Fi



](https://static.tp-link.com/upload/manual/2024/202409/20240919/Statements%20of%20PSTI%20Compliance_TP-Link.pdf#7#1)[

![](https://cdn.deepseek.com/site-icons/consumerreports.org)

advocacy.consumerreports.org

THE CONNECTED CONSUMER PRODUCT END OF LIFE DISCLOSURE LAW

and after 15 years of selling connected devices, it's time for the industry to step up and disclose how long they plan to support the ... - Manufacturers must clearly disclose minimum guaranteed support time frames by which they will provide security and software updates for connected consumer products ... that lease connected consumer products to remove those products (including



](https://advocacy.consumerreports.org/wp-content/uploads/2025/03/EOL-Legislation-2-Pager-Updated-December-2025.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/intertek.com.cn)

Intertek 中国

2025/11/06

Intertek

如操作系统、路由器、智能家居设备、防火墙等。此类产品需进行更严格的符合性评估 ... - 支持周期：必须明确并公开产品的安全支持期限，通常不得少于5年。 - 安全更新：在支持期内免费提供安全更新 ... 为每个产品确定并规划至少5年的安全支持周期。



](https://www.intertek.com.cn/listdata/1986672100768747520.html)[

![](https://cdn.deepseek.com/site-icons/intertek.com.cn)

Intertek 中国

一文读懂 | 欧盟《网络弹性法案》（CRA）

如操作系统、路由器、智能家居设备、防火墙等。此类产品需进行更严格的符合性评估 ... - 支持周期： 必须明确并公开产品的安全支持期限，通常不得少于5年。 - 安全更新： 在支持期内免费提供安全更新，并默认启用自动更新功能（用户可关闭） ... 为每个产品确定并规划至少5年的安全支持周期。



](https://www.intertek.com.cn/Reading_itemid_1980473566973399040_lcid_40.html)[

![](https://cdn.deepseek.com/site-icons/keenetic.com)

Keenetic

KeeneticOS updates — LTS Channel

For at least three years after Keenetic releases a product ... Five years after a product’s release, we may discontinue all updates, including critical software security updates. ... Keenetic Sprinter (KN-3711) support timeline ... Standard Updates until at least: October 2027 Limited Updates until at least: October 2028 End of Support date: October 2029



](https://support.keenetic.com/sprinter/kn-3711/en/69624-product-lifecycle-support-policy.html)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Product support policy for smart products from IKEA - Product support policy for smart products from IKEA

We will offer support for a minimum of three years after purchase, to ensure the hub / gateway: - Works with the IKEA Home smart app / IKEA Home Smart 1. - Gets security updates. - Gets updates to ensure compatibility with Amazon Alexa, Apple HomeKit, and Google Assistant.



](https://www.ikea.com/us/en/customer-service/privacy-security/product-support-policy-for-smart-products-from-ikea-pub0d314780/#1)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Política de apoio a produtos home smart da IKEA - Política de apoio a produtos home smart da IKEA

Isso significa que pode continuar a utilizar produtos home smart com a sua hub DIRIGERA ou gateway TRÅDFRI ... até quando durarem. ... Vamos oferecer apoio durante, pelo menos, três anos após a compra para assegurar que a hub/o gateway ... - Obtém atualizações para assegurar a compatibilidade com Amazon Alexa, Apple HomeKit e Assistente do Google.



](https://www.ikea.com/pt/pt/customer-service/privacy-security/politica-de-apoio-a-produtos-home-smart-da-ikea-pub0d314780/#1)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Politica di assistenza per i prodotti smart IKEA

Offriremo supporto per un minimo di tre anni dopo l'acquisto, per garantire che l'hub/il gateway ... - Ricevano aggiornamenti per garantire la compatibilità con Amazon Alexa, Apple HomeKit e l'Assistente Google.



](https://www.ikea.com/it/it/customer-service/privacy-security/politica-di-assistenza-per-i-prodotti-smart-ikea-pub0d314780/)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

ikea.com

Politique de prise en charge des produits connectés IKEA

• fonctionnent avec l'application IKEA Home smart correspondante (IKEA Home smart pour la passerelle DIRIGERA et IKEA Home smart 1 pour la passerelle TRÅDFRI) ; • bénéficient des mises à jour de sécurité ; • bénéficient des mises à jour de compatibilité avec Alexa d'Amazon, HomeKit d'Apple et l'Assistant Google.



](https://www.ikea.com/fr/fr/files/pdf/4c/b5/4cb537f6/new_product-support-policy-for-smart-products-from-ikea-on-country_24-10-2022_final_fr_fr.pdf#1#1)[

phaidra.ustp.at

When it comes to security, there are different amounts of information given by the companies, which can be used to judge their s...

Amazon and Google state that their security updates are done automatically, while all the others do not explicitly state it. The support periods are a minimum of four years or Google, five years for Amazon, while in some cases they are either not stated, different for certain products and services or given in terms of a gap between End of Sales and End of Maintenance, in that case, it being three years.



](https://phaidra.ustp.at/api/object/o:7799/download#17#11)[

![](https://cdn.deepseek.com/site-icons/arstechnica.com)

Ars Technica

2023/12/22

Matter was more of a nice smart home concept than useful reality in 2023 - - Status

If it can communicate via Thread and doesn't need its own proprietary hub, it doesn't matter if the company itself goes bust, Apple/Amazon/Google/Samsung Home will figure everything out. Even in the case of Google, I have more faith in them to continue support their



](https://arstechnica.com/civis/threads/matter-was-more-of-a-nice-smart-home-concept-than-useful-reality-in-2023.1497874/?thutp_user_id=359618&order=vote_score#1)[

bvse.de

The study of household development in Germany shows a market potential of 837,000 new one- and two-person households for the sma...

The study of household development in Germany shows a market potential of 837,000 new one- and two-person households for the smart home market by 2030. The market participants can basically be divided



](https://bvse.de/dateien2020/2-PDF/01-Nachrichten/04-Schrott-ES-Kfz/2023/0309-UBA-texte_13-2023_analyse_der_softwarebasierten_einflussnahme_auf_eine_verkuerzte_nutzungsdauer_von_produkten.pdf#36#5)[

bvse.de

und umfasst 8.000 Produkte, die primär durch Fachkräfte installiert werden

und umfasst 8.000 Produkte, die primär durch Fachkräfte installiert werden. Die Anbindung wird über Twisted Pair, Funk, Powerline und IP realisiert. Als letztes soll an dieser Stelle Google Nest kurz



](https://bvse.de/dateien2020/2-PDF/01-Nachrichten/04-Schrott-ES-Kfz/2023/0309-UBA-texte_13-2023_analyse_der_softwarebasierten_einflussnahme_auf_eine_verkuerzte_nutzungsdauer_von_produkten.pdf#36#18)[

![](https://cdn.deepseek.com/site-icons/arstechnica.com)

Ars Technica

2018/10/09

Google Home Hub—Under the hood, it’s nothing like other Google smart displays - Here's the question, though, which of their platforms will be more likely to survive to get future support

Here's the question, though, which of their platforms will be more likely to survive to get future support? Or are both equally likely to get eliminated at a whim when Google loses interest in it? I



](https://arstechnica.com/civis/threads/google-home-hub%E2%80%94under-the-hood-it%E2%80%99s-nothing-like-other-google-smart-displays.1439613/page-2#post-36162011#1)[

![](https://cdn.deepseek.com/site-icons/ansi.org)

American National Standards Institute - ANSI

2026/03/22

Should I Update My IoT Device? (Part 1 of 3) - ANAB Blog

The short answer is yes, almost always. ... Updates are how manufacturers fix security vulnerabilities, improve stability, protect against new hacking methods, and maintain compatibility with your network. ... 46% of IoT devices with known vulnerabilities on customer networks have no reliable path to receiving updates



](https://blog.ansi.org/anab/should-i-update-my-iot-device/)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Beveiligingsupdates en resultaten van beveiligingsvalidatie voor apparaten voor het connected home van Google

Beveiligingsupdates en resultaten van beveiligingsvalidatie voor apparaten voor het connected home van Google Google Nest-apparaten voor het connected home krijgen minimaal 5 jaar lang automatische beveiligingsupdates vanaf de datum waarop we ze voor het eerst verkopen in de Amerikaanse Google Store. ... Google Home-speaker (2026) | 25-06-2026 ... Nest Learning Thermostat (4e



](https://support.google.com/product-documentation/answer/10231940?hl=nl&ref_topic=10123615#1)[

![](https://cdn.deepseek.com/site-icons/fonearena.com)

FoneArena.com

2025/08/24

Samsung expands One UI to smart appliances with 7-year software support - Skip to content

Samsung Wi-Fi smart appliances introduced from 2024 will be eligible for seven years of updates, supporting extended functionality and security. ... Samsung confirmed that Wi-Fi smart appliances released from 2024 will receive seven years of software updates, ensuring ongoing security ... - Knox Matrix security extends to refrigerators, washers, dryers, air conditioners, EHS, and slide-in induction ranges.



](https://www.fonearena.com/blog/462474/samsung-one-ui-smart-appliances-7-year-software-support.html#more-462474#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2025/08/12

Regulating smart device support periods | Proceedings of the 34th USENIX Conference on Security Symposium - Several features on this page require Premium Access

Supporting consumer IoT devices with updates is crucial to ensure their security. However, this support period is usually ... The upcoming European Cyber Resilience Act (CRA) addresses this by requiring manufacturers to support their products for the expected use time, which should be based on reasonable user expectations. ... devices' full lifetimes...



](https://dl.acm.org/doi/10.5555/3766078.3766343#1)[

![](https://cdn.deepseek.com/site-icons/miele.de)

Miele

2025/10/16

International Repair Day – Miele provides more support for self-help initiatives

At the same time, it is a prerequisite for the Remote Update Service. This service allows Miele to automatically update its appliances with the latest software, enabling new functions and providing enhanced security features. ... with the Remote Update Service ... always up to date – easily, via the Miele app. (Photo...



](https://www.miele.de/en/m/international-repair-day-miele-provides-more-support-for-self-help-initiatives-8001.htm)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Google Nest 设备的安全更新和安全验证结果 - 发送以下项目的反馈

Google Nest 设备的安全更新和安全验证结果 自 Google Nest 智能互联家居设备在美国 Google 商店开始销售之日起，这些设备将会至少在 5 年内收到自动安全更新。安全更新会通过远程软件更新的方式 ... Nest Doorbell（室内用，有线版 - 第 3 代） | 2025 年 10 月 1 日 | 2030



](https://support.google.com/product-documentation/answer/10231940?hl=zh-#1)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/08/26

Samsung Expands One UI to Home Appliances, Bringing Unified Software Experience Across Devices

smart appliances will be receiving software updates for 7 years after launching [1], starting from 2024-launched ... Beginning in September, eligible 2024 launched models will be receiving various software updates that bring enhancements in usability, intelligence and security: - Upgraded Security: Knox Matrix [6], Samsung’s comprehensive security solution extending protection across devices based on private block chain technology ... These screen appliances will also be updated with the Knox Security dashboard provided on 2025 models ... [1]Software updates are provided for up to 7 years



](https://news.samsung.com/uk/samsung-expands-one-ui-to-home-appliances-bringing-unified-software-experience-across-devices)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Security updates and third-party assessments for Google Nest devices

Security updates and third-party assessments for Google Nest devices Google Nest connected home devices will receive automatic security updates for at least five years from the date that we start selling them on the US Google Store. Security updates will address critical issues known to Google Nest that are able to be resolved with a remote software update.



](https://support.google.com/product-documentation/answer/10231940?hl=en-AU#1)[

![](https://cdn.deepseek.com/site-icons/geappliances.com)

GE Appliances Pressroom

2025/10/08

GE Appliances Recognized for IoT CyberSecurity Innovation in 2025 CyberSecurity Breakthrough Awards Program

Prestigious Annual Awards Program Honors Outstanding Information Security Products and Companies Around the World LOS ANGELES, Calif., Oct. 9, 2025 – CyberSecurity Breakthrough, an independent market



](https://pressroom.geappliances.com/news/ge-appliances-recognized-for-iot-cybersecurity-innovation-in-2025-cybersecurity-breakthrough-awards-program)[

![](https://cdn.deepseek.com/site-icons/etsi.org)

etsi.org

"The consumer IoT device or an associated service should check after initialization whether security updates are available

"The consumer IoT device or an associated service should check after initialization whether security updates are available." (ETSI EN 303 645 [i.1]) NOTE: An example for this provision is also prov



](https://www.etsi.org/deliver/etsi_tr/103600_103699/103621/02.01.01_60/tr_103621v020101p.pdf#9#4)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

2026/03/18

March 19, 2026 - Your acknowledgment applies to all current and future devices and users in the home

Your Gemini for Home activity, such as voice assistant queries, will be saved in your Home History in My Activity. ... By default, your activity will be saved for 18 months. You can turn this off or change how long your activity is saved by visiting Home History.



](https://support.google.com/googlehome/answer/17080927?hl=en#1)[

kiloiot.io

2026/08/30

Privacy and Security | Kilo IoT

Privacy of the Kilo IoT AI Assistant — session-scoped auth, permission inheritance, org isolation, data retention. ... Raw device telemetry is not duplicated or retained by the assistant beyond the scope of your query. Passwords, API credentials ... the assistant reads only what your permissions already allow, and it stays inside your current organization.



](https://docs.kiloiot.io/kilo-iot-server/ai-assistant/privacy)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

ieee.org

2026/02/24

Balancing Usability and Compliance in AI Smart Devices: A Privacy-by-Design Audit of Google Home, Alexa, and Siri

This paper investigates the privacy and usability of AI-enabled smart devices commonly used by youth, focusing on Google Home Mini, Amazon Alexa, and Apple Siri. While th...Show More ... Results show that Google Home achieved the highest usability score, while Siri scored highest in regulatory compliance, indicating a trade-off between user convenience and privacy protection. Alexa demonstrated clearer task navigation but weaker transparency in data retention.



](https://xplorestaging.ieee.org/document/11393731)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

19 de março de 2026 - Caso se inscreva em programas e serviços de domótica oferecidos pelos nossos parceiros, por exemplo, empresas de energia ou segu...

A sua atividade é guardada na sua conta durante um máximo de 24 horas, independentemente de o histórico do Home estar ativado ou desativado. ... A sua atividade é eliminada automaticamente após 18 meses. ... como as consultas ao assistente de voz do Gemini para o Home ... Pode gerir esta definição em qualquer altura.



](https://support.google.com/googlenest/answer/17080927?hl=pt#3)[

kiloiot.io

2026/09/15

Privacy and Security | Kilo IoT

Delegate IoT setup with your own account permissions — understand AI action confirmations, saved conversations, and model-provider data handling. You can delegate configuration to Kilo's AI ... Keep account passwords and unrelated secrets out of chat, and review the AI access settings when choosing a model provider.



](https://docs.kiloiot.io/ai-assistant/privacy)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Your data stays private while Assistant's activation technologies improve - Send feedback on

Federated learning is a privacy-enhancing ... Your device may not indicate anything when it stores these recordings and may store up to 20 recordings per day ... On-device recordings from “Hey Google" activations and near-activations stay on your device for up to 63 days unless you delete them before then.



](https://support.google.com/assistant/answer/11932523?hl=en#1)[

![](https://cdn.deepseek.com/site-icons/switch-bot.com)

SwitchBot Official Website

2026/06/11

SwitchBot KATA AI Assistant Privacy Policy – SwitchBot International

SwitchBot KATA AI Assistant Privacy Policy ... We retain relevant information only for the period necessary to achieve the purposes of the Service. When the retention period expires, the processing purpose has been fulfilled, you actively delete the relevant data, or we terminate the corresponding service, we will delete



](https://www.switch-bot.com/pages/switchbot-ai-assistant-privacy-policy)[

![](https://cdn.deepseek.com/site-icons/eepw.com.cn)

电子产品世界

2025/11/12

Agentic AI的隐藏数据轨迹以及如何缩小它 - Agentic AI的隐藏数据轨迹以及如何缩小它

减少 AI 代理数据跟踪的六种方法 ... 第一种习惯是将内存限制在当前任务范围内。对家庭优化助手而言 ... 第二种是让删除操作简单彻底。每一项计划、轨迹、缓存、嵌入数据和日志都标记相同的运行 ID ... 第三种是通过临时、特定任务权限，谨慎限制设备访问权限 ... 第四种是通过可读的 “智能体轨迹” 让系统行动透明化。



](https://m.eepw.com.cn/article/202511/475432.html#1)[

![](https://cdn.deepseek.com/site-icons/semanticscholar.org)

Semantic Scholar

2026/01/04

[PDF] Balancing Usability and Compliance in AI Smart Devices: A Privacy-by-Design Audit of Google Home, Alexa, and Siri | Semantic Scholar - Another weakness, especially evident in Alexa, was the opacity

Another weakness, especially evident in Alexa, was the opacity surrounding data retention [42], [55]. Participants discovered that even after disabling voice recording history, Amazon continued to



](https://www.semanticscholar.org/reader/10116e6c96cbb46e9446cdc8bb322ae797f87ac1#3)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/04/27

I ditched cloud voice assistants for a local LLM and my smart home finally feels private - Advertisement

Technology that's meant to simplify our lives can lead us to give up all privacy at home. Most smart speakers rely on the cloud, where every whispered command to a voice assistant is sent to remote se



](https://tech.yahoo.com/home/articles/ditched-cloud-voice-assistants-local-141518919.html#1)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

European Parliament

Pesquisa | Deputados | Parlamento Europeu - Resultado da pesquisa

This regulation aims to ensure that fundamental rights ... the co-legislators agreed to prohibit: biometric categorisation systems that use sensitive characteristics (e.g. political, religious, philosophical beliefs, sexual orientation, race) ... During the negotiations, MEPs made sure that products such as identity management systems software, password managers, biometric readers, smart home assistants and private security cameras are covered by the new rules.



](https://www.europarl.europa.eu/meps/pt/indexsearch?ordering=RELEVANCE&query=sue+risk&scope=ALL&term=9#1)[

Separatore di particelle per pulizia impianti di riscaldamento Wilo-SiClean

2026/02/08

Videosorveglianza con AI: in presenza di adeguate garanzie

Il Regolamento (UE) 2016/679 (GDPR) ammette il trattamento di dati biometrici solo in casi specifici e quando esistono adeguate garanzie. ... Occorre inoltre tenere presente che l’AI Act europeo – la cui applicazione è imminente – classifica il riconoscimento biometrico in tempo reale tra ... a rischio elevato...



](https://www.impiantinews.it/sicurezza/norme-leggi/videosorveglianza-con-ai-in-presenza-di-adeguate-garanzie/#elementor-action%3Aaction%3Dpopup%3Aclose%26settings%3DeyJkb19ub3Rfc2hvd19hZ2FpbiI6IiJ9)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

ec.europa.eu

426. A mesterséges intelligenciáról szóló rendelet 5. cikke (1) bekezdésének h) pontjában foglalt tilalom hatályán kívül eső táv...

A tilalom hatályán kívül eső másik felhasználás a valós idejű távoli biometrikus azonosító rendszerek bűnüldözési célú használata magánterületen (például valakinek az otthonában)



](https://ec.europa.eu/newsroom/dae/redirection/document/118654#48#48)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

European Parliament

Pretraga | Zastupnici | Europski parlament - Rezultati pretraživanja

MEPs made sure that products such as identity management systems software, password managers, biometric readers, smart home assistants and private security cameras are covered by the new rules. ... biometric categorisation systems that use sensitive characteristics (e.g. political, religious, philosophical beliefs, sexual orientation, race)...



](https://www.europarl.europa.eu/meps/hr/indexsearch?ordering=RELEVANCE&query=risk+will&scope=ALL&term=9#1)[

![](https://cdn.deepseek.com/site-icons/zenodo.org)

zenodo.org

Per abordar aquesta tensió i garantir un equilibri entre privacitat i qualitat d’interacció, es poden implementar diverses estra...

impliquen identificació biomètrica en temps real sense bases legals justificades. ... L’Article 5(1d) prohibeix l’ús de sistemes d’identificació biomètrica en temps real en espais públics, excepte en casos legals justificats.



](https://zenodo.org/records/17542052/files/Metodologia%20de%20disseny%20i%20avaluacio%CC%81%20e%CC%80tica%20en%20la%20robo%CC%80tica%20assistencial.pdf?download=1#14#8)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dl.acm.org

Use of cameras and video recorders for one's own use is of course well established

In spring 2021, the EU introduced regulations on artificial intelligence with a view to producing binding legislation that will apply across Europe, the Artificial Intelligence Act [10]. ... The surveillance using 'real- time' biometric data is banned except for law enforcement purposes, involving certain serious crimes, in certain circumstances.



](https://dl.acm.org/doi/pdf/10.1145/3441852.3476471?__cf_chl_tk=nXVIpxENPGrbWo3DtYYhxy.glVXhBZ5jNdmGPUJNwQM-1784478672-1.0.1.1-FjUPs2oXDLy1C5om929L8EAoqmtWusMBdRn5Z1U5JrM#3#2)[

![](https://cdn.deepseek.com/site-icons/econstor.eu)

econstor.eu

- The principles of safety, security, and robustness<sup>170</sup>, which demand the identification and mitigation of risks asso...

may fall under the prohibition of the AI Act or be considered non- compliant with the proposed AI Bill ... they can be deemed high- risk whenever they profile the cyborg consumer. ... if the AloT device uses emotion recognition and biometric categorisation to profile the cyborg who wears or is integrated with it, it is labelled as high- risk under the AI Act...



](https://www.econstor.eu/bitstream/10419/331306/1/ITS-E-2025-61.pdf#4#4)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

European Parliament

Ricerca | Deputati | Parlamento Europeo - Risultati della ricerca

Products deemed to pose a higher cybersecurity risk will be examined more stringently by a notified body ... MEPs made sure that products such as identity management systems software, password managers, biometric readers, smart home assistants and private security cameras are covered by the new rules. ... that use sensitive characteristics (e.g. ... sexual orientation, race)...



](https://www.europarl.europa.eu/meps/it/indexsearch?query=risk+will&scope=ALL&term=9&ordering=RELEVANCE#1)[

![](https://cdn.deepseek.com/site-icons/stanford.edu)

law.stanford.edu

under Article 5(1), such as those employing subliminal manipulation, harmful social

scoring, or real-time remote biometric identification in public spaces; (2) high-risk systems, which are subject to extensive requirements listed in Annex III, including those used in law enforcemen



](https://law.stanford.edu/wp-content/uploads/2025/04/TTLF-WP-134-Warthon.pdf#8#3)[

![](https://cdn.deepseek.com/site-icons/vu.nl)

Vrije Universiteit Amsterdam

2024/10/25

Interview on new frontier of surveillance powered by AI

Press/Media: Expert Comment ## Media contributions 1 Media contributions - TitleIntervista alla Dott.ssa Silvia De Conca. IoT, IA Emotiva, realtà virtuale: le nuove frontiere della sorveglianza e la



](https://research.vu.nl/en/clippings/interview-on-new-frontier-of-surveillance-powered-by-ai/)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nist.gov

Challenges and Practical Approaches to Consumer Software Labeling

The Alliance has over 500 member companies supporting Smart Home, Smart Building, Cellular, and mobile application markets. ... The ioXt Alliance has an active compliance and security labeling program for Smart Home, Smart Building, Cellular Devices, and Mobile Applications. We believe that manufacturers



](https://www.nist.gov/system/files/documents/2021/09/03/IoXT-Challenges%20and%20Practical%20Approaches%20to%20Consumer%20Software%20Labeling.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/iotforall.com)

iotforall.com

2024/11/26

DesignLights Consortium Adds ioXt Alliance Certification Program to Recognized Cybersecurity Standards | IoT For All

(DLC) has added ioXt ... Adding ioXt as an option to the DLC’s Cybersecurity Standards list allows commercial lighting manufacturers to provide proof of cybersecurity standard compliance via an ioXt certificate or letter from one of its accredited testing organizations. ... the DLC and the Alliance are bringing 300+ companies together to define security specifications for smart home and buildings...



](https://dev.iotforall.com/news/dlc-ioxt)[

ioXt

ioXt Alliance News and Events Blog — ioXt

The ioXt Alliance, the Global Standard for IoT Security ... Midea Certifies with ioXt Alliance to Expand Smart Home Security The ioXt Alliance ... announced today that international household appliance manufacturer Midea, has certified seven appliances through the ioXt Certification Program. The product certification marks the beginning of Midea’s relationship



](https://www.ioxtalliance.org/news-events-blog?offset=1652470886861&category=Press+Releases)[

ismsforum.es

PSA Certified (PSA for Platform Security Architecture) is a security certification dedicated to IoT hardware such as chips, soft...

The ioXt security certification has been developed by the ioXt Alliance founded by leading technology companies willing to build confidence in IoT products. ... product.” The scheme is addressing products involved with: smart home, lighting controls, smart building, IoT Bluetooth, smart retail, portable medical, smart home, mobile apps, pet trackers, routers and automotive technology.



](https://www.ismsforum.es/backoffice/ckfinder/userfiles/files/Cybersecurity%20Certification%20Statistics%20Report\(1\).pdf#6#5)[

IoT Now

ioXt Alliance | IoT Now News & Reports

Roku adds new home monitoring system ... United States – ioXt Alliance, a global standard for IoT security, has announced the expansion of its IoT security certification program to include building network controllers (BNCs). ... a global standard for IoT security, has added Bishop Fox, the private offensive security testing firm, to the ioXt Authorised Labs Certification Program.



](https://www.iot-now.com/tag/ioxt-alliance/)[

Orange County Business Journal

2026/05/31

Gary Jabara’s ioXt Gets FCC Nod for Cybersecurity - Orange County Business Journal

Costa Mesa-based ioXt has established security standards for everyday connected devices, including cellphones, smart-home lighting controls, automotive technology and thousands of products. ... The ioXt certification is intended to give consumers confidence that smart-home devices will protect their privacy and security as alliance members work with government regulators and major industry players.



](https://www.ocbj.com/oc-homepage/gary-jabaras-ioxt-gets-fcc-nod-for-cybersecurity/)[

![](https://cdn.deepseek.com/site-icons/telekom.com)

hardware.iot.telekom.com

ioXt Alliance Certification Benefits

ioXt Alliance Certification Benefits ... Android, Mobile App, Network Lighting, Residential Camera, Speaker ... - ioXt Alliance certification scope is mapped to the most widely accepted cybersecurity standards and is the best way to comply with regulatory requirements such as - NIST IR 8259



](https://hardware.iot.telekom.com/Document/3386/DEKRA%20IoT%20-%20ioXt%20Alliance%20-%20Product%20Information.pdf#1#1)[

ioXt

2021/04/04

Midea Certifies with ioXt Alliance to Expand Smart Home Security — ioXt

Midea Certifies with ioXt Alliance to Expand Smart Home Security ## Midea Certifies with ioXt Alliance to Expand Smart Home Security ... 2021 – The ioXt Alliance, the Global Standard for IoT Security, announced today that international household appliance manufacturer Midea, has certified seven appliances through the ioXt Certification Program. ... Devices with the ioXt SmartCert gives consumers and retailers greater confidence in a highly connected world.



](https://ioxt.com/news-events-blog/midea-certifies-with-ioxt-alliance-to-expand-smart-home-security)[

ioXt

2020/08/09

ioXt Alliance Partners with Major Companies To Secure IoT | The Global Standard for IoT Security — ioXt

Wide Range of Products Certified Include Those in the Smart Home, Smart Building ... Devices certified secure by the ioXt Alliance include cell phones, smart home, lighting controls, IoT Bluetooth, smart retail, portable medical, pet trackers, routers and automotive technology. ... Devices certified by the ioXt Alliance include...



](https://www.ioxtalliance.org/news-events-blog/top-tech-certifies-with-ioxt#comments-68b9f7ff0b99f056649b0f77)[

ioXt

2025/11/10

ioXt Joins IoT Alliance Australia Co-Design Effort to Advance Smart Device Security Labelling — ioXt

ioXt Joins IoT Alliance Australia Co-Design Effort to Advance Smart Device Security Labelling ... ioXt is contributing its deep experience in standards development ... ioXt Alliance is the global standard for IoT security ... Through its certification programs and international partnerships, ioXt works to ensure IoT security is consistent, transparent, and trusted across global markets.



](https://ioxt.com/news-events-blog/ioxt-joins-iot-alliance-australia-co-design-effort-to-advance-smart-device-security-labelling)[

![](https://cdn.deepseek.com/site-icons/bsigroup.com)

BSI Knowledge

2026/02/27

PD CEN/TR 18241:2025

This document contains recommendations on how to integrate the principle of ‘data protection and privacy by design’ during the entire lifecycle of biometric access-control products and services ... NOTE 1 The GDPR requires the effective integration of data-protection safeguards into the processing of personal data (Article 25).



](https://knowledge.bsigroup.com/products/privacy-management-in-products-and-services-biometric-access-control-products-and-services-1)[

![](https://cdn.deepseek.com/site-icons/evs.ee)

Eesti Standardikeskus

2025/12/14

CEN/TR 18241:2025

Privacy management in products and services - Biometric access control products and services ... This document contains recommendations on how to integrate the principle of ‘data protection and privacy by design’ during the entire lifecycle of biometric access-control products and services, in order to achieve ‘data protection and



](https://www.evs.ee/en/cen-tr-18241-2025)[

![](https://cdn.deepseek.com/site-icons/standard.no)

Standard.no

2026/01/04

SN-CEN/TR 18241:2025 - SN-CEN/TR 18241:2025

This document contains recommendations on how to integrate the principle of ‘data protection and privacy by design’during the entire lifecycle of biometric access-control products and services, in order to achieve ‘data protection andprivacy by default’.Biometric facial recognition for access control is covered by this document.



](https://online.standard.no/en/sn-centr-18241-2025#1)[

슈프리마

2025/07/22

Suprema | Security & Biometrics

the EU is set to enforce its revised RED directive (Delegated Regulation (EU) 2022/30) starting August 1, 2025. The update introduces mandatory cybersecurity compliance for IoT devices that use wireless technologies such as Wi-Fi, Bluetooth, smart door locks, and payment terminals.



](https://www.suprema.co.kr/en/about/news-detail.asp?iBOARD_CONT_NO=7731&News_Type=Releases&iNextPg=-4)[

m.media-amazon.com

EU DATA ACT – DECLARACIÓN DE TRANSPARENCIA

No se recogen datos biométricos directamente por el dispositivo. ... De conformidad con el Reglamento (UE) 2023/2854 (EU Data Act): • El usuario propietario del dispositivo tiene derecho a acceder a los datos generados por el uso del mismo.



](https://m.media-amazon.com/images/I/71gTZRpv0UL.pdf?ref=dp_product_quick_view#1#1)[

DREJTORIA E PËRGJITHSHME E STANDARDIZIMIT

2026/02/08

prDS CEN/TR 18241:2025

#### Privacy management in products and services - Biometric access control products and services #### Scope This document contains recommendations on how to integrate the principle of ‘data protect



](https://dps.gov.al/en/project/show/dps:proj:78668)[

LVS.LV

LVS - CEN/CLC/TC 13

You are using an outdated browser. Please upgrade your browser to improve your experience. × #### System messages ## CEN/CLC/TC 13 Project No. | LVS CEN/TR 18241:2025 ---|--- Title | This documen



](https://www.lvs.lv/en/committees/project/13730?project_id=478062)[

m.media-amazon.com

Dichiarazione di trasparenza dei dati

## Informazioni sul prodotto Nome del prodotto: Smart Lock Numero di modello: V1 Marchio: ICARE ASIN: BODMN9QNS8, B0FGXJZL1M, B0DPXBGDH, B0DP6736TQ, B0DP6615GY Produttore: Zhongshan Crosses Intellig



](https://m.media-amazon.com/images/I/61DMD18tlUL.pdf?ref=dp_product_quick_view#1#1)[

SIST E-Commerce

2026/01/19

SIST-TP CEN/TR 18241:2026 - Privacy management in products and services - Biometric access control products and services

# SIST-TP CEN/TR 18241:2026 (Splošen) ## Privacy management in products and services - Biometric access control products and services ## Privacy management in products and services - Biometric acces



](https://ecommerce.sist.si/catalog/standards/sist/53d6174a-f3cc-47a6-b60d-7af7a9428a67/sist-tp-cen-tr-18241-2026)[

![](https://cdn.deepseek.com/site-icons/ecovacs.cn)

ecovacs.cn

科沃斯产品安全中心漏洞处理与评级标准

科沃斯谴责任何以漏洞测试为名，实际损害用户利益、破坏计算机信息系统安全的行为，包括但不限于利用漏洞盗取用户隐私及虚拟财产、入侵业务系统、非授权获取系统或业务数据、窃取用户数据、恶意传播漏洞或数据等。未经科沃斯明确授权，禁止在任何公共场合或平台讨论或披露相关漏洞细节。对于上述行为...



](https://security.ecovacs.cn/cn/p/rating-standards)[

![](https://cdn.deepseek.com/site-icons/ecovacs.cn)

ecovacs.cn

Vulnerability Handling and Rating Standard

Without the explicit authorization of ECOVACS, discussing or disclosing relevant vulnerability details in any public venue or platform is prohibited. ECOVACS reserves the right to pursue legal liability for the aforementioned acts. ... Vulnerability reporters may submit reports of discovered product security vulnerabilities through the ECOVACS Product Security Center.



](https://security.ecovacs.cn/en/p/rating-standards)[

service.brennenstuhl.com

Policy for the disclosure of product-related cybersecurity vulnerabilities

Policy for the disclosure of product-related cybersecurity vulnerabilities ... This policy of **Hugo Brennenstuhl GmbH & Co. Kommanditgesellschaft** defines the procedures and expectations for the detection, reporting and remediation of vulnerabilities in our products in accordance with the EN ... 645 standard (CYBER ... - We aim to rectify vulnerabilities within 90 days of notification.



](https://service.brennenstuhl.com/hc/en-us/article_attachments/22083199973789#1#1)[

Sylvania Group

Ontdekking en openbaarmaking van kwetsbaarheden

This document describes Sylvania’s policy for receiving reports related to potential security vulnerabilities in its products and services, the company’s procedures in handling a report and the company’s standard practice with regards to informing customers of verified vulnerabilities. Everyone is encouraged to report identified vulnerabilities, regardless the type of service or products. Researchers, partners, customers or any other source are welcomed to report any vulnerabilities found.



](https://www.sylvania-group.com/nl-NL/homepagina-professioneel/legal-pages/ontdekking-en-openbaarmaking-van-kwetsbaarheden/)[

Sylvania Group

Vulnerability discovery and disclosure

# VULNERABILITY DISCOVERY AND DISCLOSURE # VULNERABILITY DISCOVERY AND DISCLOSURE ## VULNERABILITY DISCOVERY AND DISCLOSURE Vulnerability discovery and disclosure policy Version 1.5– March 2025 I



](https://www.sylvania-group.com/tr-tr/homepage-professional/legal-pages/vulnerability-discovery-and-disclosure/)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

Store encrypted security camera footage in iCloud with HomeKit Secure Video

Home app to record your footage and view it from anywhere. It’s all end-to-end encrypted, and none of the video counts toward your iCloud storage. ... The video is privately analyzed by your home hub using on-device intelligence to determine if it needs to be recorded to iCloud.



](https://support.apple.com/lv-lv/guide/icloud/mme054c72692/1.0/icloud/1.0)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

Stocarea înregistrărilor criptate ale camerelor de securitate pe iCloud cu funcționalitatea Video securizat HomeKit - Este posibil ca produsele, serviciile și funcțiile sistemului de operare

vă permite să le vizualizați de oriunde. Totul este criptat end-to-end și niciun clip video nu ocupă spațiu de stocare iCloud. ... Clipul video este analizat în mod privat de către hubul locuinței dvs., utilizând inteligența integrată a dispozitivului



](https://support.apple.com/ro-md/guide/icloud/mme054c72692/1.0/icloud/1.0#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

HomeKit camera security - HomeKit camera security

HomeKit secure video HomeKit provides an end-to-end secure and private mechanism to record, analyze, and view clips from HomeKit IP cameras without exposing that video content to Apple or any third party. ... If a significant event is detected ... The related metadata for each clip including the encryption key are uploaded to CloudKit using iCloud end-to-end encryption.



](https://support.apple.com/zh-cn/guide/security-pdf/sec525461d19/1/web/1#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

デバイスがローカルネットワーク上にない場合は、暗号化されたストリームがホームハブ経由でデバイスに中継されます

HomeKitの安全なビデオ ... このローカルネットワーク接続は、HKDF-SHA-512から導出されるセッションごとの鍵ペア で暗号化されます ... 重大なイベントが検出された場合は、ランダムに生成されるAES-256鍵 を使用してAES-256-GCMでビデオクリップを暗号化します。また...



](https://help.apple.com/pdf/security/ja_JP/apple-platform-security-guide-j.pdf#55#48)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

Keamanan kamera HomeKit

Video aman HomeKit HomeKit menyediakan mekanisme aman ujung ke ujung dan pribadi untuk merekam, menganalisis ... menganalisis bingkai video secara lokal untuk kejadian signifikan apa pun. Jika kejadian signifikan terdeteksi, HomeKit akan mengenkripsi klip video menggunakan AES-256-GCM dengan kunci AES256 yang dibuat secara acak. HomeKit juga membuat bingkai poster untuk setiap klip dan bingkai poster



](https://help.apple.com/pdf/security/id_ID/apple-platform-security-guide-id.pdf#48#42)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

HomeKit มีกลไกแบบต้นทางที่ปลายทางที่ปลอดภัยและเป็นส่วนตัวในการบันทึก วิเคราะห์ และแสดงคลิปจาก กล่อง IP ใน HomeKit โดยไม่เปิดเผยเ...

HomeKit มีกลไกแบบต้นทางที่ปลายทางที่ปลอดภัยและเป็นส่วนตัวในการบันทึก วิเคราะห์ และแสดงคลิปจาก กล่อง IP ใน HomeKit โดยไม่เปิดเผยเนื้อหาวิดีโอนั้นให้กับ ... หรือบุคคลหรือบริษัทอื่นๆ เมื่อตรวจพบ การเคลื่อนไหวโดยกล่อง IP คลิปวิดีโอจะถูกส่งโดยตรงไปยังอุปกรณ์ ... ที่มีกุญแจ AES256



](https://help.apple.com/pdf/security/th_TH/apple-platform-security-guide-th.pdf#79#69)[

![](https://cdn.deepseek.com/site-icons/uspto.gov)

ptacts.uspto.gov

<table><tr><td>Claim-8,230,101</td><td>Exemplary Supporting Evidence Regarding Apple&#x27;s Accused Products</td></tr><tr><td></...

security<br>Cameras that have an Internet Protocol address (IP address) in ... The streams are encrypted using randomly generated keys on the device and an Internet Protocol camera (or IP camera), and they&#x27;re ... t on the local network, the encrypted streams are relayed through the home hub to the device. ... When an app ... HomeKit renders the video frames



](https://ptacts.uspto.gov/ptacts/public-informations/petitions/1558006/download-documents?artifactId=Tlenkx7K99jeqOSzll38VBzngzwLInDna-qDNhg2mu_RWWFkKjid9YY#3#2)[

![](https://cdn.deepseek.com/site-icons/macrumors.com)

MacRumors

2026/09/03

Apple Planning AI Home Security Camera and Service for 2027 - Skip to Content

Apple already has HomeKit Secure Video, an Apple Home feature for third-party cameras. HomeKit Secure Video features end-to-end encryption and uses iCloud to securely stream and store video from compatible HomeKit cameras. In iOS 27 ... iCloud+ and Apple's existing HomeKit Secure Video features.



](https://www.macrumors.com/2026/09/04/apple-home-security-camera-2027/?ref=weloveapple.se#1)[

![](https://cdn.deepseek.com/site-icons/macrumors.com)

MacRumors

2026/09/03

MacRumors: Apple News and Rumors - Apple could release a home security system and service in 2027, according to Bloomberg

Apple already has HomeKit Secure Video, an Apple Home feature for third-party cameras. HomeKit Secure Video features end-to-end encryption and uses iCloud to securely stream and store video from compatible HomeKit cameras. ... The new features require a 2TB or higher iCloud+ plan ... plan or better. It's



](https://www.macrumors.com/?app_v2=true%25252525252525252F%25252525252525252F%252525252525252F%25252F%25252F%252F#2)[

![](https://cdn.deepseek.com/site-icons/ifeng.com)

凤凰网科技

2026/09/04

主打隐私保护：消息称苹果首款AI家用安防摄像头瞄准2027年发布

科技媒体 9to5Mac 此前指出，苹果在 iOS 27 系统中，升级 HomeKit 的安全视频（Secure Video）功能，带来以下 4 项改进，预估会在新款安防摄像头上实现 ... 该功能面向兼容 HomeKit 的第三方摄像头提供视频传输和存储能力。该功能采用端到端加密，并通过 iCloud 处理兼容摄像头的视频流与存储。



](https://tech.ifeng.com/c/8wAANtymmGH)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/02/11

Is Alexa Safe to Use in Your Home Today?

How to Protect Your Privacy With Alexa ... As of March 28, 2025, all Amazon Echo device recordings go to Amazon's cloud servers, even if you had that "do not send" feature enabled. ... so you should take steps to prevent your smart home from getting hacked.



](https://tech.yahoo.com/home/articles/alexa-safe-home-today-190000407.html#1)[

![](https://cdn.deepseek.com/site-icons/pcrisk.com)

PCrisk.com

2026/07/23

How to stop Alexa from spying on you in 5 steps - We may earn commissions from products we recommend

Tap "More." - Select "Settings." - Open "Alexa Privacy." - Select "Manage Your Alexa Data." ... Amazon says text transcripts and typed requests can stay for up to 30 days unless you delete them yourself. Other records ... Amazon lets you delete recordings after 3 or 18 months.



](https://www.pcrisk.com/blog/tips/14078-does-alexa-spy-on-you#1)[

![](https://cdn.deepseek.com/site-icons/bgr.com)

Boy Genius Report

2026/01/30

Is Your Amazon Echo Always Listening? - BGR - Is Your Amazon Echo Always Listening?

For greater privacy, create a set time period after which your voice recordings automatically delete. ... Find this in Settings, Alexa Privacy, Manage Your Alexa Data, Voice Recordings, then Choose how long to save recordings. Choose to never save recordings or select a length of time, such as three months.



](https://www.bgr.com/2084401/does-amazon-echo-always-listen/#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com.br)

Amazon.com.br

Perguntas Frequentes sobre Alexa e os Dispositivos Alexa - 2. Quais informações Alexa recebe dos meus dispositivos de casa inteligente?

Você pode excluir as informações de status e uso associadas à sua conta Alexa para dispositivos de casa inteligente de terceiros de uma só vez, ou excluí-las automaticamente depois de 3 ou 18 meses, por meio de Configurações > Privacidade ... Se você optar por deletar automaticamente as informações após 3 ou 18 meses, podemos também reter informações agregadas



](https://www.amazon.com.br/gp/help/customer/display.html?nodeId=201602230#4)[

![](https://cdn.deepseek.com/site-icons/amazon.ae)

Amazon.ae

الأسئلة الشائعة حول Alexa وجهاز Alexa - يمكنك حذف معلومات حالة الجهاز والاستخدام المرتبطة بحسابك على Alexa لأجهزة المنزل الذكي التابعة لطرف ثالث كلها مرة واحدة أو حذفها...

يمكنك حذف معلومات حالة الجهاز والاستخدام المرتبطة بحسابك على Alexa لأجهزة المنزل الذكي ... كلها مرة واحدة أو ... 3 أشهر أو 18 شهراً من ... وإذا اخترت حذف المعلومات تلقائياً بعد مضي 3 أشهر أو 18 شهراً، يجوز لنا أيضاً الاحتفاظ بمعلومات مجمعة عن كيفية استخدامك لجهاز (أجهزة) المنزل الذكي بمرور الوقت (على سبيل المثال، المعلومات التي ... تشغيل مصباح مُعين في الغالب مساءً).



](https://www.amazon.ae/-/ar/gp/help/customer/display.html?nodeId=201602230#3)[

![](https://cdn.deepseek.com/site-icons/amazon.in)

Amazon.in

Alexa, Echo Devices, and Your Privacy - Alexa, Echo Devices, and Your Privacy

Yes. ... and typed requests to Alexa after a specified period of time (3 or 18 months) ... requests will be retained for 30 days after your last interaction with Alexa in a given chat ... We may still retain other records of your Alexa interactions, such as attachments you shared with Alexa, information you provided through your interactions...



](https://www.amazon.in/-/hi/gp/help/customer/display.html?nodeId=GVP69FUJ48X9DK8V#1)[

![](https://cdn.deepseek.com/site-icons/dailydot.com)

The Daily Dot

2026/02/16

"I'm embarrassed": Millennial dad unplugs his Amazon Echo after Gen Z daughter shows him something disturbing

"Customers can choose not to save their voice recordings at all or have their recordings automatically deleted on an ongoing three- or 18-month basis." Amazon users can access the Alexa Privacy dashboard, where they’re able to review settings and choose how recordings are stored or deleted.



](https://dailydot.com/millennial-dad-unplugs-amazon-echo-reddit)[

![](https://cdn.deepseek.com/site-icons/amazon.it)

amazon.it

Alexa, Dispositivi Echo e la tua privacy - Alexa, Dispositivi Echo e la tua privacy

Sì. ... le trascrizioni di testo e le richieste digitate ad Alexa dopo un determinato periodo di tempo (3 o 18 mesi) ... Tuttavia, le trascrizioni di testo di tali registrazioni e le eventuali richieste digitate saranno conservate per 30 giorni, dopoché verranno eliminate automaticamente.



](https://www.cdn.amazon.it/gp/help/customer/display.html?nodeId=GVP69FUJ48X9DK8V#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/02/16

“I’m embarrassed”: Millennial dad unplugs his Amazon Echo after Gen Z daughter shows him something disturbing

A millennial dad said he removed all Amazon Echo devices from his home after his Gen Z daughter showed him that Alexa had stored hundreds of voice recordings without his knowledge. u/attachedheartthe



](https://tech.yahoo.com/cybersecurity/articles/m-embarrassed-millennial-dad-unplugs-110000265.html#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Actualizaciones de seguridad y resultados de validación de la seguridad de los dispositivos de Google para hogares conectados

Actualizaciones de seguridad y resultados de validación de la seguridad de los dispositivos de Google para hogares conectados Los dispositivos Google Nest para hogares conectados recibirán actualizaciones de seguridad automáticas durante al menos 5 años a partir de la fecha en la que los empecemos a vender en Google Store de EE. UU.



](https://support.google.com/product-documentation/answer/10231940?hl=ES#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Google 智慧聯網家庭裝置的安全性更新和安全性驗證結果 - 針對何項內容提供意見：

Google 智慧聯網家庭裝置的安全性更新和安全性驗證結果 自 Google Nest 智慧聯網家庭裝置在美國 Google 商店上架日起算，使用者可享至少 5 年的自動安全性更新服務。安全性更新可解決 Google Nest 的已知重大問題，以遠端軟體更新進行修補。



](https://support.google.com/product-documentation/answer/10231940?hl=zh-Hant&ref_topic=10123615#1)[

![](https://cdn.deepseek.com/site-icons/eweek.com)

eWEEK

2026/06/21

Google Retires Nest Mini and Nest Audio: What This Means for Owners - Google Retires Nest Mini and Nest Audio: What This Means for Owners

Google told TechRadar that both speakers will continue receiving software updates, security patches, and customer support. ... Google has not announced an end-of-support date, leaving open the question of how long older hardware will receive new features compared with upcoming Gemini-native devices.



](https://www.eweek.com/de/google/google-retires-nest-mini-nest-audio-device-support/#1)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/05/21

Google Archive for May 2026 - Page 2 | The Verge - Skip to main content

9to5Google reported Friday morning that a Nest support page had been updated to say that nearly all Chromecast devices except for the most recent one that was released in 2022 were no longer receiving critical security updates. Later, the page changed back and once again shows



](https://on.theverge.com/archives/google/2026/5/2#1)[

![](https://cdn.deepseek.com/site-icons/tecnoandroid.it)

TecnoAndroid

2025/04/29

Google Nest, stop al supporto per alcuni prodotti: la lista ufficiale - Menu

A partire dal 25 ottobre 2025, alcuni prodotti non riceveranno più aggiornamenti software né assistenza tecnica, segnando la conclusione ufficiale del loro ciclo di vita. ... A partire dal 25 ottobre 2025, gli utenti dei dispositivi interessati non riceveranno più...



](https://www.tecnoandroid.it/news/google-nest-stop-supporto-25-ottobre-2025-dispositivi-lista-1557355/#1)[

![](https://cdn.deepseek.com/site-icons/howtogeek.com)

How-To Geek

2025/12/27

These smart home devices are officially too old for 2026 - These smart home devices are officially too old for 2026

As of October 25, 2025, Google has officially retired its first and second-generation Nest Learning Thermostats. ... Google has pulled support entirely, which means no more software updates. That also means no more security patches, which is a concern if your thermostat is still able to access the wider internet.



](https://www.howtogeek.com/these-smart-home-devices-are-officially-too-old-for-2026/#1)[

M3

2026/05/21

Google lägger av med säkerhetsuppdateringar för de flesta Chromecast-enheterna

Google har uppdaterat supportsidan för säkerhetsuppdateringar för Nest- och Chromecast-enheter ... Enheten lanserades den 22 september 2022, de fem garanterade åren av säkerhetsuppdateringar löper ut först 2027.



](https://www.m3.se/article/3146986#primary)[

PCMag UK

2025/03/28

Google Discontinues Nest Protect Smart Smoke Alarm - PCMag editors select and review products independently

The smart smoke alarm will continue to work and receive updates until its expiration date, and you can still pick one up until the current stock runs out. ... Both devices will continue to receive security updates and continue to work as normal through to their expiration dates.



](https://uk.pcmag.com/home-security/157319/google-discontinues-nest-protect-smart-smoke-alarm#1)[

Mobiili.fi

2025/04/27

Google lopettaa päivitykset ensimmäisille Nest-termostaateille – vetäytyy tuotesarjan osalta Euroopan markkinoilta

Petri Tapala | Julkaistu ma 28.4.2025, klo 19:48 Google lakkauttaa Nest-termostaattien tuoteryhmän myynnin Euroopassa. Samalla päivitystuki vanhoille malleille päättyy. Ensimmäisen ja toisen sukupol



](https://mobiili.fi/2025/04/28/google-lopettaa-paivitykset-ensimmaisille-nest-termostaateille-vetaytyy-tuotesarjan-osalta-euroopan-markkinoilta/)[

![](https://cdn.deepseek.com/site-icons/techlusive.in)

Techlusive

2025/08/24

Samsung Expands One UI Beyond Phones: 7-Year Updates and Smarter Features Coming to Home Appliances - Select Your Language

From September, Samsung will roll out updates to 2024-launched appliances, upgrading the security with Knox Matrix. It uses ... Appliances that come with a display will also get features like Passkey support and a Knox Security dashboard for real-time monitoring.



](https://www.techlusive.in/news/samsung-expands-one-ui-beyond-phones-7-year-updates-and-smarter-features-coming-to-home-appliances-one-ui-now-links-smartphones-tvs-and-smart-home-appliances-together-features-updates-and-more-1590186/amp/#1)[

phaidra.ustp.at

liance state that, among others, their brand Matter may only be used on Alliance certified Products, which comply with these Gui...

Samsung states [146] that OS updates for the TV are available for up to 7 years from the products release date and security software updates are guaranteed for at least three years from product launch. In order to receive OS updates ... In the case of receiving security software updates, the user must be connected to the Samsung TV via



](https://phaidra.ustp.at/api/object/o:7799/download#17#13)[

![](https://cdn.deepseek.com/site-icons/securitybrief.asia)

SecurityBrief Asia

2025/09/16

Samsung extends One UI & seven-year updates to smart appliances

This initiative will see select Samsung home appliances benefit from up to seven years of software updates ... and commencing updates in September. ... Device connectivity is also enhanced via SmartThings ... Wi-Fi-enabled Samsung appliances will be eligible for up to seven years of software updates from launch. According to the company, this ensures ongoing value by expanding features and maintaining security long after purchase.



](https://securitybrief.asia/story/samsung-extends-one-ui-seven-year-updates-to-smart-appliances)[

![](https://cdn.deepseek.com/site-icons/bacninhtv.vn)

Đài Phát thanh và Truyền hình Bắc Ninh

2025/08/25

Samsung mở rộng chương trình hỗ trợ 7 năm cập nhật

Samsung TV Plus và các chức năng SmartThings được cải tiến, bao gồm Chăm sóc gia đình ... Trong thông báo của mình, Samsung cho biết chính sách 7 năm cập nhật bảo mật của họ sẽ áp dụng cho các thiết bị hỗ trợ Wi-Fi ra mắt từ năm 2024 trở đi.



](https://bacninhtv.vn/tin-tuc/213/184963/samsung-mo-rong-chuong-trinh-ho-tro-7-nam-cap-nhat)[

![](https://cdn.deepseek.com/site-icons/udn.com)

udn科技玩家

2025/08/28

三星將One UI延伸至智慧家電 7年更新承諾讓冰箱、洗衣機也能長期進化 | udn科技玩家

三星同時承諾，所有支援 Wi-Fi的智慧家電，自2024年起上市的型號都將享有最長達7年的軟體更新。首波更新將在今年9月針對2024年推出的智慧家電陸續釋出，更新項目則涵蓋安全性、智慧功能 與介面設計三大面向。



](https://tech.udn.com/tech/story/123152/8969947)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

news.samsung.com

SAMSUNG

SmartThings亦強化裝置連線能力，將家庭設備完美整合至生態圈，讓用戶可輕鬆存取FamilyCare ... 三星承諾，自2024年起上市且具備Wi- Fi功能的智慧家電，將可在上市後享有長達7年的軟體更新。確保產品於整個生命週期內維持耐用性、效能與安全保障。



](https://news.samsung.com/tw/wp-content/themes/btr_newsroom/download.php?id=fAxR5xaTCpBFeHrtYNoQKncIe2h9FIPFzKNa3EsW0Ao%3D#1#1)[

![](https://cdn.deepseek.com/site-icons/securitybrief.co.uk)

SecurityBrief UK

2025/09/16

Samsung extends One UI & seven-year updates to smart appliances

This initiative will see select Samsung home appliances benefit from up to seven years of software updates, starting with products launched in 2024 and commencing updates in September. ... Wi-Fi-enabled Samsung appliances will be eligible for up to seven years of software updates from launch. According to the company...



](https://securitybrief.co.uk/story/samsung-extends-one-ui-seven-year-updates-to-smart-appliances)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

news.samsung.com

Samsung Knox 全星守護智慧居家

Samsung smart TV are guaranteed a minimum of three years of software updates from the product’s launch date. ... *電視連接網路時即可獲得更新。 **三星智慧電視保證自上市日期起可獲得至少三年的軟體更新。另可獲得進一步的安全更新，以修補重要問題。



](https://news.samsung.com/tw/wp-content/themes/btr_newsroom/download.php?id=U4G33M3a%2BKdlHgL%2FkDX9vncIe2h9FIPFzKNa3EsW0Ao%3D#1#1)[

![](https://cdn.deepseek.com/site-icons/thanhnien.vn)

Báo Thanh Niên

2025/08/25

Samsung mở rộng chương trình hỗ trợ 7 năm cập nhật

Tủ lạnh hoặc máy giặt thông minh mà Samsung cung cấp ra thị trường gần đây cũng được hưởng chính sách cập nhật mở rộng. Samsung đã gây chú ý trong ngành công nghệ khi công bố chính sách cập nhật hệ đ



](https://thanhnien.vn/samsung-mo-rong-chuong-trinh-ho-tro-7-nam-cap-nhat-185250825223202192.htm)[

![](https://cdn.deepseek.com/site-icons/xtool.com)

xTool UK

UK PSTI Information - UK PSTI Information

Here you can find our Statement of Compliance, made in accordance with the Cyber Security (Security Standards for Smart Devices) Rules 2025 authorised by the Cyber Security Act 2024 ... Product Type | Product Model | Minimum Support Period | Statement of Compliance ... MXP-K019-001 | 31/12/2031



](https://uk.xtool.com/pages/uk-psti-information#1)[

![](https://cdn.deepseek.com/site-icons/bsigroup.com)

v1.bsigroup.com

US product cybersecurity – PSTI Act

Manufacturers must provide information about product security update support periods. This world-leading product cybersecurity regime will come into effect on 29 April 2024. ... | Information on minimum security update periods | 5.3-13 |



](https://v1.bsigroup.com/siteassets/pdf/en/products-and-services/bsi-psti-client-a4-flyer-engb-apr-2024-v3.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/parliament.uk)

UK Parliament

2023/07/13

Written questions and answers - Written questions, answers and statements - UK Parliament

the minimum length of time a smart product sold via their website will receive security updates. ... When the Product Security and Telecommunications Infrastructure Act’s product security regime comes into effect, manufacturers will be required to publish the minimum period of time the product will receive security updates for (the “defined support period”), including in a ‘statement of compliance’ that accompanies the product.



](https://questions-statements.parliament.uk/written-questions/detail/2023-07-14/194187)[

![](https://cdn.deepseek.com/site-icons/hytera.com)

Hytera

2024/04/28

Konformitätserklärung (SoC)

dem britischen PSTI-Gesetz von 2022 und den PSTI-Vorschriften von 2023 entsprechen. ... Product Type | Model | Support Period ---|---|--- POC | PNC360S | 29 April 2024 to 31 December 2027



](https://www.hytera.com/de/psti-compliance.html)[

![](https://cdn.deepseek.com/site-icons/etsi.org)

docbox.etsi.org

Overview of the PSTI (Product Security) Regime

The PSTI Regulations 2023 will come into effect on 29 April 2024, following a 12 month transition period, requiring manufacturers, importers and distributors of consumer connectable / IoT products to comply with minimum security requirements. ... Transparency with consumers on the **minimum length of time they will receive security updates**



](https://docbox.etsi.org/Workshop/2023/10_ETSISECURITYCONFERENCE/D2-2_IOTandCERTIFICATION/DSIT_DHOLIWAR.pdf#1#1)[

opsf.org

2026/03/19

Internet of Things and Connected Devices | PCT Specification

ban on universal default passwords, vulnerability disclosure policy, and defined minimum security update support period. In force 29 April 2024. ... security_update_support_end_date | string (ISO 8601 date) | OPTIONAL | The minimum security update support end date for this product.



](https://pctspec.opsf.org/v0.2-draft.3/extensions/x-iot/#revision-notes)[

![](https://cdn.deepseek.com/site-icons/ncsc.gov.uk)

ncsc.gov.uk

Smart devices: new law helps citizens to choose secure products

From 29 April 2024, manufacturers of consumer ‘smart’ devices must comply with new UK law. The law, known as ... 3. The manufacturer must state the minimum length of time for which the device will receive important security updates.



](https://www.ncsc.gov.uk/pdfs/blog-post/smart-devices-law.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/itu.int)

itu.int

Overview of the PSTI (Product Security) regime (1/2)

Government will provide a 12 month transition period for businesses to adjust their business practices. ... - This legislation was published on 29 April 2023 triggering the start of a 12 month transition period before the PSTI (Product Security) regime comes into effect on **29 April 2024**.



](https://www.itu.int/dms_pub/itu-d/oth/07/2e/D072E0000090014PDFE.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/parliament.uk)

UK Parliament

2023/05/01

Written statements - Written questions, answers and statements - UK Parliament

Manufacturers and other businesses in the supply chain of these products now have 12 months to transition their businesses to comply with these new security requirements. ... - Manufacturers will also be required to ensure that a customer is made aware of a product’s security update support period before allowing them to purchase the product on the manufacturer’s website.



](https://questions-statements.parliament.uk/written-statements/detail/2023-05-02/hlws741)[

BTL Inc.

BTL检测集团 - Location：Home - Technical platform - UK PSTI Security and Compliance Interpretation

3. Security update support period — Manufacturers must publish the minimum security update support period for the product and must not shorten it. If the support period is extended, the new period must be promptly updated and republished. The notice of the security update support period should be presented in a way that can be understood without prior technical knowledge.



](https://www.newbtl.com/industryshow.php?id=682#1)[

Blog | Safeguard — Software Supply Chain Security Insights

2026/04/01

California SB-327 IoT Security Enforcement Update

California SB-327 was the first state-level IoT security statute in the United States when it took effect in 2020 ... SB-327 requires manufacturers of connected devices to equip the device with a "reasonable security feature" appropriate to the nature and function of the device, the information it may collect...



](https://safeguard.sh/resources/blog/california-sb-327-iot-security-enforcement-update)[

![](https://cdn.deepseek.com/site-icons/cov.com)

cov.com

LAW360

refrigerators and a range of other devices that connect to the internet as part of the rapidly growing "internet of things" would be required under Senate Bill 327 to equip products with "reasonable security features." That includes ensuring that passwords are not as easy to hack.



](https://www.cov.com/-/media/files/corporate/publications/2018/09/calif_starts_ball_rolling_with_novel_internet_of_things_law.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/businesslawtoday.org)

Business Law Today

2018/11/27

Security by Design: California’s New IoT Security Laws - Business Law Today from ABA

These two new substantially similar IoT laws (California Senate Bill 327, chapter 886 and Assembly Bill No. 1906, “Security of Connected Devices” (2018 Cal. Legis. ... 327)(to be codified at Cal.



](https://businesslawtoday.org/2018/11/security-design-californias-new-iot-security-laws/?__hstc=221931271.62dde0e6ade0fbb5f69545322973fc21.1548849326758.1548849326758.1548849326758.1&__hssc=221931271.1.1548849326758&__hsfp=858295836&hsCtaTracking=caafbbee-e787-4b39-af9a-98db27272449%7Ca6bbf04e-c1d7-4810-a004-4fc8f4c6dd06#respond)[

![](https://cdn.deepseek.com/site-icons/harvard.edu)

Harvard Journal of Law & Technology

2018/10/07

Is Your Smart Thermostat Safe from Hackers? California’s New Internet-of-Things Cybersecurity Law Seeks to Address the Issue - Is Your Smart Thermostat Safe from Hackers? California’s New Internet-of-Things Cybersecurity Law Seeks to Address the Issue

On September 28, 2018, California Governor Jerry Brown signed into law Senate Bill 327 (“SB 327”) ... SB 327 requires manufacturers to include “reasonable security features” on any device that connects to the internet via IP or Bluetooth.



](https://jolt.law.harvard.edu/digest/is-your-smart-thermostat-safe-from-hackers-californias-new-internet-of-things-cybersecurity-law-seeks-to-address-the-issue?_x_tr_sch=http#1)[

![](https://cdn.deepseek.com/site-icons/iotforall.com)

IoT For All

2024/11/19

Regulation Alone Won't Secure IoT-Enabled Devices | IoT For All

The tide of regulation began with California, who instituted a new law called SB-327 back in 2018 that requires manufacturers to equip IoT devices with “reasonable” security features. Now, all IoT devices sold in the state—and by extension, the rest ... unique password or force users to create one.



](https://www.iotforall.com/regulation-secure-iot-enabled-devices)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

rww2021.iot.ieee.org

- Cybersecurity Event Logging: IoT devices should log cybersecurity events and make the logs accessible to the owner or manufact...

California Senate Bill 327-"Security of Connected Devices"(Effective Jan ... United States – CA Senate Bill 327 “Security of Connected Devices” - Specifies the security obligations of “manufacturers” of “connected devices” ... - If a connected device is equipped with a means for authentication outside a local area network, it shall be deemed



](https://rww2021.iot.ieee.org/wp-content/uploads/sites/276/2021/01/Martin-Zoltick-Feeling-Insecure-Legal-and-Regulatory-Landscape-Reasonable-Security-Features-for-IoT-and-Connected-Devices.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/acm.org)

Association for Computing Machinery

Communications of the ACM - May 2019 - 24

ability for systems to fail predictably and safely, the use of standard protocols, the ability to preserve offline functionality, and widespread encryption and authentication of data. He also believe



](https://mags.acm.org/communications/may_2019?pm=2&u1=texterity&linkImageSrc=undefined/&pg=24#pg24)[

![](https://cdn.deepseek.com/site-icons/squirepattonboggs.com)

squirepattonboggs.com

SOUIRE

PATTON BOGGS California Passes First Cybersecurity Law Regulating IoT Devices California has become the first state in the US to adopt a cybersecurity law governing Internet of Things (IoT) devices.



](https://www.squirepattonboggs.com/~/media/files/insights/publications/2018/10/california-passes-first-cybersecurity-law-regulating-iot-devices/california-passes-first-cybersecurity-law-regulating-iot-devices.pdf#1#1)[

yjolt.org

Later, in September 2018, California enacted the California Internet of Things (IoT) Security Law, which sets a new benchmark fo...

Later, in September 2018, California enacted the California Internet of Things (IoT) Security Law, which sets a new benchmark for other states to follow. This law requires all connected devices to hav



](https://yjolt.org/sites/default/files/shackelford_scott_et_al._-_reasonable_cybersecurity.86.pdf#9#5)[

![](https://cdn.deepseek.com/site-icons/natlawreview.com)

natlawreview.com

Published on The National Law Review https://natlawreview

Published on The National Law Review https://natlawreview.com # California Enacts First IoT Cybersecurity Law Article By: Tracy P. Marshall Sheila A. Millar Security-by-design will soon be mandat



](https://natlawreview.com/node/102280/printable/pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2025/01/28

OTA 概览 | Matter | Google Home Developers

Matter 设备（即 OTA 请求者）会定期轮询 OTA 提供方，以了解是否有可用的软件更新 ... 对于已关联到 Matter 中枢但未在 Developer Console 中注册的 Matter 设备，系统会自动推送 OTA 更新 ... - 通过 Developer Console 或 Alliance 分布式合规设备总账 (DCL) 上传固件以进行 OTA 分发。



](https://developers.home.google.com/matter/ota?hl=zh-cn)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2025/01/28

نظرة عامة على OTA | Matter | Google Home Developers

يتضمّن كل تكامل Matter في Google Home Developer Console إعدادًا خاصًا بالتحديث عبر الأثير (OTA). ... تكون عملية تحديث البرامج عبر الأثير (OTA) ... عن المعلومات المخزّنة في Allianceسجلّ الامتثال الموزّع (DCL)، والذي يهدف إلى ضمان صحة الجهاز والامتثال للبروتوكول.



](https://developers.home.google.com/matter/ota?hl=ar)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2025/01/28

Omówienie OTA | Matter | Google Home Developers

Każda integracja Matter w Google Home Developer Console ma własną konfigurację aktualizacji bezprzewodowych (OTA). ... Urządzenie Matter Matter (żądający aktualizacji OTA) okresowo wysyła zapytania do dostawcy aktualizacji OTA, aby sprawdzić, czy są dostępne aktualizacje oprogramowania.



](https://developers.home.google.com/matter/ota?authuser=7&hl=pl)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

Matter はローカルデバイスの相互運用性を処理しますが、クラウド接続を追加すると、いくつかの

O ver-the-air (OTA) 更新 – インターネット経由でファームウェアとソフトウェアの更新を配信する ... Matter 標準では、OTA 更新の処理方法と Matter 認定エンドポイントへ ... Matterデバイスの各ファームウェア更新は、製造元のプライベートキーによって署名される必要があります。デバイスは...



](https://docs.aws.amazon.com/ja_jp/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#understanding-matter#10#3)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

虽然Matter支持基本的本地设备互操作性，但还需要额外的云连接才能提供强大的over- the- air更新、遥测数据、远程管理以及与专有供应商服务的集成

·Over- the- air（OTA）更新—通过互联网提供固件和软件更新使供应商能够轻松增强已经部署的设备。如果没有OTA ... Matter设备的每次固件更新都必须由制造商的私钥签名。设备使用相应的非对称公钥来验证有效载荷签名。



](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#6#2)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

重要装置必须對彼此和控制器進行身分驗證，才能進行通訊

事項標準也要求裝置實作強大的安全狀態，以進行over- the- air(OTA)更新。OTA是智慧家庭生態系統的關鍵部分，因此裝置可以接收安全更新以及新功能。每個Matter裝置的體更新都必須由製造商的私有金鑰簽署。裝置會使用對應的非對稱公有金鑰來驗證承載簽章 ... 不過，製造商應該注意，Matter的OTA機制在循序更新和復原功能方面具有限制。對於需要精細更新控制...



](https://docs.aws.amazon.com/zh_tw/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic Developer Academy

2026/04/21

Matter Over-The-Air software update - Nordic Developer Academy

Feedback If you are having issues with the exercises, please create a ticket on DevZone: devzone.nordicsemi.com Drag & Drop Files, Choose Files to Upload You can upload up to 2 files. Eng日本語 # Mat



](https://academy.nordicsemi.com/courses/matter-fundamentals/lessons/lesson-5-matter-over-the-air/topic/matter-over-the-air-software-update/?version=v3.3.0)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic Developer Academy

2026/04/21

Exercise 1 - Upgrading firmware using Matter OTA - Nordic Developer Academy

Feedback If you are having issues with the exercises, please create a ticket on DevZone: devzone.nordicsemi.com Drag & Drop Files, Choose Files to Upload You can upload up to 2 files. Eng日本語 # Exe



](https://academy.nordicsemi.com/courses/matter-fundamentals/lessons/lesson-5-matter-over-the-air/topic/exercise-1-upgrading-firmware-using-matter-ota/#login)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/06

matterjs-server/docs/websockets_api.md at main · matter-js/matterjs-server - set_node_binding - Set bindings on a node endpoint

set_node_binding - Set bindings on a node endpoint { "message_id": "1", "command": "set_node_binding", "args": { "node_id": 1, "endpoint": 1, "bindings": [ { "node": 2



](https://github.com/matter-js/matterjs-server/blob/main/docs/websockets_api.md#2)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon AWS Documentation

Security - Security

Security by design is the practice of incorporating security functions during the device design stage, rather than as an afterthought during the later stages of development. Encrypted communication an



](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/security.html#1)[

![](https://cdn.deepseek.com/site-icons/sciencedirect.com)

ScienceDirect.com

Based Serial Communication - In [183] three types of attacks on ZigBee were demonstrated using the KillerBee toolkit [184]

In [183] three types of attacks on ZigBee were demonstrated using the KillerBee toolkit [184]. ... Z-Wave vulnerabilities may depend on implementation practices, firmware, and hardware. Using reverse engineering methods, Fouladi et al. ... The attack used Z-force ... The researchers describe the issue as a lack of ‘state validation’ in some Z-Wave devices.



](https://www.sciencedirect.com/topics/engineering/based-serial-communication#2)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2018/01/07

Security survey of the IoT wireless protocols

In this paper, we present our survey of the security of the four widely used IoT protocols: Bluetooth Low Energy, LoRaWAN, ZigBee and Z-Wave. We discuss various vulnerabilities in the protocols and how the protocols evolved from the security point of view.



](https://ieeexplore.ieee.org/abstract/document/8249286)[

![](https://cdn.deepseek.com/site-icons/semanticscholar.org)

Semantic Scholar

2020/04/05

[PDF] A State-of-the-Art Review on the Security of Mainstream IoT Wireless PAN Protocol Stacks | Semantic Scholar - The work in [ 56] capitalizes on a vulnerability to allow the placement of a rogue controller into the

The work in [ 56] capitalizes on a vulnerability to allow the placement of a rogue controller into the ... The authors of [ 58 ] demonstrated that it is possible to send unauthorized commands to Z-Wave S2 certified products by forcing them to use the less secure Z-Wave S0 protocol and manipulating the ... [65] dredged up a critical vulnerability in ZigBee



](https://www.semanticscholar.org/reader/f836cc7c35f5889345a74b2f9abb4b006751a212#5)[

![](https://cdn.deepseek.com/site-icons/bsuir.by)

libeldoc.bsuir.by

Если в здании есть система умного дома, то, очень вероятно, что ис- пользуется протокол ZigBee

Однако несколько лет назад он был взломан специалистами по безопасности на конференции хакеров «Vegas Black Hat USA 2013» и «Def Con 21» [2]. ... Конференции хакеров «Vegas Black Hat USA 2013» и «Def Con 21» – не единственный случай...



](https://libeldoc.bsuir.by/bitstream/123456789/33305/1/Kostyuchenko_Problemy.PDF#2#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2019/06/02

home automation - Much of the issue comes down to initialisation, where plaintext (or well-known keys which are equivalent) is used for the first ...

Specific exploits Z-Wave hit the news in spring 2018 with an attack call Z-Shave, which seemed damning but



](https://github.com/artmg/MuGammaPi/wiki/home-automation/0723352e85b93d20de2436e39192b20acc9b3b02#2)