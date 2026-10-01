# What Works Together: Language Pairings for Product Creation

A practical guide to which programming languages complement each other when building products, and why.

---

## Web Applications

| Pairing | Why It Works |
|---------|-------------|
| **TypeScript + Python** | TypeScript handles the frontend (React, Vue, Angular) with type safety; Python powers the backend (FastAPI, Django) with rapid development and rich data libraries. |
| **TypeScript + Go** | TypeScript for the UI; Go for high-performance backend services, APIs, and microservices with low memory footprint. |
| **JavaScript + Rust (WASM)** | JavaScript orchestrates the app; Rust compiled to WebAssembly handles performance-critical browser tasks (image processing, games, crypto). |
| **TypeScript + SQL** | TypeScript for application logic; SQL (via ORMs like Prisma or Drizzle) for type-safe database queries that catch errors at compile time. |

---

## Data & AI Products

| Pairing | Why It Works |
|---------|-------------|
| **Python + SQL** | Python (pandas, Polars) for transformation and analysis; SQL for storage and retrieval. Together they cover the full data pipeline. |
| **Python + Julia** | Python for orchestration, ML frameworks, and ecosystem; Julia for high-performance numerical computing and simulations. |
| **Python + C++** | Python for prototyping and ML (PyTorch, TensorFlow); C++ for performance-critical inference engines and custom operators. |
| **R + Python** | R for statistical analysis and visualization (ggplot2); Python for production deployment, web services, and general-purpose engineering. |
| **JAX + Python** | JAX for composable function transformations and GPU/TPU acceleration; Python for the surrounding ML infrastructure. |

---

| Pairing | Why It Works |
|---------|-------------|
| **Kotlin + Swift** | Kotlin for Android; Swift for iOS. Both are modern, safe, and expressive. Shared business logic can use Kotlin Multiplatform. |
| **Dart (Flutter) + Native** | Dart/Flutter for cross-platform UI; platform-specific Kotlin/Swift for native integrations (camera, Bluetooth, etc.). |
| **Rust + Kotlin/Swift** | Rust shared core compiled to native libraries for both platforms; Kotlin/Swift for UI and platform APIs. |
| **C# + .NET MAUI** | C# across mobile and desktop with .NET MAUI; single codebase targeting iOS, Android, macOS, and Windows. |

---

## Systems & Infrastructure

| Pairing | Why It Works |
|---------|-------------|
| **Go + Python** | Go for infrastructure tools, CLIs, and network services; Python for automation scripts, data processing, and glue code. |
| **Rust + Go** | Rust for performance-critical systems (databases, OS components); Go for cloud-native tooling, APIs, and DevOps. |
| **Bash + Python** | Bash for simple system tasks and CI/CD pipelines; Python for complex automation, testing, and tooling. |
| **Terraform (HCL) + Python** | HCL for declarative infrastructure; Python for custom providers, pre/post-processing, and testing with pytest. |
| **YAML/JSON + Go** | YAML/JSON for configuration and manifests; Go for the tools that consume and validate them (Kubernetes ecosystem). |

---

## Desktop Applications

| Pairing | Why It Works |
|---------|-------------|
| **TypeScript + Electron** | TypeScript for both main and renderer processes; Electron for cross-platform desktop with web technologies. |
| **C# + WPF/WinUI** | C# with XAML-based frameworks for rich Windows desktop applications. |
| **Rust + Tauri** | Rust for the backend logic; web technologies (HTML/CSS/JS) for the UI. Lighter and more secure than Electron. |
| **Python + Qt (PyQt/PySide)** | Python for application logic; Qt for cross-platform native-looking desktop UIs. |
| **Swift + SwiftUI** | Swift with SwiftUI for modern, declarative macOS and iOS applications. |

---

## Game Development

| Pairing | Why It Works |
|---------|-------------|
| **C++ + Lua** | C++ for the engine core; Lua for game scripting, modding, and rapid iteration without recompilation. |
| **C# + Unity** | C# is Unity's primary language; the engine handles rendering, physics, and cross-platform deployment. |
| **Rust + WASM** | Rust for game logic compiled to WebAssembly; runs in browsers with near-native performance. |
| **GDScript + C#** | GDScript for rapid prototyping in Godot; C# for performance-critical modules. |

---

## Embedded & IoT

| Pairing | Why It Works |
|---------|-------------|
| **C + Python** | C for firmware and real-time constraints; Python for testing, tooling, and host-side applications. |
| **Rust + C** | Rust for safe systems programming with modern tooling; C for legacy driver compatibility and existing ecosystems. |
| **MicroPython + C** | MicroPython for rapid embedded prototyping on microcontrollers; C for performance-critical drivers. |
| **Zephyr (C) + Python** | C for the RTOS and device drivers; Python for device management, testing, and cloud connectivity scripts. |

---

## Cross-Cutting Patterns

### The "Glue + Engine" Pattern
A high-level language (Python, TypeScript, Ruby) acts as glue, orchestrating components written in a lower-level language (Rust, C++, Go). This is the most common and productive pairing in modern software.

### The "Shared Core" Pattern
Business logic is written once in a portable language (Rust, Kotlin, C#) and compiled to multiple targets, with thin native UIs on each platform.

### The "Scriptable Extensible" Pattern
A performant core (C++, Rust, Go) exposes a scripting interface (Lua, Python, JavaScript) allowing users and developers to extend the product without modifying the core.

---

## Choosing a Pairing: Decision Factors

1. **Team expertise** — A language your team knows well beats a "better" language they don't.
2. **Ecosystem fit** — Libraries and frameworks matter more than language features.
3. **Performance requirements** — Most products don't need systems languages; start high-level and optimize hot paths.
4. **Hiring pool** — Consider the availability of developers for long-term maintenance.
5. **Interop cost** — Some pairings have excellent FFI (Python-C, Rust-Any); others require serialization overhead.

---

## Summary

The most productive pairings in 2026 follow a consistent pattern: **a productive high-level language for the majority of the code, paired with a performant low-level language for the critical 5-10% that needs it.** The specific choice depends on domain, team, and ecosystem, but the architectural pattern is universal.
