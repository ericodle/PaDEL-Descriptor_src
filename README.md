# PaDEL-Descriptor

A comprehensive molecular descriptor calculation tool for cheminformatics and QSAR modeling.

## Overview

PaDEL-Descriptor is a software package for calculating molecular descriptors and fingerprints. It can calculate 1875 descriptors (1444 1D, 2D descriptors and 431 3D descriptors) and 12 types of fingerprints. These descriptors and fingerprints are calculated from the connection table of a molecule and are useful for structure-activity and structure-property studies.

## Features

- **1875 Molecular Descriptors**: 1D, 2D, and 3D descriptors
- **12 Fingerprint Types**: Various molecular fingerprint calculations
- **Molecular Standardization**: Salt removal, aromaticity detection, tautomer standardization
- **Multi-threading Support**: Parallel processing for efficient calculations
- **Multiple Input Formats**: SDF, MOL, PDB, SMILES
- **Command-line Interface**: Easy integration into workflows
- **RapidMiner Integration**: Built-in operator for data analysis workflows

## Quick Start

### Prerequisites

- Java 6 or higher
- Linux/Unix environment (tested on Debian 12)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/PaDEL-Descriptor_src.git
cd PaDEL-Descriptor_src
```

2. Compile the source code:
```bash
# Compile all modules
javac -cp "lib/*" -d libPaDEL/build/classes libPaDEL/src/*.java
javac -cp "lib/*:libPaDEL/build/classes" -d libPaDEL-Jobs/build/classes libPaDEL-Jobs/src/*.java
javac -cp "lib/*:libPaDEL/build/classes:libPaDEL-Jobs/build/classes" -d libPaDEL-Descriptor/build/classes libPaDEL-Descriptor/src/*.java
javac -cp "lib/*:libPaDEL/build/classes:libPaDEL-Jobs/build/classes:libPaDEL-Descriptor/build/classes" -d PaDEL-Descriptor/build/classes PaDEL-Descriptor/src/*.java
```

3. Set up Python environment for data analysis (optional):
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate  # On Linux/Mac
# or
env\Scripts\activate     # On Windows

# Install Python dependencies
pip install -r requirements.txt
```

### Usage

#### Process Multiple SDF Files

```bash
# Process all SDF files in your data directory
./process_all_files.sh
```

#### Manual Command-line Usage

```bash
# Process a single SDF file
./run_padel.sh -i input.sdf -o output.csv -2d -fingerprints -removesalt -detectaromaticity -standardizetautomers

# Process a directory of SDF files
./run_padel.sh -dir input_directory -file output.csv -2d -fingerprints -removesalt -detectaromaticity -standardizetautomers
```

#### GUI Usage

```bash
# Launch the graphical interface
./run_padel.sh
```

#### Data Description and Visualization

```bash
# Activate Python environment
source env/bin/activate

# Run data description and visualization
python data_analysis.py
```

This will generate:
- Statistical summaries of your molecular descriptors
- Distribution plots and correlation heatmaps
- PCA and t-SNE visualizations for data exploration
- Class-specific statistics and comparisons
- Publication-ready figures for data description

## Command-line Options

- `-i <file>`: Input SDF/MOL/PDB/SMILES file
- `-o <file>`: Output CSV file
- `-dir <directory>`: Input directory containing molecular files
- `-file <file>`: Output file for directory processing
- `-2d`: Calculate 2D descriptors
- `-3d`: Calculate 3D descriptors (requires 3D coordinates)
- `-fingerprints`: Calculate molecular fingerprints
- `-removesalt`: Remove salt from molecules
- `-detectaromaticity`: Detect and standardize aromaticity
- `-standardizetautomers`: Standardize tautomers
- `-threads <n>`: Number of threads (-1 for all available cores)
- `-log <file>`: Log file for processing details

## Output Format

The output is a CSV file with:
- First row: Descriptor names (715 descriptors by default)
- Subsequent rows: Descriptor values for each molecule
- First column: Molecule name/ID

## Example Workflow

```bash
# 1. Prepare your SDF files in a directory
mkdir my_molecules
# Copy your .sdf files to my_molecules/

# 2. Process all files
./process_all_files.sh

# 3. Results will be in results/ directory
ls results/
# Output: file1_descriptors.csv, file2_descriptors.csv, etc.
```

## Descriptor Categories

- **Constitutional Descriptors**: Molecular weight, atom counts, bond counts
- **Topological Descriptors**: Connectivity indices, molecular complexity
- **Electronic Descriptors**: LogP, TPSA, H-bond donors/acceptors
- **Pharmacophore Descriptors**: Structural features for drug-likeness
- **Molecular Fingerprints**: Structural similarity features

## Applications

- QSAR (Quantitative Structure-Activity Relationship) modeling
- Molecular similarity analysis
- Drug discovery and design
- Chemical property prediction
- Allergen classification and prediction

## License

This project is based on the original PaDEL-Descriptor software. Please refer to the original license terms.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Citation

If you use this software in your research, please cite the original PaDEL-Descriptor paper:

```
Yap, C.W. (2011) PaDEL-descriptor: An open source software to calculate molecular descriptors and fingerprints. Journal of Computational Chemistry, 32, 1466-1474.
```

## Support

For issues and questions, please open an issue on GitHub.
