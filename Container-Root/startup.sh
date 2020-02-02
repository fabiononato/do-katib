#!/bin/sh

# Container startup script
echo "Container-Root/startup.sh executed"
echo "python /src/my_awesome_model.py --gpuFraction=0.25"
python /src/my_awesome_model.py --gpuFraction=0.25
