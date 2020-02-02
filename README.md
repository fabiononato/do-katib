# *do-katib*: a simple Docker wrapped script to run Katib Experiments in Kubeflow.


This Repo contains a simple starter project which wraps a [model method](Container-Root/src/my_awesome_model.py) and parses arguments according to Katib's format.

# Building the project:

This project is set as a Depend-on-Docker automation that will help you build a container around the Katib wrapped method.

The main entrypoint to the project is the script containing the [my_model](Container-Root/src/my_awesome_model.py) method. Once you've added a call to your model into this script, you'll need to build the project image. Please refer to the Depend-on-Docker project documentation for more details.

The modifications specific to this projects are:

- a [test scrip](Container-Root/test.sh) that checks for the proper set up of the NVIDIA drivers, as this project rely on a GPU version of TF.

- an [environment file](.env) with a registry and project name specific to this project.

- a tensorflow-gpu [base image](Dockerfile) on our Dockerfile.

# Katib Templates:

Some sample Katib YAML files can be found here
