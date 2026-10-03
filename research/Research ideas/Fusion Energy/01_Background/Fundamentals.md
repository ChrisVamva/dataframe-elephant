# Fusion Fundamentals

_State as of 2026-10-02. Citations refer to `../06_Evidence/Sources.md`._

## What fusion is

Fusion combines light nuclei into heavier ones, releasing energy from the mass defect (E = mc²). Net-energy fusion requires extreme temperature because nuclei repel each other (Coulomb barrier); at reactor conditions matter is a plasma — an ionized gas confined away from material walls.

## Fuel cycles

| Cycle | Fuel | Notes |
|-------|------|-------|
| **D–T** | deuterium + tritium | Easiest ignition (highest cross-section at lowest temperature); the cycle used by essentially all current reactor designs. Drawback: tritium does not occur in nature — must be bred from lithium in the plant (see Challenges) [S49] [S12]. |
| **D–D** | deuterium only | Abundant fuel, but requires higher conditions and produces tritium/neutrons anyway. |
| **D–³He, p–¹¹B** | aneutronic ambitions | Fewer/neutrons, direct-conversion potential (TAE pursues p–¹¹B; Helion D–³He) — but far harder conditions; both companies currently operate on D–T or precursor fuels [S25] [S26]. |

## Key metrics

- **Q (target gain vs wall-plug gain)** — Q = fusion power out ÷ heating power in. Two critically different definitions:
  - *Scientific / target gain*: fusion energy ÷ energy delivered to the fuel or plasma. NIF's Apr 2025 record: 8.6 MJ out / 2.08 MJ laser in = gain 4.13 [S01].
  - *Wall-plug / engineering gain*: fusion out ÷ electricity drawn by the whole facility. NIF's wall-plug gain is ~0.008 — the lasers draw ~300+ MJ of electricity per ~2 MJ shot and fire about once per day [S03]. A power plant needs total gain ≈ 100× (target gain × driver efficiency × thermal-to-electric efficiency × availability) [S03].
  - For magnetic confinement, Q_plasma ≳ 10–30 is the commonly cited requirement for a competitive plant (SPARC targets Q>1 as a milestone; ARC and ITER target Q≈10+) [S13].
- **Triple product (n·T·τ_E)** — density × temperature × energy-confinement time; the standard single-number yardstick for comparing confinement approaches. W7-X holds the long-pulse stellarator record [S08].
- **Ignition** — self-sustaining burn where alpha-particle heating dominates over external heating. Only NIF has demonstrated it [S01].
- **Lawson criterion** — the temperature/density/confinement-time threshold for net energy; the reason approaches trade off differently (e.g., ICF reaches enormous density, magnetic confinement enormous confinement time).

## What NIF's ignition did and did not demonstrate

- **Demonstrated**: ignition physics, target gains up to 4.13, repeat capability (11 ignitions by mid-2026) [S01].
- **Not demonstrated**: wall-plug breakeven (gain is ~190× short), rep-rate (plant needs ~shots/second; NIF fires ~daily), durable low-cost target manufacturing, tritium breeding — inertial fusion energy (IFE) is a separate R&D program (DOE's $42M STARFIRE hub et al.) [S01] [S03].

## Open background questions

- Why the triple product (rather than Q alone) is the right cross-approach yardstick.
- How much of the tokamak database transfers to stellarators and alternates.
