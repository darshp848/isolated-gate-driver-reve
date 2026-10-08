# Revision provenance and validation boundary

## Publication snapshot — October 8, 2026

The native board contains the text **Rev. E** and was last saved October 8, 2026, at 02:44:43 local time after the user reported a silkscreen correction. The associated Sheet2 schematic was saved October 3. Source paths and SHA-256 hashes are in [source-manifest.json](source-manifest.json). The schematic has 152 unique designators; the board has 155 component records, including three additional fiducials. Equal counts would not prove connectivity; these counts are inventory evidence only.

The publication check read the saved binary documents, confirmed revision text and footprint patterns, identified the project's actual linked files, and compared copied-file hashes. All project document paths resolve inside the repository. This was packaging and documentation, not a fresh CAD or hardware acceptance test.

The copper and 3D illustrations were supplied by Darsh Patel during publication and visibly identify Rev E. They precede the newly reported silkscreen correction and are not regenerated outputs tied to the source hashes. An offline diagnostic of the current saved schematic resolved 344 pin endpoints into 57 groups, including the gate-side clamp, OE pullups and EN supply jumpers. That diagnostic does not replace native compilation or a current PCB pad-net comparison.

## Earlier development

- Rev C review identified direct 3.3 V PWM threshold concerns, light-load bias-supply behavior, clamp wiring, gate-loop length and isolation-layout issues.
- Rev D iteration added an AHCT buffer, preload and optional rail-clamp footprints; earlier saved-schematic review confirmed CLAMP connects to the gate after the series resistor. Component metadata still included package-selection placeholders.
- October 2–3 work transferred a KiCad placement/routing proposal to Altium and replaced sixteen headers with standard 2.54 mm footprints. Header 3D-body offsets were corrected. The reference KiCad proposal was a development aid, not an independently maintained Rev E release.
- October 3 native DRC recorded no shorts, unrouted nets or electrical clearance violations in that saved revision, while hundreds of silkscreen violations remained. These results predate subsequent edits and are not a Rev E pass.
- October 7 conversation records the user removing a redundant L4 same-net loop near R25/C28. Same-net loops can pass connectivity and short-circuit checks. The saved project instructions now require a visual copper review on every routed layer.

The documentation was reconciled with local Claude and Codex session history and saved review/transfer notes. Raw sessions are not published: they contain unrelated work and machine-specific context. Historical AI claims of generic operating voltage or switching-frequency limits are not carried forward as validated specifications.

## Before fabrication or energized use

Resolve the assembly BOM and all DNP choices. Compile and verify every connector, enable, buffer and driver pin against final pad nets. Inspect all copper layers and changed routes for loops, stubs, unexpected branches, return-path discontinuities and copper overlap between voltage domains. Repour and run final native DRC, recording tool version, exact file hashes, date and remaining dispositions.

No assembled-board working-voltage certification, transistor-independent switching-frequency rating or measured operating envelope is established here. Review the complete insulation path and converter limitations for the intended system. Bring-up should separate unpowered continuity, bias-only startup/idle/load behavior, logic/dummy-load testing, and actual transistor switching tests. The external power stage needs defined dead time and fault shutdown. Probe each floating gate relative to its own source/Kelvin return with suitable measurement equipment.

Record measured gate peaks, off-state transients, delay/overlap, rail behavior and temperatures with the transistor MPN, bus voltage, gate charge, frequency and duty range. These measurements remain separate from CAD verification.
