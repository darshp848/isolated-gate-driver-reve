# How the board works

## Signal and supply paths

Six PWM commands enter J10. U7 is an SN74AHCT244 octal non-inverting buffer operated from the control-side 5 V rail. Its TTL-compatible inputs provide an interface for 3.3 V PWM logic; its outputs feed the six UCC5310MCDR IN+ pins. The UCC inputs are CMOS, so using the buffer avoids depending on a marginal direct 3.3 V high level at a 5 V driver input supply. U7 has two independently controlled active-low output-enable banks. See [TI's buffer documentation](https://www.ti.com/product/SN74AHCT244).

Each channel's EN header interrupts the **5 V feed to that channel's driver logic supply and DC/DC converter**. It is a supply-selection jumper, distinct from J3's logic enables. Removing bias power is not a substitute for a characterized fast fault shutdown.

PS1–PS6 are MER1S0515SC unregulated isolated converters. They derive nominal 15 V floating rails from the channel's 5 V input. Each UCC5310 output is referenced to its own ISOLn− return, so the gate output can follow a floating transistor source/emitter. Keep each gate and return together; do not combine isolated returns merely because the connectors look identical.

The series gate resistors control charging/discharging current and switching behavior. The UCC5310M's CLAMP pin connects to the gate-side node after that resistor in the saved schematic diagnostic. Its active Miller clamp is intended to shunt off-state Miller current to the local return. Cable and PCB loop inductance still matter. See [TI's UCC5310 documentation](https://www.ti.com/product/UCC5310).

## Interface map

This map was derived from the **saved October 3 schematic**, using a read-only endpoint/label diagnostic. It is not an Altium-compiled netlist or verification of every October 7 PCB pad. The diagnostic's complete pin groups are in [saved-schematic-pin-groups.json](saved-schematic-pin-groups.json). Confirm the interface against final compiled nets and PCB pads before connecting hardware.

| Connector | Saved schematic connection |
| --- | --- |
| J1, J2 | Pin 1: control 5 V; pin 2: DGND. Parallel access to the same supply. |
| J10 | Pins 1–6: PWM1–PWM6. No control ground pin on this header. |
| J3 | Pin 1: U7 OE1, controlling PWM1–4; pin 2: U7 OE2, controlling PWM5–6. High disables, low enables. |
| EN1–EN6 | Pin 1: shared 5 V; pin 2: corresponding UCC VCC1 and converter +VIN. A shunt supplies that channel. |
| J8, J9 | Pin 1: Gate1/Gate2; pin 2: corresponding ISOL1−/ISOL2−. |
| J11, J12 | Pin 1: Gate3/Gate4; pin 2: corresponding isolated return. |
| J13, J14 | Pin 1: Gate5/Gate6; pin 2: corresponding isolated return. |

R13–R18 pull the PWM inputs toward DGND. Resistors also pull the buffered driver-input commands toward DGND. R30/R32 pull U7's OE nodes toward 5 V; those nodes also feed indicator branches through R33/R34. This is a later schematic change from the September audit, which reported OE bias resistors absent. A controller interface to the 5 V-biased OE pins must be selected and checked for its actual tolerances and power sequencing.

## Bias, indicators and protection footprints

The odd-numbered R1–R11 preloads span each floating rail. The earlier selected 2 kΩ preload draws 7.5 mA and dissipates 0.1125 W at 15 V. This helps maintain a minimum load on an unregulated converter; it is not an inrush limiter or precision regulator. Indicator branches add further rail loading. Their resistor fields also require reconciliation with the assembly selection.

D1–D6 span the isolated rails, cathode toward the positive rail. These optional Zener footprints permit evaluation of rail limiting; their nominal voltage is not a guaranteed transient ceiling. Initial DNP and the proposed 18 V candidate remain documented in [component selection](component-selection.md).

Gate-drive energy per cycle is approximately Qg × Vgate, giving an average gate-charge current near Qg × switching frequency. Converter capacity must cover that demand plus driver quiescent current, preload and indicators. The final resistor also needs pulse and thermal assessment. These estimates guide component selection; they do not establish a tested frequency rating.

The MER1 family has minimum-load and insulation limitations. Its nominal output and isolation test figures must not be treated as a regulated rail specification or whole-board working-voltage rating. Use the [Murata MER1 datasheet](https://www.murata.com/products/productdata/8807029833758/kdc-mer1.pdf) for the selected part and actual application.

## Layout and system responsibilities

The layout uses six repeated channel areas and a common control section on a four-layer board. The October transfer replaced small-pitch catalog header footprints with standard 2.54 mm headers and corrected their 3D-body positions. Preserve actual pad numbering and isolation-domain boundaries when editing.

A short, paired gate/Kelvin-return path reduces ringing and false turn-on risk. Isolation must be reviewed across all copper layers, not just the visible top-layer gap. Controller-side ground, floating channel returns and bench-instrument references need an intentional grounding arrangement.

The PCB contains no processor or autonomous PWM interlock. Dead time, complementary-switch assignment, current sensing, fault shutdown and startup/reset behavior belong to the complete system. An active-low buffer enable is useful command inhibition, but is not a fully qualified power-stage protection scheme.
