#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install pip if not installed
if ! command -v pip &> /dev/null
then
    echo "pip not found. Installing pip..."
    sudo apt-get install python3-pip -y
fi

# Install required Python packages
echo "Installing required Python packages..."
pip install opencv-python numpy

echo "All dependencies have been installed successfully!"
