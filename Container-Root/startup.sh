#!/bin/sh

# Container startup script
echo "Container-Root/startup.sh executed"
echo "python /src/my_awesome_model.py --gpuFraction=0.25"
python my_awesome_model.py --gpuFraction=0.50
