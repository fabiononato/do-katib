#!/bin/sh

# Unit test of container
echo "Testing for nvidia-smi access from within container"
nvidia-smi
if [ $? -eq 0 ]; then 
   echo "Test1 succeeded"
else
   echo "Test1 failed"
fi
