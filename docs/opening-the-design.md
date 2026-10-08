# Opening and exporting the design

The source workflow used Altium Designer 26; the October layout transfer recorded **26.10.1.5**. Open `hardware/isolated-gate-driver.PrjPcb`. It references the schematic, PCB and local GPIO header library using relative paths.

The original project linked to `../../3-phase-inverter/Sheet2.SchDoc` and `PCB2.PcbDoc`. A much smaller PCB2 file beside the original project was an older/unrelated board. That duplicate is not included. Stale ActiveBOM, PDN analysis, output-job and generated-report entries were removed from the project wrapper. Native schematic and board files were not edited.

Placed symbols, footprints and PCB 3D body data are preserved in the native documents. The header library is included separately for reuse. Some schematic model links still refer to the original machine's library paths or managed component sources; placed content can be inspected, but library update/replacement may require relinking `GPIO_Headers.PcbLib` and obtaining the appropriate upstream vendor libraries. The package does not claim a complete portable library for replacing every part.

Do not run an automatic library update simply to open the design. Resolve intended parts first, especially the metadata/footprint mismatches documented in [component selection](component-selection.md).

## Validation and outputs

Work in a copy of the repository. Compile the project, inspect messages, compare every schematic pin with its PCB pad net, and inspect ECO changes before applying them. Review all four copper layers, isolation-domain spacing, gate loops and return paths. Repour and run fresh native DRC on the final saved board.

Create new output jobs for the reviewed revision: schematic PDF, assembly BOM with DNP flags, pick-and-place file, fabrication drawings, Gerbers and drill files. Inspect the generated layers independently. This snapshot includes no Rev E Gerber release; prior October 4 ZIPs precede the latest board save.

The opening and export workflow follows [Altium project documentation](https://www.altium.com/documentation/altium-designer/creating-projects-documents) and [output jobs](https://www.altium.com/documentation/altium-designer/preparing-multiple-outputs-outputjob).
