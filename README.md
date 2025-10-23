# PaDEL-Descriptor

Molecular descriptor calculation tool for cheminformatics and QSAR modeling.

## Quick Start

1. **Compile:**
```bash
javac -cp "lib/*" -d libPaDEL/build/classes libPaDEL/src/*.java
javac -cp "lib/*:libPaDEL/build/classes" -d libPaDEL-Jobs/build/classes libPaDEL-Jobs/src/*.java
javac -cp "lib/*:libPaDEL/build/classes:libPaDEL-Jobs/build/classes" -d libPaDEL-Descriptor/build/classes libPaDEL-Descriptor/src/*.java
javac -cp "lib/*:libPaDEL/build/classes:libPaDEL-Jobs/build/classes:libPaDEL-Descriptor/build/classes" -d PaDEL-Descriptor/build/classes PaDEL-Descriptor/src/*.java
```

2. **Process molecules:**
```bash
# Process all SDF files
./process_all_files.sh

# Or process individual files
./run_padel.sh -i input.sdf -o output.csv -2d -fingerprints -removesalt -detectaromaticity
```

3. **Analyze results (optional):**
```bash
python3 -m venv env && source env/bin/activate
pip install -r requirements.txt
python data_analysis.py
```

## Usage

### Batch Processing
```bash
./process_all_files.sh
```

### Single File
```bash
./run_padel.sh -i molecule.sdf -o descriptors.csv -2d -fingerprints -removesalt -detectaromaticity
```

### Directory Processing
```bash
./run_padel.sh -dir molecules/ -file output.csv -2d -fingerprints -removesalt -detectaromaticity
```

## Key Options

- `-2d`: Calculate 2D descriptors
- `-3d`: Calculate 3D descriptors (requires 3D coordinates)
- `-fingerprints`: Calculate molecular fingerprints
- `-removesalt`: Remove salt from molecules
- `-detectaromaticity`: Detect aromaticity
- `-standardizetautomers`: Standardize tautomers
- `-threads -1`: Use all CPU cores

## Supported Formats

- SDF (recommended)
- MOL
- SMILES
- PDB

## Output

CSV file with 715 molecular descriptors per molecule.

## Applications

- QSAR modeling
- Molecular similarity analysis
- Allergen classification
- Drug discovery

## Citation

```
Source code obtained from http://yapcwsoft.com/dd/padeldescriptor/

Yap CW (2011). PaDEL-Descriptor: An open source software to calculate molecular descriptors and fingerprints. Journal of Computational Chemistry. 32 (7): 1466-1474
```