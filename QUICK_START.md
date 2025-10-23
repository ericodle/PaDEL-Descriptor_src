# PaDEL-Descriptor Quick Start Guide

## Essential Files for Running PaDEL-Descriptor

### Required Files:
- `lib/` - Contains all JAR dependencies (17 files)
- `build/classes/` - Compiled Java classes
- `run_padel.sh` - Executable script to run PaDEL-Descriptor
- `README_SETUP.md` - Detailed setup and usage documentation

### Source Code (for reference):
- `PaDEL-Descriptor/src/` - Main application source
- `libPaDEL-Descriptor/src/` - Descriptor calculation engine source
- `libPaDEL/src/` - Basic utilities source
- `libPaDEL-Jobs/src/` - Multi-threading job management source

## Quick Usage

```bash
# Show help
./run_padel.sh -help

# Calculate 2D descriptors
./run_padel.sh -dir /path/to/molecules -file output.csv -2d -removesalt -detectaromaticity

# Calculate all descriptor types
./run_padel.sh -dir /path/to/molecules -file output.csv -2d -3d -fingerprints -removesalt -detectaromaticity
```

## Supported Input Formats
- SDF (Structure Data Format) - **Recommended**
- MOL files
- SMILES files
- PDB files
- HIN files

## Output
- CSV file with molecular names and calculated descriptors
- Optional log file for debugging

## Memory Requirements
- Default: 512MB heap
- For large datasets: Use `java -Xmx2g` in the script

## Notes
- The GTK warning message is harmless and can be ignored
- Ensure input molecules have valid structures
- Use SDF format for best compatibility
