# PaDEL-Descriptor Setup Guide for Debian 12

This guide will help you set up and run PaDEL-Descriptor on your Debian 12 machine.

## Prerequisites

- Java 17 or higher (already installed on your system)
- Basic command-line knowledge

## Quick Start

### 1. Verify Java Installation
```bash
java -version
```
You should see OpenJDK 17.x.x or higher.

### 2. Run PaDEL-Descriptor

The project is already compiled and ready to use. You can run it using the provided script:

```bash
cd /home/eo/PaDEL-Descriptor_src
./run_padel.sh -help
```

### 3. Basic Usage Examples

#### Calculate 2D descriptors for molecules in a directory:
```bash
./run_padel.sh -dir /path/to/molecule/files -file output.csv -2d -removesalt -detectaromaticity
```

#### Calculate 3D descriptors (requires 3D coordinates):
```bash
./run_padel.sh -dir /path/to/molecule/files -file output.csv -3d -removesalt -detectaromaticity
```

#### Calculate fingerprints:
```bash
./run_padel.sh -dir /path/to/molecule/files -file output.csv -fingerprints -removesalt -detectaromaticity
```

#### Calculate all descriptor types:
```bash
./run_padel.sh -dir /path/to/molecule/files -file output.csv -2d -3d -fingerprints -removesalt -detectaromaticity
```

## Supported Input Formats

- SDF (Structure Data Format) - Recommended
- MOL files
- SMILES files (with proper formatting)
- PDB files
- HIN files

## Key Options

- `-dir <directory>`: Directory containing molecular structure files
- `-file <file>`: Output CSV file for descriptors
- `-2d`: Calculate 1D and 2D descriptors
- `-3d`: Calculate 3D descriptors (requires 3D coordinates)
- `-fingerprints`: Calculate molecular fingerprints
- `-removesalt`: Remove salt from molecules (recommended)
- `-detectaromaticity`: Detect aromaticity automatically (recommended)
- `-standardizetautomers`: Standardize tautomers
- `-log`: Create log file for debugging
- `-threads <number>`: Number of threads to use (-1 for auto)

## Example with Test Data

A test directory with sample molecules is already created:

```bash
# Test with sample data
./run_padel.sh -dir test_data -file test_output.csv -2d -removesalt -detectaromaticity -log
```

## Troubleshooting

### GTK Module Warning
The "Failed to load module canberra-gtk-module" warning is harmless and can be ignored. It's related to GUI components that aren't used in command-line mode.

### Memory Issues
If you encounter memory issues with large datasets, increase the Java heap size:

```bash
java -Xmx2g -cp "lib/*:build/classes" padeldescriptor.PaDELDescriptorApp [options]
```

### No Descriptors Calculated
If the output file only contains molecule names without descriptors, try:
1. Ensure your input files are in a supported format (SDF recommended)
2. Check that the molecules have valid structures
3. Use the `-log` option to see detailed error messages

## File Structure

- `lib/`: Contains all required JAR dependencies
- `build/classes/`: Compiled Java classes
- `test_data/`: Sample molecular structure files
- `run_padel.sh`: Convenience script to run PaDEL-Descriptor
- `PaDEL-Descriptor/src/`: Source code for the main application
- `libPaDEL-Descriptor/src/`: Source code for descriptor calculation engine

## Advanced Usage

### Using Configuration Files
You can create configuration files to avoid typing long command lines:

```bash
./run_padel.sh -config my_config.properties
```

### Custom Descriptor Selection
Use the `-descriptortypes` option to specify which descriptors to calculate:

```bash
./run_padel.sh -dir input_dir -file output.csv -descriptortypes descriptors.xml -2d
```

## For Allergen Research

This tool is particularly useful for biochemical allergen research as it can:

1. **Extract molecular descriptors** that correlate with allergenicity
2. **Calculate fingerprints** for similarity analysis
3. **Standardize molecular structures** for consistent analysis
4. **Process large datasets** efficiently with multi-threading

Common descriptors relevant to allergen research:
- TPSA (Topological Polar Surface Area)
- LogP values (lipophilicity)
- Molecular weight and volume
- Hydrogen bond donors/acceptors
- Aromatic atom counts
- Substructure fingerprints

## Support

For more information, visit the official PaDEL-Descriptor website or refer to the source code documentation.
