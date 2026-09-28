---
modified: 2026-09-28T20:23:37+03:00
---
The promise of Matter was simple: buy any device, pair it with any controller, and everything works. The reality, as of Matter 1.6 and Thread 1.4, is significantly more fragmented. While the specification has matured, ecosystem implementation remains the primary bottleneck. The gap between certification and real-world behavior is where most interoperability failures occur.

### 📱 Device Types & Feature Consistency

**What works consistently:**
- **Basic device types** (lights, plugs, switches, sensors, locks) generally commission and respond to commands across Apple, Google, Amazon, and Samsung ecosystems.
- **Matter 1.5 camera support** is the most significant recent addition. Samsung SmartThings became the first platform to fully support Matter cameras, including live streaming, two-way talk, motion detection, and pan-tilt-zoom controls. Amazon followed with Matter 1.5 support on Echo devices in March 2026. Apple and Google have been slower to implement camera support.
- **Matter 1.6** introduces NFC-based commissioning (allowing devices to be set up before they are powered on) and **Joint Fabric**, which allows multiple ecosystems to co-administer a single shared Matter network rather than running separate fabrics. However, ecosystem support for Joint Fabric is not yet widespread.

**What remains inconsistent:**
- **Advanced features** like power monitoring, scenes, and complex automation triggers are often excluded from the Matter specification and remain in vendor apps.
- **Platform-specific device types** may not appear in all ecosystems. For example, Samsung SmartThings supports 58 Matter device types, but other platforms may support fewer.
- **Automation creation** varies dramatically: Amazon, Apple, and Google lack native support for creating automation rules directly within their Matter implementations, while Samsung supports it through third-party apps linked to a Samsung account.

### ⚠️ Optional Features, Extensions, and Certification Gaps

Certification confirms protocol conformance but **does not guarantee ecosystem compatibility**. A certified device meets the specification, but it must still work with four different onboarding flows, four room-and-device naming models, and four multi-admin sharing models.

**Where incompatibility arises:**
- **Multi-admin sharing** is a major pain point. In testing, Amazon Echo did not fully support multi-admin; while Alexa could generate setup codes for HomePod Mini and SmartThings, it consistently failed with Google Home. Apple HomePod Mini exhibited robust multi-admin support but had issues with Samsung SmartThings commissioning.
- **Commissioning failures** are common, especially when sharing devices from Apple Home to other controllers. In Home Assistant, the Add Matter Device dialog frequently fails to advance to the post-commissioning step, even though the backend pairing succeeds.
- **Firmware updates** can fail due to border router issues. Apple border routers have been identified as failing to forward mDNS packets, which prevents OTA updates from working in Home Assistant.

### 🔌 What Fails When Infrastructure Goes Offline

**Thread Border Router offline:**
- Matter-over-Thread devices lose the ability to communicate with each other when the border router is down. A light switch loses control over a light after about one minute because the SRP Server (which stores IPv6 addresses) is unavailable.
- iOS has a critical flaw: if the preferred Thread network's border router is removed, iOS continues to consider that network preferred, and commissioning new devices fails until the original border router is powered back on.

**Home router or cloud outage:**
- **Local control** is one of Matter's key advantages. Commands for basic device operations (e.g., turning on a light) travel over the local network without an internet round trip.
- However, **cloud-dependent features** (remote access, voice assistants, notifications) fail when the internet is down. If an automation places a cloud action before a local action, the local action inherits the timeout and may fail.
- **Google Home hubs** can now work locally thanks to Matter, allowing supported devices to be controlled even when the internet is down.

### 🔄 Migration Between Ecosystems

Users **cannot** seamlessly migrate devices, routines, and permissions without rebuilding.

- **Device migration** requires re-commissioning. A Matter device can participate in multiple ecosystems via Multi-Admin, but this must be done device-by-device. There is no bulk migration tool.
- **Routines and automations** are ecosystem-specific. An automation built in Google Home cannot be directly transferred to Apple Home. Matter 1.6's Joint Fabric aims to address this by creating a shared Datastore, but adoption is still nascent.
- **Permissions** are managed per ecosystem. Removing a device from one ecosystem may or may not remove it from others, depending on the controller's implementation.

### 📊 Matter/Thread vs. Zigbee, Z-Wave, and Proprietary Systems (5–10 Year Outlook)

| Aspect | Matter over Thread | Zigbee | Z-Wave | Proprietary (e.g., Lutron, Philips Hue) |
|---|---|---|---|---|
| **Commissioning** | QR code/NFC; multi-admin is complex | Pairing button; mature | Inclusion/exclusion; mature | App-based; simple but siloed |
| **Multi-Admin** | Supported but inconsistent | Not supported | Not supported | Not supported |
| **Updates** | OTA via Matter; ecosystem-dependent | OTA via hub; reliable | OTA via hub; reliable | Vendor cloud; reliable |
| **Local Control** | Yes (if border router present) | Yes (via hub) | Yes (via hub) | Often requires cloud |
| **Failure Recovery** | Border router failure breaks mesh | Hub failure breaks network | Hub failure breaks network | Cloud failure breaks control |
| **Migration** | Difficult; no bulk tools | Locked to hub | Locked to hub | Locked to vendor |
| **Long-Term Reliability** | Improving, but ecosystem fragmentation is a risk | ~20 years mature; rock-solid | UL-rated for security; most stable | Vendor-dependent; risk of EOL |

**Key takeaways:**
- **Z-Wave** remains the most reliable and secure option for mission-critical applications, with unmatched out-of-the-box reliability due to mandatory certification.
- **Zigbee** is a mature workhorse with excellent battery life and a huge device ecosystem.
- **Matter over Thread** offers the promise of cross-ecosystem interoperability and local control, but currently suffers from fragmentation and inconsistent implementation.
- **Proprietary systems** offer the best user experience within their walled gardens but lock users in and carry long-term EOL risk.

### 🚨 Interoperability Risk Assessment

**High Risk:**
- **Multi-admin and ecosystem sharing**: The most fragile area. Expect duplicate device entries, failed commissioning, and inconsistent state across platforms.
- **Thread border router dependency**: A single point of failure. Without a border router, Thread devices lose mesh communication.
- **Firmware updates**: OTA failures are common, often due to border router mDNS issues.

**Medium Risk:**
- **Commissioning**: Works for basic devices but fails for complex setups or when sharing from Apple Home.
- **Local control**: Reliable for basic commands but breaks when cloud-dependent features are in the critical path.
- **Device type support**: Cameras, closures, and energy management are newer and less consistently supported.

**Low Risk:**
- **Basic device control** (on/off, dimming) works across all major ecosystems.
- **Local Matter/Thread paths** work without internet for basic operations.

### 🛠️ Product-Design Implications

1.  **Test beyond certification**: Certification is table stakes. You must test commissioning, multi-admin sharing, Thread border-router behavior, and firmware updates across all four major ecosystems.
2.  **Design for graceful degradation**: Ensure local control paths do not depend on cloud services. Place cloud actions after local actions in automations.
3.  **Handle Thread border router failures**: Implement mechanisms to detect border router loss and recover gracefully. Consider supporting multiple border routers for redundancy.
4.  **Simplify multi-admin**: Provide clear user guidance for sharing devices across ecosystems. Expect and handle duplicate entries.
5.  **Plan for migration**: Assume users may want to switch ecosystems. Design your device to be easily re-commissioned and provide clear documentation for removing it from one ecosystem before adding to another.
6.  **Monitor ecosystem adoption**: Joint Fabric and NFC commissioning are promising but not yet widely supported. Design products that can be updated via firmware to take advantage of these features when ecosystems catch up.

The state of Matter in 2026 is one of **specification maturity but ecosystem immaturity**. The standard has the tools to deliver on its promise, but platform vendors must implement them consistently for the user experience to match the marketing. Until then, interoperability remains a work in progress.

[

![](https://cdn.deepseek.com/site-icons/forkast.news)

Forkast News

2026/08/28

Matter Was Supposed to Unite Your Smart Home. It’s Creating a New Kind of Fragmentation.

Apple’s HomeKit runs its own Thread border router network. Google Home runs another. Samsung SmartThings runs a third. ... Matter 1.4 and 1.4.2 addressed some interoperability gaps, but Matter 1.6 — the version with Joint Fabric...



](https://forkast.news/matter-was-supposed-to-unite-your-smart-home-its-creating-a-new-kind-of-fragmentation/)[

Developex

2026/07/07

Matter Device Compatibility Testing - Developex

Thread border-router behavior, firmware-update handling, or controller interface behavior inside Apple Home, Google Home, Amazon Alexa, and Samsung SmartThings. ... Matter 1.4.2 set Network Infrastructure Manager requirements under which a Thread Border Router must support at least 150 devices and a Wi-Fi access point at least 100 simultaneous associations (csa-iot.org...



](https://developex.com/blog/matter-device-compatibility-testing/)[

![](https://cdn.deepseek.com/site-icons/avnet.com)

my.avnet.com

manufacturers, NXP’s pre-certified platforms and services accelerate development,

Matter needs at least one Thread border router and a Matter controller. Many smart speakers ... This process is not part of Matter 1.0, but Google, Amazon, Apple, and other smart home platforms have credential- sharing workarounds (or are working on them).



](https://my.avnet.com/wcm/connect/b832cbe9-096e-4771-a2c8-cad77dde8fdd/nxp-matter-making-smart-homes-smarter.pdf?MOD=AJPERES#3#3)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey

2026/07/27

Homey is now Matter 1.5 certified – News | Homey

Homey Pro and Homey Pro mini include a built-in Thread Border Router ... With the Matter Bridge app, supported devices connected to Homey can be shared with Apple Home, Google Home, Amazon Alexa, Samsung SmartThings, and Home Assistant, even if they don’t natively support Matter.



](https://homey.app/en-vn/news/homey-matter-1-5-certified/)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

为物联网设备制造商采用 Matter 标准

Matter 是一种开放的智能家居连接协议，支持包括亚马逊 Alexa、Google Home、App HomeKit 和三星在内的主要生态系统中的物联网设备、移动应用程序和云服务之间的通信。SmartThings ... 一台Matter设备可以由一台AmazonAlexa设备和GoogleHome设备进行管理...



](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#6#2#3#1)[

n.net.pl

2026/08/20

Standard Matter i Thread – koniec wojen o kompatybilność urządzeń Smart Home. - n.net.pl

Standard rozwijał również funkcje infrastrukturalne związane z routerami i punktami dostępowymi Matter, w tym możliwością łączenia Wi-Fi z Thread Border Routerem. ... że każda funkcja każdego urządzenia automatycznie pojawia się identycznie w Apple Home...



](https://n.net.pl/standard-matter-i-thread-koniec-wojen-o-kompatybilnosc-urzadzen-smart-home/#respond)[

smartbuildingexpo.it

SMART BUILDING EXPO

La rete Thread, per comunicare con il resto del mondo, necessita di un router di confine, il BORDER ROUTER. ... Gli ecosistemi matter, che si tratti di Amazon, Apple, Google o di un altro produttore, possono ora utilizzare i dati per verificare se un dispositivo da aggiungere di recente è conforme agli standard



](http://smartbuildingexpo.it/wp-content/uploads/2025/12/AIBACS-Marco-Praderio-Matter.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey

2026/07/27

Homey is gecertificeerd voor Matter 1.5 – News | Homey

hebben een ingebouwde Thread Border Router ... Met de Matter Bridge-app deel je ondersteunde apparaten die aan Homey zijn gekoppeld met Apple Home, Google Home, Amazon Alexa, Samsung SmartThings en Home Assistant, zelfs als die apparaten zelf geen Matter ondersteunen.



](https://homey.app/nl-nl/news/homey-matter-1-5-certificering/?utm_campaign=search&utm_content=US-keycities&utm_medium=cpc&utm_source=google)[

![](https://cdn.deepseek.com/site-icons/perplexity.ai)

Perplexity

2026/07/29

Perplexity

Homey Pro 和 Homey Pro mini 内置了 Thread 边界路由器，允许 Matter over Thread 设备无需额外硬件即可直接连接。homey+2 该认证由负责认证 Apple Home、Google Home、Amazon Alexa 和 Samsung SmartThings 的同一机构颁发 ... Google Home、Amazon Alexa、Samsung SmartThings 以及 Home Assistant。



](https://www.perplexity.ai/discover/tech/3e352898-ec6e-4c07-96b2-7de585b186e5)[

![](https://cdn.deepseek.com/site-icons/eefocus.com)

Eefocus

2026/02/11

Matter协议正式发布三年后，不同平台兼容性实测到底怎么样了？

我把市面上主流支持Matter的平台——Apple Home、Google Home、Amazon Alexa、Samsung SmartThings、Home Assistant——翻来覆去测了一遍 ... iOS 16.1开始支持Matter控制器，HomePod mini和Apple TV 4K（2021及以后）都内置Thread边界路由器，不需要额外买硬件 ... 一句话总结：苹果用户闭眼入 ... Samsung SmartThings：Matter 1.5首波落地...



](https://m.eefocus.com/e/1959616.html#1)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

Silicon Labs

2026/02/10

Matter 1.5 for Next Generation Smart Homes - Silicon Labs - Matter 1.5: Powering the Next Generation of Smart Homes

This update includes much-anticipated support for cameras, while also introducing updated features and device types for closures, soil sensors, and advanced energy management. ... enabling seamless interoperability between devices from different brands so that your smart home just works. ... It provides precise, interoperable motion and position control.



](https://www.silabs.com/blog/matter-1-5-for-next-generation-smart-homes#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon Developers

2026/04/30

Connect Your Device to Alexa with Matter | Alexa Skills Kit

Matter is an Internet Protocol (IP) wireless connectivity technology designed to enable interoperability between devices made by different manufacturers. ... Matter-compatible Echo devices support the Matter 1.5 Software Development Kit (SDK), enabling support for a subset of Matter 1.5 and lower device types.



](https://developer.amazon.com/en-IN/docs/alexa/smarthome/matter-support.html)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2026/03/03

2025回顾：Matter如何通过五大里程碑改变智能家居世界

于 2025 年末发布的 Matter 1.5 最终为视频设备带来了一个全面的框架。新的规范涵盖了大量设备，包括泛光照明摄像头、视频门铃、门铃提示器和室内对讲机。它支持直播、录制、双向音频和云台控制等基本功能。通过使用 WebRTC 等成熟技术...



](https://matter.cn/4990.html)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2025/12/22

关键一步：Matter 1.5支持摄像头，与Wi-Fi共促智能生态融合

新版本首次引入摄像头设备类型，支持视频流传输、本地与云端存储、隐私区域设置等功能，并通过WebRTC实现低延迟双向通信。同时，Matter 1.5增强了能源管理能力，支持电价与碳数据上报，助力设备符合欧盟2027年能效规范。



](https://matter.cn/4506.html)[

Microwaves & RF

2026/03/31

The Shift to TCP: How Matter 1.5 Evolved to Support Vision and Grid Intelligence

Matter 1.5 moves beyond basic control to support high-bandwidth TCP transport, standardized camera clusters, and grid-interactive energy models. ... IoT interoperability, ensuring devices work together across Thread, Wi-Fi ... Matter 1.5 unifies this landscape by leveraging TCP to standardize cameras as a supported device type, enabling live audio and video



](https://www.mwrf.com/technologies/communications/wireless/article/55368135/silicon-labs-matter-15-technical-analysis-tcp-vision-and-energy-management)[

![](https://cdn.deepseek.com/site-icons/hoperf.com)

HOPERF

2025/12/29

Smart Home Takes Another Leap Forward, HOPERF Fully Supports Matter 1.5

This update mainly adds several influential device types and application scenarios, including support for cameras, closed devices, and soil sensors. ... Matter version 1.5 adds support for camera devices, providing a unified interoperability framework for camera products from different brands and ecosystems ... Matter version 1.5 adds unified support for closed devices such as curtains...



](https://m.hoperf.com/news/Product_Launch/1358.html)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/12/18

Matter 1.5 is arriving in Samsung SmartThings - Advertisement

The major addition in Matter 1.5 was smart cameras support, and now those cameras should work seamlessly in the SmartThings app. The new Matter standard also includes more options for blinds, awnings, and garage doors, as well as some energy management features.



](https://tech.yahoo.com/home/articles/matter-1-5-arriving-samsung-163655297.html#1)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2026/08/09

新品｜Homey 更新至 Matter 1.5——支持更多智能设备

相比许多控制器仅支持的 Matter 1.3 规范，Matter 1.5 新增了对电动汽车充电桩、热泵、太阳能板和大型家用电器的兼容性 ... 将 Zigbee ... 目前 Matter Bridge 支持灯、插座、温控器、门锁、窗帘和传感器等类型...



](https://matter.cn/6029.html)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/08/09

Matter: Commissioning multi-admin device doesn't finish · Issue #53593 · home-assistant/frontend - Skip to content

Commissioning multi-admin device doesn't finish #53593 ... the Add Matter Device dialog never advances to the post-commissioning step when a multi-admin device (especially from Apple Home) is being paired. However, the actual pairing on the backend does succeed and the new Matter device works just fine.



](https://github.com/home-assistant/frontend/issues/53593#1)[

![](https://cdn.deepseek.com/site-icons/iisec.ac.jp)

iss.iisec.ac.jp

スマートホーム向け規格Matterの 競合についてのセキュリティ問題

スマートホーム向け規格Matterは、デバイスやベン ダー間の相互運用性を特徴としており、一つのデバイ スを複数のControllerで競合して操作させることができ るMulti-Admin環境に対応している ... セキュリティおよび運用の整合性に与える影響を実機 で検証し、その要因と課題を整理すること。



](https://iss.iisec.ac.jp/sympo25/posters/M2_209poster25.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

Data: Version: 1 (0x0) Subject: Subject Public Key Info: Public Key Algorithm: id- ecPublicKey Public- Key: (256 bit) pub:...

A user who wishes to have an already commissioned Node join another Fabric (and therefore another Security Domain) provides consent by instructing an existing Administrator, which SHALL put the Node into commissioning mode by using steps outlined in Section 5.6.4 ... The Node SHALL host an Section 11.19, "Administrator Commissioning Cluster". The Cluster exposes commands which enable the entry into commissioning mode for a prescribed time...



](https://csa-iot.org/wp-content/uploads/2026/03/23-27349-010_Matter-1.5.1-Core-Specification.pdf#176#152)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

b

This method allows a current Administrator to set multiple Nodes for commissioning with a new administrator with an appropriate Commissioning Window, by opening a commissioning window using the OpenCommissioningWindow ... • When commissioning fails, the commissioner MAY also reference Distributed Compliance Ledger fields such as CommissioningFallbackUrl (see Section 5.7.5 ... UserManualUrl, SupportUrl and ProductUrl to assist the user in further steps to resolve the issue(s).



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#41)[

European Research Studies Journal

2026/09/18

The Matter Protocol as a Solution to Ecosystem Fragmentation in Smart Home Environments: Architecture, Capabilities, and Implementation Challenges

Multi-Admin functionality, and the technical requirements associated with device commissioning and certification. ... while the Multi-Admin feature enables devices to operate across multiple smart home platforms. However, implementation constraints remain, particularly the computational requirements associated with certificate-based commissioning over Bluetooth Low Energy and continued fragmentation arising from differences in platform orchestration logic. Practical Implications...



](https://ersj.eu/journal/4419)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

4. Convert the Subject Public Key Info of the ICA CSR's to the equivalent Matter certificate TLV values by using the specific ru...

A user who wishes to have an already commissioned Node join another ... All Nodes SHALL ... The Fabric Synchronization feature enables commissioning of devices from one fabric to another without requiring user intervention for every device. It defines mechanisms that can be used by multiple ecosystems/controllers to communicate with one another to simplify the experience for users.



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#146)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2024/12/20

GitHub - sammachin/node-red-matter-controller · GitHub - GitHub - sammachin/node-red-matter-controller · GitHub

Currently this controller does not support commisioning via Bluetooth, this means that the Matter device must already be connected to the same network as the controller before it can be commisioned. Usually this will require you to connect ... You can then add this controller as a 2nd ecosystem, known as Multi-Admin.



](https://github.com/sammachin/node-red-matter-controller#1)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey Community Forum

2026/01/13

Matter multi-admin failing - Homey Pro Mini + Apple Home + Eve Thread devices (Matter) - Questions & Help - Homey Community Forum

In all cases, Homey goes through the Matter commissioning flow but fails at the final step (“unable to connect” / commissioning fails at the end). ... Phone must also be on the same IoT SSID/VLAN when commissioning Matter devices, or Thread networks are not found.



](https://community.homey.app/t/matter-multi-admin-failing-homey-pro-mini-apple-home-eve-thread-devices-matter/148956/4)[

Why Can't My Fibaro Home Center Discover Devices?

2026/03/18

Matter Multi-Admin Not Working — Second Platform Cannot See Device?

Re-scanning the original QR instead of the multi-admin share flow - Primary platform's hub offline during sharing - Device firmware doesn't support multi-admin despite certification ... - Second platform's hub not set up or degraded - Device at its fabric limit (typically 5)



](https://www.trunetto.com/troubleshooting/smart-hubs/matter/matter-multi-admin-second-platform-not-working)[

![](https://cdn.deepseek.com/site-icons/google.com)

Google Home Developers

2024/09/08

适用于 Android 的 Commissioning API 的多管理员 | Home APIs - Android | Google Home Developers

Android 上的 Commissioning API 支持 Matter 的多管理员 （或 多管理员），这意味着 Commissioning API 可以充当主要或 次要 Matter 调试器，并且您可以添加自己的 调试器：Matter ... - 在此模式下，系统会先使用 Google UX 添加 Google 结构。



](https://developers.home.google.com/apis/android/commissioning/multi-admin?authuser=0&hl=zh-cn#secondary)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2025/06/29

A question about matter over thread products - - State Not Answered

However, when the border router is powered off, the switch retains control over the light for about the first minute but loses this capability thereafter. ... Light Switch needs the IPv6 address of the Light Bulb, which is stored in the SRP Server. When the Thread Border Router is down, binding will not work.



](https://devzone.nordicsemi.com/f/nordic-q-a/122610/a-question-about-matter-over-thread-products/544539#1)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2023/07/05

Matter Binding after disconnecting OTBR - - State Not Answered

it is not possible to control Thread devices over Matter devices without Border Router. The Border Router is an SRP server which is needed for devices to be able to resolve other devices over matter. Additionally, while the border router is removed the Thread devices remove external IP address which is in use during Matter communication.



](https://devzone.nordicsemi.com/f/nordic-q-a/101589/matter-binding-after-disconnecting-otbr?ReplySortBy=CreatedDate&ReplySortOrder=Descending&pifragment-684=3#1)[

![](https://cdn.deepseek.com/site-icons/stackoverflow.com)

Stack Overflow

2026/09/03

iOS ThreadNetwork / MatterSupport: how can a third-party app recover when the preferred Thread network has no live border router? - Asked

I have a third-party Matter/Thread app with thecom.apple.developer.networking.manage-thread-network-credentials entitlement. ... So iOS still considers a network preferred whose border router no longer exists, and my live hub - the only device advertising_meshcop._udp on the LAN - never ... storeCredentials succeeds for it.



](https://stackoverflow.com/questions/80000743/ios-threadnetwork-mattersupport-how-can-a-third-party-app-recover-when-the-pr#1)[

![](https://cdn.deepseek.com/site-icons/threadgroup.org)

threadgroup.org

Since Thread does not require any form of translation, a Thread Border Router’s sole function is to send packages between the lo...

communication between the low power mesh network and the rest of the network remains possible even if one of those devices go offline. ... | | A network may have multiple Thread Border Routers - Seamless switching | Typically one hub - All devices go offline if hub goes offline |



](https://threadgroup.org/Portals/0/documents/Thread%20for%20Pro%20Home%20and%20Buildings%20White%20Paper%202024__02.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

silabs.com

| External Routing (including default route) | Role can be enabled, disabled, or configured by a high-level application on th...

Disabled when external interface loses connectivity. ... A user may temporarily power off device BR1 (for example, for maintenance purposes). As BR1 is also the Leader, when it is no longer be active in the Thread Network for a defined time interval, another router will take over the Leader role.



](https://www.silabs.com/documents/public/white-papers/Thread-Border-Router.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/05/04

Matter over Thread devices remain unavailable after restart – missing subscription recovery (multi-BR setup) · Issue #169781 · home-assistant/core - Skip to content

Matter over Thread devices remain unavailable after restart – missing subscription recovery (multi-BR setup) #169781 ... After restarting Home Assistant, all Matter over Thread router devices (mains-powered lights) remain unavailable indefinitely. ... Devices may reattach via a different border router after restart...



](https://github.com/home-assistant/core/issues/169781#1)[

![](https://cdn.deepseek.com/site-icons/aqara.com)

Aqara Forum

2026/09/24

A four-path check when Matter over Thread works but a vendor app says offline - Everything Matter - Aqara Forum

A device responding in a Matter controller while its vendor app says “offline” narrows the problem, but it does not by itself prove the Thread border router lacks NAT64. The two apps may be using different paths. ... If swapping to a router with confirmed ... vendor-app result while Matter control stays stable...



](http://forum.aqara.com/t/a-four-path-check-when-matter-over-thread-works-but-a-vendor-app-says-offline/339134)[

![](https://cdn.deepseek.com/site-icons/aqara.com)

Aqara Forum

2026/09/25

A four-path check when Matter over Thread works but a vendor app says offline - Everything Matter - Aqara Forum

A device responding in a Matter controller while its vendor app says “offline” narrows the problem, but it does not by itself prove the Thread border router lacks NAT64. ... Some devices might appear offline if they are experiencing intermittent power drops, even if they respond to a local Matter command once powered up.



](https://forum.aqara.com/t/a-four-path-check-when-matter-over-thread-works-but-a-vendor-app-says-offline/339134/2)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2023/06/07

Communication between Matter Devices After Disconnecting OTBR - - State Not Answered

Hey, I Got issues that when I did Matter Binding between two Matter Devices using Open Thread Border Router at that time My both Matter Devices (Two NRF52840 board) easily connected with thread networ



](https://devzone.nordicsemi.com/f/nordic-q-a/100596/communication-between-matter-devices-after-disconnecting-otbr/430738#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/12

Google Home shoes all matter over thread devices after pairing offline · Issue #4020 · home-assistant/addons - Skip to content

Skip to content ## Navigation Menu {{ message }} # Google Home shoes all matter over thread devices after pairing offline #4020 ## Description ### Describe the issue you are experiencing I have



](https://github.com/home-assistant/addons/issues/4020#1)[

![](https://cdn.deepseek.com/site-icons/arstechnica.com)

Ars Technica

2024/11/07

Matter 1.4 has some solid ideas for the future home—now let’s see the support - - Status

Z-wave and Zigbee are ~20 years old. Zwave has a market lock being the only commodity wireless tech that is UL rated for use in security systems, which is why it's the heart of Ring and Vivint and baked into a lot of other security systems.



](https://arstechnica.com/civis/threads/matter-1-4-has-some-solid-ideas-for-the-future-home%E2%80%94now-let%E2%80%99s-see-the-support.1504017/?thutp_user_id=136222&order=vote_score#1)[

heise online

2025/11/13

Re: der nächste gehypte "Standard" :-)

2) Matter (over Thread) ... - Niedrige Latenz: Reaktionen sind schneller als bei Zigbee und stabiler als bei WLAN. also. Für ... Das wollen viele nicht hören, die in Zigbee oder Z-Wave investiert sind, aber so ist es.



](https://www.heise.de/forum/heise-online/Kommentare/Smart-Home-von-Ikea-21-neue-Matter-Geraete-kommen-in-die-Regale/Re-der-naechste-gehypte-Standard/posting-45728613/show/#top)[

![](https://cdn.deepseek.com/site-icons/ravepubs.com)

rAVe [PUBS]

2026/06/07

Does Thread Matter in 2026? Comparing Matter, Thread, Zigbee, Z-Wave and Wi-Fi

Zigbee, Z-Wave ... The latest 800-series long-range Z-Wave devices can reach impressive distances and maintain strong reliability, whether your Wi-Fi is working or not. ... all Z-Wave products get vetted and require certification prior to release, so out of the box, reliability is unmatched. ... Z-Wave continues to be the most stable and secure option — even if it is not always the most cost-effective.



](https://ravepubs.com/does-thread-matter-in-2026-thread-matter-zigbee-z-wave-wifi-comparison/)[

![](https://cdn.deepseek.com/site-icons/arstechnica.com)

Ars Technica

2026/01/06

Bose open-sources its SoundTouch home theater smart speakers ahead of EoL - You are using an out of date browser

You can also buy devices that use open protocols like zwave, zigbee, or thread/matter. zwave is by far the best of the 3 because the certification requires that the devices properly implement the standard ... For me stuff I care about long-term support for is zwave (thermostat...



](https://arstechnica.com:8080/civis/threads/bose-open-sources-its-soundtouch-home-theater-smart-speakers-ahead-of-eol.1511062/?thutp_user_id=204659#1)[

Oakfield, NY — 2026 Building Permit Guide | Jaspector

2026/03/17

Smart Home Protocols | Jaspector

Compare Wi-Fi, Zigbee, Z-Wave, and Matter so you can judge compatibility, battery impact, hub needs, local control, and long-term smart home risk. ... Wi-Fi is simple and common, while Zigbee and Z-Wave often work better for low-power distributed sensors and controls.



](https://www.jaspector.com/wiki/smart-home-protocols-compared/#key-concepts)[

serenitysmarthomesnj.com

2025/07/09

Matter over Thread vs Zigbee & Z-Wave: Which Smart Home Protocol Wins in 2026?

Matter over Thread vs. ... but it doesn't fix the underlying stability challenges that still make Z-Wave (our default choice for smart home installations) more reliable for mission-critical applications. ... Zigbee: The Reliable Workhorse Strengths: Rock-solid reliability, excellent battery life, mature ecosystem with thousands of devices



](https://www.serenitysmarthomesnj.com/2025/07/10/matter-over-thread-showdown.html)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2026/08/15

New Devices: Should I stop buying Zwave and Zigbee in favor of Matter? - Get Help / Devices - Hubitat - post by calinatl on Aug 16

Z-Wave: mesh rate has been 100 kbps since the 500 series. 800 added Long Range ... same PHY as Zigbee, same interference risk with wifi. ... Zigbee: 32 is the hub's direct-child limit, and repeaters extend it. No downside to Zigbee.



](https://community.hubitat.com/t/new-devices-should-i-stop-buying-zwave-and-zigbee-in-favor-of-matter/165715/5#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2025/11/13

IKEA just announced 21 new affordable Matter-over-Thread smart home devices (which may also support Zigbee too) - Hardware - Home Assistant Community - Load more posts above

For Matter over Thread it will be worse because the technology is new and IPv6 ... Z-wave does not have all of these problems. ... In my experience, Zigbee kit is cheap and unreliable. ... Meanwhile, Z-Wave kit works fine after many years (Fibaro firmware updates not included).



](https://community.home-assistant.io/t/ikea-just-announced-21-new-affordable-matter-over-thread-smart-home-devices-which-may-also-support-zigbee-too/948187/33#1)[

routerarena.com

2025/08/20

Matter vs Zigbee vs Z-Wave vs Thread — The 2025 Smart-Home Showdown

Matter vs Zigbee vs Z-Wave vs Thread — The 2025 Smart-Home Showdown ... while retaining proven Z-Wave or Zigbee devices that continue to meet reliability needs. ... Matter gives buyers a ... while Zigbee and Z-Wave retain real advantages in cost and professional reliability respectively.



](https://www.routerarena.com/guide/Matter-vs-Zigbee-vs-Z-Wave-vs-Thread-The-2025-Smart-Home-Showdown)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2026/08/16

New Devices: Should I stop buying Zwave and Zigbee in favor of Matter? - Get Help / Devices - Hubitat - Load more posts above

## Load more posts above ## post by HAL9000 1 day ago ## post by velvetfoot 1 day ago ## post by danabw 1 day ago ## post by calinatl 1 day ago ## post by calinatl 1 day ago ## post by terminal3



](https://community.hubitat.com/t/new-devices-should-i-stop-buying-zwave-and-zigbee-in-favor-of-matter/165715/29#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

为了采用Matter标准，设备必须在IP网络上运行，例如Wi- Fi、以太网和Thread

Matter基本上排除了对任何依赖专有非IP无线标准的设备进行认证的可能性 ... 硬件限制 另一个挑战是，Matter需要最低水平的设备端处理能力和内存来支持必要的软件堆栈。但是 ... 截至2026年，Matter的采用已达到临界水平，主要生态系统（亚马逊Alexa、GoogleHome、苹果HomeKit、三星SmartThings）完全支持该标准。



](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#6#2)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/12/07

Certification chain validation discrepancies C++ / TypeScript SDK · Issue #2809 · matter-js/matter.js - Skip to content

The TS implementation rejects cryptographically valid NOCs and breaks interoperability with C++ devices and controllers. ... I had a deeper check in the Matter specification and there it basically only defines that validity need to be validated as "prescribed by RFC 5280." ...



](https://github.com/matter-js/matter.js/issues/2809#1)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

添加IP堆栈支持意味着为网络处理分配更多的内存和处理能力

Matter基本上排除了对任何依赖专有非IP无线标准的设备进行认证的可能性。这可能会限制想要为其低端产品使用替代连接方法的制造商 ... 硬件限制 另一个挑战是，Matter需要最低水平的设备端处理能力和内存来支持必要的软件堆栈。但是 ... 主要生态系统（亚马逊Alexa、GoogleHome、苹果HomeKit...



](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#6#2#3#2)[

![](https://cdn.deepseek.com/site-icons/ndss-symposium.org)

ndss-symposium.org

Poster: An Analysis of Matter IoT Security Against International Standards and Regulatory Framework

Matter devices are subject to mandatory third- party certification, with certification status recorded in a Distributed Compliance Ledger (DCL) [3] to ensure that only compliant devices join a Matter fabric. ... Such heterogeneity limited cross- platform interoperability and increased the complexity of device integration and management.



](https://www.ndss-symposium.org/wp-content/uploads/ndss26-poster-76.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/mdpi.com)

mdpi.com

activities: Matter (now supported by Connectivity Standards Alliance (CSA), Apple, Google, Amazon, and Samsung) is an applicatio...

These interoperability challenges are primarily at the semantic and organizational levels since Matter's certification standards device models and encryption (syntactic layer) but does not enforce consistent security- policy or trust- domain behavior across vendors. ... Matter- certified devices typically implement only subsets of the device types and clusters defined by the specification...



](https://www.mdpi.com/2078-2489/17/9/891/pdf?version=1789394161#15#7)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

docs.aws.amazon.com

CRL Revocation Support (Matter 版本 1.2 及更高版本)

crlDistributionPointExtensionConfiguration 在 Matter 中，CRL 分发点 (CDP) URI 未嵌入在证书中，而是从 Matter 分布式合规性账本 (DCL) 中提取的。您必须将 CDP URI 上传到 Matter DCL ... 但是，那些设计为仅通过非标准（专有）协议与供应商指定的集线器交互的设备将无法从Matter认证流程中受益。



](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/strategy-matter-standard/strategy-matter-standard.pdf#6#2#3#3)[

qu3ry.net

Matter Unified Smart Home Devices. The Protocol Still Separates Data From Authority.

1. Vendor and Product Reality Matter is governed by the Connectivity Standards Alliance (CSA) ... Google, Amazon, Samsung ... 2. The Architectural Gap ... Matter composes with AQ as the device- interoperability and cluster- modeling layer running over the memory- native protocol substrate, rather than as the governance authority itself. What stays at Matter and the CSA...



](https://qu3ry.net/articles/memory-native-protocol-matter.pdf#1#1)[

nbn-resolving.de

Trusted Product Attestation Authority (PAA) certificates are stored in the DCL [48]

There is no single company in charge of the ledger, and therefore, the data ... Matter devices can, beside others, use the DCL to check device certification compliance status, verify DACs ... Write access to the DCL is restricted to CSA and elected entities, as is documented in Section 4.1.4 and following sections.



](https://nbn-resolving.de/urn:nbn:de:bsz:289-oparu-49010-9#24#5)[

![](https://cdn.deepseek.com/site-icons/ndss-symposium.org)

dev.ndss-symposium.org

Insights from GitHub Community on the Matter Standard: Developer Perspectives and Challenges

Abstract—Matter seeks to resolve long- standing interoperability problems in the Internet of Things (IoT), yet little is known about how developers experience the standard in day- to- day work. This paper examines over 13,000 issues from the official Project CHIP GitHub repository to understand the kinds of problems contributors report when implementing and integrating Matter.



](https://dev.ndss-symposium.org/wp-content/uploads/sdiotsec26-46.pdf#4#1)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

CSA-IOT

2026/06/16

Matter 1.6 Enables More Intuitive Setup, Multi-Ecosystem Experiences, and Context-Driven Control

Matter 1.6 Enables More Intuitive Setup ... Core Enhancements Matter 1.6 brings targeted refinements to device status communication and ecosystem security, improving visibility and trust across connected environments. ... Unmounted State for Smoke and CO Alarms. Alarms are now able to indicate when they have been removed from their installed position ... accurate picture of whether a device is operational. Partitioned Certificate Revocation Lists.



](https://csa-iot.org/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2026/06/17

Matter 1.6 带来更直观的配置、多生态系统体验和基于场景的控制

Matter 1.6 带来更直观的配置、多生态系统体验和基于场景的控制 ... Matter 1.6 引入了基于 NFC 的配置功能，通过允许 Matter 设备在设备完全通电前，就通过双向 NFC 通信进行配置，从而满足这一需求。



](https://matter.cn/5763.html)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

CSA-IOT

2026/06/16

Matter 1.6 Permet une configuration plus intuitive, des expériences multi-écosystèmes et un contrôle contextuel

Matter 1.6 Permet une configuration plus intuitive, des expériences multi-écosystèmes et un contrôle contextuel ... Matter La version 1.6 apporte des améliorations ciblées à la communication de l'état ... État non monté pour les détecteurs de fumée et de CO. Les alarmes



](https://csa-iot.org/fr/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

CSA-IOT

2026/06/16

Matter A versão 1.6 permite uma configuração mais intuitiva, experiências em múltiplos ecossistemas e controle orientado pelo contexto.

Matter A versão 1.6 permite uma configuração mais intuitiva, experiências em múltiplos ecossistemas e controle orientado pelo contexto. ... Matter A versão 1.6 traz melhorias específicas para a comunicação do status do dispositivo e para a segurança do ecossistema, aprimorando a visibilidade e a confiança em ambientes conectados.



](https://csa-iot.org/pt/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/)[

![](https://cdn.deepseek.com/site-icons/cnx-software.com)

CNX Software

2026/06/18

Matter 1.6 specification adds NFC-based commissioning, thermostat suggestions, various core enhancements - CNX Software - Skip to content

Matter 1.6 specification adds NFC-based commissioning, thermostat suggestions, various core enhancements Connectivity Standards Alliance (CSA) has recently released the Matter 1.6 specification with new features such as NFC-based commissioning ... Matter 1.6 has four documents: - Matter 1.6 Core Specification - Matter 1.6 Application Clusters Specification ... - Matter 1.6 Standard Name Space Specification



](https://www.cnx-software.com/2026/06/19/matter-1-6-specification-adds-nfc-based-commissioning-thermostat-suggestions-various-core-enhancements/?noamp=mobile&amp=1#1)[

heise online

2026/06/17

Matter 1.6 makes a new attempt at cross-platform device management - zurück zum Artikel

Matter 1.6 makes a new attempt at cross-platform device management ... Matter 1.6 brings new features for shared device management, NFC setup, and connected thermostats. ... For the first time, Matter 1.6 allows complete commissioning via bidirectional NFC communication. ... Matter 1.6 [2] also brings changes for connected thermostats.



](https://www.heise.de/en/news/Matter-1-6-makes-a-new-attempt-at-cross-platform-device-management-11337186.html?view=print#1)[

![](https://cdn.deepseek.com/site-icons/macrumors.com)

MacRumors

2026/06/16

Matter 1.6 Announced With NFC Setup, Cross-Ecosystem Device Sharing, and Smarter Thermostats - Skip to Content

Matter 1.6 Announced With NFC Setup, Cross-Ecosystem Device Sharing, and Smarter Thermostats ... Matter 1.6 includes NFC-Based Commissioning for setting up light bulbs in ceiling fixtures, in-wall switches, and other products that need to be configured prior to installation. ... and CO and smoke alarms



](https://www.macrumors.com/2026/06/17/matter-1-6-specification/#1)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

Silicon Labs

2026/06/23

Matter 1.6 Spec: Smarter Thermostat Control and More - Silicon Labs

Two of the most significant additions in this Matter release are Thermostat Suggestions ... Matter 1.6 Brings Core Enhancements to Security ... The release also strengthens the Matter security infrastructure through improvements to Certificate Revocation List (CRL) management. Matter 1.6 introduces partitioned CRLs, allowing revocation information to be managed in smaller, independently updated segments rather than as a single large dataset.



](https://www.silabs.com/blog/matter-1-6-spec-smarter-thermostat-control-and-more#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/06/16

Matter updates improve smart-home setup, sharing and security - Advertisement

Other enhancements in Matter 1.6 ... Security sensors gain the ability to share event history across ecosystems. Smoke and CO alarms can flag when someone removes them from their mounting position. ... CSA has released the Matter 1.6 specification and software development kit (SDK) for device makers and platform developers to begin integrating.



](https://tech.yahoo.com/home/articles/matter-updates-improve-smart-home-145041079.html#1)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

CNET

2026/06/17

New Smart Home Update Aims to Simplify Everyday Device Connections - CNET - Skip to content

The standard adds NFC-based commissioning, a setup method that uses near-field communication technology. With NFC ... - Matter 1.6 also adds Thermostat Suggestions, which provides a framework for prioritizing smart thermostat commands and settings. ... - Smart security sensors gain the potential to store event histories, allowing people to see when a sensor was activated and whether it remains active. ... - The new Thread Tools app



](https://www.cnet.com/home/smart-home/new-smart-home-matter-standard-arrives/#1)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/12/22

Samsung SmartThings platforma postaje prva u sektoru koja podržava Matter kamere | Samsung Srbija - Nema predloga

decembar 2025 – Kompanija Samsung Electronics objavila je da njena platforma za pametni dom SmartThings sada podržava globalni standard za pametni dom Matter 1.5 ... video zvona na vratima i drugo.



](https://www.samsung.com/rs/news/local/samsung-smartthings-becomes-the-industrys-first-to-support-matter-cameras/#1)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/12/18

Samsung SmartThings Becomes the Industry’s First To Support Matter Cameras

Samsung Electronics today announced that its smart home platform, SmartThings, now supports Matter 1.5 — the global smart home standard — making it the first in the industry to support Matter-compatible cameras. ... Matter 1.5 supports a wide range of camera use cases including indoor and outdoor security cameras, video doorbells and more.



](https://news.samsung.com/global/samsung-smartthings-becomes-the-industrys-first-to-support-matter-cameras)[

![](https://cdn.deepseek.com/site-icons/samsung.com)

Samsung

2025/12/18

Samsung SmartThings trở thành nền tảng đầu tiên trong ngành hỗ trợ camera Matter - Samsung Newsroom Việt Nam

Samsung Electronics hôm nay công bố nền tảng nhà thông minh SmartThings đã chính thức hỗ trợ Matter 1.5 – tiêu chuẩn nhà thông minh toàn cầu – qua đó trở thành nền tảng đầu tiên trong ngành hỗ trợ camera tương thích Matter.



](https://news.samsung.com/vn/samsung-smartthings-tro-thanh-nen-tang-dau-tien-trong-nganh-ho-tro-camera-matter)[

![](https://cdn.deepseek.com/site-icons/smartthings.com)

SmartThings Blog

2025/12/17

SmartThings Updates Archives - Page 10 of 28 - SmartThings Blog - SmartThings Updates

As the first smart home ecosystem to support Matter 1.5 compatible cameras ... is the first global smart home platform to support Matter-compatible cameras as a fully supported device category ... SmartThings supports 58 Matter device types through the 1.5 specification...



](https://blog.smartthings.com/category/smartthings-updates/page/10/#1)[

![](https://cdn.deepseek.com/site-icons/yna.co.kr)

연합뉴스

2025/12/18

삼성전자 스마트싱스, 글로벌 표준 적용 대상에 카메라 추가 | 연합뉴스

매터 1.5의 카메라 표준은 실내외 보안, 출입문 비디오 도어벨 등 다양한 용도의 카메라를 지원하며 ▲ 라이브 영상 재생 ▲ 양방향 대화 ▲ 모션 감지 알림 ▲ 이벤트 영상 저장 ▲ 팬·틸트·줌 제어 등 다양한 편의 기능을 포함한다.



](https://www.yna.co.kr/view/AKR20251219023300003?input=feed_secretk)[

![](https://cdn.deepseek.com/site-icons/smartthings.com)

SmartThings Blog

The SmartThings Blog - Recent Articles

As the first smart home ecosystem to support Matter 1.5 compatible cameras ... is the first global smart home platform to support Matter-compatible cameras as a fully supported device category ... locks, sensors ... SmartThings supports 58 Matter device types through the 1.5 specification...



](https://blog.smartthings.com/page/2/?post_type=post#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/12/21

Samsung SmartThings gets Matter 1.5 update and it’s good news for your security cameras - Advertisement

Samsung SmartThings now supports Matter 1.5, making the smart home platform an industry first to support Matter-compatible cameras. ... Samsung SmartThings now has Matter 1.5-compatibility which expands its support to more smart home devices outside of just lighting...



](https://tech.yahoo.com/home/articles/samsung-smartthings-gets-matter-1-160000791.html#1)[

![](https://cdn.deepseek.com/site-icons/stuff.tv)

Stuff

2025/12/18

Samsung SmartThings is first to support Matter cameras with 1.5 update | Stuff - Skip to content

Samsung SmartThings is first to support Matter cameras with 1.5 update ... Today the company has announced its SmartThings platform is the first of the leading providers to offer support for Matter 1.5. The Matter 1.5 update is important because



](https://www.stuff.tv/news/samsung-smartthings-matter-1-5-cameras/#1)[

![](https://cdn.deepseek.com/site-icons/sammobile.com)

SamMobile

2025/12/18

SmartThings is the first smart home platform to support Matter cameras

Within a month, Samsung has announced that its smart home platform, SmartThings, now supports Matter 1.5. With this announcement, SmartThings has become the first smart home platform in the world to support Matter 1.5. ... history, live video streaming, motion detection...



](https://www.sammobile.com/news/smartthings-first-smart-home-platform-support-matter-1-5-cameras/)[

![](https://cdn.deepseek.com/site-icons/apple.com)

developer.apple.com

Matter Accessory Best Practices for Apple Home

A Matter device containing one or more Nodes.- Thread Border Router: A Thread Border Router connects a Thread network to other IP-based networks, such as Wi-Fi or Ethernet. More details.- mdns ... 7. Thread Border Router interoperability testing (for Thread Border Router accessories)



](https://developer.apple.com/apple-home/downloads/Matter-Accessory-Best-Practices-for-Apple-Home.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/9to5mac.com)

9to5Mac

2026/08/20

HomeKit Weekly: Homey secures Matter 1.5 certification to expand bridging and energy support - 9to5Mac - HomeKit Weekly: Homey secures Matter 1.5 certification to expand bridging and energy support

What is New in Matter 1.5 for Homey ... - Homey Pro and Homey Pro mini feature built-in Thread Border Routers, while self-hosted instances can integrate Matter over Thread accessories utilizing an available local Thread Border Router network



](https://9to5mac.com/2026/08/21/homekit-weekly-homey-secures-matter-1-5-certification-to-expand-bridging-and-energy-support/?utm_source=dlvr.it&utm_medium=threads#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Developer

2024/10/31

Commissioning Matter Thread Device without Hub - Commissioning Matter Thread Device without Hub

I talked to the engineering team about this and they've confirmed that the system does not currently support this. The devices thread radio does not expose itself as a border router, which means it's not accessible to your app or MatterSupport extension.



](https://developer.apple.com/forums/thread/766729#1)[

ifun.de | Apple-News seit 2001

2026/07/28

Thread für UniFi: Matter-Unterstützung bleibt noch offen | ifun.de - Thread im UniFi-Netzwerk

die Aufgabe des Thread Border Routers. ... Ein Thread Border Router verbindet zunächst nur das Thread-Funknetz mit dem normalen IP-Netzwerk. Ubiquiti hat weder einen integrierten Matter Controller noch eine direkte Anbindung an Apple Home, Google Home oder SmartThings angekündigt.



](https://www.ifun.de/thread-fuer-unifi-matter-unterstuetzung-bleibt-noch-offen-284716/#1)[

Wedbush Securities

2025/12/25

The Great Wall of the Smart Home Falls: Apple, Amazon, and Google Embrace Unified Mesh Standards

the release and widespread adoption of the Matter 1.5 and Thread 1.4 networking standards have effectively unified the once-fragmented ecosystems of the world’s largest tech giants. ... Thread 1.4 solved this by introducing standardized credential sharing, allowing border routers from different manufacturers to merge into a single, robust mesh network for the first time.



](https://investor.wedbush.com/wedbush/article/marketminute-2025-12-26-the-great-wall-of-the-smart-home-falls-apple-amazon-and-google-embrace-unified-mesh-standards#1#1#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

developer.apple.com

Thread Test Plan - User Experience Border Router

Discovery App (Discovery - DNS- SD Browser) on iOS or macOS on the same WiFi network as Thread Border Router.1. ... Add Apple Border Router (BR) (Thread resident) to Apple Home on SSID A.2. Pair Matter Thread accessory in Home App3.



](http://developer.apple.com/apple-home/downloads/Thread-Test-Plan-User-Experience-R1.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/gadgethacks.com)

Gadget Hacks

2026/07/13

Matter Apple Home Problems: What Buyers Actually Encounter in 2026

which Matter version the device requires, whether it communicates over Wi-Fi or Thread, and if Thread, whether the right border router is installed and running current firmware. ... Thread devices need a compatible border router; Wi-Fi devices often depend on a stable 2.4 GHz setup.



](https://apple.gadgethacks.com/news/matter-apple-home-problems-what-buyers-actually-encounter-in-2026/#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

developer.apple.com

Contents

Thread border router. ... - HomePod mini- Apple TV 4K ... Set up Apple Border Router (Thread resident) using Home App to configure the preferred network.<br>2. Set up new Border Router using Third Party App on the same network (Wi-Fi/Ethernet).<br>3. ... Pair Matter Thread accessory in Home App to confirm accessory can join the existing preferred network



](http://developer.apple.com/apple-home/downloads/Thread-Test-Plan-THClient-API-R1.pdf#1#1)[

![](https://cdn.deepseek.com/site-icons/iotforall.com)

IoT For All

2026/06/24

Matter Finally Wrote the Fix. But Will Apple, Google, and Amazon Ship It?

But Will Apple, Google, and Amazon Ship It ... and Google Home all manage the same devices from a single unified state ... A routine built in Google Home can now respond to a door unlocked through Apple Home. ... As of this week, Google Home is still catching up to earlier Matter versions.



](https://newsletter.iotforall.com/p/matter-finally-wrote-the-fix-but-will-apple-google-and-amazon-ship-it)[

![](https://cdn.deepseek.com/site-icons/samsungmagazine.eu)

Samsung Magazine

2026/06/22

The rules of the smart home are changing. Matter 1.6 will ensure simple pairing and end cross-platform chaos - A smart home is supposed to be all about convenience, but the reality is often different – complicated device pairing, switching...

Shared household across Apple, Google and Samsung ... Matter 1.6 introduces the so-called Joint Fabric – shared smart home management across platforms. This will allow systems such as Apple Home, Google Home a SmartThings from Samsung could manage one common environment without the need for repeated setup.



](https://samsungmagazine.eu/en/2026/06/23/meni-se-pravidla-chytre-domacnosti-matter-1-6-zajisti-jednoduche-parovani-a-konec-chaosu-mezi-platformami/#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/06/17

New Smart Home Update Aims to Simplify Everyday Device Connections - Advertisement

an update to the smart home standard that's designed to improve compatibility between devices and platforms such as Apple Home, Google Home and Alexa. ... Similar capabilities have long been available in many manufacturer apps, but Matter could make them more broadly available through platforms such as Google Home.



](https://tech.yahoo.com/home/articles/smart-home-aims-simplify-everyday-001048786.html#1)[

![](https://cdn.deepseek.com/site-icons/techtimes.com)

Tech Times

2026/06/18

Matter 1.6 Fixes Smart Home Setup and Ecosystem Conflicts With NFC and Joint Fabric - Matter 1.6 Fixes Smart Home Setup and Ecosystem Conflicts With NFC and Joint Fabric

As of mid-2026, Google Home is still implementing earlier Matter versions, and platform adoption lags have been the most consistent criticism ... 2022 debut. ... Matter 1.5 added camera support in November 2025; full implementation across all major platforms had not yet occurred at the time of the 1.6 announcement.



](https://www.techtimes.com/articles/318684/20260619/matter-16-fixes-smart-home-setup-ecosystem-conflicts-nfc-joint-fabric.htm#1)[

heise online

2026/06/17

Matter 1.6 makes a new attempt at cross-platform device management - Advertisement

Matter 1.6 brings new features for shared device management, NFC setup, and connected thermostats. ... To this end, the shared management of a smart home by platforms such as Apple Home, Google Home, and Alexa should become significantly easier.



](https://www.heise.de/en/news/Matter-1-6-makes-a-new-attempt-at-cross-platform-device-management-11337186.html#1)[

la-maison-intelligente.fr

2026/07/06

Matter 1.5 et 1.6 en 2026 : ce qui change pour votre maison

ajouter un appareil Matter à un deuxième écosystème (par exemple Google Home ET Apple Home simultanément) devient plus fiable ... - Vous possédez une caméra connectée que vous souhaitez intégrer nativement à Google Home, Apple ... - Google Home ... Si vous utilisez plusieurs écosystèmes (Google Home et Apple Home par exemple) ... tout s'affiche directement dans Google Home...



](https://la-maison-intelligente.fr/blog/matter-1-5-1-6-nouveautes-2026)[

heise online

2026/06/17

Matter 1.6 nimmt neuen Anlauf bei plattformübergreifender Geräteverwaltung

Matter 1.6 bringt neue Funktionen für gemeinsame Geräteverwaltung, NFC-Einrichtung und vernetzte Thermostate. ... Dafür soll die gemeinsame Verwaltung eines Smart Homes durch Plattformen wie Apple Home, Google Home und Alexa deutlich einfacher werden. Möglich machen soll das vor



](https://www.heise.de/news/Matter-1-6-nimmt-neuen-Anlauf-bei-plattformuebergreifender-Geraeteverwaltung-11336903.html?view=print#1)[

![](https://cdn.deepseek.com/site-icons/cnet.com)

N.O.V.A. 3 : premières impressions en vidéo

2026/06/17

Et si tous vos objets connectés parlaient enfin le même langage ?

Matter 1.6 introduit un réseau partagé entre ... L’idée est de mettre en place un seul réseau commun pour plusieurs plateformes comme Apple Home, Google Home, Amazon Alexa et Samsung SmartThings. ... Apple, Google, Amazon, Samsung et d’autres pourraient rejoindre le même système.



](https://fr.cnet.com/objets-connectes/4998/et-si-tous-vos-objets-connectes-parlaient-enfin-le-meme-langage)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon Developers

2026/03/15

What’s New in Alexa-Enabled Smart Home | Alexa Skills Kit

March 2026 - Matter-enabled Echo devices now support the Matter 1.5 protocol. For more details, see Connect Your Device to Alexa with Matter. ... Matter 1.4 protocol, defined by the Connectivity Standards Alliance (CSA). For more details...



](https://www.developer.amazon.com/pt-BR/docs/alexa/smarthome/whats-new.html)[

![](https://cdn.deepseek.com/site-icons/amazon.com)

Amazon Developers

2026/05/12

What’s New in Alexa-Enabled Smart Home | Smart Home

March 2026 - Matter-enabled Echo devices now support the Matter 1.5 protocol. For more details, see Connect Your Device to Alexa with Matter. ... - Matter-enabled Echo devices now support the Matter 1.4 protocol, defined by the Connectivity Standards Alliance (CSA). For more details...



](https://developer.amazon.com/it-IT/docs/alexa/smarthome/whats-new.html)[

![](https://cdn.deepseek.com/site-icons/stuff.tv)

Stuff

2025/11/19

Home security cameras can now work with gear from other brands thanks to this new update | Stuff - Skip to content

The Matter 1.5 smart home software update includes support for in-home cameras, blinds, drapes, garage doors and soil sensors. ... Provided they receive the requisite update, all Matter compatible devices will work with Apple Home, Google Home, Amazon Alexa and Samsung Smart Things without having to comply with those specific company’s standards anymore.



](https://www.stuff.tv/news/matter-1-5-smart-cameras-apple-google-home-alexa-smartthings/#primary#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2025/11/20

Buying security cameras has been a mess - Matter 1.5 may finally clean it up - Advertisement

Adding Matter compatibility for security cameras with the 1.5 update means that your Matter cameras will work across brands and ecosystems, rather than forcing you into a single ecosystem. Matter-certified cameras will work with Apple Home, Google Home, Amazon Alexa, or Samsung SmartThings, rather than with just one of these platforms.



](https://tech.yahoo.com/home/articles/buying-security-cameras-mess-matter-122300691.html#1)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2025/11/19

Camera support could be the boost Matter needs - Skip to main content

you should be able to add any certified camera to your smart home platform of choice, such as Apple Home, Amazon’s Alexa, and Google Home ... The big three — Apple Home, Amazon’s Alexa, and Google Home — have been glacially slow to adopt new Matter device types. ... As for Google Home and Amazon’s Alexa...



](https://www.theverge.com/tech/821707/matter-smart-home-standard-supports-cameras-apple-ring-google-nest?utm_source=flipboard&utm_content=theverge%2Fmagazine%2FSmart+Home#1)[

New Electronics

2025/11/25

Powering the next generation of Smart Homes - New Electronics - Search

Matter 1.5 is the latest version of the Matter smart home interoperability standard ... (CSA) in November 2025. It represents a major functional expansion aimed at improving device compatibility and smart home automation across ecosystems like Apple Home, Google Home, Amazon Alexa, SmartThings, and others.



](https://www.newelectronics.co.uk/content/blogs/powering-the-next-generation-of-smart-homes#1)[

![](https://cdn.deepseek.com/site-icons/tink.de)

tink

2025/11/24

Matter 1.5 mit Kamera-Support & Aus für Google Assistant im März | tink Blog

Die Integration funktioniert über alle Matter-fähigen Plattformen wie Apple Home, Alexa und Google Home hinweg. Die technische Basis bildet WebRTC für das Video-Streaming, wodurch Zwei-Wege-Gespräche und sowohl lokaler als auch Fernzugriff möglich werden. Besonders praktisch...



](https://www.tink.de/blog/matter-1-5-mit-kamera-support-aus-fuer-google-assistant-im-maerz/?utm_source=rss&utm_medium=rss&utm_campaign=matter-1-5-mit-kamera-support-aus-fuer-google-assistant-im-maerz)[

![](https://cdn.deepseek.com/site-icons/punto-informatico.it)

Punto Informatico

2025/11/23

Matter 1.5 supporta videocamere e porte del garage

Amazon e Google non hanno però confermato l’interoperabilità dei rispettivi prodotti. ... Ciò dovrebbe consentire il controllo attraverso qualsiasi piattaforma (Apple Home, Google Home, Amazon Alexa, Samsung SmartThings). ... Apple e Google sono tra i principali sostenitori dello standard, ma nessuna delle tre aziende ha confermato il supporto. Un portavoce di Amazon ha comunicato che non



](https://www.punto-informatico.it/matter-1-5-supporta-videocamere-porte-garage/#pageTop)[

![](https://cdn.deepseek.com/site-icons/nsf.gov)

par.nsf.gov

Based on the integration tests with legacy devices, the results reveal distinct differences in how each brand supports automatio...

Amazon, Apple, and Google do not support creating automation rules directly, as indicated by the lack of native support for such features. However ... In contrast, Samsung supports creating automation rules but requires the use of third- party apps linked through a Samsung account. ... while Apple and Samsung offer some level ... Amazon and Google lack direct mechanisms...



](https://par.nsf.gov/servlets/purl/10618356#2#2)[

![](https://cdn.deepseek.com/site-icons/allion.com.cn)

百佳泰

2024/10/10

Matter智能设备首次配对成功后，却无法操作？！ | 百佳泰 Allion Labs

当用户购入智能家庭装置后，首要的动作就是根据不同的智能家庭平台（Apple Homekit、Amazon Alexa、Google Home和Samsung SmartThings等）进行第一次的配对。以往 ... 由于Matter正处于发展的阶段，可能会因Google Home后台云端部分的更新而解决。



](https://www.allion.com.cn/tech_netc_matter_light_bulb/#1)[

release-assets.githubusercontent.com

Automations — a scene plus a trigger — aren't supported

HomeKit, Google Home and Matter model triggers in three incompatible ways and Matter has none, so there's no honest common shape. ... Everything Matter goes through the operating system's ecosystem, so the Apple Home or Google Home app has to be installed and set up.



](https://release-assets.githubusercontent.com/github-production-release-asset/32973467/996f3e8a-83da-466a-a017-65891c917912?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-08-29T08%3A35%3A45Z&rscd=attachment%3B+filename%3Ddeveloper-guide.pdf&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-08-29T07%3A35%3A10Z&ske=2026-08-29T08%3A35%3A45Z&sks=b&skv=2018-11-09&sig=asAWXz2hIcnxMJHWp7erya7YzKgZcISjWp3z7Q3nDMY%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc4Nzk5MjIzNywibmJmIjoxNzg3OTkwNDM3LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.62q1RtqActSCo0_U718GFMmZxhRPNuaySyuhG997E2A&response-content-disposition=attachment%3B%20filename%3Ddeveloper-guide.pdf&response-content-type=application%2Foctet-stream#123#105)[

![](https://cdn.deepseek.com/site-icons/csdn.net)

CSDN博客

2026/03/01

从发布到落地：Matter 协议三年，平台兼容性如何？ - 从发布到落地：Matter 协议三年，平台兼容性如何？

过去两个月，我把市面上主流支持Matter的平台——Apple Home、Google Home、Amazon Alexa、Samsung SmartThings、Home Assistant——翻来覆去测了一遍，结合一些海外集成商和资深玩家的实测数据，把“兼容性”这个词拆成了三件事 ... 一句话总结：苹果用户闭眼入 ... 两边都能控制，但Google Home这边的自动化触发偶尔会延迟3-5秒，原因不明。



](https://blog.csdn.net/weixin_41937806/article/details/158569812#1)[

Meross

Meross Offical Site, Smart House and Home Automation Device Provider.

For major platforms such as Alexa, Google, Apple, and Samsung, the answer is yes. Alexa echo, Google Nest Home, Apple HomePod mini, SmartThings Hub ... 4) Restart your hubs, such as Apple HomePod mini, Apple TV, Google Nest Hub, or Alexa Echo Dot.



](https://www.meross.com/en-gc/FAQ/558)[

Why Can't My Fibaro Home Center Discover Devices?

2026/03/18

Matter Device Not Pairing — Setup Wizard Fails or Freezes?

Phone drops to cellular mid-commissioning, breaking the WiFi handoff - Matter controller hub offline or in a stale state - Device firmware not yet updated to a Matter-compatible version ... Your Matter-certified device fails to complete commissioning in Apple Home, Google Home, Amazon Alexa, or another Matter controller app. The setup wizard stalls...



](https://www.trunetto.com/troubleshooting/smart-hubs/matter/matter-device-not-pairing-setup-wizard-fails)[

![](https://cdn.deepseek.com/site-icons/csdn.net)

【FreeRTOS 教程 七】互斥锁与递归互斥锁

2026/03/01

从发布到落地：Matter 协议三年，平台兼容性如何？

我把市面上主流支持Matter的平台——Apple Home、Google Home、Amazon Alexa、Samsung SmartThings、Home Assistant——翻来覆去测了一遍 ... 稳定、省心，但Thread网络抽风时很崩溃 ... 一句话总结：苹果用户闭眼入 ... 语音强，自动化弱，Thread网络藏太深 ... 两边都能控制，但Google Home这边的自动化触发偶尔会延迟3-5秒...



](https://aiot.csdn.net/6a7b030b10ee7a33f2997bb4.html)[

![](https://cdn.deepseek.com/site-icons/allion.com.tw)

百佳泰Allion Labs

2024/03/06

Matter (二) 智慧家庭生態系互通行不行 – 多源管理功能實測

多源管理提供蘋果 (Apple)、Google、亞馬遜 (Amazon) 與三星(Samsung) 等生態系統之間實現互通連結，多個用戶可以同時具有操控設備的權限，讓消費者能夠自由選擇生態系，即使家庭成員使用不同生態系的手機應用程式的情況下，也仍能夠分享設備管理權。



](https://www.allion.com.tw/tech_netc_matter_multi-admin/)[

![](https://cdn.deepseek.com/site-icons/matter.cn)

Matter 中文官方网站

2026/06/25

不再是新设备，Matter 1.6 聚焦于让 Matter 不再令人头疼

你不再被锁定在某个专有应用或生态系统中 ... Matter 的多管理员（multi-admin）功能提供了一种解决方案：你可以将一台 Matter 设备从一个设备网络共享到另一个设备网络。但遗憾的是，你必须一台设备一台设备地操作。在我这样的智能家居中（几乎每个灯开关都被我换成了智能开关）...



](https://matter.cn/5886.html)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/05/28

docs-matter/sld296-matter-ecosystems/multicontroller-ecosystem.md at doccurator/2.8.1 · SiliconLabsSoftware/docs-matter - Skip to content

Matter devices can participate in multiple Matter ecosystems simultaneously through a feature called Multi-Admin. Multi-admin ... Any Matter Accessory Devices (MAD) can be shared between two or more Matter fabrics by first commissioning to one Matter fabric and then sharing control of them to other Matter controllers ... - Follow the steps on screen to complete the commissioning.



](https://github.com/SiliconLabsSoftware/docs-matter/blob/doccurator/2.8.1/sld296-matter-ecosystems/multicontroller-ecosystem.md#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/07/30

Multiple Matter Controllers: Fabrics, Multi-Admin, and Local Control

Each platform normally creates and administers its own fabric, and a device joins additional fabrics through Multi-Admin sharing. ... Matter Multi-Admin lets an already commissioned device open a commissioning window for another administrator. ... After Multi-Admin sharing, several platforms can issue supported Matter commands to the same device. ... The CSA describes Multi-Admin



](https://shop.zimaspace.com/blogs/tech-ai-hub/smart-home-server-multiple-matter-controllers#1)[

![](https://cdn.deepseek.com/site-icons/macrumors.com)

MacRumors

2024/11/06

Matter 1.4 Brings Support for New Devices and Easier Integration to Smart Home Setups - Skip to Content

The update also introduces Enhanced Multi-Admin, which allows users to add Matter devices to multiple ecosystems automatically with a single authorization. For example ... Enhanced Multi-Admin achieves this by enabling "Fabric Sync," a system that allows each Matter ecosystem to securely communicate with other ecosystems a user has authorized.



](https://www.macrumors.com/2024/11/07/matter-1-4-finalized/#1)[

![](https://cdn.deepseek.com/site-icons/nsf.gov)

par.nsf.gov

The multi- admin feature of Matter standard allows one device to be shared and controlled by multiple admins, which properly fit...

The multi- admin feature of Matter standard allows one device to be shared and controlled by multiple admins, which properly fits into our design. Targeting partial view and partial control, we present a secure and private approach to enforce policies in a multi- admin Matter smart ... helps avoid device sharing) and preserving home security and user safety in the meantime.



](https://par.nsf.gov/servlets/purl/10516644#3#2)[

![](https://cdn.deepseek.com/site-icons/europapress.es)

Europa Press

2026/06/16

Matter 1.6 mejora la gestión de dispositivos entre ecosistemas en una red compartida - Matter 1.6 mejora la gestión de dispositivos entre ecosistemas en una red compartida

Esta versión profundiza en la función Multi-Admin, ya que ahora permite que varios controladores autorizados administren una única red compartida. Para ello utiliza Joint Fabric para crear 'fabrics' (tejidos ... La especificación 1.4 introdujo la función Multi-Admin basada en el acceso compartido...



](https://www.europapress.es/portaltic/software/noticia-matter-16-mejora-coordinacion-gestion-dispositivos-ecosistemas-red-compartida-20260617162808.html#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Developer

2026/02/10

OTA testing cannot be performed on the test DCL network. - OTA testing cannot be performed on the test DCL network.

Since the beginning of 2026, however, the Home app no longer delivers software update notifications. ... It looks like the TestNet DCL mobile config file (see section "3.2.3. Profile enablement" of Apple Matter OTA - User Guide r4) expired on February 7th, at which point this would have stopped working. .



](https://developer.apple.com/forums/thread/815315#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2025/06/07

Matter Documentation for Firmware Updates · Issue #39431 · home-assistant/home-assistant.io - Skip to content

On the Matter documentation page, it is noted that firmware updates may fail with HomeAssistant Matter Server, and points to Apple border routers as the primary cause of the issue. Specifically, it is noted that Apple border routers fail to forward mDNS packets and this is the primary reason that firmware updates don't work.



](https://github.com/home-assistant/home-assistant.io/issues/39431#1)[

![](https://cdn.deepseek.com/site-icons/apple.com)

Apple Developer

Matter - Matter

With the same firmware, OTA testing on the DCL test network was successful in September 2025, and the Home app was able to deliver software update notifications. Since the beginning of 2026, however, the Home app no longer delivers software update notifications.



](https://developer.apple.com/forums/tags/matter?sortBy=activity&sortOrder=DESC#1)[

![](https://cdn.deepseek.com/site-icons/ndss-symposium.org)

dev.ndss-symposium.org

The Platform & Network category covers issues related to network configuration, commissioning, and integration with platform- sp...

These issues focus on how devices exchange messages and maintain state, including OTA updates ... Developers report unintended commands emitted by bridge applications, timeouts during remote updates, firmware update failures on specific boards, problems with subscription resumption, and initialization bugs, as well as runtime issues such as JNI reference leaks (e.g.



](https://dev.ndss-symposium.org/wp-content/uploads/sdiotsec26-46.pdf#4#3)[

nbn-resolving.de

Checking for updates on a daily basis, as recommended by the specification, is security-wise a good advice, because in practice,...

daily updates are a common trade-off between the desire ... Apart from Matter-specified updates, Matter allows vendor-specific legacy out-of-band methods that in worst case implement no security at all, which can result in compromised firmware. ... The attacker could try to compromise the runtime service discovery, which is used to discover OTA providers, to control which node takes the role of the OTA provider.



](https://nbn-resolving.de/urn:nbn:de:bsz:289-oparu-49010-9#24#18)[

![](https://cdn.deepseek.com/site-icons/silabs.com)

docs.silabs.com

<table><tr><td>ID</td><td>Issue or Limitation Description</td><td>GitHub / Salesforce Reference (if any)</td><td>Workaround (if ...

/Thread ... scratch.</td><td>None. ... <td>Enabling "Logging to RTT" with SiWG917 SoC results in OTA update failure due to JLink connection preventing soft reset.</td><td>None.</td><td>Enabled ... limitation</td><td>SLEXP8022A - WF200 Wi-Fi Expansion Kit</td></tr><tr><td></td><td>The ... <td>OTA Update: sometimes boot loading



](https://docs.silabs.com/sisdk-matter-release-notes/2.7.0/sisdk-matter-release-notes.pdf#2#2)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/02/03

Eve Energy Matter firmware update error - Configuration / Matter/Thread - Home Assistant Community - Load more posts above

Some good news, the new (beta) Matter Server 8.2.0 (with the new matter.js implementation) updated all my eve plugs and ikea sensors without issues. ... If you haven’t yet done so, upgrade your Matter Server to 8.2.2 and switch to beta.



](https://community.home-assistant.io/t/eve-energy-matter-firmware-update-error/878364/30#1)[

![](https://cdn.deepseek.com/site-icons/github.com)

GitHub

2026/05/05

Matter broken after updating to 2026.5.0 · Issue #169938 · home-assistant/core

Matter broken after updating to 2026.5.0 #169938 ... After updating to Core 2026.5.0 most of my Matter devices are unavailable. ### What version of Home Assistant Core has the issue?



](https://github.com/home-assistant/core/issues/169938#13)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/28

Can Home Assistant Keep Local Control During an Outage? - English

Yes, Home Assistant can keep reliable local control during an internet outage, but only for control paths that do not require cloud services. ... Local Protocols Can Keep the Primary Control Path Inside the Home Zigbee, Z-Wave, local Matter or Thread paths, ESPHome, MQTT, and local LAN integrations can exchange device state without traversing the public internet. When the Home Assistant host...



](https://shop.zimaspace.com/blogs/tech-ai-hub/can-home-assistant-keep-reliable-local-control-during-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/yahoo.com)

Yahoo

2026/09/12

Your smart home should survive a Google outage; mine didn't, so I built one that does - Advertisement

Local control was always the point of Matter ... In a Matter home, telling a light to turn on runs over your local network, and you don't need an internet round trip to change the bulb's state. ... Matter has a feature called multi-admin that lets one device belong to several controllers at once.



](https://tech.yahoo.com/home/articles/smart-home-survive-google-outage-121510629.html#1)[

![](https://cdn.deepseek.com/site-icons/theverge.com)

The Verge

2025/01/07

Google Home hubs can now work locally thanks to Matter - Skip to main content

One of the key changes Matter is bringing to the smart home is a standardized way to enable local control of smart devices. This means your light bulb doesn’t have to talk to the cloud when you ask your voice assistant to turn it off. ... This week, Google announced it has added full



](https://on.theverge.com/2025/1/8/24338969/google-home-hubs-local-control-matter#1)[

![](https://cdn.deepseek.com/site-icons/xda-developers.com)

XDA

2026/03/01

I blocked all cloud access from my smart home for a week to see what still works

While some big-name brands failed the test, the move to local mesh protocols and Matter has made the internet optional for a truly smart home. ... Matter 1.4 has drastically improved multi-admin stability, allowing local controllers to stay synced even when offline.



](https://www.xda-developers.com/blocked-all-cloud-access-from-smart-home-for-week-what-still-works/#threads#1)[

![](https://cdn.deepseek.com/site-icons/howtogeek.com)

How-To Geek

2026/09/10

These 5 underrated smart home upgrades keep your lights working when the internet goes down - These 5 underrated smart home upgrades keep your lights working when the internet goes down

Use Matter devices with local control ### Alexa doesn't always need the cloud ... Matter changes this, because commands are designed to travel locally over Wi-Fi or Thread. ... Alexa can communicate with Matter devices locally, allowing supported Alexa-enabled devices to control them even when the internet is down. With supported Echo devices...



](https://www.howtogeek.com/smart-home-upgrades-keep-lights-working-when-internet-goes-down/#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/28

¿Puede Home Assistant mantener el control local durante una interrupción del servicio?

Los protocolos locales pueden mantener la ruta de control principal dentro del hogar Zigbee, Z-Wave, las rutas locales de Matter o Thread, ESPHome, MQTT y las integraciones de LAN locales pueden intercambiar el estado de los dispositivos sin atravesar Internet pública. Cuando el host de Home Assistant...



](https://shop.zimaspace.com/es/blogs/tech-ai-hub/can-home-assistant-keep-reliable-local-control-during-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/hipertextual.com)

Hipertextual

2025/01/07

Olvídate del Wi-Fi: Google Home lanza su actualización más esperada - Saltar al contenido

Google Home lanzó una actualización que añade control local de los dispositivos compatibles con Matter ... Con el control local, si la conexión a internet se interrumpe, las operaciones locales del dispositivo, como controlar las luces a través del Asistente de Google, deberían seguir funcionando.



](https://hipertextual.com/tecnologia/google-home-lanza-su-actualizacion-mas-esperada-wi-fi/#main#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/28

Home Assistant peut-il conserver le contrôle local en cas de panne ? - Prêt à être expédié

Les protocoles locaux peuvent maintenir le chemin de contrôle principal au sein du domicile Zigbee, Z-Wave, les chemins Matter ou Thread locaux, ESPHome, MQTT et les intégrations LAN locales peuvent échanger l’état des appareils sans passer par Internet. Lorsque l’hôte Home Assistant...



](https://shop.zimaspace.com/fr/blogs/tech-ai-hub/can-home-assistant-keep-reliable-local-control-during-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/xda-developers.com)

XDA

2026/09/02

I ditched Tuya's cloud latency for Matter, and my smart home finally responds instantly

If a brand changes its Terms of Service or shuts down its cloud servers, your Matter devices continue working locally on your network forever. ... First, deploy a dedicated Thread border router and Matter controller. ... Connect to ZBT-1 running OpenThread or a Google Nest Hub, and enable the Matter server



](https://www.xda-developers.com/finally-ditched-tuya-for-matter-smart-home-is-finally-fully-local/#1)[

![](https://cdn.deepseek.com/site-icons/zimaspace.com)

Zima Store Online

2026/08/28

Home Assistant può mantenere il controllo locale durante un’interruzione? - Italiano

I protocolli locali possono mantenere il percorso di controllo principale all’interno dell’abitazione Zigbee, Z-Wave, i percorsi Matter o Thread locali, ESPHome, MQTT e le integrazioni LAN locali possono scambiare lo stato dei dispositivi senza passare per Internet. Quando l’host di Home Assistant...



](https://shop.zimaspace.com/it/blogs/tech-ai-hub/can-home-assistant-keep-reliable-local-control-during-internet-outage#1)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

If a Fabric Synchronizing Administrator exposes such names in the Basic Information Cluster for a Synchronized Device, then the ...

a Fabric Synchronizing Administrator ... Changes to the set of Synchronized Devices Matter Devices can be added to or removed from the set of Synchronized Devices through Administrator-specific means. For example, the user can use a Manufacturer-provided app to disable synchronization of specific devices. ... Each Client ecosystem to a Fabric Synchronizing Administrator (possibly ... the client ecosystem’s fabric to commission the Aggregator.



](https://csa-iot.org/wp-content/uploads/2025/01/24-27349-006_Matter-1.4-Core-Specification-1.pdf#160#147)[

Netatmo HelpCenter

2026/01/26

Comment gérer le partage Matter ?

Comment gérer le partage Matter ? Avant de commencer, votre Thermo Hub et votre Thermostat doivent déjà être configurés dans l'application Netatmo. ... Comment ajouter le produit à un autre écosystème Matter sur iOS Ouvrez l'application Apple Home. ... Un volet s'affiche. ... Comment ajouter le produit à un autre écosystème Matter sur Android Ouvrez



](https://helpcenter.netatmo.com/hc/fr/articles/30012191384338-Comment-g%C3%A9rer-le-partage-Matter)[

![](https://cdn.deepseek.com/site-icons/omadanetworks.com)

Omada

2023/02/01

Como adicionar seu dispositivo certificado para Matter a múltiplos controladores - Este site usa cookies

O suporte a múltiplos administradores do Matter permite que seu dispositivo doméstico inteligente compatível com Matter seja controlado por meio de vários aplicativos de terceiros compatíveis com Matter. ... 2. O código de configuração ... 3.Se você já configurou um dispositivo Matter no aplicativo Tapo e deseja adicioná-lo a outros ecossistemas...



](https://www.omadanetworks.com/br/support/faq/3573/#1)[

![](https://cdn.deepseek.com/site-icons/vigi.com)

VIGI

2023/02/01

Как добавить устройство, сертифицированное Matter, к нескольким контроллерам - Как добавить устройство, сертифицированное Matter, к нескольким контроллерам

2. Код настройки Matter можно использовать только для добавления устройства в первую экосистему. ... 3. Если вы уже настроили устройство Matter в приложении Tapo и хотите добавить его в другие экосистемы, перейдите в интерфейс «Привязать к Matter» в приложении Tapo, чтобы сгенерировать новый код...



](https://www.vigi.com/kz/support/faq/3573/#1)[

![](https://cdn.deepseek.com/site-icons/samsungmagazine.eu)

Samsung Magazine

2026/06/22

Reglene for smarthjemmet endrer seg. Matter 1.6 vil sikre enkel paring og få slutt på kaos på tvers av plattformer - Et smarthjem skal visstnok handle om bekvemmelighet, men virkeligheten er ofte annerledes – komplisert enhetsparing, bytting mel...

Matter 1.6 ... Det viktige er det Matter er en global standard, så endringer er ikke begrenset til én region. ... kan det Matter 1.6 reduserer barrieren for å komme inn i smartenhetenes verden betydelig og samtidig endelig koble sammen økosystemer som hittil har operert side om side i stedet for sammen.



](https://samsungmagazine.eu/no/2026/09/18/galaxy-a57-vs-galaxy-s25/#al1#1)[

![](https://cdn.deepseek.com/site-icons/vigi.com)

VIGI

2023/02/01

Matter 인증 장치를 여러 컨트롤러에 등록하는 방법 - Matter 인증 장치를 여러 컨트롤러에 등록하는 방법

Matter의 다중 관리자 지원 기능을 통해 Matter 지원 스마트 홈 기기를 여러 Matter 지원 타사 앱으로 제어할 수 있습니다. 예를 들어 ... 이 문서에서는 연결된 Matter 활성화 기기를 다른 Matter 활성화 타사 앱이나 어시스턴트와 공유하는 방법을 안내합니다. ... 다른 Matter 활성화 타사 앱으로 SmartThings 연결 Matter 기기를 설정하는 방법



](https://www.vigi.com/kr/support/faq/3573/#1)[

Умный дом Aqara

2025/03/16

Matter без границ: Aqara представляет «Расширенный Matter Мост» | Aqara

Эта технология позволяет перенести автоматизации и специфические функции устройств “Aqara” из собственного приложения “Aqara Home” в сторонние экосистемы, такие как “Home Assistant” ... - Выберите «Подключайтесь к экосистемам» → «Matter».



](https://aqara.ru/2025/03/17/matter-%D0%B1%D0%B5%D0%B7-%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%86-aqara-%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D1%82-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD/?srsltid=AfmBOoo4qnIQneXrXPPptlD2p5zINCriyaqLfBmMiS13TSB5X9ULZe2N#respond)[

![](https://cdn.deepseek.com/site-icons/socket.dev)

Socket

2024/12/31

@sammachin/node-red-matter-controller - npm Package Security... - New:Microsoft Teams Notifications Are Now Available in Socket

New:Microsoft Teams Notifications Are Now Available in Socket.Learn more → n # @sammachin/node-red-matter-controller Matter Device Controller for Node-RED latest Scores are not yet available for



](https://socket.dev/npm/package/%40sammachin%2Fnode-red-matter-controller#1)[

![](https://cdn.deepseek.com/site-icons/csa-iot.org)

csa-iot.org

If the fail- safe timer expires prior to activation process completion, the command SHALL respond with TIMEOUT, and the Border R...

If the fail- safe timer expires prior to activation process completion, the command SHALL respond with TIMEOUT, and the Border Router state SHALL revert to the configuration set prior to the failsafe timer being armed ... If the Adjacent Infrastructure Link of the Border Router is connected...



](https://csa-iot.org/wp-content/uploads/2025/08/3-27350_matter-1-4-2-adopted-application-cluster-specification.pdf#103#103)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/01/16

Matter+Thread devices unavailable - Configuration / Matter/Thread - Home Assistant Community - Load more posts above

I couldn’t revive my old network. I recreated everything. In theopenthread/border-router Docker image I ran this to recreate the network. ... > ifconfig up ... If you are running the OTBR as an addon in HA, then the ports are disabled by default and you need to set both to active in the configuration and then restart the addon.



](https://community.home-assistant.io/t/matter-thread-devices-unavailable/971940/15#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/04/21

"Your device requires a Thread border router" << I have a ZBT-1 configured for Thread - Configuration / Matter/Thread - Home Assistant Community - post by jamespetts on Jul 22, 2025

“Your device requires a Thread border router. Connect your border router, then try setting up your device.” ... What finally solved it was doing the following in the Home Assistant Companion App: Settings → Companion App → Troubleshooting → Sync Thread credentials After doing that, pairing worked immediately.



](https://community.home-assistant.io/t/your-device-requires-a-thread-border-router-i-have-a-zbt-1-configured-for-thread/913245/12#1)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2024/04/12

Your device requires a Thread border router - Nordic Case Info

Your device requires a Thread border router I am developing a Matter device using the nRF 5340 DK. ... The first thing I did was factory reset the Smartthings hub. ... - have you tried holding down the "reset device" button on the DK board until all LEDs blink multiple times?



](https://devzone.nordicsemi.com/f/nordic-q-a/110199/your-device-requires-a-thread-border-router?ReplySortBy=Votes&ReplySortOrder=Descending#1)[

Why Can't My Fibaro Home Center Discover Devices?

2026/03/18

Thread Border Router Not Detected During Matter Device Setup?

No Thread border router installed on the network - Border router is a model/generation without Thread support - Border router on a different network segment than the controller ... Confirming the border router shows Connected in the controller's ... Restart border router and Matter controller stack Reboot the border router first, then restart the controller app/hub ... and retry commissioning



](https://www.trunetto.com/troubleshooting/smart-hubs/matter/thread-border-router-not-detected-matter-setup)[

![](https://cdn.deepseek.com/site-icons/nordicsemi.com)

Nordic DevZone

2025/06/29

A question about matter over thread products - Attachments (0)

Light Switch needs the IPv6 address of the Light Bulb, which is stored in the SRP Server. When the Thread Border Router is down, binding will not work. Another option would be to have an SRP server on some embedded device, though this is not usual practice.



](https://devzone.nordicsemi.com/f/nordic-q-a/122610/a-question-about-matter-over-thread-products/541035?ReplyOffsetId=543243&ReplyOffsetDirection=Next&ReplySortBy=Votes&ReplySortOrder=Descending#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/09/13

SLZB on-device OTBR + HA: Thread nodes unreachable (ENETUNREACH) — stale OMR prefix in RAs [solved] - Configuration / Matter/Thread - Home Assistant Community - post by TomasJirku on Jul 31

If you run a SMLIGHT SLZB coordinator in the experimental “Thread+OTBR running on device” mode and your Matter-over-Thread devices randomly fail to commission (Android says “Device requires a Thread border router” ... Step 1 — check the routing table on the HA host...



](https://community.home-assistant.io/t/slzb-on-device-otbr-ha-thread-nodes-unreachable-enetunreach-stale-omr-prefix-in-ras-solved/1019472/2#1)[

![](https://cdn.deepseek.com/site-icons/home-assistant.io)

Home Assistant Community

2026/01/10

OpenThread Border Router and SONOFF MG24 with Docker compose will not start - Configuration / Matter/Thread - Home Assistant Community - post by JBS on Dec 22, 2025

I have managed to integrate both the matter-server and the open thread border router to HA ... I added a new Matter device yesterday and noticed that the HA app, at this step, once again searched for the wrong Thread network. ... but after running the Thread authorization sync again, the HA app did search for the correct Thread network and adding the new Matter device worked as well.



](https://community.home-assistant.io/t/openthread-border-router-and-sonoff-mg24-with-docker-compose-will-not-start/965502/5#1)[

![](https://cdn.deepseek.com/site-icons/homey.app)

Homey Community Forum

2026/01/10

Zwave vs. Matter/Thread

experience has been quite the opposite. My Matter-over-Thread devices have proven to be very reliable. ... In contrast, I experienced more issues with Zigbee devices on Hubitat. Even mains-powered devices occasionally went offline, including devices installed in wall boxes, which then required re-pairing.



](https://community.homey.app/t/zwave-vs-matter-thread/149006/7)[

![](https://cdn.deepseek.com/site-icons/ifsp.edu.br)

repositorio.ifsp.edu.br

A funcionalidade ampliada do Matter está diretamente relacionada à sua capacidade de integrar diferentes redes em um mesmo ambie...

Análises de desempenho revelam que o Matter apresenta overhead superior a Zigbee e Z-Wave ... latências inferiores a 200 ms mesmo em cenários de grande escala, destacando sua confiabilidade (MADADI BAROUGH et al., 2024...



](https://repositorio.ifsp.edu.br/server/api/core/bitstreams/cf672b10-7ee3-4156-ae7b-77cab934d75f/content#7#3)[

KontraNet IoT Hub

2026/06/02

Matter 1.4 vs Zigbee vs Z-Wave: Best Smart Home Protocol for US Homes in 2026 - KontraNet IoT Hub

Door locks + security system | Z-Wave Long Range 800 | 1-mile range ... We tested Matter 1.4, Zigbee 3.0, and Z-Wave LR on real US hardware across 3 sites ... - Battery life: CR2032 sensor lifespan in months ... Test Results: - Latency: 0.3s average on Thread. ... The catch: You still need IPv6. ... 3.1 years tested on CR2032. ... leak | Zigbee or Z-Wave LR | 2-5 year battery life vs 8-14 months on Matter



](https://kontranet.com/smart-home/best-smart-home-protocol-for-us-homes/#Best_smart_home_protocol_for_US_homes)[

Botmonster Tech

2026/06/09

Zigbee vs Z-Wave vs Matter vs Thread: what Reddit says in 2026

The highest-upvoted owners rate Z-Wave the most reliable ... - Reddit’s hands-on crowd rates Z-Wave the most reliable of the four in 2026. ... The most-upvoted hands-on cohorts put it roughly Z-Wave first, Zigbee second, and Matter-over-Thread last.



](https://botmonster.com/smart-home/zigbee-zwave-matter-thread-reddit-2026/)[

teko.ch

Zigbee unterstützt die folgenden ISO-Standards:

• ISO 33000-3 ... • ISO 33000-4: Interoperabilität ... Zuverlässigkeit ... Zigbee und Z-Wave sind jeweils zuverlässig und stabil, wobei Zigbee stromsparender ist und Z-Wave eine grössere Reichweite hat. Die beste Wahl für Geräte...



](https://www.teko.ch/diplomarbeit-assets/olten/4473676-654b8ea56df65/file_654b9d67e373d.pdf#10#3)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2025/05/24

Is it finally time to embrace Matter? < Hint NOT! - Lounge - Hubitat - Load more posts above

Toss in lots of recent reboots and updates during the Beta, and Matter over Wifi is more stable then Zigbee or Zwave at this point (To be fair, there was lots of changes in my Zwave mesh due to adds/removes around Zwave LR...



](https://community.hubitat.com/t/is-it-finally-time-to-embrace-matter-hint-not/134360/107#1)[

![](https://cdn.deepseek.com/site-icons/hubitat.com)

Hubitat

2026/06/05

What do I need at Ikea? - Lounge - Hubitat - Load more posts above

Reading through the last 100 or so posts have convinced me that my rock solid zigbee, z-wave and some local WiFi devices are not going to be joined by matter anytime soon. ... But there are certainly times that Zigbee and/or ZWave+ haven’t felt so rock solid.



](https://community.hubitat.com/t/what-do-i-need-at-ikea/158182/307#1)[

nexttechbuy.com

2026/03/10

Ultimate Smart Home Device Comparison Guide 2026

Zigbee and Z-Wave mesh networks significantly outperform WiFi for reliability in larger homes, while the emerging Matter standard finally delivers on cross-



](https://nexttechbuy.com/smart-home-device-comparison-guide-2026/#respond)