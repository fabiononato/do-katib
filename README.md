# *do-katib*: a simple Docker wrapped project to run Katib Experiments in Kubeflow.

This Repo contains a simple starter project which wraps a [model method](Container-Root/src/my_awesome_model.py) and parses arguments according to Katib's format.

# How To Use This Project:

An indepth exploration of the project is provided in this Blog Post: 
[*End-to-End Hyperparameter Tuning with Katib, Tensorflow, Keras and Nvidia GPU on a gaming laptop*](https://medium.com/@fbiononatodepaula/hyperparameter-tuning-with-katib-tensorflow-keras-and-nvidia-gpu-on-a-gaming-laptop-3ada6a8a01a9)

The user familiar with ML and Containers base concepts can use the [sample method](Container-Root/src/my_awesome_model.py) to implement their own models and Experiment on an existing Kubeflow deployment.

# Katib Templates:

Some sample Katib YAML files can be found in the [katib](katib) folder. 

To run the base experiments on this project, one can simple run the following command on an existing kubernetes cluster with kubeflow deployment:

```bash
kubectl apply -f https://raw.githubusercontent.com/fabiononato/do-katib/master/katib/random-experiment.yaml
```

# Building the project:

This project is set as a Depend-on-Docker automation that will help you build a container around the Katib wrapped method.

The main entrypoint to the project is the script containing the [my_model](Container-Root/src/my_awesome_model.py) method. Once you've added a call to your model into this script, you'll need to build the project image. Please refer to the Depend-on-Docker project documentation for more details.

The modifications specific to this projects are:

- a [test scrip](Container-Root/test1.sh) that checks for the proper set up of the NVIDIA drivers, as this project rely on a GPU version of TF.

- an [environment file](.env) with a registry and project name specific to this project.

- a tensorflow-gpu [base image](https://github.com/fabiononato/do-katib/blob/master/Dockerfile#L1) on our Dockerfile.




