# Component values, footprints and assembly selection

The schematic and PCB contain parts chosen to obtain a suitable **footprint, schematic symbol or 3D CAD model**. A placeholder may have the correct package but the wrong resistance, power rating, voltage rating, product description or manufacturer part number. A familiar package name is not a component specification.

The native files are published as saved, including this metadata. This repository does not silently rewrite their values or imply that every catalog field is correct.

## Confirmed examples

| References | Metadata retained in CAD | Intended selection or disposition from the design discussions |
| --- | --- | --- |
| R1, R3, R5, R7, R9, R11 | RT0805DRD0775RL; 75 Ω, 0.125 W, 0805 | Rail preload: **2 kΩ, 0.5 W**, ERJ-P06F2001V in the earlier commissioning selection. Verify the final rail load and dissipation. |
| R2, R4, R6, R8, R10, R12 | AC2512JK-0739KL; 39 kΩ, 1 W, 2512 | Gate resistor: **10 Ω, 1 W**, AC2512FK-0710RL as a commissioning starting point. Tune with the actual transistor and switching measurements. |
| U7 | SN74AHCT244QDWR | Earlier procurement selection is SN74AHCT244DWR, DW SOIC-20. Confirm pinout, operating range and footprint for the actual ordered part. |
| D1–D6 | MMSZ5245CT1G, nominal 15 V rail Zener | Earlier procurement proposed MMSZ5248CT1G, nominal 18 V, as a **test candidate**, initially DNP. Neither nominal voltage establishes a safe gate-voltage ceiling. Population remains a qualification decision. |
| J1/J2/J3, J8/J9/J11–J14, EN1–EN6 | Several symbols retain 2 mm header descriptions/MPNs | The placed PCB uses **1×2, 2.54 mm pitch** headers. Order against the actual land pattern and mechanical requirements. |
| J10 | GRPB061VWVN-RC description retains 1.27 mm pitch | The placed PCB uses **1×6, 2.54 mm pitch**. The old symbol's MPN is not a valid purchasing instruction for that footprint. |
| R37–R42 | 680 Ω, 0.125 W indicator-resistor metadata | Later sourcing notes propose 2 kΩ. This is a recommendation requiring assembly reconciliation, not a confirmed populated value. |
| R33/R34 | 220 kΩ indicator-resistor metadata | Later sourcing notes propose 10 kΩ. This is a recommendation; check indicator loading of the OE nodes. |

These are confirmed discrepancies, not an exhaustive approved-parts list. The design also contains indicators and pull/bias components added in later iterations. Their values and exact procurement choices need reconciliation against the complete current schematic.

[CAD metadata CSV](cad-metadata-NOT-FOR-ORDER.csv) is supplied for inspection only. [Placed footprints CSV](placed-footprints.csv) lists the actual saved PCB patterns. Neither file is an approved assembly BOM. Earlier Rev C/D purchase quantities, stock allocation and spare counts have not been carried into this repository as a Rev E order.

## Preparing an assembly BOM

1. Select the actual transistor, its recommended gate voltage, gate charge and operating conditions.
2. Reconcile every designator with its circuit role, desired value, tolerance, voltage/power/pulse rating and population state.
3. Select the actual manufacturer part, then check pin numbering, package dimensions, pad geometry, orientation and 3D body. Matching package size alone is insufficient.
4. Update all schematic parameters and DNP flags, not just visible comments; review the schematic-to-PCB ECO before applying it.
5. Generate a new BOM and compare it by designator with the reviewed assembly plan. Generate fabrication and placement outputs from that same saved revision.

The 2 kΩ preload and 10 Ω gate resistor above are historical commissioning choices. They are not universal choices for every MOSFET, IGBT or SiC device.
