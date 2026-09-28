---
modified: 2026-09-28T20:43:08+03:00
---
This test matrix synthesizes published test reports, independent laboratory methodologies, vendor documentation, community bug databases, and regulatory standards into a repeatable protocol. It does not represent a single controlled laboratory run; rather, it consolidates documented evidence across ecosystems and device categories, identifies where evidence is thin, and specifies the protocol by which a team could execute the matrix independently. The comparison table reflects observed results where available and marks untested cells explicitly.

---

## 📋 Reproducible Test Protocol

### Scope and Inventory

Test at least **four ecosystems** (Apple Home, Google Home, Amazon Alexa, Samsung SmartThings), with Home Assistant as a reference local controller. The device inventory must include at least one device from each of the following categories:

| Category | Minimum Required Devices | Protocol Diversity |
|---|---|---|
| **Lock** | 2 (one Matter-native, one bridge-based) | Matter-over-Thread, Matter-over-Wi-Fi, or bridge |
| **Sensor** | 2 (one battery-powered, one mains-powered) | Matter-over-Thread, Zigbee bridge |
| **Light** | 2 (one bulb, one switch/dimmer) | Matter-over-Thread, Matter-over-Wi-Fi |
| **Camera** | 1 (Matter 1.5-capable) | Matter-over-Wi-Fi |
| **Thermostat** | 1 (Matter-native) | Matter-over-Thread |
| **Energy device** | 1 (smart plug with power monitoring, or simulated inverter) | Matter-over-Wi-Fi |

Allion Labs' inventory model—124 devices across 53 brands, 105 models, seven radio protocols, eight voice platforms, 443 smartphones, and 453 access points—provides the benchmark for breadth. A single-vendor, single-protocol test teaches nothing.

### Environment Requirements

- **Network topology:** One router with VLAN segmentation capability; one Thread Border Router per ecosystem under test; at least one Wi-Fi 6 or Wi-Fi 7 access point.
- **Test controller phones:** One device per ecosystem (iOS 18+ for Apple, Android 15+ for Google, Alexa app latest for Amazon, SmartThings app for Samsung).
- **Network capture:** mDNS/Bonjour traffic capture capability; Thread sniffer if available.
- **Isolation capability:** Ability to disable WAN uplink while preserving LAN and Wi-Fi.

### Test Procedure

Each test case follows a fixed structure. Record **ecosystem, device, firmware version, controller version, network topology, date, steps, expected result, observed result, recovery time (seconds), user effort (clicks/taps/retries), and evidence (screenshots, logs, packet captures)**.

| Test # | Test Case | Steps | Expected Result | Failure Criteria |
|---|---|---|---|---|
| **T1** | **Onboarding (primary ecosystem)** | Scan Matter QR code, complete commissioning, name device, assign room | Device joins fabric, appears in app, responds to on/off within 2 s | Commissioning fails, >2 attempts required, device appears in wrong category |
| **T2** | **Onboarding (secondary ecosystem via multi-admin)** | Generate multi-admin code from primary ecosystem, add to secondary ecosystem | Device appears in both fabrics, responds to commands from both | Pairing fails, device appears but does not respond, state desync |
| **T3** | **Thread commissioning via Border Router** | Commission Matter-over-Thread device using Thread Border Router (MeshCoP) | Device joins Thread mesh, communicates through border router | Commissioning stalls, TLS handshake fails, SRP timeout |
| **T4** | **Device discovery** | Add new device to ecosystem, verify automatic discovery | Device appears in discovery list within 30 s | Device not discovered, requires manual intervention, appears after >60 s |
| **T5** | **Routine creation and execution** | Create automation (e.g., motion → light on), execute trigger | Routine runs within expected latency | Routine fails to trigger, executes wrong action, partial execution |
| **T6** | **Permission model** | Add guest user with restricted access; attempt to control restricted device | Guest cannot control lock/camera; can control permitted devices | Guest can control restricted devices, permission model not enforced |
| **T7** | **Firmware update** | Initiate OTA update from ecosystem app; monitor completion | Update completes, device returns online, version increments | Update fails, device bricks, version does not change, device offline |
| **T8** | **Local control (internet outage)** | Disable WAN uplink, preserve LAN; attempt basic device control | Basic commands work locally; cloud-dependent features fail gracefully | Local commands fail; device requires cloud round-trip |
| **T9** | **Border router outage** | Power off Thread Border Router; attempt to control Thread device | Thread device loses connectivity; recovery when border router restored | Device fails to recover, requires re-commissioning |
| **T10** | **Cloud shutdown simulation** | Block vendor cloud domain at DNS or firewall level; observe device behavior | Device maintains local control if local path exists; cloud features fail | Device becomes unresponsive; no local fallback |
| **T11** | **Device replacement** | Remove old device, add replacement with same Matter code or new commission | Replacement commissions successfully; routines update | Replacement fails to commission, routines break, ghost device remains |
| **T12** | **Migration between ecosystems** | Remove device from primary ecosystem; commission in secondary ecosystem | Device commissions in new ecosystem; old fabric cleaned up | Commissioning fails, device remains bound to old fabric, state inconsistency |

### Evidence Recording

For each test, record:
- **Screenshots** of app state before and after each step
- **Packet captures** for mDNS, Thread, and Matter interaction model traffic
- **Timing data** for commissioning, response latency, and recovery
- **Firmware and app versions** (exact build numbers)
- **User effort metrics** (taps, retries, manual interventions)
- **Failure classification** per the F0–F3 model described below

---

## 📊 Comparison Table: Observed Ecosystem Behavior

This table reflects documented behavior from published test reports and community evidence. Cells marked **—** indicate no reliable published data; cells marked **⚠** indicate mixed or conditional results. This is not a single controlled test run; it is a synthesis of available evidence.

| Test | Apple Home | Google Home | Amazon Alexa | Samsung SmartThings | Home Assistant (reference) |
|---|---|---|---|---|---|
| **T1 Onboarding success** | 98% (fastest QR recognition) | 95% (sometimes requires manual device type selection) | 92% (occasionally stalls at "discovering devices") | 90% (more steps, stable success) | ⚠ Dependent on dongle; commissioning via Matter Server can fail to advance |
| **T2 Multi-admin** | Robust for sharing; issues when receiving from Samsung | ⚠ Alexa→Google sharing consistently fails in testing | Does not fully support multi-admin; setup code generation inconsistent | ⚠ Apple→Samsung commissioning issues | Works but requires manual "Share device" per device |
| **T3 Thread commissioning** | 100% direct from hub; fails via MatterSupport extension | — | — | — | ⚠ Stalls after Thread attach; ULA routing and mDNS verified but commissioning does not progress |
| **T4 Device discovery** | Automatic, reliable | ⚠ Requires manual type confirmation | ⚠ Occasional stalls | Reliable | ⚠ Dependent on integration quality |
| **T5 Routine execution** | Local execution reliable | ⚠ Mixed; cloud dependency for complex routines | ⚠ Buggy; controls slower than legacy【—】 | Reliable for basic routines | Local execution reliable; AI-generated routines require review |
| **T6 Permission model** | ⚠ All-or-nothing for most devices; locks require secondary verification | ⚠ Voice Match + restricted profiles; uneven for guests | ⚠ Limited granularity | ⚠ Limited granularity | ⚠ Manual policy enforcement possible |
| **T7 Firmware update** | ⚠ OTA can fail; rollback limited | ⚠ OTA failures documented | ⚠ OTA failures documented | ⚠ Samsung fridge bricked by SmartThings update (2026) | ⚠ SONOFF OTA issues: update reaches 100% without version change |
| **T8 Local control (WAN down)** | Strong local control via HomeKit | ⚠ Google Home hubs can work locally with Matter | ⚠ Cloud-dependent features fail | ⚠ Local execution for basic commands | Strong local control (gold standard) |
| **T9 Border router outage** | ⚠ iOS retains "preferred" Thread network after border router removal; commissioning fails until restored【—】 | — | — | — | ⚠ Recovery requires re-commissioning in some cases |
| **T10 Cloud shutdown** | ⚠ iLife robot vacuum: F3 failure, no local fallback | — | — | — | Local integrations survive (Wemo example: HA local integration survived Belkin cloud shutdown) |
| **T11 Device replacement** | ⚠ Ghost devices can persist | ⚠ Routines may not update | ⚠ Routines may not update | ⚠ Routines may not update | ⚠ Requires manual re-commissioning |
| **T12 Migration** | ⚠ Apple→HA "relatively hassle-free" | ⚠ Rebuild routines required | ⚠ Rebuild routines required | ⚠ Rebuild routines required | Full export/import possible with backup |

### Latency Benchmarks (Documented)

| Ecosystem | Average Response Time | Stability |
|---|---|---|
| Apple Home | 0.3 s | Most stable, almost no failures |
| Google Home | 0.4 s | Stable; occasional first-tap delay |
| Amazon Alexa | 0.5 s | Relatively stable; slower during peak hours |
| Samsung SmartThings | 0.5 s | Stable; as fast as Samsung's own devices |

---

## 🧭 Failure Taxonomy

The F0–F3 failure classification model, developed in a controlled cloud disruption study, provides a reproducible framework for categorizing device behavior during infrastructure failure.

| Class | Label | Definition | Example |
|---|---|---|---|
| **F0** | **Full functionality** | Device operates normally across all tested scenarios | Local control path intact; device responds to commands during WAN outage |
| **F1** | **Partial degradation** | Device retains core function but loses advanced features | Smart plug operates locally but loses remote access and scheduling |
| **F2** | **Degraded state** | Device remains reachable but key functions fail or behave unpredictably | Thermostat maintains last setpoint but cannot be adjusted; state desync across fabrics |
| **F3** | **Unsafe or non-functional** | Device becomes unresponsive or behaves unsafely; no local fallback | iLife robot vacuum: F3 failure during cloud disruption; Eight Sleep smart bed: unable to cool or heat during AWS outage |

### Additional Failure Modes Observed in Testing

| Failure Mode | Description | Documented Example |
|---|---|---|
| **Commissioning stall** | Device attaches to Thread network but Matter commissioning does not progress | Eve Thermo gen5: fully verified IPv6/Thread/Matter setup, commissioning still does not proceed |
| **Argument parsing error** | Certification tool sends invalid commissioning method | TH UI sends `thread` but SDK expects `thread-meshcop` |
| **State desync across fabrics** | Same device reports different states in different ecosystems | Brightness set to specific percentage in one app shows different value in another |
| **Ghost device persistence** | Removed device still appears in ecosystem after decommissioning | Common after migration; requires factory reset and re-commission |
| **Firmware update bricking** | OTA update renders device non-functional with no rollback | Samsung Bespoke AI refrigerator: update pushed due to "system error"; device became inoperative |
| **Border router bounce** | Devices bounce between Thread networks from different ecosystems | HomePod Mini + Google Nest Hub causes erratic behavior; workaround is disabling one border router |

---

## 🎯 Prioritized Recommendations

### For Test Teams

1. **Test multi-admin as a first-class scenario, not an afterthought.** Multi-admin is the most fragile area of Matter interoperability. Pairing failures, state desync, and inconsistent permission models are documented across Apple, Google, Amazon, and Samsung. Allocate at least 30% of test time to cross-ecosystem sharing and permission scenarios.

2. **Separate certification conformance from real-world interoperability.** Matter certification proves the device speaks the protocol correctly; it does not prove the device behaves well in a house with three ecosystems, two border routers, and a mesh network. Use the CSA certification tool for conformance, but build a separate interoperability test suite with real devices and real network topology.

3. **Test local control with WAN disabled, not just cloud features with LAN present.** The presence or absence of a local control path determines device behavior during cloud unavailability. Disable only the WAN uplink while keeping LAN, Wi-Fi, and local servers powered. Record which functions survive and which fail.

4. **Use the F0–F3 classification for every outage test.** The taxonomy provides a reproducible, user-observable way to categorize device resilience without access to vendor internals. This enables comparison across devices and ecosystems.

5. **Test migration and replacement as destructive scenarios.** Assume routines will break, ghost devices will persist, and permissions will need to be re-established. Document the exact recovery steps and measure user effort in taps and retries.

### For Product Teams

6. **Design for graceful degradation, not just graceful failure.** Every cloud-dependent feature must have a documented local fallback. The F3 failure class—device becomes non-functional with no local fallback—is unacceptable for any device that controls physical access, comfort, or safety.

7. **Never rely on a single Thread Border Router.** Multiple border routers from different ecosystems can cause devices to bounce between networks. Design for a single, stable Thread network and document the workaround for multi-router environments.

8. **Make firmware updates reversible.** The Samsung refrigerator bricking incident demonstrates that OTA updates can render devices non-functional with no rollback. Matter OTA has limited recovery capabilities; design devices with a physical factory-reset path that restores the last known-good firmware.

9. **Publish support periods and update mechanisms as contractual commitments.** A support period is not a marketing claim. It should be stated in product documentation, reflected in the update mechanism, and honored through the end of the period.

10. **Measure active homes and automation executions, not registered devices.** Device counts overstate engagement by 2–3x. Track active devices per household, automation executions per week, and verified recovery times after infrastructure failure.

### For Standards and Certification Bodies

11. **Extend certification to include multi-admin and outage scenarios.** Current certification proves specification conformance but not operational resilience. Add mandatory test cases for multi-admin pairing, state consistency across fabrics, local control during WAN outage, and border router recovery.

12. **Standardize failure classification reporting.** Require manufacturers to publish F0–F3 classifications for their devices under documented outage conditions. This enables consumers and integrators to compare resilience across products.

13. **Define a canonical "ActiveHousehold" metric.** The absence of consistent measurement obscures the true state of adoption. Standardize metrics for active devices, automation executions, and verified savings so that vendor forecasts can be independently validated.

### Evidence Gaps Requiring Further Testing

| Gap | Why It Matters | Recommended Test |
|---|---|---|
| **Energy device interoperability** | Matter 1.5 energy clusters exist but no commercial PV inverter or battery was available for testing; researchers had to build a simulator | Test with first-generation Matter energy devices when available; document simulator results separately |
| **Cloud shutdown (real, not simulated)** | The F0–F3 model was developed in controlled DNS-blocking scenarios, not real vendor shutdowns | Coordinate with vendors to test documented shutdown scenarios (Belkin Wemo, Neato) |
| **Permission models for guests and children** | Research proposes "Circles of Trust" but no commercial product implements fine-grained permissions | Test guest access, child profiles, and short-term rental scenarios across all ecosystems |
| **Long-term firmware update reliability** | Single failure (Samsung fridge) is documented, but systematic OTA reliability data is absent | Track firmware update success rates across 100+ devices over 12 months |

---

## ⚠️ Limitations

This matrix is a synthesis, not a single controlled laboratory experiment. The comparison table draws from published test reports, community bug databases, vendor documentation, and independent laboratory methodologies. Sample sizes vary: Allion Labs' inventory covers 124 devices but does not publish per-test results; the cross-platform Matter test covers six ecosystems but uses a limited device set; community reports are anecdotal and may not generalize. **No single test in this matrix has been independently replicated across all four ecosystems with the full device inventory.** Any organization executing this protocol should expect results to differ from those reported here, and should record and publish their findings to contribute to the shared evidence base.

[

![](https://cdn.deepseek.com/site-icons/spc.org.cn)

中国标准在线服务网

2026/02/01

【国家标准】 信息技术 信息设备互连 智能家居系统评价参数体系和评价方法

本文件确立了智能家居系统互联互通的评价参数体系，包括功能、性能、兼容性、易用性、可靠性、安全等评价参数，描述了相应的评价方法。 本文件适用于智能家居系统互联互通能力的评价 ... 2026-02-01



](https://www.spc.org.cn/online/48ae1303c20e2167dfb9e3fd70c2b1bf.html)[

![](https://cdn.deepseek.com/site-icons/cesi.cn)

中国电子技术标准化研究院

智能家居互联互通测试技术和测试标准研究

智能家居互联互通测试技术和测试标准研究 为了明确不同技术层次下测试目标、测试方法和测试工具的适用边界，介绍测试工作过程、要素以及面向互联互通的测试分类 ... 结合智能家居技术架构特点，构建了面向接入与连接、协议互联与数据互通、场景构建与业务协同以及统一用户体验的分层测试架构。在此基础上...



](http://www.its.cesi.cn/portal/qkContent/articleDetail/f6b39ede-8bef-11f1-9b7a-6c92bf2dcd1b)[

![](https://cdn.deepseek.com/site-icons/it168.com)

It168

2026/07/13

2026智能照明生态横评：米家 vs Apple vs 华为 vs 天猫精灵，各生态入门成本、隐藏费用、切换代价全对比 - 数码

IDC中国智能家居追踪数据显示，截至2026年，"生态兼容性"以满分权重登顶消费者决策因素榜首——这直接影响你能接哪些设备、能用什么语音助手、以后想换平台的代价多大。当前中国智能照明市场形成四大主流阵营 ... - 不想被任何生态捆绑 → 选支持 Matter协议 的设备，跨平台互通



](https://m.it168.com/article_6940415.html#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

探用 IoT 装置製造商的事項標準

2026年3月（文件歷史記錄） ... 此標旨在改善不同製造商装置之間的相容性和互通性。事是一種開放式的智慧型家庭連線通協定 ... 事填1.5推出超越初始版本的廣充装置支援，現在包括增強型能源管理装置、機器人清空、空氣品質感應器、空氣淨化器，以及改善對攝影機和安全系統的支援。此標也新增了進功能 ... 隨著2025年11月20日推出1.5版，Matter智慧型家庭標准已大幅成熟。標准擴充了對攝影機串流...



](https://docs.aws.amazon.com/zh_tw/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#3#1)[

![](https://cdn.deepseek.com/site-icons/patsnap.com)

Patsnap Eureka

2026/05/14

CN122053418A – Method and system for testing access interconnection of swan monk system | Patsnap Eureka - [0019] In one feasible embodiment, assuming the application scenario is a cross-device interconnection test of the HarmonyOS eco...

assuming the application scenario is a cross-device interconnection test of the HarmonyOS ecosystem in smart homes ... The core test objective is to verify the device access compatibility and data interoperability ... a combined test indicator matrix is constructed, which includes the normal threshold range of each feature (e.g.



](https://eureka.patsnap.com/patent/CN122053418A#2)[

![](https://cdn.deepseek.com/site-icons/allion.com)

Allion Labs

2006/09/13

Smart Home Ecosystem & Device Consulting | Allion Labs

Allion Labs tests all four hops — against 124 real smart home devices across Matter, Thread, Zigbee, Z-Wave, Wi-Fi and Bluetooth LE, 443 smartphones and 453 access points. Service page maintained by the Allion Networking Business Group · Device figures from the Allion equipment register, extract of August 2026 · Last updated 4 September 2026



](https://www.allion.com/consulting/smart_home_interoperability_test-2/)[

![](https://cdn.deepseek.com/site-icons/eefocus.com)

Eefocus

2026/03/12

Matter协议跨平台兼容性实测：2026年各生态表现如何

Matter协议跨平台兼容性实测：2026年各生态表现如何 ... 最近几个月，陆续有机构和个人对主流生态的Matter兼容性做了实测。下面把测试结果汇总一下，看看苹果、谷歌、亚马逊、三星、涂鸦、小米这些平台，在真实使用场景下表现如何。 ## 1. 测试范围和方法 测试时间：2025年底至2026年初 ... - 跨生态控制一致性 ... 2026年Matter跨平台兼容性实测总结



](https://m.eefocus.com/e/1970935.html#1#1)[

![](https://cdn.deepseek.com/site-icons/cesi.cn)

中国电子技术标准化研究院

智能家居互联互通成熟度标准化需求分析研究

智能家居互联互通成熟度标准化需求分析研究 ... 识别出跨生态协同、动态语义互译等关键标准缺口，构建L1~L5 5 级互联互通成熟度模型，并在该模型的基础上提出基础共性 ... 应用与体验等标准化需求并构建“基础—技术—评估—应用”标准体系框架...



](http://www.its.cesi.cn/portal/qkContent/articleDetail/9e7846f1-8bf0-11f1-9b7a-6c92bf2dcd1b)[

![](https://cdn.deepseek.com/site-icons/renrendoc.com)

renrendoc.com

中华人民共和国国家标准

信息技术 信息设备互连智能家居系统评价参数体系和评价方法 ... 本文件确立了智能家居系统互联互通的评价参数体系，包括功能、性能、兼容性、易用性、可靠性、安全等评价参数，描述了相应的评价方法。



](https://www.renrendoc.com/free-down/5314121112004332.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/cesi.cn)

中国电子技术标准化研究院

智能家居互联互通标准体系研究

为了推动我国智能家居互联互通标准体系建设，在总结 GB/T 46456 系列标准以及其他智能家居互联互通国家标准、在研标准项目基础上，分析了现有智能家居互联互通国家标准的框架、通用要求、测试方法以及智能家居互联互通局域互联、设备配网、场景要求相关标准及测试方法。研究表明...



](http://www.its.cesi.cn/portal/qkContent/articleDetail/bf4614f4-8bef-11f1-9b7a-6c92bf2dcd1b)[

![](https://cdn.deepseek.com/site-icons/allion.com.tw)

百佳泰Allion Labs

2024/03/06

Matter (二) 智慧家庭生態系互通行不行 – 多源管理功能實測

多源管理提供蘋果 (Apple)、Google、亞馬遜 (Amazon) 與三星(Samsung) 等生態系統之間實現互通連結，多個用戶可以同時具有操控設備的權限，讓消費者能夠自由選擇生態系，即使家庭成員使用不同生態系的手機應用程式的情況下，也仍能夠分享設備管理權。



](https://www.allion.com.tw/tech_netc_matter_multi-admin/)[

preferredbypete.com

2026/04/02

Matter Protocol - Actually Ready in 2026?

The pairing process is better than it was but multi-admin setups (using the same device with HomeKit AND Google Home) still breaks randomly. ... The multi-admin thing drives me absolutely crazy too, and I think the underlying issue is that the spec allows too much flexibility in how manufacturers handle fabric sharing.



](https://preferredbypete.com/community/threads/matter-protocol-actually-ready-in-2026.47371/#post-69294)[

![](https://cdn.deepseek.com/site-icons/vercel.app)

C24-CRUNCH-ROBOTICS

2026/09/12

{REPO} · Code Crunch Worldwide

Commission your Matter-over-Thread light into two independent fabrics — chip-tool plus at least one of Apple Home or Google Home (ideally both) — and prove all controllers can toggle the same physical device independently. ... Subscribe to the OnOff attribute from one controller and toggle from ... demonstrating the device reports state changes into every fabric independently...



](https://codecrunchglobal.vercel.app/course?course=c7&path=curriculum%2Fweek-15-lorawan-zigbee-thread-matter%2Fchallenges%2Fchallenge-01-multi-admin-matter.md)[

digital-magazin

2026/07/31

Matter Smart Home: 6 Tests 2026 | dm

Multi-Admin und lokaler Steuerung wirklich zählt. ... Test 3: Funktioniert Multi-Admin für alle Menschen und Plattformen im Haushalt ... Genau hier wird Multi-Admin interessant. Der Begriff beschreibt die Möglichkeit ... Testen Sie Multi-Admin bewusst mit einem einfachen Gerät, etwa einer Lampe oder Steckdose.



](https://digital-magazin.de/matter-smart-home-6-tests-geraetechaos-2026/)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2024/08/19

Testing copies of Homeassitant - Configuration / Matter/Thread - Home Assistant Community - post by stevegroom on Aug 20, 2024

Best is to delete the Matter integration and uninstall the Matter Server on one of the two installation. Then readd them and use the multi-admin feature: On the first instance go to each device page and use the “Share device” feature to add it to the other controller.



](https://community.home-assistant.io/t/testing-copies-of-homeassitant/761968/4#1)[

![](https://cdn.deepseek.com/site-icons/aqara.com)

Aqara Forum

2026/09/19

FP400 - Can't reach on LAN - Aqara Products - Aqara Forum

From a Matter perspective, there is fundamentally no functional disadvantage for the second Matter controller if it has been added via a sharing or multi-admin code. ... Matter has no hierarchy between fabrics. A controller joining via a multi admin code gets its own fabric with its own operational credentials and is a full peer, not a guest.



](https://forum.aqara.com/t/fp400-cant-reach-on-lan/336270/41)[

The Thinking Home - A Practical Guide to Planning and Building a Reliable and Private Smart Home

2025/10/04

Matter Protocol News: The Illusion of Choice

Blog ### Does Matter Deepens Vendor Lock-In? In the world of the smart home, the latest Matter protocol news often presents a sleek, heavily marketed promise of a simplified, locally controlled futu



](https://xeazy.com/matter-protocol-news-how-matter-deepens-vendor-lock-in/)[

![](https://cdn.deepseek.com/site-icons/deepwiki.com)

DeepWiki

2026/03/06

Fabric Synchronization and Joint Fabric | project-chip/connectedhomeip-doc | DeepWiki - Loading

## Purpose and Scope This page explains Matter's multi-admin fabric management, fabric synchronization mechanisms, and joint fabric capabilities that enable cross-ecosystem device coordination. It co



](https://deepwiki.com/project-chip/connectedhomeip-doc/5.4-fabric-synchronization-and-joint-fabric#1)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey Community Forum

2026/08/22

Matter devices are unavailable - Questions & Help - Homey Community Forum

## Load more posts above ## post by Pascal_Nohl 3 days ago ## post by Doekse 3 days ago ## post by Rammstein 3 days ago ## post by Doekse 3 days ago ## post by Pascal_Nohl 3 days ago ## post by



](https://community.homey.app/t/matter-devices-are-unavailable/148583/382)[

21 MQTT Knowledge Check – Application Protocols

2026/06/28

38 Matter Fabric Security – Zigbee, Thread & Matter

Skip to main content ← All Modules | Zigbee, Thread & Matter Reader: user_p2lj9x9... Last content update: 29 June 2026 # 38 Matter Fabric Security zigbee-thread matter security commissioning



](https://iotclass.org/zigbee-thread/matter-arch-fabric-security.html#knowledge-check-1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/18

[Bug] Thread commissioning fails - TH uses "thread" but SDK expects "thread-meshcop" · Issue #879 · project-chip/certification-tool - Skip to content

[Bug] Thread commissioning fails - TH uses "thread" but SDK expects "thread-meshcop" #879 ... Thread commissioning via Border Router (MeshCoP) fails when initiated from the TH UI. The TH backend sends --commissioning-method thread to the Matter SDK, but the SDK only accepts thread-meshcop as a valid commissioning method choice, causing an argument parsing error.



](https://github.com/project-chip/certification-tool/issues/879#1)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2026/01/07

TLS Handshake Failure During TCAT Commissioning Using tcat_ble_client on nRF54L15 - Attachments (0)

I am currently working with the nRF54L15 ... However, during the commissioning process, the TLS handshake fails and commissioning does not complete. ### Issue Description When initiating the TCAT connection from thetcat_ble_client, the TLS handshake fails before successful authentication and network joining.



](https://devzone.nordicsemi.com/f/nordic-q-a/126430/tls-handshake-failure-during-tcat-commissioning-using-tcat_ble_client-on-nrf54l15/558313#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/03/13

Matter over Thread, commissioning fail in chip tool (CON-1595) · Issue #1325 · espressif/esp-matter - Skip to content

Matter over Thread, commissioning fail in chip tool (CON-1595) #1325 ## Description Description I have a Thread Network that seems to work perfectly. ... The Thread Border Router is not a Matter device, but the Child should be able to be commissioned. I noticed that the BR...



](https://github.com/espressif/esp-matter/issues/1325#issue-2920588505#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Developer

2025/12/16

MatterSupport extension MatterAddDeviceExtensionRequestHandler Thread device failure - MatterSupport extension MatterAddDeviceExtensionRequestHandler Thread device failure

When commissioning directly from my hub, the entire commissioning completes successfully 100% of the time. This failure only happens when I use MatterSupport to initiate commissioning for Matter over Thread devices specifically. ... Install the latest beta of iOS 26 on a test device and test again.



](https://developer.apple.com/forums/thread/793998#1)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2026/07/06

Matter over Thread Commissioning Fails: Device drops with SRP timeout and MAC Security/Duplicated errors - [1783455039.316] [3846:3849] [DMG] 0x1 = "" (0 chars),

[1783455039.317] [3846:3849] [CTL] Successfully finished commissioning step 'FailsafeBeforeThreadEnable' ... 'FailsafeBeforeThreadEnable' -> 'ThreadNetworkEnable'



](https://devzone.nordicsemi.com/f/nordic-q-a/128657/matter-over-thread-commissioning-fails-device-drops-with-srp-timeout-and-mac-security-duplicated-errors/568951#46)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/04/17

Matter‑over‑Thread commissioning stalls after successful Thread attach for Eve Thermo gen5(ULA routing and mDNS verified) - post by fazkoenig on Apr 19

Matter‑over‑Thread commissioning does not progress beyond discovery when using Home Assistant as the first Matter commissioner, even though ... This issue report documents a fully verified IPv6/Thread/Matter setup where commissioning still does not proceed, to help clarify whether this is an expected device limitation...



](https://community.home-assistant.io/t/matter-over-thread-commissioning-stalls-after-successful-thread-attach-for-eve-thermo-gen5-ula-routing-and-mdns-verified/1005391#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Developer

2025/05/12

Matter request extension no long working for Thread devices - Matter request extension no long working for Thread devices

My app has been working fine until just recently, now it can not add Matter devices over Thread (Wifi commissioning still works). ... error 12:18:03.369036-0700 homed [2610726604/1195614123(679130348)] ... to find metric hmmtrAccessoryMetricNameCommissioningAccessory to complete



](https://developer.apple.com/forums/thread/783968#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/09/24

Matter over Thread commissioning fails with SLZB-MR5U — "Discovery timed out" every time - Configuration / Matter/Thread - Home Assistant Community

No device could be commissioned (2 attempt(s) started of 2 discovered, all canceled or timed out) ... - Stale/conflicting Thread credentials on the commissioning phone — cleared all Home Assistant Companion App data and re-logged in; no change - Physical Thread radio range/interference — tested with the sensor a few cm from the SLZB-MR3...



](https://community.home-assistant.io/t/matter-over-thread-commissioning-fails-with-slzb-mr5u-discovery-timed-out-every-time/990934/7)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2024/09/17

Matter commissioning issue in ThreadNetworkSetup step - - State Not Answered

After commissioning with a smart speaker such as Apple HomePod, if the device is deleted and re-commissioned with a Test-harness, it results in an error with networkingStatus=2 in 'ThreadNetworkSetup'. networkingStatus=2 means that adding the network configuration would exceed the limit.



](https://devzone.nordicsemi.com/f/nordic-q-a/114809/matter-commissioning-issue-in-threadnetworksetup-step?ReplySortBy=CreatedDate&ReplySortOrder=Ascending#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/02/16

[Bug] TC-ACE-1.3 Fails in TH GUI for NFC-Thread Commissioning – Unable to Remove Passcode/Discriminator from dut_config · Issue #874 · project-chip/certification-tool - Skip to content

Mount the NFC Reader (E.g: HID OMNIKEY) and DUT (E.g: STM32WBA65I-DK1 board) to the controller. - Place the NFC reader and the DUT NFC antenna physically close to each other. - Reset the DUT



](https://github.com/project-chip/certification-tool/issues/874#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/03/01

I ran my smart home without the internet for a day—here’s what broke

I ran my smart home without the internet for a day—here’s what broke ... I disabled internet access for my smart home, but kept my local network up and running, and this is what stopped working. ... Mobile notifications stopped working ... it prioritizes



](https://tech.yahoo.com/home/articles/ran-smart-home-without-internet-131515870.html#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/07/19

Turns out, not all smart devices are that smart without Wi-Fi

I cut off my internet access ... local network. The goal ... Local-first platforms like Home Assistant keep logic and automation local, ensuring that your automations remain active even without an internet connection. Plan for local control that keeps your automations alive, even when the internet is unavailable.



](https://tech.yahoo.com/home/articles/turns-not-smart-devices-smart-100510839.html#1)[

![](https://cdn.deepseek.com/site-icons/xda-developers.com)

XDA

2026/03/01

I blocked all cloud access from my smart home for a week to see what still works

smart device in my house. ... Realistically, when it comes to smart homes, local control is the gold standard. While some big-name brands failed the test, the move to local mesh protocols and Matter has made the internet optional for a truly smart home. ## The local based products were king ... Alongside a range of my smart home devices staying completely stable, I also had some that failed the test completely.



](https://www.xda-developers.com/blocked-all-cloud-access-from-smart-home-for-week-what-still-works/#threads#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/09/03

Can Home Assistant Work During an Internet Outage? - Ready to ship

Run a Bounded WAN-Outage Test During a planned window, disable only the WAN uplink while leaving the router, switches, access points, DNS server, Home Assistant host, and local devices powered. ... dashboard access, event-to-action response, and integration state. ... test local DNS and the direct address before blaming the application.



](https://shop.zimaspace.com/blogs/support-tips/can-home-assistant-keep-working-temporary-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/androidpolice.com)

Android Police

2025/07/19

I turned off my Wi-Fi to see if my smart home would survive, and wow

The goal was to test how my smart home devices behaved without their cloud connection. ... Local-first platforms like Home Assistant keep logic and automation local, ensuring that your automations remain active even without an internet connection. Plan for local control that keeps your automations alive, even when the internet is unavailable.



](https://www.androidpolice.com/smart-home-vs-no-wifi/?post=39af-4d3c-96e1650027ec#thread-posts#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/28

Can Home Assistant Keep Local Control During an Outage? - English

local dashboard access, motion lighting, door or leak automations, climate changes, manual app control on Wi-Fi, state history, voice, remote access, and cloud-only devices. A practical real no-WAN test keeps the router, Wi-Fi, switches, and local servers powered while only the upstream internet path is removed.



](https://shop.zimaspace.com/blogs/tech-ai-hub/can-home-assistant-keep-reliable-local-control-during-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/09/03

인터넷이 끊겨도 Home Assistant를 사용할 수 있나요? - 한국어

범위를 제한한 WAN 장애 테스트를 실행하세요 계획된 시간에 WAN 업링크만 비활성화하고, 라우터, 스위치, 액세스 포인트, DNS 서버, Home Assistant 호스트 및 로컬 장치의 전원은 켜진 상태로 유지하세요.



](https://shop.zimaspace.com/ko/blogs/support-tips/can-home-assistant-keep-working-temporary-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/howtogeek.com)

How-To Geek

2026/03/01

I ran my smart home without the internet for a day—here’s what broke - I ran my smart home without the internet for a day—here’s what broke

so I decided to test it out. I disabled internet access for my smart home, but kept my local network up and running, and this is what stopped working. ... it prioritizes local control so that when the internet goes down, your entire smart home doesn't have to go down with it.



](https://www.howtogeek.com/i-ran-my-smart-home-without-internet/#threads#1)[

![](https://cdn.deepseek.com/site-icons/ieee.org)

IEEE Xplore

2026/05/12

Enerhome: IoT-Based Smart Home Management with Rainmaker

a dual-mode IoT-based smart home ... This paper proposes ENERHOME ... energy monitoring and appliance control system that aims at improving reliability and energy awareness in residential environments. ... Energy data is synchronized with the ESP RainMaker cloud platform for remote monitoring using a mobile application, while local control guarantees proper functioning in the case of network failure. The experimental validation testifies to the stability of operation, the precision of measurement within the limits of acceptable deviation, and switching of appliances timely.



](https://ieeexplore.ieee.org/document/11507775)[

![](https://cdn.deepseek.com/site-icons/makeuseof.com)

MakeUseOf

2026/05/20

I switched my smart home off the cloud and it finally works when the internet goes down

I switched my smart home off the cloud and it finally works when the internet goes down ... By adding Home Assistant to our smart home, we now have a system that works perfectly well even when our internet is taking a break. ... Home Assistant ... a virtual machine on my Mac mini server.



](https://www.makeuseof.com/switched-smart-home-off-cloud-finally-works-when-internet-down/?utm_medium=referral&utm_campaign=flipboard#1#1#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/24

‘I can’t believe it’s already broken’: Samsung customers are complaining to the company over spoiled food after an update bricked AI smart fridges

Samsung Electronics' online community forums were filled with dozens of posts from "Samsung Members" claiming their refrigerators became inoperative following a firmware update from the company's smart home platform "SmartThings." The customers reported that following the update, refrigerators went offline ... the Bespoke AI 4-Door refrigerator series released on or after 2024.



](https://tech.yahoo.com/home/articles/t-believe-already-broken-samsung-090000321.html)[

![](https://cdn.deepseek.com/site-icons/sonoff.tech)

SONOFF

2026/05/10

Fixing the SNZB-02DR2 OTA Issue: Improving Home Assistant Support for Telink OTA

In September 2025, the newly released SNZB-02DR2 worked as expected on SONOFF's own gateway, but OTA issues started to appear on Home Assistant. Reported symptoms included update check failures, upgrades reaching 100% without changing the installed firmware version, and missing firmware push notifications. ... The second is OTA image parsing failure.



](https://sonoff.tech/blogs/news/fixing-the-snzb-02dr2-ota-issue-improving-home-assistant-support-for-telink-ota)[

![](https://cdn.deepseek.com/site-icons/androidauthority.com)

Android Authority

2026/09/22

Samsung accidentally freezes its smart fridges with a software update

Samsung accidentally freezes its smart fridges with a software update ... - Samsung has halted a SmartThings update to smart fridges in Korea after some owners reported that their fridges stopped working. ... ZDNet Korea suggests that the update was pushed out to users due to a “system error.” ... had stopped distributing the update.



](https://www.androidauthority.com/samsung-accidentally-freezes-its-smart-fridges-with-a-software-update-3714472/?utm_campaign=DonanimHaber&utm_medium=referral&utm_source=DonanimHaber)[

![](https://cdn.deepseek.com/site-icons/impress.co.jp)

INTERNET Watch

2026/09/24

スマート冷蔵庫のファームウェアアップデート失敗で冷蔵機能が停止、食品が腐る事態に【やじうまWatch】

食品が腐る事態に ... サムスン製のスマート冷蔵庫の一部がファームウェアアップデートに失敗し、動作しなくなったことで、韓国内で問題になっている。 これはインターネットに接続可能なサムスンの「Bespoke AI」シリーズの4ドア冷蔵庫で9月22日に発生したもの。SmartThingsアプリを経由してのファームウェアアップデート直後に突然電源が落ち、動作しなくなったという。



](https://internet.watch.impress.co.jp/docs/yajiuma/2143157.html)[

![](https://cdn.deepseek.com/site-icons/ouest-france.fr)

Android MT

2026/09/23

Quand une mise à jour Samsung transforme des frigos connectés en boîtes inertes

En Corée du Sud, une mise à jour SmartThings a paralysé plusieurs réfrigérateurs Samsung, ravivant les inquiétudes sur la fiabilité des appareils électroménagers connectés. ... Samsung a confirmé sur son forum officiel qu’une erreur ... Autrement dit, un firmware encore en développement se serait retrouvé installé sur des appareils grand public, sans validation préalable.



](https://android-mt.ouest-france.fr/news/quand-une-mise-a-jour-samsung-transforme-des-frigos-connectes-en-boites-inertes/223211/)[

![](https://cdn.deepseek.com/site-icons/fortune.com)

Fortune

2026/09/24

‘I can't believe it's already broken’: Samsung customers are complaining to the company over spoiled food after an update bricked AI smart fridges | Fortune

Samsung Electronics’ online community forums were filled with dozens of posts from “Samsung Members” claiming their refrigerators became inoperative following a firmware update from the company’s smart home platform “SmartThings.” The customers reported that following the update, refrigerators went offline ... The firmware update appeared to have adversely impacted the Bespoke AI 4-Door refrigerator series released on or after 2024.



](https://fortune.com/2026/09/25/samsung-customers-complain-spoiled-food-after-update-bricked-ai-smart-fridges/?itm_source=parsely-api)[

![](https://cdn.deepseek.com/site-icons/techspot.com)

TechSpot

2026/09/23

Samsung confirms faulty update bricked its smart refrigerators, promises an emergency fix

Samsung confirms faulty update bricked its smart refrigerators, promises an emergency fix ... Many of these smart fridges stopped working earlier this week following a buggy firmware update. ... went offline ... Samsung has acknowledged the issue, claiming that the problem occurred because the update was accidentally released prematurely during a test earlier this week. ... From refrigerators to microwaves, and from toothbrushes to toilets, almost nothing seems safe from unnecessary AI integration circa 2026.



](https://www.techspot.com/news/113978-samsung-confirms-faulty-update-bricked-smart-refrigerators-promises.html)[

![](https://cdn.deepseek.com/site-icons/zhiding.cn)

至顶网

2026/09/23

三星部分AI冰箱因更新故障变身"巨型冰砖"

三星SmartThings软件更新误将内部测试固件推送给用户，导致韩国部分Bespoke AI四门冰箱断电无响应，食物腐坏。事件恰逢韩国秋夕假期前夕，部分用户被告知最快9月29日后才能获得上门服务。 据ZDNet Korea等媒体报道，三星在韩国推送的一次SmartThings软件更新出现问题，导致部分智能冰箱用户的设备失去响应。有用户投诉称，冰箱因关机无法制冷，导致食物变质。 三星表示正在解



](https://www.zhiding.cn/edge-ai/2026/0924/3200414.shtml)[

![](https://cdn.deepseek.com/site-icons/huawei.com)

HUAWEI Global

2026/05/21

华为全屋智能 蓝牙网关检测到新版本在升级过程失败页面显示为重试

适用产品： 华为鸿蒙智家 蓝牙网关 Lite，华为全屋智能 蓝牙网关 适用版本： 不涉及系统版本 适用产品： 适用版本： 适用产品 请选择 为您查询到以下结果，请选择 无法查询到结果，请重新选择 华为全屋智能 蓝牙网关检测到新版本在升级过程失败页面显示为重试 问题现象： 蓝牙网关检测到新版本在升级过程失败页面显示为“重试”状态。 解决方案： 您好，我们已在蓝牙网关3.1.



](https://consumer.huawei.com/cn/support/content/zh-cn16046174/)[

![](https://cdn.deepseek.com/site-icons/roku.com)

Roku

2026/01/27

How to fix Roku Smart Home device software update issues | Official Roku Support - How to fix Roku Smart Home device software update issues

Firmware updates for supported Roku® Smart Home devices are released on a regular basis, but a variety of issues can cause a failure, such as a bad internet connection or an outdated Roku Smart Home m



](https://support.roku.com/article/fix-smart-home-device-software-update-issues#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/29

新しいサーバーへの安全なHome Assistant移行チェックリスト - 日本語

新しいホームサーバーへのHome Assistant安全移行チェックリスト ... ロールバック用のコピーを利用できる状態で行う復旧テストとして扱ってください。新しいバックアップを作成し、古いサーバーの依存関係を記録してから、移行先で復元し、無線機器とネットワークストレージを再接続し、重要な自動化をテストします。



](https://shop.zimaspace.com/ja/blogs/support-tips/safe-home-assistant-migration-checklist-new-home-server#1)[

patentimages.storage.googleapis.com

（19）国家知识产权局

本发明公开了一种基于联邦学习的智能家居搬家方法及系统，通过在区块链中屏蔽智能家具隐私参数，根据相似智能家具集合和智能家具参数相似度，对旧居已屏蔽智能家具参数选择性迁移，获得客户新居智能家具新参数。提高了智能家具搬家的安全性...



](https://patentimages.storage.googleapis.com/2a/84/29/13e15e629a1d38/CN114817210B.pdf#2#1)[

![](https://cdn.deepseek.com/site-icons/nsf.gov)

par.nsf.gov

Based on the integration tests with legacy devices, the results reveal distinct differences in how each brand supports automatio...

Based on the integration tests with legacy devices, the results reveal distinct differences in how each brand supports automation rules involving both Matter- certified and non- Matter- certified devices. Amazon ... The Matter Protocol's multi- admin feature allows for devices to be commissioned and managed across multiple hubs, providing flexibility and interoperability in smart- home ecosystems.



](https://par.nsf.gov/servlets/purl/10618356#2#2)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/31

Vérifiez une restauration de Home Assistant avant de mettre le serveur à la retraite - Prêt à être expédié

Comment vérifier une restauration de Home Assistant avant de mettre l’ancien serveur hors service Ne mettez pas ... Une discussion de la communauté présente explicitement un test de restauration isolé comme la méthode sûre pour valider une migration entre plateformes de virtualisation. Cela confirme la méthode de test...



](https://shop.zimaspace.com/fr/blogs/support-tips/verify-home-assistant-restore-before-retiring-old-server#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/29

새 서버로 안전하게 Home Assistant를 이전하기 위한 체크리스트 - 한국어

이 작업을 롤백용 사본을 계속 사용할 수 있는 복구 테스트로 진행하세요. ... 기존 서버를 폐기하기 전에 인수 테스트를 수행하세요 - 예상한 사용자, 대시보드, 통합 구성 요소, 도우미 ... - 새 Home Assistant 호스트를 한 번 재시작한 후 중요한 로컬 제어 테스트를 반복하세요.



](https://shop.zimaspace.com/ko/blogs/support-tips/safe-home-assistant-migration-checklist-new-home-server#1)[

![](https://cdn.deepseek.com/site-icons/howtogeek.com)

How-To Geek

2026/01/21

Using Apple Home? You’re the perfect candidate for a Home Assistant upgrade - Using Apple Home? You’re the perfect candidate for a Home Assistant upgrade

Apple Home is my favorite of the “big 4” proprietary smart home systems, with its focus on local control and tight integration with Apple’s devices. ... Moving from Apple Home to Home Assistant is relatively hassle-free. ... Home Assistant is a platform that exists to bring devices together from a broad range of manufacturers and ecosystems.



](https://www.howtogeek.com/using-apple-home-youre-the-perfect-candidate-for-a-home-assistant-upgrade/#1)[

![](https://cdn.deepseek.com/site-icons/aqara.com)

Aqara Forum

2025/07/09

Hubitat Migration Experience: A Smooth Transition from SmartThings - General - Aqara Forum

Hi everyone, I wanted to share my recent experience migrating from SmartThings to Hubitat. ... The idea of having a more deeply supported ecosystem with Hubitat was really appealing. ... - Test each device: After migration, make sure to test each device’s functionality to ensure everything is working as expected.



](https://forum.aqara.com/t/hubitat-migration-experience-a-smooth-transition-from-smartthings/102834)[

![](https://cdn.deepseek.com/site-icons/jeedom.com)

Communauté Jeedom

2025/11/04

Zigbee --> jeezigbee - Plugins / Protocole domotique - Communauté Jeedom

Le mieux est en effet d’en profiter pour utiliser une autre clé Zigbee plus récente et mieux supportée ... Migration quasi terminée avec la sonoff type E. ... C’est clair que la fonction remplacer fonctionne parfaitement pour ce job, et heureusement que j’ai peu de modules encastrés derrière des prises ou interrupteurs.



](https://community.jeedom.com/t/zigbee-jeezigbee/144238/12)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/09/02

Home AssistantはopenHABの代わりになりますか？ - 日本語

Home Assistantは家中のデバイス制御でopenHABを置き換えられますか？ Home Assistantは、重要なデバイス、オートメーション、認証情報、ローカルでのフォールバック動作を、検証済みの並行移行によって維持できる場合に限り、家全体の制御においてopenHABを置き換えられます。



](https://shop.zimaspace.com/ja/blogs/product-comparisons/can-home-assistant-replace-openhab-whole-home-device-control#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/29

Checklist pour migrer Home Assistant en toute sécurité vers un nouveau serveur - Prêt à être expédié

Prêt à être expédié. Trouvez la configuration Zima qui vous convient. Prêt à être expédié. Trouvez la configuration Zima qui vous convient. Prêt à être expédié. Trouvez la configuration Zima qui vou



](https://shop.zimaspace.com/fr/blogs/support-tips/safe-home-assistant-migration-checklist-new-home-server#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/05/21

GitHub - raul-marquez-csa/certification-tool: A test harness and tooling designed to simplify development, testing, and certification for devices, guided by the Connectivity Standards Alliance. · GitHub - GitHub - raul-marquez-csa/certification-tool: A test harness and tooling designed to simplify development, testing, and certific...

A test harness and tooling designed to simplify development, testing, and certification for devices, guided by the Connectivity Standards Alliance. · GitHub ... the Connectivity Standards Alliance has developed a standardized set of tools as well a test harness that is presently used for Matter certifications. ... Detailed instructions for how to use this



](https://github.com/raul-marquez-csa/certification-tool#1)[

![](https://cdn.deepseek.com/site-icons/deepwiki.com)

DeepWiki

2026/03/06

YAML Test Framework | project-chip/connectedhomeip-doc | DeepWiki - Loading

The YAML Test Framework provides a declarative approach to writing Matter specification conformance tests. Tests are written in YAML format and executed against Matter devices to validate protocol compliance and cluster behavior without writing procedural code. ... YAML tests serve as the foundation for Matter certification, enabling consistent specification compliance validation across the entire ecosystem.



](https://deepwiki.com/project-chip/connectedhomeip-doc/4.3-c++-unit-testing-framework#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon Developers

Provision ACK-based Matter Prototype Devices | Alexa Connect Kit

Provision ACK-based Matter Prototype Devices To join a Matter network, smart home devices must present proper credentials to prove their certification as authentic Matter products. These credentials include a device attestation certificate (DAC) and a certification declaration (CD). ... Follow these steps to generate a PAI certificate, DAC, and CD for the test VID and PID ... Step 1...



](https://developer.amazon.com/pt-BR/docs/alexa/ack/matter-provision-device.html)[

![](https://cdn.deepseek.com/site-icons/buildwithmatter.com)

Matter Handbook

Self Pre-Test | Matter Handbook

tests are run through the test harness ... In the self pre-test phase, tests can either be run through the test harness or locally ... The test harness runs on a Raspberry Pi, external to the development computer. ... Tests can be automated in YAML or Python. Tests that are automated in YAML are located in the YAML SDK folder.



](https://handbook.buildwithmatter.com/certification/certifying-a-product/self-pre-test/)[

GitHub

3. Matter Certification

Test Harness on RaspberryPi is used for Matter Certification Test. ... A Certification Declaration ... A test CD signed by the test CD signing keys in `connectedhomeip <https://github.com/espressif/connectedhomeip/tree/v1 ... /test/certification-declaration>`__ SDK repository is required for Matter Certification Test...



](https://raw.githubusercontent.com/espressif/esp-matter/105e8981f95bff9ba4b0b41b223ec90b8cd2bc11/docs/en/certification.rst#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/12/18

connectedhomeip-doc/platforms/bouffalolab/matter_factory_data.html at 93592dde9d76b1898c747137f70d3ae2b95da6d8 · project-chip/connectedhomeip-doc · GitHub - <div class="highlight-shell notranslate"><div class="highlight"><pre><span></span>openssl<span class="w"> </span>x509<span class...

<li><p>Check PAA/PAI/DAC certificate chain.</p> ... <li><p>Check Certification Declare. ... <p>Self-defined DAC certificates may use in development and test scenario. ... <li><p>Export ... <li><p>Generate DAC certificate and key</p>



](https://github.com/project-chip/connectedhomeip-doc/blob/93592dde/platforms/bouffalolab/matter_factory_data.html#8)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2025/04/21

About TC-DA-1.2

You can generate a Certification Declaration for testing using the CHIP Certificate Tool. When you generate it, you can specify the certification type with the --certification-type parameter. ... This script is meant to create CDs for integration testing, such as testing with TH.



](https://devzone.nordicsemi.com/f/nordic-q-a/120881/about-tc-da-1-2?ReplySortBy=Votes&ReplySortOrder=Descending)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2024/07/18

PICS Tool certification related information (matter V1.3) (CON-1268) · Issue #1019 · espressif/esp-matter - Skip to content

The PICS Tool is used for generating the PICS (Protocol Implementation Conformance Statement) as per the application. You can get this PICS from the CSA. Check this link ... while executing TCs using the Test Harness (TH). ... For more information, check the Matter TH User Guide.- Matter TH User Guide...



](https://github.com/espressif/esp-matter/issues/1019#1)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2022/12/14

Matter デバイスのテスト証明書を作成する | Google Home Developers

# Matter デバイスのテスト証明書を作成するコレクションでコンテンツを整理 必要に応じて、コンテンツの保存と分類を行います。 必須ではありませんが、一部のテスト シナリオでは、非本番環境の Matter 証明書を作成する必要があります。 デバイス OTA ソフトウェア アップデートなどの Google エコシステムの一部の機能は、テスト VID/PID を使用して実行できません。 こ



](https://developers.home.google.com/matter/test/certificates?authuser=0&hl=ja)[

![](https://cdn.deepseek.com/site-icons/deepwiki.com)

DeepWiki

2026/03/06

Integration Tests and PICS/PIXIT | project-chip/connectedhomeip-doc | DeepWiki - Loading

## Purpose and Scope This page documents system-level integration testing in the Matter SDK and the role of PICS (Protocol Implementation Conformance Statement) and PIXIT (Protocol Implementation eXt



](https://deepwiki.com/project-chip/connectedhomeip-doc/4.4-test-execution-and-automation#1)[

PCMag

2026/06/04

How We Test Smart Home Devices - PCMag editors select and review products independently

How We Test Smart Home Devices We install and test more than 100 smart devices in our homes each year to assess their ease of use, reliability, and performance, helping you choose the best ones for your budget. ... Updated June 5, 2026



](https://www.pcmag.com/about/how-we-test-smart-home-devices#1)[

blueasialabs.com

2026/07/05

EN 18031 Test Items: 14 Security Mechanism Categories Explained for 2026

1. Authentication and Access Control ... The lab tests role-based access ... The 2026 lab baseline is mandatory TLS 1.3, with TLS 1.2 accepted only as a transitional compatibility measure for legacy devices. Certificate validation ... the top four failure points in 2026 are ... hardcoded encryption keys (rank 2)...



](https://www.blueasialabs.com/fr/shouyehuandeng/en-18031-test-items-14-security-mechanism-categories-explained-for-2026)[

tvgreport.com

2026/08/10

Matter 1.5 Camera and Energy Features: Home-Lab Test Plan | TVG Report

Test Matter 1.5 devices by separating five checks: commissioning, local control, network path, permission model, and recovery after power, hub, or internet failure. ... Start with commissioning. Pair the device with the ecosystem or controller you actually use, then record the steps, app version, firmware version, network type, and whether a factory reset was needed.



](https://tvgreport.com/matter-15-cameras-energy-smart-home-lab-test-plan/#content)[

![](https://cdn.deepseek.com/site-icons/springer.com)

When Historical Fiction Meets Present-Day War: Marsha Forchuk Skrypuch’s Kidnapped from Ukraine Series and the Russia–Ukraine War - Children's Literature in Education

2026/08/23

Secure Resilient Reproducible IoT-Smart Home Testbed for Cybersecurity Research

we designed and developed a reproducible smart home IoT cybersecurity testbed ... The testbed proposes how to integrates heterogeneous devices Raspberry Pi (gateway/MQTT broker–client) ... the edge and Zigbee for low-power sensing/actuation ... aligning simulator parameters with the lab setup and validating results against analytical bounds and synchronised traces.



](https://link-hkg.springer.com/chapter/10.1007/978-981-92-3681-7_23)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arXiv

2026/03/01

SimuHome: A Temporal- and Environment-Aware Benchmark for Smart Home LLM Agents - STEP3: Query Synthesis

As illustrated in Figure 3, we evaluate agent performance using two complementary methods, chosen based on what each episode requires for assessment. Episodes where success is determined by physical state changes in the home environment are evaluated by the simulator, which can objectively verify outcomes. ... Simulator-based Evaluation. At the end of each episode...



](https://arxiv.org/html/2509.24282v3#2)[

ASHB - Association for Smarter Homes & Buildings

2024/09/19

IS-2024-133 Ensuring the Quality of Smart Home Devices Through Comprehensive Testing Methodologies - ASHB - Association for Smarter Homes & Buildings

It discusses the necessity of real-house testing to ensure seamless functionality, interoperability, and user experience in real-world conditions. The paper contrasts lab testing with real-house environments, addressing challenges such as device diversity, network complexity, and rapid technological advancements.



](https://www.ashb.com/public_research/is-2024-133-ensuring-the-quality-of-smart-home-devices-through-comprehensive-testing-methodologies/)[

nexttechbuy.com

2026/03/10

Ultimate Smart Home Device Comparison Guide 2026

My Smart Home Testing Methodology ... My home became a ... Every device underwent a 30-day minimum testing cycle. I tracked response latency with millisecond precision, measured hub reconnection times after router restarts, and logged every automation failure in a detailed spreadsheet.



](https://nexttechbuy.com/smart-home-device-comparison-guide-2026/#respond)[

Trusted Tech Spot

2026/08/14

AI-Powered Home Automation Systems 2026: A Comparative Guide [2026 Tested]

###### Local LLMs & Offline AI # AI-Powered Home Automation Systems 2026: A Comparative Guide 15 Aug ## Key Takeaways - Matter-over-Thread + local LLMs now define the 2026 flagship tier: Home Ass



](https://trustedtechspot.com/ai-powered-home-automation-systems-2026-comparative-guide/)[

flippers.cloud

2026/01/31

How to Vet Smart-Home Products: A Flipper’s Testing Protocol

fflippers 2026-02-01 10 min read A flipper’s repeatable protocol—modeled on ZDNet testing and Verge skepticism—to vet smart-home devices for accuracy, battery life, interoperability, and ROI. ## H



](https://flippers.cloud/how-to-vet-smart-home-products-a-flipper-s-testing-protocol)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/11

Aqara Smart Lock U100 no longer working since upgraded to 2025.5.0 · Issue #144779 · home-assistant/core - Skip to content

Aqara Smart Lock U100 no longer working since upgraded to 2025.5.0 #144779 ... I have mine connected via Matter using the E1 hub (the U100 doesn't natively support Matter, it requires a hub to enable Matter support).



](https://github.com/home-assistant/core/issues/144779#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/12/12

2025.12.3 Broke Aqara Smart Lock U300 Passthrough Mode Operating Mode · Issue #158949 · home-assistant/core - Skip to content

Aqara Smart Lock U300 were able to select passthrough mode via the matter integration. ... matter-diagnostics-and-actions The implementation was not correct because it did not comply with Matter specifications. Namely, modes must be authorized taking into account theSupportedOperatingModes attribute ... Either home assistant is not reading the lock characteristics right, the lock fails to report "passthrough" ... some combination thereof is happening.



](https://github.com/home-assistant/core/issues/158949#1)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2025/07/16

Matter door lock sample builds but can't commission - Matter door lock sample builds but can't commission

having some issues with the matter door lock sample for the nRF54L15DK on NCS 3.0.2. ... It seems like theres a failure to init the door lock cluster with "RFID users: 86" even though i haven't touched anything by default and it seems like the source code should be initing this to 0.



](https://devzone.nordicsemi.com/f/nordic-q-a/123054/matter-door-lock-sample-builds-but-can-t-commission/543397#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/04

Ultraloq Bolt F Matter - Paired Door Sensor Doesn't Report State · Issue #144274 · home-assistant/core - Skip to content

You can simply check that in the Matter Server debug interface you already discovered. If it doesn't update, this is a device issue, not a HA issue. I have actually tested this feature with a Nuki lock and an optional door sensor and there it works fine.



](https://github.com/home-assistant/core/issues/144274#1)[

![](https://cdn.deepseek.com/site-icons/amazon.de)

Amazon.de

2025/12/09

Aqara Smart Lock U200 Türschloss mit Fingerabdruck & Matter Thread - Batterie entfernt

Die Home-Assistant Integration via Matter klappt mit einem als Thread-Border-Router genutztem ZBT-1 grundsätzlich. Es gibt aber einen im Aqara-Forum von Aqara bestätigten Bug. ... Es war dafür nicht nötig, dass Schloss aus Home-Assistant zu entfernen und neu per Matter zu pairen.



](https://www.amazon.de/Aqara-U200-Fingerabdruck-Aufladbarem-Unterst%C3%BCtzt/dp/B0D1C75J4F/ref=bmx_dp_d_sccl_1_4/260-3083827-2096928?pd_rd_w=Z7DIV&content-id=amzn1.sym.8e3eb1de-d4d8-458f-bd5d-a4e642cf0078&pf_rd_p=8e3eb1de-d4d8-458f-bd5d-a4e642cf0078&pf_rd_r=PE3H85CSAS9B1E6ADZGZ&pd_rd_wg=huZe7&pd_rd_r=69ea6523-0cc3-4924-958d-3f5f97df5bb4&pd_rd_i=B0D1C75J4F&th=1#4)[

m.media-amazon.com

Yes, you can directly connect Smart Lock U400 to a third- party Matter ecosystem without connecting the Aqara Home app by scanni...

you can directly connect Smart Lock U400 to a third- party Matter ecosystem without connecting the Aqara Home app by scanning the Matter pairing code on the door lock. ... No response or failed binding when scanning the Aqara pairing code to add the door lock Press the Set button once to ensure your door lock is in pairing mode, and then scan the setup code to add your door lock to the corresponding ecosystem.



](https://m.media-amazon.com/images/I/71k4hlg8jZL.pdf?ref=dp_product_quick_view#2#2)[

![](https://cdn.deepseek.com/site-icons/amazon.de)

Amazon.de

EZVIZ Smart Lock DL01 Pro with Keypad & Gateway & Door Sensor, Electronic Door Lock with Replaceable Batteries, Smart Door Lock, Open via Ezviz App, Code, RFID Card, Supports Matter : Amazon.de: DIY & Tools - Reviewed in Germany on 20 February 2026Brief content visible, double tap to read full content

Gutes Schloss mit schlechter Integration in EZVIZ Ecosystem ... Ich habe das EZVIZ-System bestehend aus dem DL01 Pro Schloss, dem A3 Gateway und der HP7 Video-Türsprechanlage installiert und intensiv getestet. ... Ein zentrales Problem ist die unzureichende Zusammenarbeit zwischen Schloss, Gateway und Monitor.



](https://www.amazon.de/dp/B0D9GTRH22/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0D9GTRH22&pd_rd_w=neSrc&content-id=amzn1.sym.bf6dbf94-e926-4351-8952-c09f45cdef70&pf_rd_p=bf6dbf94-e926-4351-8952-c09f45cdef70&pf_rd_r=5MRFCVS6ZBHE2QC56C4T&pd_rd_wg=PdM7E&pd_rd_r=c5f2465f-621a-4021-80b5-54ff0b177f5f&aref=lLhAAKe3rA&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw#2)[

m.media-amazon.com

Aqara Smart Lock U400 Pairing Guide

cover the Matter code with your finger while scanning, so the app reads the correct code.- The Matter QR code on the lock becomes invalid once the lock is paired with any Matter ecosystem. ... Mode”).- If something goes wrong while pairing with your first Matter ecosystem, first reset the lock, then delete the U400 device card from that Matter ecosystem, and go to your iPhone’s Settings...



](https://m.media-amazon.com/images/I/C1TkUPQFpyL.pdf?ref=dp_product_quick_view#1#1)[

![](https://cdn.deepseek.com/site-icons/amazon.nl)

Amazon.nl

Aqara Smart Lock U200 (Inclusief Vingerafdruk Toetsenbord), Matter over Thread, Slim Deurslot met Apple Home Key en Oplaadbare Batterij, Ondersteunt Homekit, Google Home, Alexa en SmartThings, Zilver : Amazon.nl: Klussen & gereedschap - Inmiddels heb ik het product ontvangen en geïnstalleerd

lukte het verbinden via Matter lange tijd niet en lukte het ook maar niet om de firmware te updaten. ... Koppelen met Apple Home lukte niet met het scanner van de Matter code, maar je moet dus eerst op de knop “set” drukken van het slot zelf en dan scannen. Slot werd meteen herkend.



](https://www.amazon.nl/dp/B0D1BZPJP1?maas=maas_adg_D61894AB99C650FB9E661A6721026D41_afap_abs&ref_=aa_maas&tag=maas#2)[

![](https://cdn.deepseek.com/site-icons/amazon.de)

Amazon.de

2026/08/01

SwitchBot WiFi Smart Lock Ultra mit Keypad Vision Pro – 3D-Gesichts- & Venen-Erkennung, kontaktlose Entsperrung, passend für Europrofil-Zylinder, kompatibel mit Matter, Alexa, Google und IFTTT : Amazon.de: Baumarkt - Ich habe das Komplettset (Lock Ultra, Keypad Pro und Hub Mini Matter enabled) über Cloud, Matter und Bluetooth in Home Assistant...

Keypad Pro und Hub Mini Matter enabled) über Cloud, Matter ... Bluetooth funktioniert einigermaßen, aber Matter und Cloud sind eine Katastrophe. ... Warum also das Lock Ultra die Daten nur selten an Cloud oder Matter übergibt ... Der Testpin wurde fast nie erkannt. ... Incluye Hub compatible con Matter, por lo que se integra perfectamente con cualquier asistente (Alexa, Google, Apple).



](https://www.amazon.de/dp/B0G2WT4HRL/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B0G2WT4HRL&pd_rd_w=Tp5V9&content-id=amzn1.sym.a863b3ec-3f18-43b6-9daa-f3f68293b955&pf_rd_p=a863b3ec-3f18-43b6-9daa-f3f68293b955&pf_rd_r=JJVZM3P8GYE8AER1DDY1&pd_rd_wg=VaB8H&pd_rd_r=e4433d4f-ba12-4557-8a52-8966f89f8310&aref=WWIf05tNnE&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy#4)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2026/03/16

Hands on with Aqara’s new Matter-compatible camera - Skip to main content

Aqara’s G350 brings Matter 1.5 camera support, promising easier smart home integration — but it only works with Samsung SmartThings. ... Today, the G350 only supports Matter on Samsung SmartThings, as none of the other platforms have added Matter 1.5 yet.



](https://www.theverge.com/tech/895326/aqara-g350-matter-camera-samsung-smartthings-hands-on-review#1)[

![](https://cdn.deepseek.com/site-icons/9to5mac.com)

9to5Mac

2026/04/30

Aqara Camera Hub G350 Review - HomeKit Weekly: A look into the first Matter certified camera from Aqara

It supports Matter 1.5, the latest standard that finally brings cameras into the Matter ecosystem. Apple Home has not yet updated to support Matter 1.5 cameras ... Because Apple has not yet updated the Home app to support Matter 1.5 cameras, the G350’s setup currently relies on the standard Apple Home integration.



](https://9to5mac.com/2026/05/01/aqara-camera-hub-g350/#1)[

![](https://cdn.deepseek.com/site-icons/gizmodo.com)

Gizmodo

2026/07/04

Aqara Camera Hub G350 Review: An Excellent Indoor Matter Camera - Skip to content

This is among the first smart security cameras to support Matter 1.5, a new version ... 2025) that adds cameras to the mix. That means the Camera Hub G350 can pair with any smart home ecosystem, although so far, only Samsung SmartThings supports Matter-enabled cameras. ... The camera also has native support for



](https://gizmodo.com/aqara-camera-hub-g350-review-an-excellent-indoor-matter-camera-2000748785#1)[

iphone-ticker.de | Alles zum iPhone. Seit 2007.

2026/03/20

Aqara G350 ausprobiert: 4K-Kamera und Matter-Hub kombiniert

Mit dem Kamera-Hub G350 hat Aqara als erster Anbieter eine Matter-zertifizierte Kamera im Programm. Mit der Ende vergangenen Jahres verabschiedeten Version 1.5 des Standards können erstmals auch Kameras über das Matter-Protokoll mit Smarthome-Systemen kommunizieren.



](https://www.iphone-ticker.de/aqara-g350-ausprobiert-4k-kamera-und-matter-hub-in-einem-geraet-274947/)[

Lyd & Bilde

2026/08/14

KI-overvåking med 4K-video

I tillegg er det det første overvåkingskameraet som støtter siste Matter-versjon, noe som betyr at det både kan kobles til og styres av valgfritt smarthjem-økosystem. ... De fleste smarthjem-økosystemer holder på å rulle ut støtte for Matter 1.5...



](https://www.lydogbilde.no/test/smart-hjem/aqara-camera-hub-g350/)[

![](https://cdn.deepseek.com/site-icons/trustedreviews.com)

Trusted Reviews

2026/04/07

Aqara Camera Hub G350 Review - Advertisement

Matter compatible Camera works with compatible Matter systems ... Right now, if you want to use this as a Matter camera, you’ll need SmartThings, which is currently the only platform supporting Matter camera streams. ... I tested the G350 for a couple of weeks before it was officially announced and anytime I tried to pair it via Matter...



](https://www.trustedreviews.com/reviews/aqara-camera-hub-g350#1)[

![](https://cdn.deepseek.com/site-icons/mac4ever.com)

Mac4Ever

2026/06/08

Test de l'Aqara G350, la caméra HomeKit déguisée en lapin - Tests

une caméra de surveillance intérieure motorisée à 360° vendue 139,99 € et présentée comme la première caméra certifiée Matter du marché. ... La partie hub Zigbee, Thread et Matter, destinée à raccorder les capteurs maison d'Aqara à l'écosystème connecté...



](https://www.mac4ever.com/securite/196620-test-de-l-aqara-g350-la-camera-homekit-deguisee-en-lapin#1)[

![](https://cdn.deepseek.com/site-icons/gizmodo.jp)

ギズモード・ジャパン

2026/07/19

うさちゃんが見てる。Matter対応の360度全方位スマートセキュリティカメラ | ギズモード・ジャパン - 04:45:59

・ほとんどのエコシステムはまだMatter1.5をサポートしていない ... スマートホーム機器の共通規格「Matter 1.5」をサポートしているため、複数のプラットフォームをまたいで、さまざまなメーカーのスマートホーム機器とともに一元管理も可能です。 一方、現在のところMatter対応カメラに対応しているのはSamsung（サムスン）のSmartThingsのみ。



](https://www.gizmodo.jp/article/aqara-camera-hub-g350-review-an-excellent-indoor-matter-camera/#1)[

![](https://cdn.deepseek.com/site-icons/smartthings.com)

SmartThings Community

2026/08/21

Aqara G350 and SmartThings: Matter Cameras Have Come a Long Way - Devices & Integrations / Connected Things - SmartThings Community

You could try my Matter Switch Camera driver, which is a modified version of the official driver, from this channel. Log in → Accept → Enroll → Available Drivers → Check here (select the camera) if the driver has changed automatically ... For Matter cameras, the presets are stored in themechanicalPanTiltZoom capability...



](https://community.smartthings.com/t/aqara-g350-and-smartthings-matter-cameras-have-come-a-long-way/310676/7)[

![](https://cdn.deepseek.com/site-icons/smartthings.com)

SmartThings Community

2026/04/23

Matter Camera UI looks very basic in SmartThings App — generated presentation instead of `matter-camera`? - Devices & Integrations - SmartThings Community

Small update on the Aqara Camera Hub G350. ... Unfortunately, the actual Matter implementation does not seem to have changed in any meaningful way. ... I tested the camera with several driver variants: - the currentmain Matter Switch driver - the currentproduction Matter Switch driver - my own experimental Matter camera driver based on the Matter Switch driver



](https://community.smartthings.com/t/matter-camera-ui-looks-very-basic-in-smartthings-app-generated-presentation-instead-of-matter-camera/308853/16)[

heise online

2024/12/09

Bosch Heizkörper-Thermostat II +M im Test | heise online bestenlisten - Heise > Bestenlisten > Testbericht > Bosch Heizkörper-Thermostat II +M im Test: Dank Matter vielseitig einsetzbar

Bosch Heizkörper-Thermostat II +M im Test ... - dank Matter & Thread kompatibel zu vielen Smart-Home-Zentralen - sehr leise - lokaler Betrieb ohne Cloud möglich ... Dank Matter und Thread ist das neue Heizkörperthermostat ... Wenn die LED orange blinkt, war der Wechsel von Matter-Modus zu Zigbee erfolgreich. Wenn die LED blau blinkt...



](https://www.heise.de/bestenlisten/testbericht/bosch-heizkoerper-thermostat-ii-m-im-test/5fscdd4#1)[

![](https://cdn.deepseek.com/site-icons/chip.de)

CHIP

2026/02/24

Eve Thermo Matter (5. Gen.) im Test: Gut verarbeitet, flott zu installieren - Eve Thermo Matter (5. Gen.) im Test

Dadurch lässt er sich an diverse Matter-fähige Smart-Home-Zentralen für direkte Steuerung ohne Internetzwang anlernen. ... Dieser Thermostat unterstützt den Matter-over-Thread-Standard ... Matter-Codes an die Zentrale anlernen. Es lassen sich auch lokale Profile anlegen, die ohne Zentrale ablaufen.



](https://www.chip.de/test/Eve-Thermo-5.-Gen.-im-Test_186691899.html#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2025/06/03

Nest thermostat + matter = local hvac control? - Configuration - Home Assistant Community - Load more posts above

I have a new Google Nest Thermostat working over matter while disconnected from the internet. Only been testing for an hour or so, and will reconnect to the internet (thermostat provided gratis by the power company, so they want to see it online) but I’m pleased to see matter working for local control.



](https://community.home-assistant.io/t/nest-thermostat-matter-local-hvac-control/603058/11#1)[

![](https://cdn.deepseek.com/site-icons/github.io)

GitHub Pages

Matter ASR Thermostat Example

The ASR Thermostat Example demonstrates controlling a thermostat and getting temperature from local sensor. ... After successful commissioning, usechip-tool to control the board For example,read local-temperature value: ./chip-tool thermostat read local-temperature <NODE ID> 1 increases the temperature by sending a SetpointRaiseLower command...



](https://project-chip.github.io/connectedhomeip-doc/examples/thermostat/asr/README.html)[

![](https://cdn.deepseek.com/site-icons/amazon.ca)

Amazon.ca

Aqara Smart Thermostat W200 with Apple Adaptive Temperature & Clean Energy Guidance, 4" Touchscreen, Matter Controller, Built-in Radar Sensor, Works with Apple Home, Siri, Google Assistant, Alexa : Amazon.ca: Tools & Home Improvement - I use the open source software Home Assistant for my smart home functions so I was looking forward to trying out the Aqara W200 ...

I think I would have been able to connect the thermostat directly to my Home Assistant Matter controller without using the Aqara app but ... did first pair it with the app (and update the firmware) and then connected it to Home Assistant. With the current firmware, Matter exposes thermostat mode (off, heat, cool and auto), HVAC action (heating, cooling and fan), current temperature...



](https://www.amazon.ca/dp/B0G25F5XC1/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0G25F5XC1&pd_rd_w=qBnLn&content-id=amzn1.sym.516c2169-755e-413a-a38a-68230f4ab66f&pf_rd_p=516c2169-755e-413a-a38a-68230f4ab66f&pf_rd_r=H3JMQGRB9P9CVK8KEN3M&pd_rd_wg=FM7d5&pd_rd_r=7962403d-b987-455e-8164-cb3ef3bff8fc&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw#customerReviews#2)[

![](https://cdn.deepseek.com/site-icons/github.io)

GitHub Pages

Matter ASR Thermostat Example The ASR Thermostat Example demonstrates controlling a thermostat and getting temperature from local sensor. ... After successful commissioning, use `chip-tool` to control the board For example,read local-temperature value ... increases the temperature by sending a SetpointRaiseLower command...



](https://project-chip.github.io/connectedhomeip-doc/_sources/examples/thermostat/asr/README.md)[

![](https://cdn.deepseek.com/site-icons/nxp.com.cn)

nxp.com.cn

NXP Semiconductors

4.4.2 Compile and run the Matter thermostat example ... For example, you can read the local temperature by issuing the following command using the CHIP tool: [out/chip-tool/chip-tool thermostat read local-temperature 3840 1]



](https://www.nxp.com.cn/docs/en/application-note/AN13445.pdf#4#4)[

elko.se

ELKO One - Matter Thermostat 16 A Device User Guide

It explains how to set up the thermostat with Matter- compatible smart home systems, adjust presets, and customize installer and user settings for optimal heating control. Users will learn how to manage temperature set points, schedules, child lock, and standby mode, as well as perform resets and firmware updates.



](https://www.elko.se/getfile.php/13260697-1777612958/ELKO.se/Produkter%20PIM/EKO50/SE-EKO50107/documents/EKO5010x_DUG_EN.pdf#4#1)[

heise online

2024/11/11

Heizkörperthermostat Eve Thermo im Test: Dank Matter nicht nur für Apple | heise online bestenlisten - Heise > Bestenlisten > Testbericht > Heizkörperthermostat Eve Thermo im Test: Dank Matter nicht nur für Apple

Kai Schmerer Nach seinem Studium begann Kai seine journalistische Laufbahn Mitte der 90er bei der PC Professionell. Für Heise Bestenlisten by TechStage berichtet er über interessante Produkte aus den



](https://www.heise.de/bestenlisten/testbericht/heizkoerperthermostat-eve-thermo-im-test-dank-matter-nicht-nur-fuer-apple/jrpzptl#1)[

![](https://cdn.deepseek.com/site-icons/amazon.ca)

Amazon.ca

meross Smart Thermostat for Home, WiFi Thermostat Works with Matter, Alexa, Apple Home, Google Assistant, App Voice Control, 7x24h Scheduling, Energy Saving, C-Wire Required : Amazon.ca: Tools & Home Improvement - I’ve been running this thermostat for over a month now

I’ve been running this thermostat for over a month now. I originally bought it because I refused to pay a monthly subscription just to use full features on a device I own. Update: After 30 days, it ha



](https://www.amazon.ca/meross-Thermostat-Assistant-Scheduling-Required/dp/B0DXPKXHLL/ref=vse_cards_2?_encoding=UTF8&pd_rd_w=fwjXQ&content-id=amzn1.sym.a109fb27-80e9-4ca8-bde3-c78b9972e5bf&pf_rd_p=a109fb27-80e9-4ca8-bde3-c78b9972e5bf&pf_rd_r=1ETV7VJHAXE6Y9S23EVZ&pd_rd_wg=aTAlO&pd_rd_r=8530d568-262c-4049-a0ae-d293ab811848#2)[

![](https://cdn.deepseek.com/site-icons/acm.org)

energy.acm.org

Version 1.5 (November 2025) introduced clusters for tariff and pricing information, as well as electrical grid condition signall...

Version 1.5 (November 2025) introduced clusters for tariff and pricing information, as well as electrical grid condition signalling [10]. ... 5 Integration of Matter into the DataWallet ... The results show that integrating Matter into an energy data agent such as the DataWallet is feasible and simplifies device connectivity



](https://energy.acm.org/eir/wp-content/plugins/pdfjs-viewer-shortcode/pdfjs/web/viewer.php?file=https://energy.acm.org/eir/wp-content/uploads/2026/09/sigenergy-eir-final230.pdf&attachment_id=1569&dButton=true&pButton=true&oButton=false&sButton=true#zoom=0&pagemode=none&_wpnonce=b3daed07ba#3#2)[

![](https://cdn.deepseek.com/site-icons/ul.com)

UL Solutions

2025/11/19

Matter Testing and Certification Services - Skip to main content

Additionally, Matter 1.5 covers advanced energy management so devices can support standardized exchange of energy data among utilities, grid operators and energy services. ... - Interoperability testing Currently, products enabled for Matter 1.5 include: - Batteries - Battery-powered devices



](https://www.ul.com/services/matter-testing-and-certification-services#1)[

![](https://cdn.deepseek.com/site-icons/allion.com)

Allion Labs

2025/11/30

Matter 1.5 Officially Released: Allion Continues to Deliver Comprehensive Certification Testing and Consulting as a CSA Authorized Lab

This new version significantly enhances interoperability and energy-management capabilities across the global smart home ecosystem. ... It also introduces a redesigned energy-management framework that streamlines smart home development, strengthens cross-brand interoperability, and further improves user experience and system performance.



](https://www.allion.com/news-center/matter_1-5_introduces/#search-lightbox)[

![](https://cdn.deepseek.com/site-icons/allion.com.cn)

百佳泰

2025/11/26

Matter 1.5正式发布，百佳泰作为CSA官方授权实验室持续提供产品认证测试与顾问服务

不仅新增了对摄影机、门锁、土壤传感器和新型能源管理功能等重要设备类别及应用场景支持，并导入全新的能源管理框架 ... - 新增能源管理能力，让装置能以标准化方式交换电价、费率以及碳排放强度等信息。



](https://www.allion.com.cn/news-center/matter_1-5_introduces/#wechat)[

![](https://cdn.deepseek.com/site-icons/ul.com)

UL Solutions

Matter 测试与认证服务

此外，Matter 1.5 涵盖了高级能源管理功能，使设备能够支持公用事业公司、电网运营商与能源服务商之间的标准化能源数据交换。通过加强对 TCP（传输控制协议）传输操作的支持 ... 目前，支持 Matter 1.5 的产品包括...



](https://www.ul.com/zh-hans/services/matter-testing-and-certification-services#1)[

elaad.nl

<table><tr><td>Acceptance Criteria</td><td>1. Can send the following S2 messages:<br>a

<td>Acceptance Criteria</td><td>1. ... Includes test tools and sample configuration</td></tr><tr><td>Documentation &amp;amp ... Programming languages: C/C++ ... This work package focuses on leveraging the Matter 1.4.1 protocol to enable interoperability and flexibility control for Electric Vehicle Supply Equipment (EVSE)...



](https://elaad.nl/wp-content/uploads/downloads/RFP-Interoperability-v1.1.pdf#5#2)[

![](https://cdn.deepseek.com/site-icons/linkedin.com)

LinkedIn · Fabian Warislohner

2025/12/16

#matter #iot #smarthome #certification #interoperability #bureauveritas #innovation #connecteddevices | Bureau Veritas Consumer Products Services

✅ • Seamless Interoperability – Matter 1.5 enables smart home and IoT devices to work flawlessly together across manufacturers • Expanded Device Portfolio – v1.5 introduces new product categories including cameras and door/window closures, alongside enhanced energy management capabilities for greater control and efficiency • Broader



](https://www.linkedin.com/posts/bureau-veritas-consumer-products-services_matter-iot-smarthome-activity-7407041913863692288-4lwR)[

![](https://cdn.deepseek.com/site-icons/allion.com.tw)

百佳泰Allion Labs

2025/11/26

Matter 1.5正式發布，百佳泰作為CSA官方授權實驗室持續提供全方位認證測試與顧問服務

CSA 連接標準聯盟（Connectivity Standards Alliance）日前於西班牙巴塞隆納舉辦的11月份會員大會中正式發布最新的 Matter 智慧家庭通訊協定版本－ Matter 1.5 ，將為全球智慧家庭生態圈帶來更高水準的互通性與能源管理能力。不僅新增了對攝影機、門鎖、土壤感測器和新型能源管理功能等重要設備類別及應用場景支援，並導入全新能源管理框架，從而簡化智慧家庭開發流程，



](https://www.allion.com.tw/news-center/matter_1-5_introduces/#main)[

![](https://cdn.deepseek.com/site-icons/9to5mac.com)

9to5Mac

2026/08/20

HomeKit Weekly: Homey secures Matter 1.5 certification to expand bridging and energy support - 9to5Mac - HomeKit Weekly: Homey secures Matter 1.5 certification to expand bridging and energy support

Athom has announced that it has officially achieved Matter 1.5 certification for its Homey software component, covering the Homey Pro (2023 — 2026), Homey Pro mini, and the Homey Self Hosted Server. T



](https://9to5mac.com/2026/08/21/homekit-weekly-homey-secures-matter-1-5-certification-to-expand-bridging-and-energy-support/?utm_source=dlvr.it&utm_medium=threads#1)[

![](https://cdn.deepseek.com/site-icons/acm.org)

dl.acm.org

A PRE-SURVEY QUESTIONNAIRES

Suppose you have a home equipped with smart IoT devices such as light bulbs, cameras, and a speaker. One day, you have decided ... to AirBnB guest. ... door. Create a permission group for your guest that only grants them access to the light bulb and speaker, but not the camera.



](https://dl.acm.org/doi/suppl/10.1145/3613904.3641991/suppl_file/pn6139-supplemental-material-2.pdf?__cf_chl_tk=pDL1_KIo1pwZosjy1fB.96UCPrTy3kskhcloY5JXbTo-1780732086-1.0.1.1-dtUuH_6640TxbhuE1hDImLzffgRsrpVSOZwn96bcFpw#1#1)[

patentimages.storage.googleapis.com

[0181] In some embodiments, if the light bulb does not host its own PDS and corresponding DIR, a hub's PDS and a corresponding D...

[0181] In some embodiments ... requesting guest access), the smart gateway may identify a device to which the request is directed (e.g. ... The device may then check if the entity is allowed to perform the requested action. [0183] In some embodiments, an authorized ... the target device's PDS and/or the corresponding DIR may perform a counterparty check with the requesting entity's



](http://patentimages.storage.googleapis.com/53/93/ce/9ce91c486a6018/US20190222575A1.pdf#8#7)[

patentimages.storage.googleapis.com

In some embodiments, a setAttribute transaction may be sent by the target device's PDS to the corresponding DIR

This may be enforced using the illustrative state machine 300 in the example of FIG. 3, where an attestation may be moved from a VERIFIED state to an EXPIRED state after a selected amount of time has elapsed. ... etc. For instance ... The target device's PDS and/or ... a trusted entity (e.g.



](https://patentimages.storage.googleapis.com/8d/76/72/f549ae057aa5be/US10454927.pdf#8#7)[

![](https://cdn.deepseek.com/site-icons/acm.org)

ACM Digital Library

2024/06/24

Circles of Trust: A Voice-Based Authorization Scheme for Securing IoT Smart Homes | Proceedings of the 29th ACM Symposium on Access Control Models and Technologies - Several features on this page require Premium Access

Circles of Trust: A Voice-Based Authorization Scheme for Securing IoT Smart Homes ... This concept can be applied to an authorization framework, by linking relationships to an access level ... homeowners and their spouses can be fully-trusted, whereas visitors and children may not. ... Each subsequent layer has fewer access privileges than the previous, granting users in outer layers, like visitors, limited capabilities to manipulate devices.



](https://dl.acm.org/doi/abs/10.1145/3649158.3657044#1)[

المكتبة الرقمية السعودية

DSpace Repository :: Browsing by Author "Alghamdi, Leena" - Browsing by Author "Alghamdi, Leena"

ItemRestrictedIMPROVING SMART HOME ACCESS CONTROL MECHANISMS TO ACCOUNT FOR COMMUNITY-BASED SHARING BEYOND THE HOME (Saudi Digital Library ... The analysis uncovered significant limitations, such as reliance on rigid "all-or-nothing" access models, limited granularity in permissions, and insufficient transparency. ... MiSu introduced features like time-based permissions, device specific access, and real-time activity



](https://drepo.sdl.edu.sa/browse/author?value=Alghamdi,%20Leena#1)[

![](https://cdn.deepseek.com/site-icons/ucf.edu)

ucf stars

2025/05/29

Improving Smart Home Access Control Mechanisms to Account for Community-Based Sharing Beyond The Home - Skip to main content

The analysis uncovered significant limitations, such as reliance on rigid "all-or-nothing" access models, limited granularity in permissions, and insufficient transparency. ... MiSu introduced features like time-based permissions, device-specific access, and real-time activity logs to accommodate diverse sharing scenarios.



](https://stars.library.ucf.edu/etd2024/92/#1)[

![](https://cdn.deepseek.com/site-icons/ucf.edu)

stars.library.ucf.edu

Moreover, several studies have proposed fine-grained access control systems to address intra-household dynamics

several studies have proposed fine-grained access control systems to address intra-household dynamics. ... In this study, we developed a concrete app, MiSu, to instantiate a flexible ... Homeowners were first asked to check and use the smart devices connected to the app, then share selected devices with the guest, specifying permissions for each. Afterward...



](https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1128&context=etd2024#21#11)[

Quests, loot, mounts, and realms

Docs · Home households and roles · three.ws

It covers the five roles, what each one may do, how a scoped member sees a narrowed house ... A guest can never confirm a guarded action. ... | no guest | scoped ... viewer | ... - guest is visiting. Scoped ... - viewer is a wall display or a monitoring seat. Scoped ... guest and viewer carry an allowlist of areas and entities ... a member normalizes their scope to {"mode"...



](https://three.ws/docs/home-households)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Patents

2023/05/07

Safe login management method for intelligent household cloud platform - Correspondingly, the invention also discloses a safe login management system of the intelligent household cloud platform, which ...

The main controller is used for proving whether the identity of the guest is legal or not through a zero knowledge proving method. ... step 2, the main controller proves whether the identity of the guest is legal or not through a zero knowledge proof method...



](https://patents.google.com/patent/CN116232771A/en#2)[

![](https://cdn.deepseek.com/site-icons/ucf.edu)

stars.library.ucf.edu

| Homeowners can customize access for shared users by specifying device-level rights, sharing specific device attributes, or imp...

Homeowners can customize access for shared users by specifying device-level rights, sharing specific device attributes, or implementing role-based access control. | Property-Level Control (n=2 ... | | Partial Access with Role-based Access (Predefined Permissions) (n=7, 54%) | Apple Home | ... |Evaluating a mobile app (MiSu)



](https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1128&context=etd2024#21#16)[

![](https://cdn.deepseek.com/site-icons/finna.fi)

Finna

User experiences and device functionality during smart home cloud service disruptions

User experiences and device functionality during smart home cloud service disruptions ... Device behavior was classified using the F0–F3 failure classification model, introduced in this study to categorize observable behavior from full functionality to unsafe or degraded states. ... A cloud-dependent ... during DNS blocking due to the use of hardcoded network endpoints. ... control path determines device behavior during cloud unavailability.



](https://utu.finna.fi/ty_masto/Record/theseus_tamk.10024_920383?lng=fi)[

![](https://cdn.deepseek.com/site-icons/linkedin.com)

LinkedIn · Fabian Warislohner

2025/10/31

Craziest AWS Outage story from last week! Eight Sleep’s smart beds malfunctioning during the AWS outage might be the most unexpected headline of the week. When AWS went down this week, most of us…

Craziest AWS Outage story from last week! Eight Sleep’s smart beds malfunctioning during the AWS outage might be the most unexpected headline of the week. When AWS went down this week ... They literally couldn’t cool or heat their beds and were stuck. ... The system relies on AWS to regulate temperature, track sleep data, and manage subscriptions. When the cloud crashed, their comfort did too.



](https://www.linkedin.com/posts/yash-sharma009_craziest-aws-outage-story-from-last-week-activity-7390252640082919424-J_ee)[

![](https://cdn.deepseek.com/site-icons/asee.org)

nemo.asee.org

Work-in-Progress: From Cloud APIs to Local Intelligence: Restoring Weather data and Thermostat Control in a Smart Residential Mi...

Legacy smart residential microgrid systems used for academic purposes often depend on third- party cloud APIs that may eventually become restricted or discontinued over time, causing major system failures and loss of core functionality. This work summarizes two technical and educational case studies from the recent revitalization of Bucknell University's smart residential microgrid testbed.



](https://nemo.asee.org/public/conferences/374/papers/52259/download#1#1)[

![](https://cdn.deepseek.com/site-icons/devpost.com)

Devpost

2026/08/06

Blast Radius - Blast Radius

Nobody could tell you, before it happened, how much of your home would survive a shutdown. ... Belkin killed the Wemo cloud, but Home Assistant's Wemo integration is local, so it survived the real shutdown. The cloud ones died.



](https://devpost.com/software/blast-radius-ig6wz9#updates#1)[

![](https://cdn.deepseek.com/site-icons/arxiv.org)

arxiv.org

Securing Smart Home Devices against Compromised Cloud Servers

Our experiments show that compared ... FIDELIUS reduces more than ... This is particularly concerning—e.g., recent work shows that if an attacker can control enough high- wattage IoT devices, the attacker can cause power grid failures [16]. ... Compared to Particle.io, FIDELIUS reduces more than \(50\%\) of



](https://arxiv.org/pdf/2006.11657#2#1)[

Pilot Protocol

2026/06/18

Smart Home Without Cloud: Local Device Communication

In January 2026, Belkin shut down the Wemo cloud service. Overnight, every Wemo smart plug, light switch, and motion sensor lost remote access and scheduled automations. Users who had spent hundreds ... to apps that could not connect. ... Remote access stopped. ... but the app that most people used became non-functional.



](https://pilotprotocol.network/blog/smart-home-without-cloud-local-device-communication)[

Hiverlab

2025/10/26

AWS IoT Outage Disrupts Smart Beds from Eight Sleep

Amazon Web Services outage disabled temperature and motion controls on smart beds. - Users of Eight Sleep’s Pod line and hotels offering the product experienced discomfort. - Eight Sleep’s CEO apologized, promising a new “Backup Mode” for offline use. - The event highlights critical IoT vulnerability to cloud dependence.



](https://hiverlab.com/aws-iot-outage-disrupts-smart-beds-from-eight-sleep/)[

![](https://cdn.deepseek.com/site-icons/shelly.cloud)

Shelly community

2025/11/26

Shelly 1 gen4: set relay behavior when WiFi or cloud is down

View in the app A better way to browse. Learn more. Shelly community A full-screen app on your home screen with push notifications, badges and more. To install this app on iOS and iPadOS - Tap th



](https://community.shelly.cloud/topic/12321-shelly-1-gen4-set-relay-behavior-when-wifi-or-cloud-is-down/#comment-48225)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/02/14

6 new IKEA Matter over Thread smart home gadgets that are worth the money

At present, you need an IKEA Dirigera hub ($109) to update the firmware ... an existing Matter over Thread setup (like Home Assistant). IKEA has a generous money-back guarantee, so you could swap older units out and play the smart home lottery. You could also purchase the hub, update items, and return it once you're done. Hopefully...



](https://tech.yahoo.com/home/articles/6-ikea-matter-over-thread-140015793.html#1)[

![](https://cdn.deepseek.com/site-icons/amazon.ca)

Amazon.ca

2026/08/30

meross Smart Thermostats for Home, Matter Programmble WiFi Thermostat | Works with Alexa, Apple Home, Google Assistant, App & Voice Control, Energy Saving, for HVAC Systems, C-Wire Required : Amazon.ca: Tools & Home Improvement - Reviewed in Canada on November 8, 2025Brief content visible, double tap to read full content

while supporting Matter (huge plus) and being cheaper as well. ... I ordered the Meross Smart Thermostat to replace my Google Nest ... I was replacing a Nest Thermostat so my wire color code matched, which help me in the wire placement. I took a chance purchasing this Matter device due to all the negative reviews.



](https://www.amazon.ca/dp/B0DXPKXHLL/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B0DXPKXHLL&pd_rd_w=bEmBg&content-id=amzn1.sym.516c2169-755e-413a-a38a-68230f4ab66f&pf_rd_p=516c2169-755e-413a-a38a-68230f4ab66f&pf_rd_r=5VE5M24GXX7W50E2EVZG&pd_rd_wg=gMT5p&pd_rd_r=7a558c51-8897-42c2-82c1-6d5020b3ecfc&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw#2)[

![](https://cdn.deepseek.com/site-icons/pcwelt.de)

PC-Welt

2025/01/12

Die beste Hardware, die Sie 2025 kaufen können - Für Matter-Geräte, die ausschließlich das stromsparende Funkprotokoll Thread unterstützen, was auf viele Temperatursensoren und ...

Auf die Kompatibilität zu Matter zu achten empfiehlt sich auch beim Kauf neuer Smart-Home-Komponenten ... Alternativen ohne Matter-Unterstützung sind die AVM Fritz Dect 210 für den Außeneinsatz (rund 45 Euro) oder die Shelly Plus Plug S Gen2 für rund 18 Euro.



](https://www.pcwelt.de/article/2162349#5)[

![](https://cdn.deepseek.com/site-icons/amazon.de)

Amazon.de

2026/08/11

meross Matter WLAN Steckdose mit Stromverbrauch, Zeitschaltuhr, 5x5x4.6cm | 16A Smart Steckdose mit Stromzähler für Balkonkraftwerk, funktioniert mit Home Assistant, HomeKit, Alexa und Google Home : Amazon.de: Baumarkt - Eine Person fand diese Informationen hilfreichFeedback wird gesendet

Sobald die Steckdose im WLAN war, ließ sie sich in ihrem bestehenden Matter-System einbinden. Für Menschen ... Dank Matter-Unterstützung war die Einbindung ein Kinderspiel. ... die auch noch den Stromverbrauch misst und sich dank Matter zukunftssicher in jedes System (Home Assistant, Apple Home...



](https://www.amazon.de/dp/B0F4KL53FB/?_encoding=UTF8&aref=m3eExZNWQg&pd_rd_i=B0F4KL53FB&pd_rd_i=B0F4KL53FB&ref_=sbx_be_s_sparkle_ssd_pce&pd_rd_w=7h9le&content-id=amzn1.sym.5f48dd2b-900b-4810-ac42-3d84e7cd4fa3&pf_rd_p=5f48dd2b-900b-4810-ac42-3d84e7cd4fa3&pf_rd_r=JXVKZFXNG4N0E3WJFTFA&pd_rd_wg=zyYPu&pd_rd_r=3bc14e39-9901-4e91-98e2-d68ad108ca98&pf_rd_p=5f48dd2b-900b-4810-ac42-3d84e7cd4fa3&pf_rd_r=JXVKZFXNG4N0E3WJFTFA&pd_rd_wg=zyYPu&pd_rd_w=7h9le&pd_rd_r=3bc14e39-9901-4e91-98e2-d68ad108ca98#3)[

![](https://cdn.deepseek.com/site-icons/notebookcheck-tr.com)

Notebookcheck

2026/04/29

Mikrofon ve hoparlöre sahip yeni akıllı ev ekranı Matter'ı destekliyor

Mikrofon ve hoparlöre sahip yeni akıllı ev ekranı Matter'ı destekliyor ... WiFi, hem 2.4GHz hem de 5GHz bantları dahil olmak üzere destekleniyor, ancak sistem aynı zamanda bir Matter köprüsü görevi de görüyor.



](https://www.notebookcheck-tr.com/Mikrofon-ve-hoparloere-sahip-yeni-akilli-ev-ekrani-Matter-i-destekliyor.1286225.0.html)[

![](https://cdn.deepseek.com/site-icons/amazon.com.au)

Amazon.com.au

2024/10/15

Customer Review

Reviewed in Australia on 16 October 2024 Had one of these already that I upgraded to matter and this model works perfectly as a replacement of my older versions to upgrade to matter and ensure it is future proof. Works with Google, SmartThings, Homekit and Alexa.



](https://www.amazon.com.au/gp/customer-reviews/R36AARU759664N)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

matter.cn

Aqora网关M100是一款小巧灵活的智能家居中枢，支持Zigbee3.0和Thread双协议，兼容Matter标准，可作为Matter控制器、桥接器，轻松接入Apple Home、Google Home、Amo- zonAlexa等主流平台

也给用户带来了更加放心便捷的使用感受，无需担心智能硬件厂家的App因云端故障等原因导致无法正常使用的问题，甚至有些Matter设备的固件升级也是可以通过生态平台的App来完成的 ... Matter标准的另一大优势在于其跨生态的兼容性。不再受限于单一的智能生态系统，设备可以在苹果家庭App和三星SmartThings等不同的智能平台间实现共享，满足家庭成员使用不同手机生态的需求，也可以给不同成员分配相应的控制权限和内容。



](https://matter.cn/wp-content/uploads/2025/08/Matter%E4%B8%AD%E5%9B%BD%E7%94%9F%E6%80%81%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%9B%AE%E5%BD%95-V1.pdf#3%233)[

![](https://cdn.deepseek.com/site-icons/amazon.it)

Amazon.it

Meross Matter Smart Socket with Energy Consumption, Alexa WiFi Sockets with Matter, Easy to Install, Photovoltaic Solar Panel Output Size, Support for Apple Home, Alexa and Google Home : Amazon.it: Sports & Outdoors - Reviewed in Italy on 20 August 2025Brief content visible, double tap to read full content

Meross Matter Smart Socket with Energy Consumption, Alexa WiFi Sockets with Matter, Easy to Install, Photovoltaic Solar Panel Output Size, Support for Apple Home, Alexa and Google Home ... - Matter Simple Setup (MSS) ... Simply connect the WiFi plug to the power source and tell the Amazon Echo to detect the device...



](https://www.amazon.it/dp/B0CGKKBR4P?tag=wnnewsamznlnkamznamznmklu-21#2)[

berrybase.de

SMLIGHT SMHUB Nano MG24, Linux Hub, Zigbee, Thread, Matter, Wi-Fi 6, Ethernet, PoE, Home Assistant, B-Ware

SMHUB Nano MG24, Linux Hub, Zigbee, Thread, Matter, Wi-Fi 6, Ethernet, PoE, Home Assistant, B-Ware ... Matterbridge ... Der SMHUB Nano MG24 kann als eigenständiger Smart Home Controller, als Matter Bridge oder als Funk Koordinator eingesetzt werden.



](https://www.berrybase.de/it/product-datasheet/019eb0b896db7225bb953f652e746f6d/create#1#1)[

![](https://cdn.deepseek.com/site-icons/amazon.co.uk)

Amazon UK

Meross Matter Smart Light Switch with Energy Monitor, Wireless Relay WiFi Switch Works with Alexa/HomeKit/Google Home, Smart Switch Module Voice & Remote Control, Neutral Wire Required : Amazon.co.uk: DIY & Tools - Some caution is required before selecting this option for remotely switching your lights as a neutral wire is required as not al...

'Matter' worked as promised with all the apps such as Alexa and Home and is a significant improvement on the setup process for the early Meross devices. ... Meross Matter Smart Light Switch with Energy Monitor, Wireless Relay WiFi Switch Works with Alexa/HomeKit/Google Home, Smart Switch Module Voice & Remote Control, Neutral Wire Required ... - Smart Switch Supports Matter Protocol



](https://www.amazon.co.uk/Monitor-Wireless-HomeKit-Control-Required/dp/B0F4WV8TKC/ref=dp_prsubs_d_sccl_1/521-0563992-2573419?pd_rd_w=NFEmH&content-id=amzn1.sym.e3e7b9bd-6b57-4b28-8a30-37934a5f8707&pf_rd_p=e3e7b9bd-6b57-4b28-8a30-37934a5f8707&pf_rd_r=EGHJTA1HCYDRDN3QA389&pd_rd_wg=otkDQ&pd_rd_r=a9b9b5b9-55c4-45a6-acc8-ae3e5a9e9d94&pd_rd_i=B0F4WV8TKC&th=1#2)[

![](https://cdn.deepseek.com/site-icons/um.edu.mt)

um.edu.mt

The Effort \(E = 9\) person - hours was reported in Table 4.41 under arrangements "Mechanical installations" such as fitting pul...

"Smart installations" such as integrating a sensor hub ... Finally, the effort with \(k = 20\) person- hours per FP in smart installations was calculated using Equation 4.22 ... The Effort \(E = 200\) person - hours was reported in Table 4.41 under smart installations.



](https://www.um.edu.mt/library/oar/bitstream/123456789/148128/1/2601ENRENR600005074639_1.PDF#44#42)[

![](https://cdn.deepseek.com/site-icons/d-nb.info)

d-nb.info

There was a significant difference at \( \alpha = 0.001 \) between the experimental time required to develop a use-case \( t_e \...

0.001\) of the required effort \((dof1 = 2 ... To evaluate the effort required in the treatments, SLOC was used a metric, which is a typical choice in programming of code changes. Also, task completion time was selected which is commonly used in empirical studies with users. Moreover...



](https://d-nb.info/1366372271/34#41#26)[

heise online

2024/11/09

Re: Wenn man sonst kein Hobby hat...

HomeKit: Einmal komplett eingerichtet (dauert zwei Stunden bei über 40 Geräten): Läuft! Alexa: Einmal Komplett eingerichtet (dauert ca 1 Stunde): Läuft! HomeAssistent. Komplett eingerichtet (dauert einen ganzen Tag)...



](https://www.heise.de/forum/heise-online/Kommentare/Anti-Matter-Warum-ich-von-dem-neuen-Smart-Home-Standard-erstmal-genug-habe/Re-Wenn-man-sonst-kein-Hobby-hat/posting-44508795/show/)[

![](https://cdn.deepseek.com/site-icons/uni-halle.de)

opendata.uni-halle.de

1. 1.It was easy to learn the handling of the interaction method (\(1=\text{hard}\), \(5=\text{easy}\))

S4 | Effort | \( Z = -3.126 \) | \( p < 0.001^* \) ... The strongest effect is measured for \(S4\) that shows that the NRS approach is less



](https://opendata.uni-halle.de/bitstream/1981185920/35294/1/Sprute_Dennis_Dissertation_2020.pdf#26#16)[

![](https://cdn.deepseek.com/site-icons/elsevierpure.com)

Elsevier

Design and Verification of a Smart Home Management System for Making a Smart Home Composable and Adjustable by the Elderly

To evaluate the usability of the developed system ... a simulated environment. The results showed that the average time required for setting up the system was approximately 2 min, and the average of the system usability scale to evaluate the configuration system was 78.5, which was sufficiently high...



](https://tus.elsevierpure.com/en/publications/design-and-verification-of-a-smart-home-management-system-for-mak)[

![](https://cdn.deepseek.com/site-icons/ulisboa.pt)

fenix.tecnico.ulisboa.pt

complaints nor users that did not like the system

Many felt that the system is practical and should be ... claims, the configuration processes times remain much lower compared with the obtained in configuring the real devices as we showed in Section 5.3. ... The times obtained in the configuration processes, with and without instruction manual, using AutoDev were much lower than those for the configuration processes ... These tests results demonstrate that configure these devices are a very time consuming task compared



](https://fenix.tecnico.ulisboa.pt/downloadFile/281870113704305/AutoDevDissertation.pdf#11#10)[

![](https://cdn.deepseek.com/site-icons/mendeley.com)

Mendeley

Design and Verification of a Smart Home Management System for Making a Smart Home Composable and Adjustable by the Elderly

To evaluate the usability of the developed system ... The results showed that the average time required for setting up the system was approximately 2 min, and the average of the system usability scale to evaluate the configuration system was 78.5, which was sufficiently high, indicating that the system was acceptable.



](https://www.mendeley.com/catalogue/77e8e376-82a0-3e83-b537-39fc353683bb/)[

Trusted Shops

2025/03/16

Bewertungen zu Bosch Smart Home DE | Lies 1.989 Bewertungen zu Bosch Smart Home DE

Das System ließ sich einfach installieren, der Zeitaufwand ist optimierbar (ca. 1,5 h für den Controller und 5 Thermostate), einen Thermostat musste ich auf Werkseinstellung zurücksetzen, das war mit etwas Recherche (5 bis 10 min) im Internet verbunden (auch optimierbar).



](https://www.trustedshops.de/bewertung/info_XFC0F590509CEAFC8665ACCA8D0240BEF.html?stars=3&stars=4&stars=5)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2026/08/19

Home automation: hobby or time sink? - Lounge - Hubitat - post by eelton on Aug 20

I'm sure it's been many hundreds--probably thousands--of hours of setup. ... Effort usually peaks around the second year, when users are constantly adding, refining, troubleshooting, and redesigning. Unfortunately ... When I moved 3 years ago ... Took about 6 months to get this house setup. I have a single C-8 Pro...



](https://community.hubitat.com/t/home-automation-hobby-or-time-sink/165788/3#1)[

![](https://cdn.deepseek.com/site-icons/beds.ac.uk)

beds.ac.uk

2020/10/28

Study of Effectiveness of Prior Knowledge for Smart Home Kit Installation - Another evaluation metric is the time each participant spends in the experiment’s training section and installation section

Another evaluation metric is the time each participant spends in the experiment’s training section and installation section. ... We believe that the



](https://0-www-mdpi-com.brum.beds.ac.uk/1424-8220/20/21/6145#2)