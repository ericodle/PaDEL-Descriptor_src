#!/bin/bash

# PaDEL-Descriptor Runner Script
# Usage: ./run_padel.sh [options]

# Set the base directory
BASE_DIR="/home/eo/PaDEL-Descriptor_src"

# Change to the base directory
cd "$BASE_DIR"

# Run PaDEL-Descriptor with all arguments passed to this script
java -cp "lib/*:build/classes" padeldescriptor.PaDELDescriptorApp "$@"
