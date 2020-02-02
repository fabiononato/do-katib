import argparse
import numpy as np

import tensorflow as tf


def my_model(args):

    #We ar getting command line arguments `args` to set up our model
    my_par1 = args.myParameter1
    my_par2 = args.myParameter2

    # Assume that you have 8GB of GPU memory and want to allocate ~0.8GB if your args.gpuFraction == 0.1:
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpuFraction)

    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    tf.keras.backend.set_session(sess)

    #++++ Add your model depending on my_par1 and my_par2 here! ++++

    print('Here we execute my_model.fit({},{})'.format(my_par1,my_par2))

    # Remember to print out the 


if __name__ == '__main__':

    # This python script will be our MAIN entrypoint, hence parsing here the command line arguments.
    parser = argparse.ArgumentParser(description="Training my_model()",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--gpuFraction', type=float, default=0.1,
                    help='Fraction of GPU allocatable by TF')
    parser.add_argument('--myParameter1', type=int, default=3,
                    help='Hyperparameter 1')
    parser.add_argument('--myParameter2', type=float, default=0.001,
                    help='Hyperparameter 2')


    args = parser.parse_args()
    printArgs(args)

    my_model(args)
