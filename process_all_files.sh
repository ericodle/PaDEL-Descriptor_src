#!/bin/bash

# Process all SDF files individually with correct parameters
# Usage: ./process_all_files_correct.sh

BASE_DIR="/home/eo/Documents/prf_You"
OUTPUT_DIR="/home/eo/PaDEL-Descriptor_src/results"
TEMP_DIR="/home/eo/PaDEL-Descriptor_src/temp_processing"

# Create output and temp directories
mkdir -p "$OUTPUT_DIR"
mkdir -p "$TEMP_DIR"

echo "Processing all SDF files from $BASE_DIR"
echo "Output will be saved to $OUTPUT_DIR"
echo ""

# Process each file individually
for file in "$BASE_DIR"/*.sdf; do
    filename=$(basename "$file" .sdf)
    output_file="$OUTPUT_DIR/${filename}_descriptors.csv"
    
    echo "Processing $filename..."
    echo "  Input: $file"
    echo "  Output: $output_file"
    
    # Copy single file to temp directory for processing
    rm -rf "$TEMP_DIR"/*
    cp "$file" "$TEMP_DIR/"
    
    # Run PaDEL-Descriptor with correct parameters
    ./run_padel.sh \
        -dir "$TEMP_DIR" \
        -file "$output_file" \
        -2d \
        -removesalt \
        -detectaromaticity \
        -standardizetautomers \
        -log \
        -usefilenameasmolname \
        -maxruntime 30000 \
        -threads -1 \
        -descriptortypes PaDEL-Descriptor/src/META-INF/descriptors.xml
    
    if [ $? -eq 0 ]; then
        echo "  ✅ Success: $filename processed"
        # Count molecules and descriptors in output
        mol_count=$(tail -n +2 "$output_file" | wc -l)
        desc_count=$(head -1 "$output_file" | tr ',' '\n' | wc -l)
        echo "  📊 Molecules processed: $mol_count"
        echo "  🔬 Descriptors calculated: $desc_count"
    else
        echo "  ❌ Error processing $filename"
    fi
    echo ""
done

echo "All files processed!"
echo "Results saved in: $OUTPUT_DIR"

# Clean up temp directory
rm -rf "$TEMP_DIR"

echo ""
echo "Summary of results:"
for file in "$OUTPUT_DIR"/*_descriptors.csv; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" _descriptors.csv)
        mol_count=$(tail -n +2 "$file" | wc -l)
        desc_count=$(head -1 "$file" | tr ',' '\n' | wc -l)
        echo "  $filename: $mol_count molecules, $desc_count descriptors"
    fi
done
