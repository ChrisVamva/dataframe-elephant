# The Two Gains: 4.13 vs 0.008 — How NIF Can Be Both a Triumph and 100× Short of a Power Plant

On December 5, 2022, the National Ignition Facility fired 2.05 megajoules of laser light into a peppercorn-sized capsule of frozen hydrogen, and got 3.15 megajoules of fusion energy back out. It was the first time in history that a fusion experiment released more energy from its fuel than was delivered to that fuel, and the announcement dominated the news cycle. Headlines said fusion had achieved "ignition." Some said "breakthrough." A few, carelessly, said "breakeven."

Three and a half years later, NIF has now achieved ignition eleven times, and the all-time record has climbed to 8.6 megajoules out from 2.08 megajoules of laser light in — a gain of 4.13, set on April 7, 2025. That is a genuine scientific triumph, verified shot by shot on Lawrence Livermore's own milestone records.

It is also true that on the accounting that decides whether a machine can generate electricity, NIF's gain is about 0.008.

Both of those numbers describe the same machine, on some of the same shots. Neither is a lie. The gap between them — a factor of roughly 500 in how you count the energy — is the entire engineering story of inertial fusion, and the reason a working fusion power plant is still a separate research program rather than a construction project. This article climbs the ladder from one number to the other, because almost every fusion headline you read silently chooses which of the two gains it is quoting.

---

## The first gain: what NIF actually demonstrated

Start with what the record shots measured, because the achievement is real.

The yardstick NIF broke is called *scientific gain*, or *target gain*: the fusion energy coming out of the fuel capsule, divided by the laser energy arriving at it. The progression, all verified via LLNL's published shot records:

| Date | Fusion output | Laser input | Target gain |
|------|--------------|-------------|-------------|
| Dec 5, 2022 | 3.15 MJ | 2.05 MJ | ≈ 1.5 (first ignition) |
| Jul 30, 2023 | 3.88 MJ | — | — |
| Feb 12, 2024 | 5.2 MJ | — | ≈ 2.4 |
| **Apr 7, 2025** | **8.6 MJ** | **2.08 MJ** | **4.13 (all-time record)** |
| Jun 20, 2026 | 7.9 MJ | — | ≈ 3.8 (11th ignition) |

"Ignition" has a precise meaning here: the burn becomes self-sustaining, with the helium nuclei produced by fusion — the alpha particles — depositing enough heat in the fuel to dominate the external heating. The fusion drives itself. NIF is still the only facility anywhere that has demonstrated it.

And it isn't a fluke. Eleven ignitions by mid-2026 means the physics is repeatable — you can build the target, tune the laser, and make the capsule burn on demand, more often than not. When the April 2025 shot nearly tripled the output of that first December breakthrough while using roughly the same laser energy, it demonstrated that the design space has room in it: better targets and better tuning buy real gain.

**The takeaway so far:** the plasma physics question that NIF was built to answer — can a fuel capsule ignite in the laboratory? — is answered, repeatably, with a growing margin. That is what 4.13 means.

---

## The second gain: the number the power grid sees

Target gain divides fusion output by the energy that arrived at the target. It is silent about where that energy came from — and getting 2.08 megajoules of laser light onto a capsule is spectacularly expensive in electricity.

NIF's lasers are about 0.5% efficient at converting electricity into laser light. To deliver roughly 2 megajoules onto the target, the facility draws more than 300 megajoules of electricity from the grid — the better part of a hundred kilowatt-hours, a few days of an average household's consumption, spent in an instant — for each shot.

Now do the same division as before, but with electricity as the denominator. On the first ignition shot in December 2022: 3.15 megajoules out, more than 300 megajoules in. That is the second number, the *wall-plug gain* (sometimes called *engineering gain*): about 0.008 — under one percent. On the April 2025 record shot the picture is somewhat better — 8.6 megajoules out against the same few hundred megajoules in, about three times higher, near 0.02 — but the conclusion doesn't move: on the accounting a power company would use, NIF remains on the order of a hundred times short of merely breaking even, before generating a single sellable watt.

This is not an accounting trick designed to diminish the result. The two gains measure two different things, and both are legitimate:

- **Target gain** asks: *does the plasma physics work?* Answer: yes, ignition, gain 4.13, repeatably.
- **Wall-plug gain** asks: *does the machine produce more electricity than it consumes?* Answer: not within two orders of magnitude.

The trap is that "gain" and "breakeven" get used interchangeably in coverage, when they live on opposite sides of a factor of ~500. When a headline says NIF "got more energy out than in," the true statement is "more energy out of the fuel than the laser put into the fuel" — a statement that says nothing about the wall socket.

**The takeaway:** the 0.008 is not a failure of NIF; it was never designed to be a power plant. It is the distance between a physics demonstrator and a power plant, expressed as a single number.

---

## What a plant would actually need: the ~100× rule

If target gain 4.13 is a triumph and wall-plug gain is ~0.008, what number does a *power plant* need?

The requirement is a chain of multiplications, not a single ratio. A useful rule of thumb from fusion plant analyses: total plant gain — target gain, times driver efficiency, times thermal-to-electric conversion efficiency, times plant availability — needs to come out roughly a hundred times above where NIF's demonstrated performance sits today. With laser efficiency at ~0.5%, that means target gains in the hundreds, shots delivering on the order of a hundred times NIF's record output — not 8.6 megajoules, but hundreds of them, every shot, forever.

And gain isn't even the hardest part. Three more requirements sit behind it, none of which NIF addresses, because it was built as a physics machine:

**Repetition rate.** NIF fires about once per day. A plant needs its driver pulsing on the order of *once per second* — tens of millions of shots a year. The laser system, the optics, the target injection, and the chamber that must absorb the blast all have to survive that cadence for decades. Nothing on Earth has demonstrated anything close to it at ignition-relevant energies.

**Target manufacturing.** Each ignition requires a near-perfect, millimeter-scale cryogenic capsule. A plant consumes them like ammunition. Mass-producing such targets at low cost is its own industrial discipline — as undeveloped as the rep-rate lasers.

**The tritium problem, unchanged.** Every D–T fusion plant, laser or magnetic, must breed its own tritium fuel from lithium inside the plant, and no integrated breeding blanket has ever operated in a fusion neutron environment. That constraint is identical for every approach on Earth, and a triumph of target gain does not exempt a machine from it.

This is why, a year after the first ignition was digested, the US Department of Energy did something telling: in December 2023 it created inertial fusion *energy* hubs — $42 million for the STARFIRE collaboration and others — aimed precisely at the pieces NIF doesn't touch: efficient lasers, roughly hertz-scale repetition rates, and mass target manufacturing. The gesture concedes the argument. Ignition is solved; the power plant is a separate program.

The private sector is working the same gap. Xcimer Energy switched on Phoenix, a laser it bills as the world's largest private laser, in June 2026 and says it passed a DOE preconceptual design milestone for its Athena plant concept — both company claims, not independently verified. First Light Fusion abandoned its projectile-compression approach entirely in 2025, pivoting to a high-gain laser concept (FLARE) and tritium-breeding work while financially strained. The pattern in both cases: everyone building toward inertial *energy* is building toward the ~100×, not celebrating the 4.13.

**The takeaway:** "ignition demonstrated" and "plant feasible" are separated by three engineering Grand Canyons — gain, rep-rate, target cost — plus the tritium cycle every approach shares. The 4.13 is the ticket to attempt the crossing, not the crossing.

---

## The same trap, magnetic edition

If you think the two-gains confusion is a laser-fusion quirk, look at the magnetic-confinement side of the field, because the identical rhetorical move happens there with a different letter.

Magnetic machines quote Q: fusion power out divided by heating power delivered to the plasma — the tokamak's version of target gain. JET — the record-holder, now in decommissioning — finished its final deuterium–tritium campaign in 2023 with 69 megajoules over five seconds and Q ≈ 0.33. The commonly cited bar for a *competitive* magnetic power plant is Q_plasma of roughly 10–30, because a plant must pump its own magnets, cryogenics, and fuel systems — the magnetic sibling of NIF's 300 megajoules of laser electricity, usually called recirculating power.

So when you read that SPARC targets Q > 1, or ITER targets Q = 10, you are reading target-gain-family numbers: physics milestones on the way to a machine whose *net* electricity is a further engineering step beyond. The scale is less brutal than the laser case — the factor-of-500 cliff is a NIF-specific consequence of ~0.5%-efficient lasers — but the structure of the confusion is identical. Plasma-gain milestones get covered as if they were plant milestones.

**The takeaway:** every confinement approach has two numbers — one for the plasma, one for the wall plug — and public coverage almost always quotes the flattering one. Learn to ask *which denominator* and fusion headlines become roughly 500 times less confusing.

---

## What we don't know

The figures here are as strong as fusion data gets — the ignition shots and record yields are verified primary sources from LLNL — but several load-bearing numbers deserve their asterisks:

- The **~0.008 wall-plug gain** is anchored to the December 2022 first ignition shot (scope note on M006); the April 2025 record shot's wall-plug figure works out to roughly 0.02 — about three times better, since laser energy and efficiency barely changed. Both are far from breakeven, but the headline 0.008 is the first shot's number, not the record's.
- The **~300+ MJ electricity per shot** and **~0.5% laser efficiency** are secondary-source figures (fusionbenchmark.com, citing LLNL and peer-reviewed work), not numbers LLNL publishes as a headline metric.
- The **~100× total-gain rule** is a rule of thumb from plant analyses, not a design specification; the exact multiple depends on driver efficiency and conversion assumptions that vary by concept.
- **Records move.** The eleven-ignition count and the 8.6 MJ record reflect the dataset's snapshot (October 2, 2026); NIF's milestone page is the live authority, and the twelfth ignition may already have happened by the time you read this.
- The **private-sector claims** (Xcimer's Phoenix and Athena milestone) are company statements without independent verification, and First Light's pivot was reported while the company was under financial strain.

---

## The number to remember

**Two numbers, one machine.** Target gain 4.13: the physics is solved, repeatably, with margin — a genuine, verified, historically singular achievement. Wall-plug gain ~0.008: as a power plant, NIF is on the order of a hundred times short of breaking even, fires once a day instead of once a second, and breeds none of its own tritium.

Neither number is wrong, and the tension between them is not a scandal. It is the normal shape of progress in a field where the science and the engineering are separated by decades: NIF was built to answer a plasma question, and it answered it. The machines that follow — DOE's IFE hubs, Xcimer's lasers, whatever replaces First Light's abandoned projectiles — exist to answer the wall-plug question.

The next time a fusion headline quotes a gain, the only follow-up question that matters is: *gain over what?* The answer is either a milestone or a power plant. Confusing the two is how a December 2022 physics triumph became, in the retelling, a power plant that doesn't exist.

---

## Appendix: Sources & Methods

**Status:** Edited draft (editor pass 2026-10-03)
**Snapshot date:** October 2, 2026 (Fusion Energy Stage 2 extraction)
**Intended reader:** Science-curious general readers and energy journalists
**Update triggers:** New NIF ignition shots or record yields; any LLNL revision of wall-plug figures; DOE IFE hub results; independent verification or refutation of Xcimer claims; First Light funding developments

This article is grounded in the Fusion Energy research corpus (Stage 1 survey, promoted to Stage 2 on 2026-10-02), extracted as 66 claims, 78 metrics, 67 entities, and 51 sources with evidence classes assigned per claim. Key anchors:

| Statement in article | Evidence anchor | Class / confidence |
|---|---|---|
| Ignition shots, dates, yields; gain 4.13 record (Apr 7, 2025); 11 ignitions by mid-2026 | C001, C002, M001–M004; S01 (LLNL) | documented fact / high |
| Wall-plug gain ~0.008; lasers draw ~300+ MJ/shot; ~1 shot/day | C003, M005–M006; S03 | documented fact / medium |
| Laser wall-plug efficiency ~0.5% | M007; S01, S03 | documented fact / medium |
| ~100× total gain required for a plant; product chain (gain × driver efficiency × conversion × availability) | M008; S03 | documented fact / medium (rule of thumb) |
| Ignition definition (self-sustaining alpha-heated burn); target vs wall-plug gain boundaries | E007, E008, E010 | concept definitions |
| Plant needs ~shots/second; target manufacturing unsolved; DOE IFE hubs $42M (STARFIRE, Dec 2023) | C066, M031; S01, S22 | documented fact / medium |
| Xcimer "Phoenix" laser and Athena DOE milestone | C038, E043–E044; S43 | reported signal / low (company claims) |
| First Light Fusion pivot to FLARE, financial strain | C039, M049; S47 | reported signal / low |
| JET 69 MJ, Q ≈ 0.33, decommissioned; competitive Q_plasma 10–30 | C004–C005, M010–M011, M009; S04, S13 | documented fact / high–medium |
| No integrated tritium breeding blanket ever operated | C041, E064; S49, S12 | documented fact / high |

Verification note: values were cross-checked between the Stage 1 notes (`01_Background/Fundamentals.md`, `02_Approaches/ICF.md`) and the Stage 2 metric table at extraction time; the wall-plug figure's anchoring to the December 2022 shot (scope note on M006) is disclosed in "What we don't know." The Stage 1 gate caveat applies to this article's tables: fusion records move — re-verify NIF's milestone page before publication.
