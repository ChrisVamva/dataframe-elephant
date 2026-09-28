---
modified: 2026-09-28T20:50:54+03:00
---
# Smart-Home Product Security and Privacy Lifecycle Scorecard

## Scoring Rubric

Each product is assessed across 14 lifecycle controls. Two scores are assigned per control:

- **Control Maturity (CM):** 0–3 scale measuring how well the control is implemented.
- **Evidence Quality (EQ):** 0–3 scale measuring how well the implementation is documented, tested, or independently verified.

| CM Score | Definition | EQ Score | Definition |
|---|---|---|---|
| **3** | Control is implemented, enforced by design, and verified by independent testing or certification | **3** | Independent laboratory testing, regulatory filing, or peer-reviewed study confirms the control |
| **2** | Control is implemented and documented, but not independently verified | **2** | Vendor documentation, certification record, or third-party audit exists |
| **1** | Control is partially implemented or inconsistently enforced | **1** | Vendor claims only; no independent verification |
| **0** | Control is absent, not documented, or actively contradicted by evidence | **0** | No evidence, contradictory evidence, or evidence of failure |

**Penalty rule:** A control rated **CM 0 or 1** with **EQ 2–3** indicates a documented failure—the vendor claims the control exists, but evidence shows it does not work. These cases are flagged as **compliance without safety**.

**Composite Score:** Weighted average of CM scores across 14 controls, with weights reflecting household risk exposure.

| Control | Weight | Rationale |
|---|---|---|
| Identity and authentication | 1.0 | Foundation for all access control |
| MFA | 0.8 | Critical for account and device access |
| Secure onboarding | 1.0 | Entry point for device compromise |
| Encryption (transit and rest) | 1.0 | Protects data in motion and at rest |
| Network isolation | 0.7 | Limits lateral movement |
| Update delivery | 1.0 | Determines vulnerability window |
| Support-period disclosure | 0.8 | Enables informed purchasing |
| Vulnerability reporting | 0.8 | Determines response capability |
| Incident response | 0.7 | Determines recovery capability |
| Data retention | 0.7 | Limits exposure duration |
| Deletion and export | 0.7 | User control over data |
| Local control | 1.0 | Resilience against cloud failure |
| End-of-life handling | 0.8 | Determines device fate post-support |
| Ownership transfer | 0.7 | Prevents credential persistence |

**Maximum composite: 3.00. Minimum passing score for recommendation: 2.00, with no individual control below 1.0 and no "compliance without safety" flags.**


## Lifecycle Control Definitions

| # | Control | What It Measures | Key Evidence Sources |
|---|---|---|---|
| 1 | **Identity** | Unique device identity (certificate-based), user account authentication, session management | Matter DAC/NOC certificates ; vendor IAM documentation |
| 2 | **MFA** | Multi-factor authentication for account access and sensitive device actions (lock/unlock, camera disable) | Vendor security pages; independent testing |
| 3 | **Secure Onboarding** | Encrypted commissioning channel, device attestation, no default credentials, no plaintext transmission | Matter PASE ; consumer association tests  |
| 4 | **Encryption** | TLS for transit; AES for data at rest; end-to-end encryption for camera video | Product documentation; packet capture testing |
| 5 | **Network Isolation** | VLAN support, IoT network segmentation, Matter fabric separation | Router documentation; Matter fabric model |
| 6 | **Update Delivery** | Automatic OTA updates; signed firmware; anti-rollback; update frequency | Vendor support policies ; CVE evidence  |
| 7 | **Support-Period Disclosure** | Published security support period; clarity on end-of-support consequences | UK PSTI statements; vendor pages  |
| 8 | **Vulnerability Reporting** | Public VDP; security.txt; bug bounty; response SLA | Consumer Reports VDP survey ; vendor pages |
| 9 | **Incident Response** | PSIRT; CVE assignment; patch timeline; customer notification | CVE databases ; vendor advisories |
| 10 | **Data Retention** | Published retention periods; default retention settings; user control | Privacy policies; vendor documentation  |
| 11 | **Deletion and Export** | User-initiated deletion; data export; backup limitations; service degradation after deletion | Privacy policy analysis  |
| 12 | **Local Control** | Device functions without cloud; local automation; offline operation | Product documentation; outage testing |
| 13 | **End-of-Life Handling** | EoL/EoS disclosure; local fallback after cloud shutdown; migration path | Vendor EoL policies  |
| 14 | **Ownership Transfer** | Factory reset removes credentials; biometric templates erased; device usable by new owner | Vendor reset documentation  |


## Product Comparison

### Representative Products by Category

| Category | Product | Matter | Cloud Dependency |
|---|---|---|---|
| **Smart Lock** | Aqara Smart Lock U200 | Yes | Matter controller + Aqara cloud |
| **Smart Lock** | Kwikset Aura | No (BLE/Wi-Fi) | Kwikset cloud |
| **Camera** | eufy Indoor Cam S350 | No | Optional cloud; local hub |
| **Camera** | Ring Stick Up Cam | No | Ring cloud (required for clips) |
| **Hub** | Apple HomePod mini | Yes | iCloud (E2E encrypted) |
| **Hub** | Samsung SmartThings Station | Yes | Samsung cloud |
| **Router** | eero Pro 7 | Yes (Thread/Zigbee) | Amazon cloud (optional) |
| **Appliance** | Samsung Bespoke AI Washer | Yes (SmartThings) | Samsung cloud |
| **Energy Device** | Span.IO Panel | No | Span cloud |
| **AI Assistant** | Amazon Echo (Alexa+) | Yes | Amazon cloud (required) |

### Scorecard Results

| Control | Aqara U200 | Kwikset Aura | eufy S350 | Ring Stick Up | Apple HomePod | Samsung Station | eero Pro 7 | Samsung Washer | Span.IO | Amazon Echo |
|---|---|---|---|---|---|---|---|---|---|---|
| **1. Identity** | CM2/EQ2 | CM2/EQ1 | CM2/EQ2 | CM2/EQ2 | CM3/EQ3 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM2/EQ1 | CM2/EQ2 |
| **2. MFA** | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM2/EQ3 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ2 |
| **3. Secure Onboarding** | CM1/EQ2 ⚠ | CM2/EQ1 | CM2/EQ2 | CM2/EQ2 | CM3/EQ3 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM2/EQ2 |
| **4. Encryption** | CM1/EQ2 ⚠ | CM1/EQ1 | CM2/EQ2 | CM2/EQ2 | CM3/EQ3 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM2/EQ1 | CM2/EQ2 |
| **5. Network Isolation** | CM1/EQ1 | CM0/EQ0 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 |
| **6. Update Delivery** | CM1/EQ2 ⚠ | CM1/EQ1 | CM2/EQ2 | CM2/EQ2 | CM3/EQ3 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM2/EQ2 |
| **7. Support Disclosure** | CM0/EQ0 | CM0/EQ0 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 |
| **8. Vuln Reporting** | CM1/EQ1 | CM0/EQ0 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM0/EQ0 | CM2/EQ2 |
| **9. Incident Response** | CM1/EQ2 ⚠ | CM0/EQ0 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 |
| **10. Data Retention** | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM3/EQ3 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ2 |
| **11. Deletion/Export** | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 |
| **12. Local Control** | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM0/EQ0 | CM3/EQ3 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM0/EQ0 | CM0/EQ0 |
| **13. EoL Handling** | CM0/EQ0 | CM0/EQ0 | CM1/EQ1 | CM1/EQ1 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 | CM0/EQ0 | CM1/EQ1 |
| **14. Ownership Transfer** | CM1/EQ1 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM2/EQ2 | CM1/EQ1 | CM1/EQ1 | CM1/EQ1 |
| **Composite** | **1.00** | **0.94** | **1.48** | **1.24** | **2.48** | **1.52** | **1.75** | **1.26** | **0.83** | **1.31** |

**⚠ Flags:**
- **Aqara U200:** Secure onboarding and encryption rated CM1/EQ2—CVE-2025-65291 documents failure to validate server certificates, enabling MITM attacks . Update delivery rated CM1/EQ2—CVE-2025-65295 documents firmware signature validation failure .
- **Kwikset Aura:** No published VDP, no CVE history, no incident response documentation. Identity rated CM2/EQ1—BLE authentication process was reverse-engineered, indicating weak authentication .

**Highest scorer: Apple HomePod mini (2.48).** Driven by E2E encryption, local processing, zero-knowledge architecture, and independent verification. Still weak on MFA for device actions, data export granularity, and support-period disclosure.

**Lowest scorer: Span.IO Panel (0.83).** No Matter support, no local control, no vulnerability disclosure, no published retention policy. Critical energy infrastructure with limited lifecycle transparency.


## Missing Evidence

The following evidence gaps prevent confident scoring for several controls. These are not vendor failures—they are industry-wide evidence gaps that should be filled through independent testing.

| Control | Missing Evidence | Impact |
|---|---|---|
| **MFA for device actions** | No independent testing of whether lock/camera actions can be performed with account password alone | Critical for physical security products |
| **Network isolation** | No standard test methodology for measuring lateral movement risk in smart home networks | Affects all products |
| **Update delivery reliability** | No systematic data on OTA success rates, rollback capability, or update latency across brands | Determines real-world vulnerability window |
| **Incident response timelines** | No public data on time-to-patch for smart home CVEs | Affects all products |
| **Data retention after deletion** | No independent verification that deleted data is actually removed from backups | Affects cameras, hubs, assistants |
| **Ownership transfer completeness** | No testing of whether biometric templates, Wi-Fi credentials, and cloud tokens are fully erased on factory reset | Affects locks, cameras, hubs |
| **EoL local fallback** | No systematic testing of device behavior after cloud shutdown | Affects all cloud-dependent products |
| **Matter attestation revocation** | No documented process for revoking compromised device certificates | Affects all Matter devices  |


## Consumer Buying Guidance

### Products with Strong Lifecycle Controls

- **Apple HomeKit ecosystem (HomePod, Apple TV):** Best-in-class privacy architecture. HomeKit data is E2E encrypted via iCloud, Apple cannot access it, and camera video is processed locally on Apple TV or HomePod with AES-256-GCM encryption . Local control is reliable during internet outages. Best choice for households prioritizing privacy and offline resilience.

- **Samsung SmartThings with Knox Matrix:** Appliances and hubs with Knox Vault (dedicated hardware security chip) and Knox Matrix (blockchain-based trust chain) provide stronger device-level security than most competitors. UL Solutions "Diamond" certification for Samsung appliances is independently verified .

- **eero Pro 7 as router + Thread Border Router:** Router-integrated Matter control eliminates a separate hub. eero has a public bug bounty program via HackerOne . Good for households that want integrated networking and smart home control.

### Products with Significant Gaps

- **Aqara hubs and locks:** Multiple CVEs document unencrypted data upload, failed certificate validation, and firmware signature bypass . Avoid until vulnerabilities are patched and independently verified.

- **Ring cameras:** TAKE encryption (new default) limits law enforcement access, but Ring historically shared footage without consent and requires cloud subscription for clip storage . Not recommended for privacy-sensitive households.

- **Span.IO energy panel:** No Matter support, no local control, no vulnerability disclosure, no published data retention policy. Critical infrastructure with minimal lifecycle transparency. Avoid until controls are documented and independently verified.

- **Kwikset Aura smart lock:** No VDP, no CVE history, BLE authentication reverse-engineered. Insufficient evidence of secure design .

### Universal Recommendations for Any Purchase

1. **Check for a published support period.** If the vendor does not state how long security updates will be provided, assume no guaranteed support. UK PSTI compliance statements and CRA disclosures (from 2027) are the most reliable sources.
2. **Prefer Matter-certified devices with local control.** Matter PASE commissioning and device attestation are mandatory and independently verified . Matter devices can operate locally if the ecosystem supports it.
3. **Prefer products with a public VDP and security.txt.** Consumer Reports found that some companies want security reports but make it difficult to submit them . A monitored inbox and clear disclosure policy are minimum requirements.
4. **Avoid devices that require cloud for basic function.** If the device cannot lock, record, or control temperature without internet, it will become e-waste when the cloud shuts down.
5. **Factory-reset before disposal or transfer.** Verify that biometric templates, Wi-Fi credentials, and cloud tokens are erased. Vendor documentation varies widely on what a factory reset actually removes .


## Engineering Priorities

### Priority 1: Fix Documented Failures

| Failure | Product | Required Fix |
|---|---|---|
| Plaintext transmission of credentials and unlock commands | Aqara, 亚太天能, 阿尔法极光, 幻侣 | Enforce TLS 1.3 for all device-to-cloud and device-to-app communication |
| Firmware signature bypass | Aqara Hub M2/M3/G3 | Implement signature verification with anti-rollback protection  |
| Server certificate validation failure | Aqara Hub M2/M3/G3 | Enable TLS certificate pinning or validation  |
| Printed photo unlocks face recognition | 青稞, 博克, 幻侣 | Implement 3D liveness detection (structured light or binocular IR)  |
| IC card cloning | 12 of 19 lock models tested | Implement encrypted challenge-response for IC cards; do not use static UIDs  |
| Plaintext video transmission | TP-Link Tapo C210, D-Link DCS-8350LH | Encrypt all video streams by default  |

### Priority 2: Close Evidence Gaps

- **Publish support periods as contractual commitments**, not marketing claims. The CRA's five-year minimum (December 2027) will make this mandatory in the EU; voluntary compliance ahead of the deadline builds trust.
- **Implement and document MFA for sensitive device actions** (lock/unlock, camera disable, alarm disarm). Google Home developer documentation already mandates secondary verification for locks—this should be industry standard.
- **Publish VDP and security.txt.** Consumer Reports' 2025 survey found that more companies are adopting VDPs, but enforcement and response SLAs remain inconsistent .
- **Design for graceful degradation** when cloud services shut down. Every cloud-dependent feature must have a documented local fallback.

### Priority 3: Build for Regulatory Compliance

- **CRA readiness:** Report actively exploited vulnerabilities within 24 hours. Maintain SBOM. Provide security updates for 5 years or the remaining support period .
- **U.S. Cyber Trust Mark:** ioXt Alliance is the new Lead Administrator, replacing UL Solutions . Products certified under this program will carry a QR code linking to a product registry with support period and security disclosures.
- **Matter attestation lifecycle:** Current model trusts devices for life after attestation . Build revocation capability before regulators mandate it.

### Priority 4: Design for Ownership Transfer

- **Factory reset must erase:** Wi-Fi credentials, cloud tokens, biometric templates, access schedules, and device configuration. Vendor documentation varies widely on what is actually removed .
- **Ownership transfer must invalidate old credentials.** The device should generate new keys on re-commissioning and reject old authentication tokens. Matter's fabric model supports this, but implementation is inconsistent.
- **Provide a structured data export** before reset, so households can migrate automations and permissions if they replace the device.


## Where Compliance Does Not Demonstrate Practical Safety

The following table identifies cases where a product or category can achieve formal compliance while failing to protect the household.

| Compliance Signal | Practical Failure | Evidence |
|---|---|---|
| **Matter certification** | Matter certifies protocol conformance, not ecosystem compatibility. A Matter-certified device may fail multi-admin pairing, lose state across fabrics, or not support firmware updates. |  |
| **UK PSTI compliance** | PSTI requires disclosure of a support period, but does not mandate a minimum length. A manufacturer can declare a 12-month support period and be compliant. |  |
| **CE marking (pre-CRA)** | CE marking does not currently require cybersecurity testing for most smart home products. The CRA will change this in December 2027. |  |
| **Vendor security whitepapers** | Claims of "military-grade encryption" or "bank-level security" are not independently verified. Aqara's CVEs demonstrate that documented security features can be absent in practice. |  |
| **Bug bounty programs** | A public bug bounty does not guarantee timely fixes. Consumer Reports found that some companies have VDPs but no documented response SLAs . |  |
| **UL Solutions certification** | UL "Diamond" certification verifies specific claims (Knox Matrix, Knox Vault), but does not assess the full lifecycle or data practices. |  |
| **Privacy policy** | A privacy policy that states data is "encrypted" may not specify whether encryption is end-to-end, whether keys are escrowed, or whether law enforcement can access plaintext. |  |

**Key finding:** No single certification, label, or regulatory compliance currently demonstrates practical household safety across the full lifecycle. Matter certifies interoperability. CRA certifies security-by-design process. ioXt certifies specific controls. None certifies that a device will remain secure, functional, and privacy-preserving after five years, a cloud shutdown, or a change of ownership. Consumers must evaluate controls individually, and manufacturers must design for lifecycle resilience, not just certification compliance.

[

securingdigitaleconomy.org

This capability can be quite difficult from a technical and feasibility point of view

Baseline Practices: A plan for secure updates with anti- rollback protection and proper access control throughout a defined security support period, where technically feasible.102 ... sensitive data from a device when it changes hands, such as in the sale of a house for smart home devices ... Device providers should have ... the handling of any the end- of- life (EoL) or end- of- service (EoS) security vulnerabilities...



](http://securingdigitaleconomy.org/wp-content/uploads/2021/03/CSDE-2021-Botnet-Report-March-24-2021.pdf#8#6)[

af.iotsf.org

<table><tr><td>Req No</td><td>Requirement</td><td>Primary Keyword</td><td>Secondary Keyword</td><td>Compliance Class And Applica...

<td>Req No</td><td>Requirement</td><td>Primary ... settings.</td><td>Business</td><td>Process</td><td>Mandatory for Class 1 and above</td> ... 2.4.16 Device Ownership Transfer ... be<br>carried out to maintain ... Mandatory for Class 1 and<br ... with<br>relevant local data privacy ... a new end user is supported, user settings and confidential user data on the device should be reliably erasable by triggering a user reset function. ... Software<br>Development Lifecycle (<br>SDLC)...



](https://af.iotsf.org/pdf/IoTSAF-4.0.0_revB.pdf#12#10)[

iotsecuritymapping.com

Specifically, a device should limit the information provided in response to discovery and other requests from untrusted sources

IoT providers must publicly disclose vulnerable customers and changes to functionality at end-of-life (EOU)/end-of-support (EOS). ... automated software updates throughout a clearly defined and disclosed security support period.[[55]] By default ... IoT providers should clearly disclose whether and to what extent device functionality will be limited due to an increased risk of vulnerability after the security support period ends.[[61]] To set consumer expectations...



](https://iotsecuritymapping.com/wp-content/uploads/2022/05/CableLabs-A-Vision-for-Secure-IoT.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/internetsociety.org)

internetsociety.org

19. Disclose the data retention policy and duration of personally identifiable information stored

20. Publicly disclose if and how IoT device/product/service ownership and the data may be transferred ... The ownership of longer-life connected home devices such as keyless entry systems ... upon home sale. ... For additional information regarding both smart homes and smart devices, see related consumer recommendations for buyers and sellers...



](https://www.internetsociety.org/wp-content/uploads/2019/04/iot_framework_resource_guide_1-5-17.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

export.arxiv.org

3) Device Activation and Secure Communication Setup: Once the server confirms the device request, it creates a long-lived authen...

Once the server confirms the device request, it creates a long-lived authentication token \(T_{D}\) , and generates a dedicated server key pair \((S_{p}^{D} ... This transaction is stored in the Identity Channel ... If device ownership changes, a new record ... The Server then updates its records to invalidate the device's authentication token \(T_{D}\) and adds the device's key to ... via Online Certificate Status Protocol (OCSP) stapling [25].



](https://export.arxiv.org/pdf/2508.21480#2#2)[

appsecuritymapping.com

i

iii. ... The secure system lifecycle policies and processes associated with the IoT product ... The process of working with component suppliers and third-party vendors ... the duration of its supported lifecycle. iii. Any post end-of-support considerations, such ... How to maintain the IoT product and its product components during its lifetime, including after the period of security support (e.g., delivery of software updates



](https://appsecuritymapping.com/wp-content/uploads/2022/09/NIST.CSWP.02042022-2.pdf#3#2)[

![](https://cdn.deepseek.com/site-icons/github.io)

sdiotsec.github.io

access control, least functionality, and disabling unnecessary capabilities

TABLE V SW UPDATE REQUIREMENTS AND SUPPORT PERIOD. ... The UK PSTI Act and ETSI EN 303 645 (clause 5.3- 13) mandate updates for a specified support period, while UK ICO guidance advises disclosing this period to users. No other reviewed frameworks explicitly require update- lifespan disclosure (see Table V).



](https://sdiotsec.github.io/accepted_papers/sdiotsec26-final66.pdf#3#2)[

phaidra.ustp.at

liance state that, among others, their brand Matter may only be used on Alliance certified Products, which comply with these Gui...

liance state that, among others, their brand Matter may only be used on Alliance certified Products, which comply with these Guidelines, by companies that hold that Certification. Additionally, the Al



](https://phaidra.ustp.at/api/object/o:7799/download#17#13)[

![](https://cdn.deepseek.com/site-icons/ofca.gov.hk)

ofca.gov.hk

(a) only IoT devices provided by manufacturers/vendors which implement appropriate security policies and resilient measures\(^1\...

(a) only IoT devices provided by manufacturers/vendors which implement appropriate security policies and resilient measures\(^1\) should be deployed. Suitable testing should also be conducted to verif



](https://www.ofca.gov.hk/filemanager/ofca/en/content_757/traac4_2022.pdf#4#4)[

home.jeita.or.jp

4.2.20.3. スマートホーム分野★2 における要件

## 【機器の要件】 IoT 機器の提供事業者は、ユーザや設置事業者等が簡単な方法でIoT 機器のユ ーザデータを消去できるような手段を提供しなければならない。 ## 4.2.21. 要件 17-2 （運用要件） ## 4.2.21.1. ★1 における要件 ## 【カテゴリ】 製品に関する情報提供を行う ## 【要件】 製造業者は、製品をセキュアに設定・利用・廃棄する方



](https://home.jeita.or.jp/smarthome/pdf/security/guideline.pdf#23#19)[

![](https://cdn.deepseek.com/site-icons/workercn.cn)

中工网

2026/04/15

照片也能“以假乱真”！比较试验显示智能门锁藏隐患

在27款能够配网的样品中，“亚太天能A9pro/纳米枪灰”“阿尔法极光P14Ultra智享版”“幻侣T7对讲”3款产品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。



](https://www.workercn.cn/c/2026-04-16/8781837.shtml)[

![](https://cdn.deepseek.com/site-icons/workercn.cn)

中工网

2026/04/16

照片也能开锁！智能门锁藏隐患-工人日报-中工网

在信息识别卡防复制、数据传输加密和人脸识别防伪3项核心安全技术上 ... 在27款能够配网的样品中，“亚太天能A9pro/纳米枪灰”“阿尔法极光P14Ultra智享版”“幻侣T7对讲”3款样品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。



](https://www.workercn.cn/papers/grrb/2026/04/17/4/news-8.html)[

![](https://cdn.deepseek.com/site-icons/ithome.com)

IT之家

2026/05/06

京津冀三地消协实测 30 款智能门锁：IC 卡易复制、人脸识别存缺陷、数据传输不加密...

同时，在 27 款能够配网的样品中，“亚太天能 A9pro / 纳米枪灰”“阿尔法极光 P14Ultra 智享版”“幻侣 T7 对讲”3 款产品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。



](https://www.ithome.com/0/947/198.htm)[

甘肃省产品质量监督检验研究院

2026/05/10

30款智能门锁测评：过半样品存在核心安全技术隐患，IC卡防复制能力普遍薄弱-甘肃省产品质量监督检验研究院

试验结果显示，亚太天能A9pro/纳米枪灰、阿尔法极光P14Ultra智享版、幻侣T7对讲等3款样品，在传输用户账号、密码及远程开锁指令等敏感数据时，均未采用有效的加密协议（如TLS），而是以明文形式传输。



](https://www.gszjy.org.cn/article/3262.html)[

![](https://cdn.deepseek.com/site-icons/gmw.cn)

光明网

2026/04/20

你家的智能门锁，一张照片就能打开？ - 你家的智能门锁，一张照片就能打开？

京津冀三地消协最近进行了一次比较试验，发现不同品牌的智能门锁在防复制、加密传输、人脸防伪这三项核心技术上，表现参差不齐。买智能门锁之前 ... 此次比较试验 ... 数据保密性、图像识别、环境温度等11个项目进行了检测 ... 个别产品在核心安全技术上存在一定漏洞。



](https://m.gmw.cn/2026-04/21/content_1304427688.htm#1)[

![](https://cdn.deepseek.com/site-icons/gmw.cn)

光明网

2026/05/07

一张打印照片就能打开智能锁？消协实测曝光 - 一张打印照片就能打开智能锁？消协实测曝光

近日，京津冀三地消协组织共采集20个主流品牌、30款热销智能门锁进行比较试验 ... 此外，有3款产品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。此类漏洞使得用户的登录凭证和远程指令极易在网络中被截获...



](https://m.gmw.cn/2026-05/08/content_1304448707.htm#1)[

中国市场监管新闻网

2026/04/19

京津冀消协组织发布智能门锁比较试验结果

在信息识别卡防复制、数据传输加密和人脸识别防伪三项核心安全技术上 ... 在27款能够配网的样品中，“亚太天能A9pro/纳米枪灰”“阿尔法极光P14Ultra智享版”“幻侣T7对讲”3款产品在传输用户账号、密码及远程开锁指令等敏感数据时，采用了明文传输方式，未进行有效加密。



](http://www.cmrnn.com.cn/content/2026-04/20/content_288841.html)[

广州市消费者委员会

2026/04/26

京津冀消协组织发布智能门锁比较试验结果：青稞、博克、幻侣3款样品可被平面照片解锁

近期，北京市消费者协会、天津市消费者协会、河北省消费者权益保护委员会联合开展智能门锁比较试验，对市面上20个品牌的30款产品进行全面检测。试验结果显示，当前智能门锁在基础可靠性、用户体验及宣传规范性上均有显著提升，但信息识别卡防复制、数据传输加密、人脸识别防伪3项核心安全指标表现参差不齐，分别标称青稞、博克、幻侣品牌的3款产品可被红外相机拍摄的平面照片解锁，人脸识别防伪能力不足。 据悉，本次受测



](https://www.guangzhou315.com/html/web/bijiaoshiyan/2048674348774936578.html)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/03/10

How to ditch Ring’s surveillance network - Skip to main content

Here’s how to secure your existing Ring cameras, along with our picks for security cameras that store footage locally or use end-to-end encryption. ... Put simply, if you don’t want any cloud exposure, choose local storage. If you want cloud convenience with stronger protections, choose an end-to-end encrypted system.



](https://on.theverge.com/tech/890910/best-ring-alternatives-privacy-focused-video-doorbell-local-storage-reolink-aqara-tapo-ecobee#1)[

Abode

2026/03/08

Home Security Camera Privacy 2026: What Gets Recorded, Who Sees It & How to Keep Your Footage Private

Abode | Optional (with plan) | Yes ... | Yes (HKSV) | Warrant required | ★★★★★ Ring (Amazon) | Required for clips | Limited (Ring Edge) | Optional (off by default) | Previously shared without consent* | ★★☆☆☆ Nest ... | No | No | Has shared in emergencies without warrant | ★★★☆☆ ... Wyze | Optional | Yes (microSD) | No | Warrant required | ★★★☆☆ eufy | Optional | Yes (local hub)



](https://goabode.com/blog/home-security-camera-privacy/#hide-mini-cart)[

![](https://cdn.deepseek.com/site-icons/ltn.com.tw)

自由電子報3C科技

2025/10/31

你家也在用？實測10款網路攝影機資安風險多、小米等品牌上榜 - 自由電子報 3C科技

例如無法防禦駭客的暴力攻擊、傳送資料過程中沒有加密等，甚至是應用程式安全性不足 ... TP-Link Tapo C210和D-Link DCS-8350LH則在影片數據傳輸時未進行加密，後者也存在容易被駭客暴力破解登入的風險。



](https://3c.ltn.com.tw/news/63787)[

ezone.hk 即時科技生活

2026/07/03

消委會．家居IP Cam｜9款家用監控鏡頭影片易外洩恐變「直播」 推薦1款安全鏡頭【附詳細名單】 | ezone

消委會發現有4款（「imou」、「TP-Link」、「EZVIZ」、「D-Link」）未有將影片數據加密，受攻擊時駭客可輕易窺探影片內容；至於「reolink ... 駭客可從普通文字檔找到路由器（router）的帳戶資料，資料存有外洩風險。



](https://dev.e-zone.com.hk/article/20035960/2071077/#mcetoc_1i4jn0cgg2m)[

![](https://cdn.deepseek.com/site-icons/amazonaws.com)

ec2-18-163-36-20.ap-east-1.compute.amazonaws.com

小心私隱被竊！ 9成家用鏡頭存安全漏洞 - 消費者委員會

本會首次測試市面10款家用監控鏡頭的網絡安全，結果發現，只有1款樣本符合歐洲的網絡安全標準，餘下9款均存有不同的網絡安全問題，例如未能防禦駭客的「暴力攻擊」、傳送資料時沒有加密等。此外監控鏡頭的應用程式亦有待改善...



](https://ec2-18-163-36-20.ap-east-1.compute.amazonaws.com/tc/article/557-home-surveillance-cameras/557-home-surveillance-cameras-samples-and-test-items#tab)[

![](https://cdn.deepseek.com/site-icons/consumer.org.hk)

消費者委員會

小心私隐被窃！ 9成家用镜头存安全漏洞 - 消费者委员会 - Skip to main content

本会首次测试市面10款家用监控镜头的网络安全，结果发现，只有1款样本符合欧洲的网络安全标准，余下9款均存有不同的网络安全问题，例如未能防御骇客的「暴力攻击」、传送资料时没有加密等。



](https://www.consumer.org.hk/sc/article/557-home-surveillance-cameras/557-home-surveillance-cameras-test-results#tab#1)[

![](https://cdn.deepseek.com/site-icons/linkedin.com)

LinkedIn · Fabian Warislohner

2026/04/20

#privacy #homesecurity #iot #dataprotection #privatedata | Vinny Peone | 38 条评论 - 跳到主要内容

"The "Fortress" choice that treats your data as a high-security asset rather than a marketing product, offering the best protection for a premium price." 𝐆𝐫𝐚𝐝𝐞: 𝐀 Wyze ... "The "Mixed Signal" choice that markets "local storage" ... past encryption scandals." 𝐆𝐫𝐚𝐝𝐞...



](https://www.linkedin.com/posts/vinnypeone_privacy-homesecurity-iot-share-7452395228033990656-ZbAv/#1)[

SmartSMSSolutions

2026/01/22

Security Cameras & Doorbells: Cloud vs Local, Encryption & Access Controls | SmartSMSSolutions - Security Cameras & Doorbells: Cloud vs Local, Encryption & Access Controls | SmartSMSSolutions

# Security Cameras & Doorbells: Cloud vs Local, Encryption & Access Controls | SmartSMSSolutions Protect your security camera footage with this guide to storage options, encryption types, and account



](https://smartsmssolutions.com/resources/blog/business/security-camera-privacy-encryption#1)[

![](https://cdn.deepseek.com/site-icons/consumerreports.org)

innovation.consumerreports.org

Consumer Reports

## Digital Standard Test Summary Notes ### Examining data privacy & data security in Wireless Security Cameras | July 2020 --- ## Purpose of this document: This document is what our testing te



](https://innovation.consumerreports.org/wp-content/uploads/2020/07/Summary-Note_Shared.pdf#2#1)[

![](https://cdn.deepseek.com/site-icons/nsf.gov)

par.nsf.gov

Comparing smart-home devices that use the Matter protocol

Abstract—This paper analyzes Google Home, Apple HomeKit, Samsung SmartThings, and Amazon Alexa platforms, focusing on their integration with the Matter protocol. ... We conducted (from May to August 2024) a comparative analysis to explore how Google Home Nest, Apple HomePod Mini, Samsung SmartThings station ... the power of Matter to provide seamless and integrated smart- home experiences.



](https://par.nsf.gov/servlets/purl/10618356#2#1)[

![](https://cdn.deepseek.com/site-icons/springer.com)

Springer

2025/04/24

Jointly Achieving Smart Homes Security and Privacy through Bidirectional Trust - Journal on Information Security

Table 2 Information Used in a Smart Home Environment Based on Their Category Device Vendor Name Address Country Behavioral Data Sensitive Data Identification Documents Biometric Data Audio Third Party Data IDApple ... Amazon Echo Yes ... No No ... Yes AirPlay Apple ... Yes Google Home ... Yes Samsung Smartthings Hub



](https://link.springer.com/article/10.1186/s13635-025-00199-2/tables/2)[

![](https://cdn.deepseek.com/site-icons/ua.pt)

ria.ua.pt

<table><tr><td></td><td>Home Assistant</td><td>OpenHAB</td><td>SmartThings</td><td>Apple HomeKit</td><td>Google Nest</td></tr><t...

<td>Apple HomeKit</td><td>Google Nest ... Access</td><td>✓ only local with hub or paid ... 000 [T3]</td></tr><tr><td>Privacy and Data Protection</td><td>✓ all local or paid cloud</td><td>✓ all local or cloud</td><td>all online on Samsung servers</td><td>not even Apple can access, end to end encryption</td><td>privacy concerns on voice recordings</td></tr><tr><td>Updates



](https://ria.ua.pt/bitstream/10773/45304/1/Documento_Nuno_Cunha.pdf#19#4)[

mattercatalog.com

2026/03/04

Best Matter Smart Home Hubs in 2026: Which Controller Should You Choose?

Apple HomePod mini, Google Nest Hub, Amazon Echo, or Samsung SmartThings Station — which Matter hub is right for you ... Apple: HomePod mini ($99) ... Best for: Apple household users, iPhone/iPad/Mac owners, those who prioritize privacy (all processing is local). Thread border router: Yes ✅ ... Amazon Echo 4th Gen or Google Nest Hub 2nd Gen at $99.



](https://mattercatalog.com/blog/best-matter-smart-home-hub-2026)[

![](https://cdn.deepseek.com/site-icons/zdnet.com)

ZDNET

2025/12/21

Best home automation systems 2026: As a smart home reviewer I rounded up the top ones - ZDNET - Skip to content

Bottom Line Why we like it ... - More secure than the cloud ... Apple HomeKit is ideal for iPhone users looking to expand their smart home. ... Who it’s for ... Who should look elsewhere ... Apple’s strict data and privacy controls make it one of the most secure smart home systems.



](https://www.zdnet.com/home-and-office/smart-home/best-home-automation-system/?itm_source=parsely-api#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

xplorestaging.ieee.org

A home hub is required to complete setup of this accessory

Comparisons of how apple homekit and google home handle different tasks using our framework. We find issues at nearly every life cycle stage for both platforms, but apple has more desirable features. ... | Deploy | Confidentiality | Discover new devices | Difficult since devices may use different commissioning mechanisms ... | Prevent privacy interference | Some integrations may not encrypt data\(^3\) ... | Decommission | Confidentiality | Remove sensitive information



](https://xplorestaging.ieee.org/ielx8/7756/5210084/10627940.pdf?arnumber=10627940#3#3)[

![](https://cdn.deepseek.com/site-icons/uni-mate.hu)

stud.mater.uni-mate.hu

• Funkciók és szolgáltatások széles skáláját kínálja az Alexa hangsegéddel

• Könnyen beállítható és használható • Integrálható az okos otthon eszközök széles skálájával ... Hátrányai ... Előnyei ... • Erős biztonsági és adatvédelmi funkciókat kínál



](https://stud.mater.uni-mate.hu/8282/1/814336414.pdf#17#6)[

![](https://cdn.deepseek.com/site-icons/medium.com)

Medium · Dented Feels

2026/07/17

Matter vs. HomeKit vs. Google Home 2026 — The Honest Smart-Home Hub Showdown - Sitemap

to ANY hub (Apple, Google, Amazon, Samsung SmartThings, Home Assistant). ... Best privacy story (all routines run locally on Apple TV / HomePod; nothing in the cloud unless you opt in), Home Key support for Yale/Schlage locks ... Weak spots ... privacy story is weaker than Apple’s (more telemetry sent to Google).



](https://medium.com/@frankchethalan/matter-vs-homekit-vs-google-home-2026-the-honest-smart-home-hub-showdown-8f90498ab5af#1)[

Shipshape: AI

2026/03/04

Smart Home Brand & Ecosystem Comparison Guide

Apple HomeKit / Apple Home - Voice Assistant: Siri ... - App: Apple Home (iOS/macOS/watchOS) - Protocol Support: WiFi ... Best-in-class privacy (all processing local or encrypted end-to-end), seamless Apple device integration ... - Weaknesses ... - Privacy: Best — local processing, end-to-end encryption, no ad targeting ... Moderate — data used for Google services ... Moderate — Samsung data practices similar to Google/Amazon



](https://www.shipshape.ai/help/brands/smart-home-brands)[

![](https://cdn.deepseek.com/site-icons/uni-lj.si)

Univerza v Ljubljani

Uporaba biometričnih podatkov v pametnih domovih

O Samsung SmartThings smo na svetovnem spletu našli največ kršitev, za Amazonov pametni dom pa je potrjeno, da ustvarja in shranjuje zvočne posnetke uporabnikov. Glede na preučene



](https://repozitorij.uni-lj.si/Export.php?format=DC-XML&id=139440&lang=slv)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

重要装置必须對彼此和控制器進行身分驗證，才能進行通訊

在製造期間，装置會怖建唯一的身分和X.509證，為装置證明證(DAC) ... 事填需要装置證明證(DAC)，該證必须由符合事填公有金基設施(PKI)證政策(CP)的装置證明CA發行。装置廠商可以使用AWS私有CA執行下列動作...



](https://docs.aws.amazon.com/zh_tw/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

a

b. Factory reset SHALL remove from the Node all security- and privacy-related data and key material created during or after commissioning except data explicitly required to persist across resets. [CM35 for T16 ... Devices SHOULD protect the confidentiality of attestation (DAC) private keys. ... confidentiality of Node Operational Private Keys.



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#148)[

![](https://cdn.deepseek.com/site-icons/aliyun.com)

阿里云文档中心

2026/01/07

PCA FAQ - Search for Help Content

Matter device authentication is based on a public key infrastructure (PKI) and uses standard X.509 digital certificates to identify devices and secure communication. Matter uses two types of device certificates ... A Node Operational Certificate (NOC) is issued by a Matter administrator during commissioning to authenticate devices and ensure the privacy and integrity of data communication.



](https://help.aliyun.com/en/ssl-certificate/pca-faq#1)[

![](https://cdn.deepseek.com/site-icons/alibabacloud.com)

Alibaba Cloud

2026/03/12

PCA FAQ - Alibaba Cloud - Search for Help Content

Matter's device authentication is based on a public key infrastructure (PKI) and uses standard X.509 digital certificates to identify devices and secure communication between them. Matter uses two types of device certificates ... A Node Operational Certificate (NOC) is issued by a Matter administrator during commissioning to authenticate the identity of other devices and ensure the privacy and integrity of data communication.



](https://www.alibabacloud.com/help/en/ssl-certificate/pca-faq#1)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2025/05/12

双认证赋能未来：Matter与RED DA EU 2022/30如何重塑物联网安全与市场竞争力

Matter要求使用TCP/MRP over UDP和AES-128-CCM或符合RED安全通信保密性要求的等效协议 ... - Matter通过角色分离与最小权限原则满足RED对用户数据保护的合规性要求 ... Matter要求设备使用PKI证书，直接满足RED要求。



](https://matter.cn/3670.html)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

the IPv6 hop count

Each Matter device holds a number of certificate chains. A Device Attestation Certificate (DAC) proves the authenticity ... Each Matter device is issued an Operational Node ID and a Node Operational Certificate (NOC) for that Operational Node ID. ... These steps help to protect the privacy of the end-user and to adapt to dif- ferent trust models.



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#7)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

| [4] | FIPS 140-3* | Security Requirements for Cryptographic Modules, FIPS 140-3, March 22, 2019. https://nvlpubs

During the transition period until September 21, 2026, every reference of FIPS 140-3 in this document SHALL refer to as either the use of FIPS 140-3 or FIPS 140-2. After September 21...



](http://csa-iot.org/wp-content/uploads/2024/02/Alliance-PKI-Certificate-Policy-2024-01-25.pdf#9#2)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon AWS Documentation

보안 - AWS 규범적 지침

설계에 따른 보안이란 개발 후반 단계에서 사후 고려 사항으로 사용하는 것이 아니라 장치 설계 단계에서 보안 기능을 통합하는 방식입니다. 암호화된 통신 및 over-the-air (OTA) 업데이트는 설계상 보안의 예입니다. Matter는 신뢰할 수 있고 안전한 제조 시설에서 시작하여 설계에 따른 보안을 구현함으로써 스마트 홈 기기를 위한 강력한 기반을 제공



](https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/strategy-matter-standard/security.html)[

![](https://cdn.deepseek.com/site-icons/psacertified.org)

psacertified.org

NISTIR 8425 forms the basis of the Federal Communications Commission work on the US Cyber Trust Mark [18] for IoT products

NISTIR 8425 forms the basis of the Federal Communications Commission work on the US Cyber Trust Mark [18] for IoT products. However, it currently restricts the scope of IoT devices to those that are i



](https://www.psacertified.org/app/uploads/2024/08/JSADEN001-L1-V3.1-Beta-01_.pdf#11#10)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nvlpubs.nist.gov

1 Pour plus d'informations sur la réponse du NIST à l'appel à recommandations de l'EO 14028 concernant un label de cybersécurité...

Profil du noyau de base de l'IdO pour les produits IdO grand public ... Le NIST décrit un dispositif IdO comme un équipement informatique doté d'au moins un transducteur (c'est-à-dire un capteur ou un actionneur) et d'au moins une interface réseau [IR8259]. Tous les produits IdO



](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8425.fre.pdf#5#2)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

docs.fcc.gov

PUBLIC SAFETY AND HOMELAND SECURITY BUREAU SELECTS IOT ALLIANCE TO SERVE AS NEW LEAD ADMINISTRATOR OF THE U.S. CYBER TRUST MARK ...

the Public Safety and Homeland Security Bureau (Bureau) announces the selection of iotX Alliance (iotX) to serve as the Lead Administrator of the Federal Communications Commission's (FCC or Commission) voluntary cybersecurity labeling program for consumer wireless Internet of Things (IoT) products (U.S.



](https://docs.fcc.gov/public/attachments/DA-26-354A1.pdf#1#1)[

brightsight.com

Training course Focus on consumer IoT cybersecurity solutions

NIST 8259a and NIST 8425 is referenced in the USCSA consumer label program proposal. ... In the USA, The White House with NIST is working on a national cybersecurity labeling program for Internet-of-Things (IoT) devices for a targeted rollout in 2023.



](https://www.brightsight.com/IoT%20training%20course.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/soumu.go.jp)

tele.soumu.go.jp

HCT

1.2 NIST Core Baseline 8425 1.3 IoT Products and Exclusions ... NISTs Core Baseline 8425 established the NISTIR 8259 Series of reports that provides guidance for manufacturers and their supporting third parties as they conceive, design ... and support IoT devices across their spectrum of customers.



](https://www.tele.soumu.go.jp/resource/j/equ/mra/pdf/07/e/2-a_E.pdf#1#1)[

mail.intgovforum.org

Annex to the conclusions of Oscar Giudice

The documents analyzed included in this category were ... NISTIR 8259 - Foundational Cybersecurity Activities for IoT Device Manufacturers NISTIR 8259A - IoT Device Cybersecurity Capability Core Baseline NISTIR 8259B - IoT Non-Technical Supporting Capability Core Baseline



](https://mail.intgovforum.org/pipermail/dc-isss_intgovforum.org/attachments/20230203/9432a598/attachment-0001.docx#1#1)[

![](https://cdn.deepseek.com/site-icons/nist.gov)

nvlpubs.nist.gov

NIST has been involved in many efforts to promote safe and secure use of IoT

This resulted in the NIST IR 8259 series (8259, 8259A, 8259B, and 8259C). ... NIST also issued a white paper that recommended consumer label criteria for IoT products and software...



](https://nvlpubs.nist.gov/nistpubs/gcr/2023/NIST.GCR.23-039.pdf#103#31)[

ioXt

ioXt Alliance IoT Security News — ioXt

is highlighting the importance of lifecycle-based cybersecurity following the release of NIST IR 8259r1, Foundational Cybersecurity Activities for IoT Product Manufacturers. ... today announced its continued support for the European Union’s Cyber Resilience Act (CRA)...



](https://ioxt.com/in-the-news)[

ioXt

ioXt Alliance News and Events Blog — ioXt

Guidance ioXt, the Global Standard for ... is highlighting the importance of lifecycle-based cybersecurity following the release of NIST IR 8259r1, Foundational Cybersecurity Activities for IoT Product Manufacturers. # ioXt Supports the EU Cyber Resilience Act as Global Cybersecurity Expectations Continue to Evolve



](https://ioxt.com/news-events-blog?category=Press+Release)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

fcc.gov

Cybersecurity Labeling for Consumer IoT Products

NISTIR 8259 Series of reports, Foundational Activities for IoT Device Manufacturers, provides guidance for designing securable IoT products with core device capabilities and non-technical activities that support common cybersecurity goals ... <center>NISTIR 8259



](https://www.fcc.gov/sites/default/files/12-IoT-Cyber-Labeling-Slide-Deck-3-TCB_Apr_2025_Final.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/meti.go.jp)

meti.go.jp

IoT製品の設定は変更可能で、デフォルト設定を復元できる機能を有すること

IoT製品の設定は変更可能で、デフォルト設定を復元できる機能を有すること。あらゆる変更は、許可されたエンティティによってのみ実行可能であること。 ・ データ保護： IoT製品が保存及び伝送するデータを、不正アクセスや改ざんから保護できること。 NISTIR 8259Aに基づく IoT製品に求められるサイバーセキュリティ能力 ・ インタフェースのアクセス制御： IoT製品のネット



](https://www.meti.go.jp/meti_lib/report/2021FY/050560.pdf#18#11)[

![](https://cdn.deepseek.com/site-icons/vulners.com)

Vulners.com

CVE Search Engine - Security Vulnerabilities and Exploits Search Tool - Vulners

RedhatCVE•added 2025/12/11 5:3 a.m.•1 views ... Aqara Hub devices including Camera Hub G3 4.1.90027, Hub M2 4.3.60027, and Hub M3 4.3.60025 automatically collect and upload unencrypted sensitive information.



](https://vulners.com/search/tags/Aqara%20Hub#1)[

isomer-user-content.by.gov.sg

<table><tr><td>CVE-2025-56400</td><td>applications, as well as other third-party applications that integrate the SDK, allows an ...

or alarms.</td><td>8.8</td><td>More Details</td></tr><tr><td>CVE-2025-12138</td><td>The ... Details</td></tr><tr><td>CVE-2025-62730</td><td>SOPlanning ... <table><tr><td>CVE-2025-10555</td><td>A stored Cross-site Scripting (XSS) vulnerability affecting Service Items Management in DELMIA Service Process Engineer on Release 3DEXPERIENCE R2025x ... Details</td></tr><tr><td>CVE-2025-65951</td><td>Inside ... Details</td></tr><tr><td>CVE-2025-62207</td><td>Azure ... Vulnerability</td><td>8.6</td><td>More Details</td></tr><tr><td>CVE-2025-64066</td><td>Primakon



](https://isomer-user-content.by.gov.sg/36/d5b5fcaf-5767-4e7c-8106-45640ff74bfc/26_Nov_2025.pdf#22#3)[

isomer-user-content.by.gov.sg

<table><tr><td>2025-55602</td><td>D-Link DIR-619L 2.06B01 is vulnerable to Buffer Overflow in the formSysCmd function via the bi...

parameter.</td><td>7.5</td><td>More Details</td></tr><tr><td>CVE-2025-55631</td><td>Reolink Smart 2K+ Plug-in Wi-Fi Video Doorbell with Chimie - firmware v3.0.0.4662_2503122283 ... Incorrect access control in the RTMP server settings of Reolink Smart 2K+ Plug-in



](https://isomer-user-content.by.gov.sg/36/f65547f0-d0fb-4e07-9789-d8be3570001e/27_Aug_2025.pdf#35#9)[

jpcert.or.jp

<table><tr><td>項番</td><td>脆弱性識別番号</td><td>脆弱性</td><td>JVN<br/>公表日</td><td>CVSS<br/>基本値</td></tr><tr><td>16</td><td>JVN#77560819<...

Collector」における複数の脆弱性</td><td>2025年11<br/>月21日</td><td>7.8 ... <td>SwitchBot製「スマートテレビドアホン」に利用可能なデバッグ機能が存在している脆弱性</td> ... 2025年10<br/>



](https://www.jpcert.or.jp/pr/2026/vulnREPORT_2025q4.pdf#6#3)[

![](https://cdn.deepseek.com/site-icons/opencve.io)

Opencve

Vulnerabilities (Tuya)

CVE-2025-56400 | 3 Apple, Google, Tuya | 6 Ios, Android, Smart and 3 more | 2025-12-30 | 8.8 High ... CVE-2025-56557 | 1 Tuya



](https://app.opencve.io/cve/?vendor=tuya&product=tuya)[

isomer-user-content.by.gov.sg

<table><tr><td>CVE-2025-55627</td><td>Insufficient privilege verification in Reolink Smart 2K+ Plug-in Wi-Fi Video Doorbell with...

5627</td><td>Insufficient privilege verification in Reolink Smart 2K+ Plug-in Wi-Fi Video Doorbell with Chime - firmware v3.0.0.4662_2503122283 ... privileges.</td><td>5.3</td><td>More ... Details</td></tr><tr><td>CVE-2025-55626</td><td>An Insecure Direct Object Reference (IDOR) vulnerability in Reolink Smart 2K+ Plug-in Wi-Fi Video Doorbell with Chime - firmware



](https://isomer-user-content.by.gov.sg/36/f65547f0-d0fb-4e07-9789-d8be3570001e/27_Aug_2025.pdf#35#20)[

![](https://cdn.deepseek.com/site-icons/aquasec.com)

Aqua Vulnerability Database

2025/12/17

CVE-2025-10910 | Vulnerability Database | Aqua Security

CVE-2025-10910 ## Authorization Bypass Through User-Controlled Key A flaw in the binding ... The vulnerability has been verified for the Govee H6056 - lamp device in firmware version 1.08.13, but may affect also other Govee cloud‑connected devices.



](https://avd.aquasec.com/nvd/2025/cve-2025-10910/)[

![](https://cdn.deepseek.com/site-icons/circl.lu)

CIRCL -- Computer Incident Response Center Luxembourg

2025/10/05

GHSA-PC64-X6MJ-QCJF - Vulnerability-Lookup

2025-10-06 21:30 – Updated ... The YoSmart YoLink Smart Hub firmware 0382 is unencrypted, and data extracted from it can be used to determine network access credentials. ... "https://nvd.nist.gov/vuln/detail/CVE-2025-59450"



](https://vulnerability.circl.lu/vuln/ghsa-pc64-x6mj-qcjf#1)[

![](https://cdn.deepseek.com/site-icons/vuldb.com)

VulDB

2025/10/10

CVE-2025-11648 in Furbo 360

CVE-2025-11648 in Furbo 360 ... A vulnerability has been found in Tomofun Furbo 360 and Furbo Mini. ... The firmware versions determined to be affected are Furbo ... MC0020_FW_074.



](https://vuldb.com/cve/CVE-2025-11648#1)[

![](https://cdn.deepseek.com/site-icons/incibe.es)

INCIBE

2025/12/17

CVE-2025-10910

Gravedad CVSS v4.0: CRÍTICA Tipo: No Disponible / Otro tipo Fecha de publicación: 18/12/2025 Última modificación: 15/04/2026 ## Descripción *** Pendiente de traducción *** A flaw in the bindi



](https://www.incibe.es/incibe-cert/alerta-temprana/vulnerabilidades/cve-2025-10910?utm_source=feedly)[

![](https://cdn.deepseek.com/site-icons/wpi.edu)

digital.wpi.edu

| Xiaomi US | ✗ | ✗ | ✓ | ✓ | ✓ |

Data deletion policies vary widely among companies, with different methods and restrictions in place. The most common practice is deletion via email, offered by 16 companies. 3 allow ... Deletion via the web is available from 18 companies ... 20 companies require approval before proceeding with data deletion, adding an extra layer of control over the process. ... 7 companies degrade or even deny service once data is deleted, raising concerns ... While some companies offer clear data deletion options and concise privacy policies...



](https://digital.wpi.edu/downloads/w0892g20p?locale=it#7#3)[

Sergei Tokmakov, Esq.

Smart Home & IoT Terms of Service Reviews | 2026 | ToS Watchdog - Smart Home & IoT Terms of Service

Philips Hue Best in Category | 65/100 | B- | Cloud dependency for features | Limited data collected Amazon Alexa | 58/100 ... Google Nest | 52/100 ... Local control options are limited or nonexistent. ... - ✓ Local control option available - ✓ Limited personal data collection



](https://terms.law/ToS-Watchdog/smart-home/#1)[

etran.rs

Studies have been conducted that show that the user attitude towards data collection depends on multiple factors, such as the en...

This service allows administrators to handle privacy policy updates, and the users to request the export or deletion of personal data, as well as the deletion of the user account. First ... the following functionalities: - Update of Privacy Policy and Terms of Service- Export of Personal Data ... The Privacy Policy should help users



](https://etran.rs/2021/zbornik/Sessions/S013_RT_RTI_2021.pdf#29#12)[

![](https://cdn.deepseek.com/site-icons/change.org)

Change.org

2026/04/27

Sign the Petition

By default, the two companies process the data by uploading it to a cloud system which have greater security risks than a local one. ... - Personal data should be stored on the local device by default ... - Users should have access to review and delete all stored data ... the organization assumes



](https://www.change.org/p/amazon-and-google-data-management)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Podcasts

The OPSEC Podcast - Podcast - Most people think of their smart home devices as tools they control

In March 2025, Amazon removed the local voice processing option from Echo devices. ... This episode documents what each major smart home ecosystem actually does with your data — and what you can do to reduce the exposure. ... accountReview and delete camera history in Google Home Home Network Hardening Segment IoT devices onto a separate network...



](https://podcasts.apple.com/ng/podcast/the-opsec-podcast/id1832928172#1)[

![](https://cdn.deepseek.com/site-icons/iheart.com)

iHeart

2026/07/12

The Smart Home Is a Listening Post: Amazon, Google, and the Surveillance You Paid For The OPSEC Podcast | iHeart - July 13, 2026 • 25 min •

and Google Nest ... In March 2025, Amazon removed the local voice processing option from Echo devices. In February 2026 ... This episode documents what each major smart home ecosystem actually does with your data — and what you can do to reduce the exposure. ... - Review and delete camera history in Google Home



](https://www.iheart.com/podcast/1333-the-opsec-podcast-287830054/episode/the-smart-home-is-a-listening-post-amazon-google-and-the-surveillance-you-paid-for-338755608#1)[

![](https://cdn.deepseek.com/site-icons/spotify.com)

Spotify - Web Player: Music for everyone

無駄 (Muda) in the Glass Cathedral: Why Gen Alpha is Done with Dealer Theatre - Most people think of their smart home devices as tools they control

In March 2025, Amazon removed the local voice processing option from Echo devices. ... This episode documents what each major smart home ecosystem actually does with your data — and what you can do to reduce the exposure.Key Settings to Change Right NowAmazon Echo / Alexa:Alexa



](https://open.spotify.com/episode/5m6E8UZunLLvlSfTCwNFLy#1)[

smartstorage.website

2026/02/01

Cloud Sovereignty & Smart Home Data for Sellers

map where recordings live, disclose clearly, and use NAS or sovereign clouds to reduce legal and privacy risks. ... - Prefer local control: When possible, use NAS, on-prem storage or sovereign-cloud configurations to reduce cross-border, third-party and regulatory risk.



](https://smartstorage.website/what-homeowners-need-to-know-about-cloud-sovereignty-when-se)[

Home Security Reviews

2025/11/23

Smart Home Privacy 2026: Which Devices Spy on You, What Data They Collect, and How to Lock Them Down - Home Security Reviews

Privacy Comparison by Security System (2026) System | Data Processing | E2E Encryption | Law Enforcement ... with warrant | No | No Eufy (post-2023) | Local + optional cloud | No | N/A (local storage) | No (after 2022 scandal) | Yes



](https://home-security-reviews.com/smart-home-privacy/#login)[

Shein governance, tracked over time.

Right to Deletion with Backup Limitation | Eufy | ConductAtlas

You also have the right to object to the processing of Service Data or to export Service Data to another service. ... the right to request the deletion or removal of your Relevant Personal Data where there is no other legal basis for us to keep using it...we may not be able to immediately remove the information from the backup system...



](https://conductatlas.com/platform/eufy/eufy-privacy-policy/provision/CA-P-064115/right-to-deletion-with-backup-limitation/)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

HomeKit 数据安全性

HomeKit 数据会在用户使用 iCloud 的 Apple 设备和 iCloud 钥匙串之间安全同步。在此同步过程中，HomeKit 数据会使用 iCloud 端对端加密进行加密，Apple 无法访问 ... 第三方 App 对家庭数据的访问由用户在“隐私”设置中控制。此类 App 请求家庭数据（类似于访问“通讯录” ... HomeKit 数据不会包括在本地备份中。



](https://support.apple.com/zh-cn/guide/security/sec49613249e/1/web/1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

HomeKit 摄像头安全性

本地网络连接由会话独有的 HKDF-SHA512 派生密钥对加密，该密钥对由家居中枢和 IP 摄像头在 HomeKit 会话中进行协商 ... 如果检测到重要的事件，HomeKit 会使用 AES-256-GCM 并通过随机生成的 AES256 密钥来加密该视频片段。HomeKit 还会为每个片段生成海报帧...



](https://support.apple.com/zh-cn/guide/security/sec525461d19/1/web/1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

Безопасность данных HomeKit

В ходе этого процесса данные HomeKit шифруются посредством сквозного шифрования iCloud, и Apple не может получить доступ к этим данным. ... Эти данные имеют класс защиты «Защищено до первой ... хранилище Data Vault. Данные HomeKit не копируются в локальные резервные копии.



](https://support.apple.com/ru-ru/guide/security/sec49613249e/web)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

デバイスがローカルネットワーク上にない場合は、暗号化されたストリームがホームハブ経由でデバイスに中継されます

このローカルネットワーク接続は、HKDF-SHA-512から導出されるセッションごとの鍵ペア で暗号化されます ... 重大なイベントが検出された場合は、ランダムに生成されるAES-256鍵 を使用してAES-256-GCMでビデオクリップを暗号化します。



](https://help.apple.com/pdf/security/ja_JP/apple-platform-security-guide-j.pdf#55#48)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

Keamanan kamera HomeKit

Streaming dienkripsi ... Koneksi jaringan lokal dienkripsi dengan pasangan kunci turunan HKDF-SHA512 per sesi yang dinegosiasikan melalui sesi HomeKit antara hub rumah dan kamera IP. ... Jika kejadian signifikan terdeteksi, HomeKit akan mengenkripsi klip video menggunakan AES-256-GCM ... kunci AES256 yang dibuat secara acak.



](https://help.apple.com/pdf/security/id_ID/apple-platform-security-guide-id.pdf#48#42)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

HomeKit มีกลไกแบบต้นทางที่ปลายทางที่ปลอดภัยและเป็นส่วนตัวในการบันทึก วิเคราะห์ และแสดงคลิปจาก กล่อง IP ใน HomeKit โดยไม่เปิดเผยเ...

HomeKit มีกลไกแบบต้นทางที่ปลายทางที่ปลอดภัยและเป็นส่วนตัวในการบันทึก วิเคราะห์ และแสดงคลิปจาก กล่อง IP ใน HomeKit โดยไม่เปิดเผยเนื้อหาวิดีโอนั้นให้กับ ... หรือบุคคลหรือบริษัทอื่นๆ เมื่อตรวจพบ การเคลื่อนไหวโดยกล่อง IP คลิปวิดีโอจะถูกส่งโดยตรงไปยังอุปกรณ์



](https://help.apple.com/pdf/security/th_TH/apple-platform-security-guide-th.pdf#79#69)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

HomeKit 通訊安全性 - HomeKit 通訊安全性

HomeKit 提供家庭自動化的基礎架構，利用 iCloud 與 裝置安全功能來保護與同步隱私資料，無須透露給 Apple ... 為了在 Apple 裝置與 HomeKit 配件之間建立關係，系統會使用「安全遠端密碼」（3072 位元）通訊協定來交換密鑰，並在使用者裝置上輸入配件製造商提供的八位數代碼，然後使用 ChaCha20-Poly1305 AEAD 與 HKDF-SHA-512 衍生密鑰來加密。



](https://support.apple.com/zh-mo/guide/security/sec3a881ccb1/1/web/1#seca5773eb35#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

HomeKit-kamerasikkerhed - HomeKit-kamerasikkerhed

Når appen Hjem bruges til at se kameraklip, hentes dataene fra iCloud, og nøglerne til dekryptering af streams pakkes ud lokalt vha. end-to-end-kryptering af iCloud.



](https://support.apple.com/da-dk/guide/security/sec525461d19/web#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Support

Sécurité de la communication HomeKit - Sécurité de la communication HomeKit

les clés sont échangées à ... Chaque session est établie à l’aide du protocole Station‑to‑Station et chiffrée avec les clés obtenues avec la fonction de dérivation HKDF‑SHA512 à partir des clés Curve25519 de session.



](https://support.apple.com/fr-ca/guide/security/sec3a881ccb1/web#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

help.apple.com

Cuando se detecta una invocación correcta de Siri, el HomePod envía el audio a los servidores de Siri y cumple la intención del ...

Cuando se detecta una invocación correcta de Siri, el HomePod envía el audio a los servidores de Siri y cumple la intención del usuario usando las mismas garantías de seguridad, privacidad y encriptac



](https://help.apple.com/pdf/security/es_ES/apple-platform-security-guide-y.pdf#50#44)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Google Home ja Nest: Yksityisyys- ja tietosuojakeskus - Hallitset tiliäsi itse

Voit muuttaa asetusta milloin tahansa. ... Yli 18 kuukautta vanha kodin historia poistetaan oletuksena automaattisesti. Voit laittaa automaattisen poiston pois päältä tai muuttaa sen asetukseksi 3 tai 36 kuukautta.



](https://support.google.com/googlenest/answer/9415830?hl=fi&ref_topic=7173611#4)[

purl.fdlp.gov

In addition to the features described above that are available to all Nest camera users, users can also choose to purchase a sub...

Using the Nest Aware service, users can choose to continuously record and store camera footage captured by their doorbell for up to 30 days. ... Google's Privacy Policy (available at https://policies.google.com/privacy) applies ... and how you can update, manage, export, and delete your information. In addition...



](https://purl.fdlp.gov/GPO/gpo253757#20#16)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

FAQ terkait privasi: Google Nest - Kirim masukan terkait

Perubahan izin yang dilakukan pada Google Home Anda, seperti menambahkan atau menghapus orang dari rumah ... Kebijakan Privasi Google berlaku untuk perangkat dan layanan rumah yang terhubung dari kami dan menjelaskan jenis informasi yang kami kumpulkan; alasan kami mengumpulkannya; serta cara Anda dapat memperbarui, mengelola, mengekspor, dan menghapus informasi Anda.



](https://support.google.com/googlenest/answer/9415830?hl=id&authuser=7&ref_topic=7173611&co=GENIE.Platform%3DiOS#1)[

![](https://cdn.deepseek.com/site-icons/senate.gov)

judiciary.senate.gov

Images and video data collected via Google's smart-display devices or Nest Cams are not used to develop, test, or train biometri...

Using the Nest Aware service, users can choose to continuously record and store camera footage captured by their doorbell for up to 30 days. ... Google's Privacy Policy (available at https://policies.google.com/privacy) applies to our ... and how you can update, manage, export, and delete your information. In addition...



](https://www.judiciary.senate.gov/imo/media/doc/3BD806CC-5056-A066-6087-5AF50E5B59E5/QFR%20Responses%20-%20White%20-%202021-06-15_829e2a74-278d-41b9-bb37-8bb37c786808.pdf#3#2)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Central de privacidade do Google Home e Google Nest - Enviar feedback sobre…

mudanças nas permissões do Google Home, como a adição ou remoção de pessoas de uma casa ... A Política de Privacidade do Google se aplica aos nossos serviços e dispositivos de casa conectada e explica quais dados são coletados, por que fazemos isso e como atualizar, gerenciar, exportar e excluir suas informações.



](https://support.google.com/googlenest/answer/9415830?hl=pt-BR&authuser=8&ref_topic=7173611&co=GENIE.Platform%3DiOS#1)[

![](https://cdn.deepseek.com/site-icons/govinfo.gov)

govinfo.gov

Answer

Fixed and Nexus phones--devices where Google is the OS provider--receive security updates for at least 3 years from when the device first became available on the Google Store, or at least 18 months from when the Google Store last sold the device, whichever is longer.



](https://www.govinfo.gov/content/pkg/CHRG-115shrg58443/pdf/CHRG-115shrg58443.pdf#37#28)[

![](https://cdn.deepseek.com/site-icons/googlenestcommunity.com)

Google Nest Community

2026/02/11

How Long is Nest Camera Video Data Retained for Free Users? At least 10 days. - Enter a search word

The published video history periods depending on camera model and subscription type are valid. ... This process generally takes around 2 months from the time of deletion. This often includes up to a month-long recovery period in case the data was removed unintentionally." ... Data can remain on these systems for up to 6 months."



](https://www.googlenestcommunity.com/t5/Cameras-and-Doorbells/How-Long-is-Nest-Camera-Video-Data-Retained-for-Free-Users-At-least-10-days/td-p/790686#1)[

![](https://cdn.deepseek.com/site-icons/archive.org)

archive.org

Chromecast > Data security and privacy on devices that work with Assistant

Google's Privacy ... and how you can update, manage, export, and delete your information, including when you interact with the Google Assistant. ... Please read the Google Privacy Policy ... and our commitment to privacy in the home. to understand what data Google collects, why we collect it, and the settings and tools available to you to update...



](https://archive.org/download/gov.uscourts.cand.345331/gov.uscourts.cand.345331.303.21.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/gigazine.net)

GIGAZINE

2026/02/15

Google's network camera Nest reveals that past recording data that free users cannot play is automatically saved on the server - Google's network camera Nest reveals that past recording data that free users cannot play is automatically saved on the server

you can check the past 60 days of 'activity detected video history' and view up to 10 days of continuous video history 24 hours a day, 365 days a year. ... 'Videos for non-subscribers are marked for deletion ... Jackson pointed out that there is nothing in Google's terms of service that would



](https://gigazine.net/gsc_news/en/20260216-google-nest-cam-send-data-server#gsc.tab=0#1)[

![](https://cdn.deepseek.com/site-icons/inc.com)

Inc.com

2026/02/10

Google Nest Just Revealed It Keeps Video You Thought Was Deleted

Without a paid plan, Nest provides only a short window of event-based video history—roughly three hours. After that, clips are supposedly deleted. ... In other words, the footage exists in Google’s systems before you ever decide whether to pay to keep it.



](https://www.inc.com/jason-aten/google-nest-just-revealed-it-keeps-video-you-thought-was-deleted/91301163)[

![](https://cdn.deepseek.com/site-icons/ietf.org)

IETF Mail Archive

2026/08/30

IETF Mail List Archives Search Results - Ring, Amazon’s smart home security division, is adopting a new encryption standard called TAKE, short for Throw Away the Key Enc...

Ring, Amazon’s smart home security division, is adopting a new encryption standard called TAKE, short for Throw Away the Key Encryption, as its default method for protecting stored video. ... it can hand over to police ... It should also limit what the company can share with law enforcement.



](https://mailarchive.ietf.org/arch/search/?email_list=newsclips&gbt=1&index=J-69Mw2H2X1wZUd7NOSI4U1wYe8&token=CwnWmZUtysu1uWDZ#3)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/08/25

Ring is shaking up its camera encryption to ease privacy concerns - Skip to main content

Ring says its new encryption limits what it can give police The ‘Throw Away the Key Encryption’ (TAKE) method will become the default on all Ring cameras ... “Where TAKE is enabled, Ring will only be able to provide non-video information (such as basic subscriber information) and encrypted video files in response to the valid legal process.”



](https://www.theverge.com/tech/984838/ring-take-encryption-throw-away-the-key-law-enforcement#1)[

![](https://cdn.deepseek.com/site-icons/gizmodo.com)

Gizmodo

2026/08/25

Ring Says Its New Encryption System Could Make It Harder for Police to Access Videos - Skip to content

Ring Says Its New Encryption System Could Make It Harder for Police to Access Videos The new default system deletes Ring’s copy of encryption keys after 24 hours, limiting what the company can turn over to law enforcement. Reading time 3 minutes Amazon’s ... new encryption system designed to reduce how long the company itself can access them.



](https://gizmodo.com/ring-says-its-new-encryption-system-could-make-it-harder-for-police-to-access-videos-2000803553?utm_source=flipboard&utm_content=Gizmodo%2Fmagazine%2FTech#1)[

![](https://cdn.deepseek.com/site-icons/techrepublic.com)

TechRepublic

2026/08/26

Ring’s New TAKE Encryption Deletes Video Keys Without Giving Up AI Features - TechRepublic - Ring’s New TAKE Encryption Deletes Video Keys Without Giving Up AI Features

TAKE also affects what Ring says it can provide to authorities. The company responds to legally valid government demands, including search warrants, subpoenas, and court orders. Ring’s privacy policy says that when TAKE or E2EE protects footage, the company can provide non-video information but not the protected recordings.



](https://www.techrepublic.com/de/article/news-ring-take-encryption-ai/#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/08/25

Ring's new encryption should keep the company out of your security footage - Advertisement

Ring's new encryption should keep the company out of your security footage Ring is at last addressing some of its longstanding privacy issues by limiting its access to your security camera videos. The Amazon brand has introduced a ... Ring already bars its staff and law enforcement from accessing cloud videos without either your permission or a warrant. However ... to law enforcement's community requests.



](https://tech.yahoo.com/home/articles/rings-encryption-keep-company-security-151226424.html#1)[

![](https://cdn.deepseek.com/site-icons/cnn.com)

CNN

2026/08/25

Ring hopes new encryption tech will ease surveillance fears around its home security cameras | CNN Business - Ad Feedback

Ring hopes new encryption tech will ease surveillance fears around its home security cameras ... Ring’s update effectively means customers don’t have to worry about any third parties, including law enforcement and Amazon itself ... Ring will roll out the new ... Ring users can still voluntarily share footage with law enforcement if police request it through the company’s Neighbors app.



](https://www.cnn.com/2026/08/26/tech/ring-cameras-encryption-update#1)[

![](https://cdn.deepseek.com/site-icons/engadget.com)

Engadget

2026/08/25

Ring introduces better default encryption standards to address privacy concerns - Engadget - Ring introduces better default encryption standards to address privacy concerns

Ring introduces better default encryption standards to address privacy concerns ... Ring is addressing ... For years, police could request security camera footage from Ring and not even have to disclose anything publicly. ... It finally ended this request-for-access feature for law enforcement in 2024.



](https://www.engadget.com/2244922/ring-introduces-better-default-encryption-standards-to-address-privacy-concerns/#1)[

![](https://cdn.deepseek.com/site-icons/senate.gov)

markey.senate.gov

United States Senate

including an absence of security requirements for law enforcement agencies accessing user footage, restrictions on third- party sharing ... and declined to make end- to- end encryption the default for consumers. ... (NPSS), enabling law enforcement to request ... Does Amazon share biometric data — including any outputs of facial recognition use collected by Ring doorbells — either voluntarily or in response to legal process, with law enforcement agencies...



](https://www.markey.senate.gov/imo/media/doc/letter_to_ring_on_frt.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/howtogeek.com)

How-To Geek

2026/08/25

Ring's new encryption should keep the company out of your security footage - Ring's new encryption should keep the company out of your security footage

Ring is at last addressing some of its longstanding privacy issues by limiting its access to your security camera videos. The Amazon brand has introduced a TAKE (Throw Away the Key Encryption) security strategy that it claims will improve privacy for your footage while still enabling a raft of smart home features. ... Ring already bars its staff and law enforcement from accessing cloud videos without either your permission or a warrant. However...



](https://www.howtogeek.com/ring-take-security-camera-encryption/#1)[

![](https://cdn.deepseek.com/site-icons/techspot.com)

TechSpot

2026/08/26

Ring rolls out new encryption system that could limit what it can hand over to police - Ring rolls out new encryption system that could limit what it can hand over to police

Ring rolls out new encryption system that could limit what it can hand over to police ## New encryption deletes its own keys after 24 hours to limit access to your video footage ... It should also limit what the company can share with law enforcement. ... each Ring camera encrypts footage with keys that rotate every five minutes ... the company can only provide non-video information...



](https://www.techspot.com/news/113636-ring-new-encryption-limits-what-can-give-police.html?rand=98523#1)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/09/03

Ver estado de seguridad de tus dispositivos con Knox Matrix - No hay sugerencias

La función "Estado seguridad dispositivos" solo es compatible con ... 7.0 o posterior. Paso 1. ... Paso 2. ... Paso 3. Verás el teléfono actual y otros dispositivos en caso de haber más dispositivos compatibles asociados a tu cuenta Samsung. En este menú también verás el estado de tus dispositivos. Verificar el estado de seguridad de tus dispositivos desde SmartThings



](https://www.samsung.com/co/support/mobile-devices/how-to-view-the-security-status-of-your-devices-with-knox-matrix/#1)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/11/12

Make Your Smart Home More Secure: Samsung Appliances’ Built-In Security - Samsung Newsroom U.K.

The company’s unique security solutions, including Knox Matrix[2] and Knox Vault[3] have been applied to a wide range of home appliances, helping create a safer and more secure home environment. ... To stay ahead of this potential threat, Samsung is implementing PQC within Knox Matrix in home appliances.



](https://news.samsung.com/uk/make-your-smart-home-more-secure-samsung-appliances-built-in-security)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/08/24

Samsung Strengthens Smart Home Security With Additional ‘Diamond’ Security Ratings From UL Solutions in 2025 - Samsung Newsroom Malaysia

uses a camera during the cleaning process and offers features such as home monitoring through SmartThings connectivity.[5] Similarly ... Samsung is strengthening ... marketing claims verified by UL Solutions this year by applying Knox Matrix Trust Chain[6] and Knox Vault.[7] Knox Matrix Trust Chain utilizes blockchain technology to monitor connected appliances’ security status in real time. Knox Vault...



](https://news.samsung.com/my/samsung-strengthens-smart-home-security-with-additional-diamond-security-ratings-from-ul-solutions-in-2025)[

samsungiotcloud.com

保护隐私，担忧不再

通过Samsung Knox Matrix，可互相监控有无设备受到安全威胁，检测到威胁时会立即断开相应设备，确保家庭安全。可连接更多设备 ... 在全球家电行业中首次获得UL Solutions最高安全等级“钻石”认证的三星AI家电和连续10年获得CC认证的Smart TV助您轻松享受SmartThings服务。



](https://cxoffering.samsungiotcloud.com/virtual_ambassador/zh-US/118)[

samsungiotcloud.com

Safeguard personal data in your home

Samsung’s Knox Vault isolates and stores sensitive information, such as passwords and biometric data, in a dedicated hardware security chip. ... Powered by Samsung Knox Matrix, they continuously monitor for potential security threats, instantly isolating any compromised device to keep your home safe. ... Experience peace of mind and enjoy SmartThings with Samsung’s AI appliances...



](https://cxoffering.samsungiotcloud.com/virtual_ambassador/en-US/118)[

samsungiotcloud.com

คุ้มครองข้อมูลส่วนตัวในบ้านของคุณ

เมื่ออุปกรณ์ภายในบ้านของเรามีความฉลาดมากขึ้น ความปลอดภัยก็มีความสำคัญมากยิ่งขึ้นเช่นกัน แม้ว่าทุกคนจะหลับอยู่ อุปกรณ์ Samsung จะยังทำงานร่วมกันตลอดเวลาเพื่อปกป้องกันและกัน Samsung Knox Matrix จะทำหน้าที่คอยตรวจสอบ



](https://cxoffering.samsungiotcloud.com/retail_th/th-TH/118)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

news.samsung.com

三星於 SDC23 為開發者解鎖直覺、個人化與安全的體驗

主題演講中，三星介紹導入最新 SmartThings 互聯功能及升級版 Samsung Knox Matrix 而至臻完善的多裝 ... **Matrix，為三星基於區塊鏈的未來安全願景，能守護生態圈中的串聯裝置與用戶 ... Knox Matrix 中包括 Credential Sync 和 Trust Chain 的重要機制。



](https://news.samsung.com/tw/wp-content/themes/btr_newsroom/download.php?id=jSNoDMVUfN0DBYPklREZcHcIe2h9FIPFzKNa3EsW0Ao%3D#1#1)[

![](https://cdn.deepseek.com/site-icons/kompas.com)

Kompas.com

2025/04/03

Samsung Rilis Perangkat Elektronik Rumah Tangga Bespoke 2025 dengan Visi AI Home - Samsung Rilis Perangkat Elektronik Rumah Tangga Bespoke 2025 dengan Visi AI Home

Fitur ini dirancang untuk menyimpan informasi sensitif, seperti kata sandi dan data otentikasi, di dalam chip terpisah guna memberikan perlindungan lebih terhadap kebocoran data. Sebagai langkah menghadapi potensi ancaman siber masa depan, Samsung turut menerapkan teknologi post-quantum cryptography (PQC) pada perangkat yang memiliki layar, sebagai bagian dari Knox Matrix Credential Sync.



](https://tekno.kompas.com/read/2025/04/04/17041747/samsung-rilis-perangkat-elektronik-rumah-tangga-bespoke-2025-dengan-visi-ai?page=3#1)[

Appliance Retailer

2025/01/06

CES 2025: Samsung unveils ‘AI for All’ experience - Appliance Retailer

To protect user privacy, the Samsung Knox Matrix employs blockchain technology to shield the user’s home and data from digital threats. The Knox Matrix Dashboard is a simple security control centre which connects all home devices. As information syncs, the Knox Matrix’s Credential Sync centralises the ability to encrypt



](https://www.applianceretailer.com.au/ces-2025-samsung-unveils-ai-for-all-experience/)[

mydigitalpublication.co.uk

2025/01/19

New Electronics • January 2025 • Page 13

Samsung Knox Matrix has been developed to protect home appliances along with mobile devices and TVs using blockchain technology to ensure that connected devices are working together to protect the user’s home ... Knox Matrix’s Credential Sync ensures that data can only be encrypted or decrypted from the user’s devices...



](https://ne.mydigitalpublication.co.uk/january-2025/page-13)[

![](https://cdn.deepseek.com/site-icons/consumerreports.org)

Consumer Reports

2025/07/08

More Smart Home Companies Want to Hear from Security Researchers - Innovation at Consumer Reports

This story was updated on Monday July 14, 2025 to reflect new information from Abode, which alerted us to its dedicated security contact and shared its bug bounty program. ... The first step in creating any form of vulnerability disclosure policy (VDP) is ensuring that reports of security vulnerabilities make it to a monitored inbox in the company...



](https://innovation.consumerreports.org/more-smart-home-companies-want-to-hear-from-security-researchers/)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Bug Hunters

Android and Google Devices Security Reward Program Rules | Google Bug Hunters

We require submissions to demonstrate clear user risk and include a functional Proof of Concept (PoC). ... Active Hardware Targets – To be eligible for evaluation, vulnerabilities must reproduce on the latest publicly available build of the following supported devices: Pixel Families - Pixel phones, Pixel Tablets, and Pixel Watches Smart Home and Google Nest - Nest Cameras, Speakers, Displays, Thermostats, and Routers



](https://bughunters.google.com/about/rules/android-friends/android-and-google-devices-security-reward-program-rules)[

SimpliSafe Support Home

2026/05/31

How do I report a possible security issue in the system? | SimpliSafe Support

We have partnered with Bugcrowd to host a Bug Bounty program and encourage you to submit your reports with them. ... report would be better served by disclosing directly to SimpliSafe®, you can do that by following the policy below. Doing so foregoes the right to any reward as outlined in our Bug Bounty program. This policy ... 90 calendar days from receipt by us (software ... 120 ... (hardware, firmware...



](https://support.simplisafe.com/articles/alarm-event-monitoring/how-do-i-report-a-possible-security-issue-in-the-system?lang=en_US)[

![](https://cdn.deepseek.com/site-icons/hackerone.com)

HackerOne

eero - Bug Bounty Program | HackerOne

eero Program Policy ##Introduction The first mesh home wifi system, eero blankets any home in reliable and secure wifi. ... The eero Bug Bounty Program is designed to recognize security research on our consumer electronics, and associated Devices and Services cloud services and web/mobile applications through bounty rewards.



](https://hackerone.com/eero/policy_versions?type=team&change=3766578)[

FireBounty

2026/02/02

TWITTER

A vulnerability disclosure policy (VDP), also referred to as a responsible disclosure policy, describes how an organization will handle reports of vulnerabilities submitted by ethical hackers. A VDP must thus be easily identifiable via a simple way, a security.txt notice.



](https://firebounty.com/482867-domoticlabeu/)[

![](https://cdn.deepseek.com/site-icons/sonos.com)

Sonos

2026/03/30

Sonos协调漏洞披露政策 - Sonos

可以发送电子邮件至security@sonos.com报告漏洞（邮件主题为“Vulnerability Report”） ... - 报告漏洞后，外部各方预计在3个工作日内收到报告确认。 - 在整个处理过程中，包括修复漏洞期间，我们将每2-3周向外部各方通报其报告的状态。



](https://www.sonos.com/zh-cn/vulnerability-disclosure-policy)[

Meross

Meross Security Advisory Policy

how to send us security advisories, and how long we ask security researchers to wait before publicly disclosing vulnerabilities discovered. ... - Be fully aware that Meross has no vulnerability bounty program, which means that reporters will not receive payment for submitting vulnerabilities and that by submitting, reporters waive any claims to compensation.



](https://www.meross.com/tr-tur/security-advisory-policy)[

![](https://cdn.deepseek.com/site-icons/ixbt.com)

IXBT.com

2025/06/04

Сбер назначил награду за найденные уязвимости в умных устройствах - Сбер назначил награду за найденные уязвимости в умных устройствах

Для участия необходимо зарегистрироваться на платформе и ознакомиться с условиями. Каждый отчет рассматривается индивидуально с учётом детализации и значимости представленной информации. Для максимально эффективного анализа участники должны предоставлять подробные описания выявленных уязвимостей.



](https://www.ixbt.com/news/2025/06/05/sber-naznachil-nagradu-za-najdennye-ujazvimosti-v-umnyh-ustrojstvah.html#1)[

mediola - connected living AG

2026/08/18

Security - mediola - connected living AG

Security at mediola (Vulnerability Disclosure Policy) ... or other security-related concern affecting our products or services ... - Allow us reasonable time to investigate and remediate the reported vulnerability before disclosing any information publicly (Coordinated Vulnerability Disclosure). - Avoid any actions that could negatively impact the availability or performance of our services...



](https://www.mediola.com/en/security-2)[

Sylvania Group

Descubrimiento y divulgación de vulnerabilidades

# DESCUBRIMIENTO Y DIVULGACIÓN DE VULNERABILIDADES # VULNERABILITY DISCOVERY AND DISCLOSURE ## VULNERABILITY DISCOVERY AND DISCLOSURE Vulnerability discovery and disclosure policy Version 1.5– Mar



](https://www.sylvania-group.com/es-es/pagina-de-inicio-profesional/legal/descubrimiento-y-divulgacion-de-vulnerabilidades/)[

![](https://cdn.deepseek.com/site-icons/freshfields.com)

Freshfields

2026/01/18

Decoding the Cyber Resilience Act – Part 1: Scope and Impact | Freshfields

The Cyber Resilience Act (Regulation (EU) 2024/2847, the CRA) establishes a harmonised EU framework imposing cybersecurity requirements for products with digital elements made available on the Union market. In force since 10 December 2024 ... It includes common connected devices, such as smart home devices, security cameras, and wearable fitness trackers, as well as standalone software, such as mobile apps.



](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/decoding-the-cyber-resilience-act-part-1-scope-and-impact-102m2cz)[

![](https://cdn.deepseek.com/site-icons/sgs.com)

SGS TIC Mall

2026/07/01

Digital trust series | Securing Your Smart Home: Are You Ready for the EU’s Cyber Resilience Act?

The European Union has officially stepped in to address this with the Cyber Resilience Act (CRA). With full enforcement arriving in December 2027, security is moving from an optional "extra" to a mandatory baseline for anyone selling electronics in the EU.



](https://ticmall.sgs.com/zh/blog_details/ee-regulations-update-digital-trust-series-securing-your-smart-home-are-you-ready-for-the-eu-s-cyber-resilience-act)[

![](https://cdn.deepseek.com/site-icons/bund.de)

Bundesamt für Sicherheit in der Informationstechnik

2026/09/10

Cyber Resilience Act

All products sold in the EU that contain ‘digital elements’ must fulfill the essential requirements of the CRA. ... Consequently the CRA applies to both connected hardware products (e.g. smartphones, laptops, smart home products, smart watches, internet connected toys, but also microprocessors, firewalls and smart meter gateways within smart



](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber_Resilience_Act/cyber_resilience_act_node.html?utm_source=handpickedberlin&utm_medium=email&utm_campaign=can-you-learn-german-with-netflix)[

![](https://cdn.deepseek.com/site-icons/kirkland.com)

Kirkland & Ellis LLP

2026/09/21

The EU Cyber Resilience Act: Preparing for the New Reporting Obligations for “Products With Digital Elements” | Publications | Kirkland & Ellis LLP

The CRA applies to all “products with digital elements”, both hardware and software, that have a direct or indirect data connection to other devices or networks. Products in scope range from consumer IoT devices (smart watches, baby monitors, connected home devices) to enterprise software, industrial systems, operating systems and firmware.



](https://www.kirkland.com/publications/kirkland-alert/2026/09/the-eu-cyber-resilience-act)[

![](https://cdn.deepseek.com/site-icons/sgs.com)

SGS TIC Mall

2026/07/01

Digital trust 系列 | 守護智慧居家安全：您準備好迎接歐盟的網絡韌性法案嗎？

為了應對這些風險，歐盟正式推出了《網絡韌性法案》（Cyber Resilience Act，簡稱 CRA）。這項法規將於 2027 年 12 月全面強制實施，這意味著對於打算進入歐盟市場的電子產品製造商而言，網絡安全已不再是「加分選項」，而是進入市場的必備門檻 ... - 安全設計 (Security by Design)： 確保產品從最初的構想階段就將安全納入考量。



](https://ticmall.sgs.com/tc/blog_details/ee-regulations-update-digital-trust-series-securing-your-smart-home-are-you-ready-for-the-eu-s-cyber-resilience-act)[

![](https://cdn.deepseek.com/site-icons/europa.eu)

oeil.secure.europarl.europa.eu

Cyber Resilience Act

Certain categories of products with digital elements should be subject to stricter conformity assessment **procedures. Consumer products with digital elements categorised in this Regulation as important ... and should undergo a stricter conformity assessment procedure. This applies to smart home products with security functionalities, such as smart door locks, baby monitoring systems and alarm systems, connected toys and personal wearable health technology.



](https://oeil.secure.europarl.europa.eu/oeil/en/procedure-document-summary/pdf?id=1780114#1#1)[

Alston & Bird Privacy, Cyber & Data Strategy Blog

2025/12/09

New EU Regulation Clarifies Cybersecurity Rules for IoT Devices and Other ‘Products with Digital Elements’ | Alston & Bird Privacy, Cyber & Data Strategy Blog

‘Smart home general purpose virtual assistants’ referenced in the ‘important class I’ category of the CRA include PDEs whose core functionality is to ‘communicate on the public Internet, [and] process demands ... and that […] provide access to other services or control the functions of connected devices in residential setting.’ Examples include smart



](https://www.alstonprivacy.com/new-eu-regulation-clarifies-cybersecurity-rules-for-iot-devices-and-other-products-with-digital-elements/)[

![](https://cdn.deepseek.com/site-icons/lewissilkin.com)

Lewis Silkin

2026/07/30

EU Cyber Resilience Act guidance now out: here's what you need to know

With mandatory vulnerability reporting starting 11 September 2026 and full application from 11 December 2027 ... The CRA is aimed at bolstering cybersecurity across the EU by introducing stringent security requirements for digital products and ensuring that smart devices are secure throughout their lifecycle. For more details...



](https://www.lewissilkin.com/insights/2026/07/31/eu-cyber-resilience-act-guidance-now-out-heres-what-you-need-to-know-102nfex#1)[

![](https://cdn.deepseek.com/site-icons/euralarm.org)

Euralarm

2026/02/11

Euralarm publishes Fact sheet on Cyber Resilience Act classification for fire safety and security products

Euralarm publishes Fact sheet on Cyber Resilience Act classification for fire safety and security products ... Smart home products with security functionalities (Important Class I) Identity management systems and privileged access management products (Important Class I) Hardware devices with security boxes (Critical products)



](https://www.euralarm.org/resource/euralarm-publishes-fact-sheet-on-cyber-resilience-act-classification-for-fire-safety-and-security-products.html)[

Snellman Advokatbyrå

2025/12/01

Cyber Resilience Act: Technical Descriptions for Important and Critical Products Are Published - EU Digital Compliance Tracker (Snellman)

Class I and Class II important ... These include smart home virtual assistants, smart home security devices (such as smart door locks, cameras and baby monitors), internet-connected toys with interactive or location-tracking capabilities, and personal wearables designed for health monitoring or for use by children.



](https://digitalcompliance.snellman.com/technical-descriptions-for-important-and-critical-products-are-published/)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

Federal Communications Commission (.gov)

2026/08/10

U.S. Cyber Trust Mark

Which products will not be included in the program ... - The U.S. Cyber Trust Mark logo will appear on wireless consumer IoT products that meet the program’s cybersecurity standards. ... - Examples of eligible products may include internet-connected home security cameras, voice-activated shopping devices, smart appliances, fitness trackers, garage door openers, and baby monitors.



](https://www.fcc.gov/CyberTrustMark)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

docs.fcc.gov

FCC FACT SHEET\* Cybersecurity Labeling for Internet of Things Report and Order PS Docket No. 23-239

The FCC Label would include the U.S. Cyber Trust Mark and a QR Code linking to a product registry. ... IoT Labeling Program will provide consumers with an easy-to-understand and quickly recognizable FCC IoT Label that includes the U.S. government certification mark (referred to as the Cyber Trust Mark) that provides assurances regarding the baseline cybersecurity of an IoT product...



](https://docs.fcc.gov/public/attachments/DOC-400674A1.pdf?ref=broadbandbreakfast.com#15#1)[

![](https://cdn.deepseek.com/site-icons/archives.gov)

National Archives (.gov)

2025/01/06

White House Launches "U.S. Cyber Trust Mark", Providing American Consumers an Easy Label to See if Connected Devices are Cybersecure | The White House

Voluntary cybersecurity labeling program for wireless interconnected smart products ... their homes. Today, the White House announced the launch of a cybersecurity label for internet-connected devices, known as the U.S. Cyber Trust Mark ... as well as the trademarked, distinct shield logo that will be applied to products certified for the U.S.



](https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2025/01/07/white-house-launches-u-s-cyber-trust-mark-providing-american-consumers-an-easy-label-to-see-if-connected-devices-are-cybersecure/)[

![](https://cdn.deepseek.com/site-icons/federalregister.gov)

Federal Register (.gov)

2024/07/29

Secretary. - Federal Communications Commission

the Federal Communications Commission ... The program will provide consumers with an easy-to-understand and quickly recognizable FCC IoT Label that includes the U.S. Cyber Trust Mark and a QR code linked to a dynamic ... The Commission's IoT Labeling Program will provide consumers with an easy-to-understand and quickly recognizable FCC IoT Label that includes the U.S. ... as the U.S. Cyber Trust Mark) that provides assurances regarding the baseline cybersecurity of an IoT product...



](https://www.federalregister.gov/documents/full_text/xml/2024/07/30/2024-14148.xml#1)[

![](https://cdn.deepseek.com/site-icons/keystonecompliance.com)

Keystone Compliance

2026/06/21

FCC Cyber Trust Mark and Cybersecurity Testing | Applus+ Keystone

The FCC created it for consumer Internet of Things (IoT) devices like smart cameras, thermostats, locks, lights, wearables, baby monitors, and similar connected products. ... - The Cyber Trust Mark logo — This gives shoppers a quick visual signal that the product has gone through the FCC Cyber Trust Mark process.



](https://keystonecompliance.com/fcc-cybersecurity-testing/)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

docs.fcc.gov

Before the

The Commission’s IoT Labeling Program will provide consumers with an easy-to-understand and quickly recognizable FCC IoT Label that includes the U.S. government certification mark (referred to as the Cyber Trust Mark) that provides assurances regarding the baseline cybersecurity of an IoT product...



](https://docs.fcc.gov/public/attachments/FCC-24-26A1.docx#18#1)[

Fact Sheets by Year: 2019

2025/09/08

How the FCC Cyber Trust Mark Helps to Protect the Smart Home

Consumers have long lacked clarity on what makes a connected product 'secure.' As a voluntary cybersecurity labeling program for consumer IoT products, the Cyber Trust Mark aims to change that. ... The Cyber Trust Mark is a voluntary cybersecurity labeling program for wireless consumer IoT products created by the U.S. Federal Communications Commission (FCC). Under this program ... Displayed as an easy-to-recognize logo and QR code...



](https://w3inte.intertek.com.do/blog/2025/09-09-fcc-cyber-trust-mark/)[

![](https://cdn.deepseek.com/site-icons/fcc.gov)

docs.fcc.gov

Statement of

But if an attacker hacks your smart home device, like an Alexa ... If manufacturers want to be eligible for the US Cyber Trust Mark, they will have to declare that they have taken every reasonable measure to create a secure device. ... support period up front ... we are



](https://docs.fcc.gov/public/attachments/FCC-24-26A4.docx#1#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Moving guide for Nest devices - Send feedback on

Leave a device for the next resident Important: This action will clear your data from the device and can't be undone. To give a device to another person, first perform a factory reset: - Open the Google Home app . - Tap Home All devices , then touch and hold your device's tile. ... - Perform a factory reset.



](https://support.google.com/googlenest/answer/11151047?hl=en#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

移走 Nest 裝置的操作指南 - 傳送關於「」的意見

將裝置留給下一位住客 重要事項：此操作會清除裝置資料，且無法復原 ... - 開啟 Google Home 應用程式 。 - 輕按「住宅」圖示 所有裝置 ，然後 按住裝置圖塊。



](https://support.google.com/googlenest/answer/11151047?hl=zh-HK#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Guía para gestionar dispositivos Nest al cambiar de vivienda - Enviar comentarios sobre

Dejar un dispositivo para el próximo residente Importante: Esta acción borrará tus datos del dispositivo y no se puede deshacer. Para ceder un dispositivo a otra persona, restablece primero su estado de fábrica: Abre la aplicación Google Home . ... mantén pulsado el recuadro de tu dispositivo. Toca Ajustes Quitar dispositivo Quitar. Restablece el estado de fábrica.



](https://support.google.com/googlenest/answer/11151047?hl=es#1)[

![](https://cdn.deepseek.com/site-icons/roku.com)

Roku

2026/03/04

How to factory reset your Roku Smart Home device | Assistance Roku officielle France - How to factory reset your Roku Smart Home device

A factory reset disconnects your Roku® Smart Home device from Wi-Fi® and restores factory default settings. ... After unlinking your smart home device, you can then perform a factory reset to restore the device to factory default settings and ensure all data is erased. ... If the device is currently linked to someone else's account (for example ... you will need that person's email and password.



](https://support.roku.com/fr-fr/article/factory-reset-your-smart-home-device#1)[

hydrificwater.com

🎁 Can I Transfer My Droplet to Someone Else? | Droplet Resource Center

Yes — but only if the original owner performs a Factory Reset first. ... 💾 Historical data does not transfer between accounts 🛠️ Factory Reset is required to clear calibration and tagging data 🔐 Without a reset, the device stays locked to the original account



](https://help.hydrificwater.com/en/articles/11462096-can-i-transfer-my-droplet-to-someone-else)[

![](https://cdn.deepseek.com/site-icons/tuya.com)

Tuya

2024/08/19

有线网关与无线网关硬件复位会清除子设备信息吗？

1. 被原账号、原家庭配走，则子设备数据默认恢复； 2. 被原账号、不同家庭配走：子设备数据默认清除（云端会下发恢复出厂指令给网关，同时云端子设备数据清除）...



](https://support.tuya.com/zh/help/_detail/Kd2xdzz4k2sdp)[

![](https://cdn.deepseek.com/site-icons/lorex.com)

Lorex USA

2025/10/22

Transferring Lorex Devices and Account Ownership - Your cart

2. Remove the Device from Your App Account ... - Factory reset your device. Resetting will erase all settings and restore the device to its original state. ... - Tap the Reset button in the app to reset the device. - Once reset, tap Delete to remove it from your account. ... This will erase all settings and return the device to its original state for a new setup.



](https://www.lorex.com/blogs/help/transferring-lorex-devices-and-account-ownership?_pos=322&_sid=ad4e4d76f&_ss=r#1)[

![](https://cdn.deepseek.com/site-icons/huawei.com)

HUAWEI Global

2026/05/21

华为全屋智能主机 如何重启及恢复交房配置？

华为全屋智能主机 如何重启及恢复交房配置 ... “恢复交房”指的是将智能主机和全屋设备与之前绑定的华为帐号解除绑定 ... - 二次销售或转让：在出售房屋或将整套智能系统转让给他人前，需要进行此项操作以清除个人数据。



](https://consumer.huawei.com/cn/support/content/zh-cn15941926/)[

ntia.doc.gov

Risks to one’s personal and physical safety have become reality

Ideally, they would have an “easy button” to reset a device when sold, transferred or rented to others. ... while deleting user data and disabling any access by the previous owner ... Often listed as a home or car feature, sellers should be encouraged to disclose all such devices, disable their access, and provide new owners the ability to re-set them.



](https://www.ntia.doc.gov/files/ntia/publications/ota-docket170105023-7023-01.pdf#3#3)[

![](https://cdn.deepseek.com/site-icons/se.com)

维护操作日志

Decommissioning a Wiser System

Reset all Devices to the factory settings. Reset the Hub to the factory settings. NOTE: Before an IoT device is permanently removed from your network, a full factory reset must be done to erase all data. ### Removing a device Possible reasons ... Ownership of the Wiser System is to be transferred to another user.



](https://productinfo.se.com/elko-wiser-home/elko-wiser-home-system-user-guide-norway/English/System%20User%20Guide_%20Wiser%20Home_Norway%20\(bookmap\)_DD01117490.xml/$/SUG_Home-Decommissioning-FB340869)[

![](https://cdn.deepseek.com/site-icons/patsnap.com)

Patsnap Eureka

2026/08/03

CN122513769A – An identity verification method and device, an electronic device, and a storage medium | Patsnap Eureka - [0113] Based on the above examples, Figure 6 A flowchart illustrating the routine two-factor authentication process between user...

the user terminal (a combination of a mobile phone and an ESP32 module) initiates an authentication request by clicking "Unlock" on the App interface; the authentication master control device (smart lock) then broadcasts a wireless broadcast signal containing a first random number (R1=0x8A3F) and a first timestamp (T=1717020000) through its BLE controller...



](https://eureka.patsnap.com/patent/CN122513769A#4)[

![](https://cdn.deepseek.com/site-icons/nsf.gov)

par.nsf.gov

ten popular MaaG IoT devices, our study shows that it is generally difficult for mainstream IoT manufacturers to ensure that the...

Figure 2 outlines the AMT process we recovered from Kwikset (i.e., Kwikset Aura Smart Lock [2]) by reverse engineering the Kwikset mobile app and app traffic. The user with the Kwikset app first needs to be authenticated to the lock before operating it. Based on a BLE connection (non- authenticated ... the Kwikset app obtains a random string \(rs_{lock}\) from the lock (step 1&2)...



](https://par.nsf.gov/servlets/purl/10418560#7#2)[

abloy.com

Introduction

The invite is sent via SMS or email to a user’s device and requires action within a customisable time period, or the link will expire. The user will get a certificate, that represents their identity in the CUMULUS ecosystem. Once an invite link is used, it cannot be reused.



](https://www.abloy.com/global/market-documents/products/cumulus-whitepaper/ABLOY%20CUMULUS_White%20Paper_Technical%20Implementation%20and%20Cryptography_2024.pdf#1#1)[

patentimages.storage.googleapis.com

[0040] As described above, smart lock **104** may be opened by wirelessly transmitting a token from the user's mobile device to ...

[0040] As described above, smart lock **104** may be opened by wirelessly transmitting a token from the user's mobile device to the smart lock **104**. ... For example, the master or administrator may request the user provide identification information that proves the user's identity or authenticity...



](https://patentimages.storage.googleapis.com/27/0a/33/4c9e5477492e14/US20200043261A1.pdf#5#3)[

patentimages.storage.googleapis.com

US 20240221430A1

A method of enrolling a user at a biometric lockset is described. The method includes receiving user access information from a mobile device of an administrative user of the biometric lockset. The user access information indicates to the biometric lockset to enter an enrollment mode in which a user identity is associated with fingerprint data in a user entry within a memory of the biometric lockset.



](https://patentimages.storage.googleapis.com/95/3b/6b/5244e5a100b69f/US20240221430A1.pdf#5#1)[

Fenda Smart Home

2026/02/01

Airbnb and Short-Term Rentals: Remote Guest Access, Audit Logs, and Power Resilience with Fenda

Fenda combines CNAS-lab validated 3D face + palm vein MFA, duress/anti-peep protections, AES-encrypted Wi‑Fi/Tuya logging ... wrong‑try lockout, anti peep password smart lock input, dual authentication smart lock (e.g., face/PIN). ... Integrated cameras and intercom confirm identity before remote unlock...



](http://fendasmarthome.com/blog/airbnb-remote-guest-access-audit-power-resilience-fenda)[

patentimages.storage.googleapis.com

US 20240046722A1

A biometric wireless electronic lockset includes a processor, a battery, a memory communicatively connected to the processor, a user interface ... Each known user entry includes a user identity of a known user, biometric data, and an indication of whether the known user is an authorized user.



](https://patentimages.storage.googleapis.com/a4/e6/dc/78b84296dedcb0/US20240046722A1.pdf#4#1)[

![](https://cdn.deepseek.com/site-icons/patsnap.com)

Patsnap Eureka

2026/07/13

CN122394811A – A smart lock security authentication method based on mobile terminal virtual credentials | Patsnap Eureka - [0041] After the dynamic token is generated, it is output from the secure storage area to the application processing layer of th...

After obtaining the dynamic token, the application processing layer of the mobile terminal performs the operation of generating a response digest. This operation ... the door lock extracts the random challenge value and response digest content and forwards it to the local proof verification module ... the mobile terminal holds a valid credential identity key, which matches the credential



](https://eureka.patsnap.com/patent/CN122394811A#2)[

![](https://cdn.deepseek.com/site-icons/uspto.gov)

United States Patent and Trademark Office (USPTO) (.gov)

2024/04/01

in response to receiving an indication to initiate an enrollment code verification process based on a selection of the enrollment invitation link ... in response to receiving an indication that the unique enrollment code has been received by a mobile device and verified, enter into a secure enrollment mode that enables the guest user to enroll as a user of the electronic lock.



](https://patentsgazette.uspto.gov/week14/OG/html/1521-1/US11948415-20240402.html)[

![](https://cdn.deepseek.com/site-icons/raspberrypi.com)

Raspberry Pi Official Magazine

2026/05/12

ROOT Observer: a privacy-focused security camera — Raspberry Pi Official Magazine

“Each camera is a standalone device storing all footage locally. ... Notification thumbnails are stored in S3, but fully encrypted with keys only the intended device holds, similar to how Signal handles end-to-end encrypted notification images. ... all fully end-to-end encrypted with unique shared secrets per client.



](https://magazines-assets.raspberrypi.com/articles/root-observer-a-privacy-focused-security-camera)[

![](https://cdn.deepseek.com/site-icons/patsnap.com)

Patsnap Eureka

2025/12/10

US20250380014A1 – System and method for internet of things (IOT) camera security | Patsnap Eureka - [0265] In some embodiments of the invention, to protect user privacy, any audio / video content captured by IoT devices and stor...

camera-specific session keys and stored on persistent storage 2451 on the IoT service 120. ... 3146B may be stored within persistent storage 2451 on the IoT service 120, which



](https://eureka.patsnap.com/patent/US20250380014A1#9)[

m.media-amazon.com

EU Data Act Transparency Declaration

The device supports a flexible "Local- First" storage architecture, giving the user control over data location: Local Storage (Standalone): By default, video and audio are stored on a microSD card (up to 128GB) inserted directly into the camera. This data is encrypted and stays on the device.



](https://m.media-amazon.com/images/I/91Syj9NrzAL.pdf?ref=dp_product_quick_view#1#1)[

m.media-amazon.com

Product: Reolink Argus 3 Ultra (4K Battery Camera + Solar Panel) Date: 17 December 2025

Storage: Local (Default): The primary storage method is a microSD card (not always included). Data stored here is processed and encrypted locally. Cloud (Optional): If the user subscribes to Reolink Cloud, motion- triggered clips are encrypted and uploaded to remote servers for backup. ... Reolink does not access or store the user's video content or local SD card data unless the user actively subscribes to the Cloud storage service.



](https://m.media-amazon.com/images/I/812eMA5zOQL.pdf?ref=dp_product_quick_view#1#1)[

![](https://cdn.deepseek.com/site-icons/eufy.com)

Eufy

2026/08/30

eufy Support | Troubleshooting & Customer Service

Unless the users has opted to utilize our optional cloud backup feature, their videos stay local and are never stored in the cloud. ... Your videos are stored locally and secured with AES encryptions by your eufy devices. ... If you use cloud backup, data is encrypted between your eufy devices and AWS (Amazon Web Services). In addition...



](https://service.eufy.com/article-description/Privacy-Commitment-1617358267456?ref=uesr_cental)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/07/28

GitHub - x41sec/EncroCam: Privacy security camera based on commodity hardware · GitHub - GitHub - x41sec/EncroCam: Privacy security camera based on commodity hardware · GitHub

it will tell you where to configure further steps like an uptime monitor and SFTP server details, or you could run it as-is (storing data only locally). ... * ~40MB for EncroCam, mainly for the encrypted partition of 32 MB. ... and written to a file in the local recordings directory...



](https://github.com/x41sec/EncroCam/#install#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

Building a Privacy-Preserving Smart Camera System - 28times28absent28\text{\,} | 85yearstimes85years85\text{\,}\mathrm{y}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{s} | 511yearstimes511...

}\mathrm{s} and storage space needed to save to disk the encryption keys in the worst-case scenario ... The escrow material is encrypted and stored on the camera. ... Further, this encryption is performed end-to-end: data is encrypted locally at the camera before being stored in the cloud and decrypted locally at the smartphone after being retrieved. As a result...



](https://ar5iv.labs.arxiv.org/html/2201.09338#3)[

Wellbots

2026/09/20

Aqara Camera Hub G5 Pro PoE - Price:

The G5 Pro is compatible with HomeKit Secure Video, features encrypted local eMMC storage, and for the first time, supports end-to-end encryption of the footage sent to both Apple and Aqara clouds, bringing data security to a whole new level.



](https://www.wellbots.com/products/aqara-camera-hub-g5-pro-poe#1)[

![](https://cdn.deepseek.com/site-icons/synology.com)

Synology BeeDrive

BeeDrive & BeeStation

All video footage is stored locally on your BeeStation Plus. You retain full data ownership at all times. ... Remote access is provided through Synology QuickConnect, which establishes an ... Video streams are encrypted end to end and are never routed through Synology servers. Your data always remains on your own BeeStation Plus.



](https://bee.synology.com/en-br/BeeStation/BeeCamera)[

![](https://cdn.deepseek.com/site-icons/digitaltrends.com)

Digital Trends

2026/08/25

Ring’s new encryption hopes to solve surveillance fears without killing any smart features - Digital Trends may earn a commission when you buy through links on our site

Without a Ring subscription, none of this applies, though a Ring security hub with a microSD card offers local storage instead. If you lose your device, Ring offers several recovery options, including cloud backup, a passphrase, a passkey, another authorized device, or camera-based recovery.



](https://www.digitaltrends.com/home/rings-new-encryption-option-gives-you-more-control-over-who-can-access-your-camera-footage/#1)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey Support

2026/05/17

Software support for Homey Pro

We provide software support for Homey for at least five years after release. ... We have since extended this support period. Homey Pro (Early 2023) will now receive software updates until at least June 2031, similar to Homey Pro (2026).



](https://support.homey.app/hc/en-us/articles/13455016712604-Software-support-for-Homey-Pro)[

kyberturvallisuuskeskus.fi

Statement of compliance for the Cybersecurity Label

Cozify Hub is being supported with automated security fixes, feature updates and value-added services at least 5 years from the date of application. ... 1) Cozify Hub is provided with continuous Over-The-Air (OTA) software updates, typically once per 30 to 60 days.



](https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/file/statement-of-compliance-cozify-hub.pdf#1#1)[

Z-Wave Manuals

Homey Pro 2026

Future-proof platform support – Homey Pro (2026) will receive software updates until at least June 2031 – considered part of the same generation as the 2023 model. ... - Update guarantee: Software support until at least June 2031



](https://manual.zwave.eu/backend/make.php?lang=en&sku=ATHEHOMEY04PRO&cert=&type=mini)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Product support policy for smart products from IKEA - Product support policy for smart products from IKEA

gateway We will offer support for a minimum of three years after purchase, to ensure the hub / gateway ... We will offer support on smart products from IKEA for at least five years after purchase, if paired with DIRIGERA hub or TRÅDFRI gateway to ensure that your smart products from IKEA...



](https://www.ikea.com/us/en/customer-service/privacy-security/product-support-policy-for-smart-products-from-ikea-pub0d314780/#1)[

![](https://cdn.deepseek.com/site-icons/notebookcheck.com)

Notebookcheck

2025/12/09

Homey Pro 2026 steuert Smart-Home-Geräte von über 1.000 Herstellern - Homey Pro 2026 steuert Smart-Home-Geräte von über 1.000 Herstellern

Der Homey Pro Smart-Home-Hub erhält erstmals seit dem Jahr 2023 ein Upgrade ... Aus diesem Grund wird der Homey Pro 2026 als gleiche Generation wie das Modell aus 2023 behandelt, und soll mindestens bis 2031 mit Software-Updates versorgt werden.



](https://www.notebookcheck.com/Homey-Pro-2026-steuert-Smart-Home-Geraete-von-ueber-1-000-Herstellern.1182772.0.html#1)[

Recordere

2025/10/30

Homey Pro-software får forlænget support til juni 2031 - recordere.dk

Homey Pro-software får forlænget support til juni 2031 ... at softwaresupporten for hubben Homey Pro (og mini-udgaven) forlænges fra den oprindeligt lovede femårs-periode til mindst juni 2031. ... Bemærk dog at selvom supporten er forlænget til mindst juni 2031, betyder det ikke automatisk, at al hardwarefunktionalitet er garanteret i hele perioden.



](https://www.recordere.dk/2025/10/homey-pro-software-faar-forlaenget-support-til-juni-2031/#disqus_thread)[

![](https://cdn.deepseek.com/site-icons/coolblue.nl)

Coolblue

eufy Smart Display E10 | Coolblue | Smart home hubs - Insure your smart home hub

Introduction year and updates Guaranteed support with updates | 12 months after release date ---|--- Year introduced | 2025 Introduction month | April ... Support for future updates Expected date of last security update | April 2026 Expected frequency security updates



](https://www.coolblue.nl/en/product/963519/eufy-smart-display-e10.html#1)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Product support policy for smart products from IKEA - Product support policy for smart products from IKEA

DIRIGERA hub and TRÅDFRI gateway We will offer support for a minimum of three years after purchase, to ensure the hub / gateway ... for at least five years after purchase, if paired with DIRIGERA hub or TRÅDFRI gateway to ensure that your smart products from IKEA



](https://www.ikea.com/pt/en/customer-service/privacy-security/product-support-policy-for-smart-products-from-ikea-pub0d314780/#hnf-content#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Help

Mises à jour de sécurité et résultats de la validation de sécurité pour les appareils Google Nest - Envoyer une rétroaction au sujet de…

Les appareils pour maison connectée de Google Nest recevront des mises à jour de sécurité automatiques pendant au moins cinq ans après leur date de mise en vente initiale dans la boutique Google Store des États-Unis. ... Nest Hub (2ᵉ génération)



](https://support.google.com/product-documentation/answer/10231940?hl=fr-CA&ref_topic=10123615#1)[

![](https://cdn.deepseek.com/site-icons/ikea.com)

IKEA

Product Support Guidelines: Smart Products - Product support policy for IKEA smart products

We offer software support within three years from the purchase date to ensure that the DIRIGERA hub / TRÅDFRI gateway ... We offer software support for our smart products within five years from the purchase date, provided they are connected to the DIRIGERA hub or TRÅDFRI gateway, to ensure that the products...



](https://www.ikea.com/no/en/customer-service/privacy-security/home-smart-policy/#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

Who Will Fix This? Roles for IT-Security Incident Response in the Smart Home

In this work, we systematize roles relevant for incident response in smart homes through a systematic literature review of 22 studies in HCI and usable security. ... Our findings show that incident response in smart homes cannot be reduced to technical remediation by a single actor, but requires coordinating actions across overlapping roles. ... we systematize roles



](https://dlnext.acm.org/doi/pdf/10.1145/3772363.3799356?__cf_chl_tk=i6pSJlP0.arrbL.XT1c.nCjnjFxcrrwA7XBD6IBQDCU-1786181396-1.0.1.1-mMh4Ol9gdx_XBHp1gTjhxQsv2gtbogbdQmSMlfrcypk#2#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

ieee.org

2026/04/06

An Automated VAPT Framework for Smart Home IoT Environments: Protocol-Aware Vulnerability Detection and Mitigation

The proliferation of Internet of Things (IoT) devices in smart homes has enhanced automation, comfort, and energy efficiency while simultaneously ... This research presents ProVAPT SmartHome, an automated and protocol-aware Vulnerability Assessment and Penetration Testing (VAPT) framework specifically designed to secure smart home IoT ecosystems.



](https://xplorestaging.ieee.org/document/11459590)[

![](https://cdn.deepseek.com/site-icons/punto-informatico.it)

Punto Informatico

2026/09/10

Vulnerabilità nei prodotti: segnalazione obbligatoria in UE

A partire da oggi, produttori hardware e software sono obbligati ad inviare segnalazioni per vulnerabilità attivamente sfruttate e incidenti gravi. ... dispositivi per smart home (elettrodomestici ... - Report finale entro 14 giorni dalla disponibilità di una misura correttiva (patch) per le vulnerabilità...



](https://www.punto-informatico.it/vulnerabilita-prodotti-segnalazione-obbligatoria-ue/)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

JavaScript disabled - Who Will Fix This

response in smart homes cannot be reduced to technical remedi ... A well-researched approach to remedy attacks is Incident Re- sponse (IR). ... systematize roles involved in smart home incident response, identi- fying four internal roles (Primary User, Incidental User, Informal IT Administrator, and Attacker) that are central to how incidents



](https://dl.acm.org/doi/epdf/10.1145/3772363.3799356#1)[

mediola - connected living AG

2026/08/18

Sicherheit - mediola - connected living AG

Sicherheitsbezogene Hinweise und Schwachstellenmeldungen richten Sie bitte direkt an unser Product Security Incident Response Team (PSIRT) ... Erstbewertung | Innerhalb von 5 Werktagen (Mo-Fr) | Wir überprüfen die Lücke auf Validität und Schweregrad (z.



](https://www.mediola.com/security-info)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dlnext.acm.org

<table><tr><td>Role</td><td>Responsible</td><td>Accountable</td><td>Consulted</td><td>Informed</td></tr><tr><td>Primary User</td...

External roles shape the conditions under which smart home incident response is possible. ... Internet Service Providers (ISPs) can observe ... ISPs typically lack insight into household roles, device ownership, or interpersonal context, and remain limited to detection and notification rather than in- home remediation [20 ... Smart home security incidents challenge traditional incident response assumptions due to informal authority, unequal access, and multiple affected household members.



](https://dlnext.acm.org/doi/pdf/10.1145/3772363.3799356?__cf_chl_tk=i6pSJlP0.arrbL.XT1c.nCjnjFxcrrwA7XBD6IBQDCU-1786181396-1.0.1.1-mMh4Ol9gdx_XBHp1gTjhxQsv2gtbogbdQmSMlfrcypk#2#2)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arxiv.org

R2: Validation Mechanisms Second, current guidance lacks mechanisms for validation

this suggests that improving smart home incident response does not necessarily require inventing new recommendations ... Report a cybercrime, incident or vulnerability. https://www.cyber.gov.au/report-and-recover/report, accessed: 2026-01-11



](https://arxiv.org/pdf/2603.21703#2#2)[

![](https://cdn.deepseek.com/site-icons/blackcloak.io)

BlackCloak

2024/12/23

How BlackCloak Responded to a CEO's Home Network Attack

The BlackCloak security team quickly identified the source of the vulnerability and recognized the immediate risk it posed. ... To remediate the issues, the BlackCloak team promptly contacted Liam and his security team with immediate recommendations. The original installation team was brought in to close the open port and change the default password to a secure one.



](https://blackcloak.io/client-stories/a-compromised-home-the-call-was-coming-from-inside-the-house/)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arxiv.org

Cybersecurity Guidance for Smart Homes: A Cross-National Review of Government Sources

incident reporting, general security recommendations, and incident response. Our findings show that governments provide abundant general security advice and accessible reporting channels, but structured incident response guidance tailored to smart homes is rare. Only two sources offer step- by- step recovery guidance for non- expert users, highlighting a gap between preventive advice and post- incident support.



](https://arxiv.org/pdf/2603.21703#2#1)[

![](https://cdn.deepseek.com/site-icons/ycombinator.com)

Hacker News

2025/08/12

We caught companies making it harder to delete your personal data online - Some companies somehow blatantly get away with not allowing any export at all

That will send the deletion request to every registered data broker in the state who will then have 45 days to comply. Part of that compliance is sending deletion notifications to everyone downstream that they have shared or sold your data to in the past. The penalty for not responding to a DROP request is going to be $200 a day...



](https://news.ycombinator.com/item?id=44888445#1)[

m.media-amazon.com

• I dati relativi ai punti funzione del dispositivo (DataPoint) vengono conservati per un periodo predefinito di 7 giorni, che p...

I dati relativi ai punti funzione del dispositivo (DataPoint) vengono conservati per un periodo predefinito di 7 giorni ... • Gli utenti possono cancellare i propri dati in qualsiasi ... i registri di utilizzo dei dispositivi vengono conservati per 7 giorni, quindi eliminati automaticamente.



](https://m.media-amazon.com/images/I/914kKL8VUtL.pdf#4#2)[

Shein governance, tracked over time.

US Right to Deletion with Exceptions | Eufy | ConductAtlas

Request Deletion of your information, subject to certain exceptions prescribed by law. ... You also have the right to object to the processing of Service Data or to export Service Data to another service. ... the right to have us delete Personal Data we maintain about you (subject to certain exceptions).



](https://conductatlas.com/platform/eufy/eufy-privacy-policy/provision/CA-P-064175/us-right-to-deletion-with-exceptions/)[

m.media-amazon.com

Het in de Smart Life-app geïntegreerde energiebesparingsalgoritme genereert labels voor "aanbevolen temperatuur" en "afwezig/aan...

Webselfservice-export : Bezoek het officiële privacyplatform op https ... → Exporteer ... 5.2 Gegevensverwijderingsproces ... Apparaat verwijderen" en vink ... • Het systeem activeert onmiddellijk het gegevensverwijderingsproces, en alle historische apparaatgegevens (inclusief cloud en lokale cache) worden permanent verwijderd.



](https://m.media-amazon.com/images/I/81KdQ3kbiYL.pdf?ref=dp_product_quick_view#6#6)[

m.media-amazon.com

Déclaration de Transparence (Data Act)

Vous disposez d’un droit d’accès immédiat et gratuit via l'application Bosch Smart Home. Vos historiques sont exportables aux formats JSON ou CSV. ... Conservation et suppression Les données sont conservées le temps nécessaire à la prestation de services. Vous pouvez supprimer vos données à tout moment via les paramètres de votre compte.



](https://m.media-amazon.com/images/I/31jcQX2d1hL.pdf?ref=dp_product_quick_view#1#1)[

homeowners.cloud

2026/02/11

Smart Home Privacy & EU Sovereign Cloud — Buyer Guide

In 2026, buyers must treat smart‑home data like a closing condition — and ask for specific contract language and technical actions before signing. ... in many cases the seller or an individual user can request a data export or deletion from the vendor under GDPR.



](https://homeowners.cloud/smart-home-privacy-for-eu-homebuyers-how-the-new-sovereign-c)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

docs.silabs.com

2. New Product Family Setup: Once your Product Family is successfully certified by Connectivity Standards Alliance, Kudelski IoT...

Once your Product Family is successfully certified by Connectivity Standards Alliance ... 3. Certificate Request: Once a PAI is created, you can request a batch of certificates for your devices. For the CPMS workflow ... 4. Certificate Delivery: In the CPMS workflow ... which can then be programmed into your devices on the manufacturing line. 5. DACs are billed after your devices are manufactured and shipped.



](https://docs.silabs.com/matter/2.7.0/assets/matter.pdf#35#31)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

docs.silabs.com

Matter Device Attestation

Each certified device must be configured with a unique Device Attestation Certificate (DAC) and its corresponding DAC private key ... 2. The device issues a CSR, signed with its new private key, that is sent to the CA. 3. The CA issues the new certificate from the certificate Chain and signs it using its own PAI private key. 4. The newly created DAC is returned to the device.



](https://docs.silabs.com/matter-device-attestation/2.8.1/matter-device-attestation.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/keyfactor.com)

Keyfactor Docs

Matter - Guide for the OEM / Vendor | Keyfactor Docs

During manufacturing, each device is assigned an initial, long-lived (permanent) DAC certificate that is delivered and embedded by the OEM. Onboarding: Upon joining a network (Fabric), each device is vetted for genuineness and conformity and gets an operational, dynamic certificate (NOC) delivered by the LAN (Local Area Network) gateway.



](https://docs.keyfactor.com/solution-areas/latest/matter-guide-for-the-oem-vendor#Matter-GuidefortheOEM/#Manufacturing-in-Multiple-Locations)[

![](https://cdn.deepseek.com/site-icons/keyfactor.com)

Keyfactor Docs

During manufacturing, each device is assigned an initial, long-lived (permanent) DAC certificate that is delivered and embedded by the OEM. 2. **Onboarding:**Upon joining a network (Fabric), each device is vetted for genuineness and conformity and gets an operational, dynamic certificate (NOC) delivered by the LAN (Local Area Network) gateway.



](https://docs.keyfactor.com/solution-areas/latest/matter-guide-for-the-oem-vendor.md)[

MosChip

2026/07/15

A PoV on Matter Security and Zero Trust Architecture

While Matter establishes a strong foundation for secure device onboarding through mechanisms such as device attestation and certificate-based authentication ... genuine before allowing it to join the network and establishes an initial level of trust. ... In the current Matter model, once a device completes attestation, it is generally trusted for the rest of its lifetime unless it is explicitly removed or revoked.



](https://moschip.com/blog/device-software-engineering/a-pov-on-matter-security-and-zero-trust-architecture/)[

GitHub

.. _ug_matter_device_attestation: Matter Device Attestation ######################### .. contents:: :local: :depth: 2 D

Device Attestation (DA) is a process of verifying if a Matter device is certified and is produced by a manufacturer that is member of `Connectivity Standards Alliance`_. ... This data must be regenerated when :ref:`ug_matter_device_attestation_testing_da` of the Matter end product. ... To pass the Device Attestation procedure, a Matter ... Device Attestation procedure: factory data and Certification Declaration. ... After the manufacturer obtains VID, PID, PAI...



](https://raw.githubusercontent.com/nrfconnect/sdk-nrf/refs/tags/v3.1.0-preview1/doc/nrf/protocols/matter/end_product/attestation.rst#1)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

silabs.com

Agenda

Issuer: Bulby ... - Device Attestation Cert (DAC) ... All commissionable Matter Nodes SHALL include a Device Attestation Certificate (DAC) and corresponding private key, unique to that Device. The DAC is used in the Device Attestation process, as part of Commissioning a Commissioner into a Fabric.



](https://www.silabs.com/documents/public/presentations/mat-201-building-a-secure-matter-solution.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/buildwithmatter.com)

Matter Handbook

During the development phase, the manufacturer is able test their Devices without the full Attestation process. ... 3. Commissionee generates the Attestation Information and signs it with the Attestation Private Key. 4. Commissioner recovers the DAC and PAI certificate from the Commissionee, and looks up the PAA certificate from its Matter trust store.



](https://handbook.buildwithmatter.com/how-it-works/attestation.md)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/28

docs-matter/sld391-matter-device-attestation/index.md at doccurator/2.8.0 · SiliconLabsSoftware/docs-matter - Skip to content

Matter Device Attestation ... this step in the Commissioning process is called Device Attestation. Each certified device must be configured with a unique Device Attestation Certificate (DAC) and its corresponding DAC private key ... The CA ... own PAI private key. The newly created DAC is returned to the device. ... - The commissioner ... - The commissioner ... attested) and makes an Attestation Request. - The commissionee



](https://github.com/SiliconLabsSoftware/docs-matter/blob/doccurator/2.8.0/sld391-matter-device-attestation/index.md#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2022/07/12

Attestazione | Matter | Google Home Developers

Oggetto - Numero di serie del certificato ... chiave privata di attestazione. - Il commissario recupera il certificato DAC e PAI dal dispositivo e cerca il certificato PAA nel suo archivio attendibile Matter. - Il commissario convalida le informazioni dell'attestazione.



](https://developers.home.google.com/matter/primer/attestation?authuser=2&hl=it)[

ioXt

2025/03/18

Cyber Trust Mark to Distinguish Secure Smart Home Devices — ioXt

the White House officially launched the U.S. Cyber Trust Mark program ... as a mechanism for companies providing wireless smart home devices to test and ... UL Solutions, a global independent test and certification company for electrical equipment, is the Lead Administrator. ... The ioXt Alliance is the global standard for securing IoT devices, offering certification and cybersecurity guidelines that ensure the safety and reliability of connected products.



](https://ioxt.com/news-events-blog/cyber-trust-mark-to-distinguish-secure-smart-home-devices)[

BTL Inc.

BTL检测集团 - Location：Home - > North America > USA - U

Home - > North America > USA - U.S. Cyber Trust Mark Program Countdown to Relaunch: ioXt Takes Over as Lead Administrator ... The U.S. Cyber ... While UL Solutions submitted initial recommendations in June 2025, ioXt is expected to revise and resubmit them. ... expected for smart home hubs, baby monitors, smart locks...



](https://www.newbtl.com/newshow.php?id=747#1)[

![](https://cdn.deepseek.com/site-icons/nextgov.com)

Nextgov/FCW

2026/04/12

FCC selects ioXt Alliance to lead cyber labeling program

The program, called the Cyber Trust Mark, was launched during the Biden administration and is designed to certify consumer smart devices with a label that deems them cybersecure. The ioXt Alliance is a standards and certifications body for internet-of-things devices like remote thermostats, fitness trackers and connected cars.



](https://www.nextgov.com/cybersecurity/2026/04/fcc-selects-ioxt-alliance-lead-cyber-labeling-program/412800/?oref=ng-category-lander-river)[

BTL Inc.

BTL检测集团 - 位置：首页 - > 北美 > 美国 - 美国 Cyber Trust Mark 计划重启倒数：ioXt 接手首席管理者

任命非营利组织 ioXt Alliance 为 U.S. Cyber Trust Mark 计划首席管理者(Lead Administrator),接替去年底退出的 UL Solutions ... UL Solutions 虽已于 2025 年 6 月提交初步建议,但 ioXt 预计将进行调整与重新提交。



](https://newbtl.com/cn/newshow.php?id=747#1)[

東研信超股份有限公司（BTL）

Contact

The U.S. Cyber Trust Mark is a voluntary FCC-led cybersecurity certification and labeling program for consumer IoT products, modeled after the successful Energy Star framework. ... While UL Solutions submitted initial recommendations in June 2025, ioXt is expected to revise and resubmit them. ... expected for smart home hubs, baby monitors, smart locks...



](https://www.btl.com.tw/men/newshow.php?id=749)[

VitalLaw.com

2026/04/14

New Administrator Chosen for FCC’s IoT Security Program

The FCC has selected ioXt Alliance (ioXt) as the new lead administrator of the U.S. Cyber Trust Mark Program ... some IoT (Internet of things) devices may display a seal of approval ... ... a voluntary cybersecurity labeling program under which manufacturers of some IoT (Internet of things) devices may display a seal of approval if their devices comply with IoT security guidance issued by the National Institute of Standards and Technology.



](https://www.vitallaw.com/news/new-administrator-chosen-for-fcc-s-iot-security-program/cspd0129e06391cb9b4c37a36541c170e862fb#.)[

BTL Inc.

BTL检测集团 - 位置：首页 - > 北美 > 美国

任命非营利组织 ioXt Alliance 为 U.S. Cyber Trust Mark 计划首席管理者(Lead Administrator),接替去年底退出的 UL Solutions。这项决定为历经半年空窗期的美国消费性 ... UL Solutions 虽已于 2025 年 6 月提交初步建议,但 ioXt 预计将进行调整与重新提交。



](https://newbtl.com/m/newshow.php?id=747#1)[

東研信超股份有限公司（BTL）

2026/04/22

美國 Cyber Trust Mark 計畫重啟倒數：ioXt 接手首席管理者-東研信超

1、ioXt 提交技術標準與測試程式建議:作為首席管理者,ioXt 必須識別或開發 IoT 專屬標準與測試程式,並建議 FCC 核准;UL Solutions 雖已於 2025 年 6 月提交初步建議,但 ioXt 預計將進行調整與重新提交。



](https://www.btl.com.tw/news/392)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

news.samsung.com

Newsroom Beitrag

Eines seiner Dienste, das IoTSicherheitsbewertungsprogramm, prüft unter anderem, wie sicher vernetzte Geräte und SmartHome-Produkte sind. ... 1 Zertifikat V747452 für den Family Hub+ (https://verify.ul.com/verifications/1302)



](https://news.samsung.com/de/wp-content/themes/btr_newsroom/download.php?id=wt3jq9OdP6Vh1akko57dWncIe2h9FIPFzKNa3EsW0Ao%3D#1#1)[

CISO Whisperer

2026/04/14

FCC Picks IoXt Alliance To Lead U.S. Cyber Trust Mark Program - CISO Whisperer

The Federal Communications Commission selected the ioXt Alliance as the new lead administrator for the U.S. Cyber Trust Mark Program ... internet-connected



](https://cisowhisperer.com/fcc-picks-ioxt-alliance-to-lead-u-s-cyber-trust-mark-program/)