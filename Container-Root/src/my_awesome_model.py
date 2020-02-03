import argparse
import numpy as np

import tensorflow as tf
import datetime


def get_model(learningRate=0.1,activationFunction='linear'):
    # User Defined a simple Keras model with Callback
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, activation = activationFunction, input_dim = 784))
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=learningRate), loss='mean_squared_error', metrics=['mae'])
    return model

class KatibLossPrint(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
            """
            Simple function for printing the history so that Katib picks it up
            """
            hist = self.model.history.history
            history_keys = list(hist.keys())
            print('\nepoche {}:'.format(epoch))
            for cur_key in history_keys:
                print('{}={}'.format(cur_key,hist[cur_key][-1]))

def my_model(args):

    #We ar getting command line arguments `args` to set up our model
    my_par1 = args.myParameter1
    my_par2 = args.myParameter2
    my_par3 = args.myParameter3

    # Assume that you have 8GB of GPU memory and want to allocate ~0.8GB if your args.gpuFraction == 0.1:
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=args.gpuFraction)

    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

    tf.keras.backend.set_session(sess)

    #++++ Add your model depending on my_par1 and my_par2 here! ++++

    print('Here we execute my_model.fit({},{})'.format(my_par1,my_par2))

    # Load example MNIST data and pre-process it
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32') / 255
    x_test = x_test.reshape(10000, 784).astype('float32') / 255

    model = get_model(learningRate=my_par2, activationFunction=my_par3)
    _ = model.fit(x_train, y_train,
          batch_size=64,
          epochs=my_par1,
          steps_per_epoch=5,
          verbose=0,
          callbacks=[KatibLossPrint()])


if __name__ == '__main__':

    # This python script will be our MAIN entrypoint, hence parsing here the command line arguments.
    parser = argparse.ArgumentParser(description="Training my_model()",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--gpuFraction', type=float, default=0.5,
                    help='Fraction of GPU allocatable by TF')
    parser.add_argument('--myParameter1', type=int, default=3,
                    help='Hyperparameter 1 - Epoches')
    parser.add_argument('--myParameter2', type=float, default=0.01,
                    help='Hyperparameter 2 - Learning Rate')
    parser.add_argument('--myParameter3', type=str, default='linear',
                    help='Hyperparameter 3 - Activation Function')


    args = parser.parse_args()
    my_model(args)
