import scipy.misc
import os
import numpy as np

from model_genetic import DCGAN
from utils import pp, visualize, to_json, show_all_variables

import tensorflow as tf

#use absolute paths
ABS_PATh = os.path.dirname(os.path.abspath(__file__)) + "/"


flags = tf.app.flags
flags.DEFINE_integer("epoch", 25, "Epoch to train [25]")
flags.DEFINE_float("learning_rate", 0.0002, "Learning rate of for adam [0.0002]")
flags.DEFINE_float("beta1", 0.5, "Momentum term of adam [0.5]")
flags.DEFINE_float("train_size", np.inf, "The size of train images [np.inf]")
flags.DEFINE_integer("batch_size", 64, "The size of batch images [64]")
flags.DEFINE_integer("input_height", 108, "The size of image to use (will be center cropped). [108]")
flags.DEFINE_integer("input_width", None, "The size of image to use (will be center cropped). If None, same value as input_height [None]")
flags.DEFINE_integer("output_height", 64, "The size of the output images to produce [64]")
flags.DEFINE_integer("output_width", None, "The size of the output images to produce. If None, same value as output_height [None]")
flags.DEFINE_string("dataset", "celebA", "The name of dataset [celebA, mnist, lsun]")
flags.DEFINE_string("input_fname_pattern", "*.png", "Glob pattern of filename of input images [*]")
flags.DEFINE_string("checkpoint_dir", ABS_PATh + "checkpoint", "Directory name to save the checkpoints, absolute path is required [checkpoint]")
flags.DEFINE_string("data_dir", ABS_PATh + "data", "Root directory of dataset, absolute path is required [data]")
flags.DEFINE_string("sample_dir", ABS_PATh + "samples", "Directory name to save the image samples, absolute path is required [samples]")
flags.DEFINE_boolean("train", False, "True for training, False for testing [False]")
flags.DEFINE_boolean("crop", False, "True for training, False for testing [False]")
flags.DEFINE_boolean("visualize", False, "True for visualizing, False for nothing [False]")
flags.DEFINE_integer("generate_test_images", 100, "Number of images to generate during test. [100]")
flags.DEFINE_boolean("is_custom_mnist", False, "is_custom_mnist. [False]")  #note that you can simply put your image classes folders in dataset folder which i'd called custom mnist of course it can be any labelled image dataset
flags.DEFINE_string("load_checkpoint", '', "Load a particular checkpoint ['']")

# genetic parameteres 
flags.DEFINE_boolean("give_birth", False, "True for giving birth of new genome")
flags.DEFINE_integer("matron_id", 0, "True for giving birth of new genome")
flags.DEFINE_integer("sire_id", 0, "True for giving birth of new genome")
flags.DEFINE_string("extra", "", "Extra parameteres to be used to give birth")
flags.DEFINE_integer("ENV", 2, "Environment")
flags.DEFINE_boolean("is_sub_process", True, "True for sub process means training or testing process")


FLAGS = flags.FLAGS


iS_DEBUG = 0
# python3 main.py --dataset datasetA1 --input_height=466 --input_width=344 --output_height=466 --output_width=344 --train=True --crop
# python3 main.py --dataset datasetB --input_height=300 --input_width=300 --output_height=300 --output_width=300 --train=True --crop
# python3 main.py --dataset datasetB1 --input_height=128 --input_width=128 --output_height=128 --output_width=128 --train=False --crop=False --give_birth=True --generate_test_images=100
# python3 main.py --dataset mnist --input_height=128 --input_width=128 --output_height=128 --output_width=128 --train=True --crop --dataset=mnist --is_custom_mnist=True

def main(_):
  pp.pprint(flags.FLAGS.__flags)

  if FLAGS.input_width is None:
    FLAGS.input_width = FLAGS.input_height
  if FLAGS.output_width is None:
    FLAGS.output_width = FLAGS.output_height

  if not os.path.exists(FLAGS.checkpoint_dir):
    os.makedirs(FLAGS.checkpoint_dir)
  if not os.path.exists(FLAGS.sample_dir):
    os.makedirs(FLAGS.sample_dir)

  #gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
  run_config = tf.ConfigProto()
  run_config.gpu_options.allow_growth=True

  with tf.Session(config=run_config) as sess:
    if FLAGS.dataset == 'mnist' and FLAGS.is_sub_process:
      dcgan = DCGAN(
          sess,
          input_width=FLAGS.input_width,
          input_height=FLAGS.input_height,
          output_width=FLAGS.output_width,
          output_height=FLAGS.output_height,
          batch_size=FLAGS.batch_size,
          sample_num=FLAGS.batch_size,
          y_dim=10,
          z_dim=FLAGS.generate_test_images,
          dataset_name=FLAGS.dataset,
          input_fname_pattern=FLAGS.input_fname_pattern,
          crop=FLAGS.crop,
          checkpoint_dir=FLAGS.checkpoint_dir,
          sample_dir=FLAGS.sample_dir,
          data_dir=FLAGS.data_dir,
          is_custom_mnist=FLAGS.is_custom_mnist)
    elif FLAGS.is_sub_process:
      dcgan = DCGAN(
          sess,
          input_width=FLAGS.input_width,
          input_height=FLAGS.input_height,
          output_width=FLAGS.output_width,
          output_height=FLAGS.output_height,
          batch_size=FLAGS.batch_size,
          sample_num=FLAGS.batch_size,
          z_dim=FLAGS.generate_test_images,
          dataset_name=FLAGS.dataset,
          input_fname_pattern=FLAGS.input_fname_pattern,
          crop=FLAGS.crop,
          checkpoint_dir=FLAGS.checkpoint_dir,
          sample_dir=FLAGS.sample_dir,
          data_dir=FLAGS.data_dir, 
          is_give_birth=FLAGS.give_birth,
          is_custom_mnist=FLAGS.is_custom_mnist, 
          load_checkpoint=FLAGS.load_checkpoint)
    else:
      dcgan = None

    show_all_variables()

    if FLAGS.train:
      dcgan.train(FLAGS)
    else:
      if FLAGS.is_sub_process:
        if not dcgan.load(FLAGS.checkpoint_dir)[0]:
          raise Exception("[!] Train a model first, then run test mode")
      

    # to_json("./web/js/layers.js", [dcgan.h0_w, dcgan.h0_b, dcgan.g_bn0],
    #                 [dcgan.h1_w, dcgan.h1_b, dcgan.g_bn1],
    #                 [dcgan.h2_w, dcgan.h2_b, dcgan.g_bn2],
    #                 [dcgan.h3_w, dcgan.h3_b, dcgan.g_bn3],
    #                 [dcgan.h4_w, dcgan.h4_b, None])

    # Below is codes for visualization
    if not FLAGS.give_birth and iS_DEBUG == 0:
      OPTION = 1
      visualize(sess, dcgan, FLAGS, OPTION)


    # give birth(genetic), create image as in test mode
    if FLAGS.give_birth:
      res = {}
      res["type"] = "success"
      res["msg"] = ""

      OPTION = 1
      if FLAGS.is_sub_process:
        loop_size = 100
        if FLAGS.ENV >= 2:
          loop_size = 1

        for idx in np.arange(0, loop_size, 1):
          res = dcgan.giveBirth(sess, dcgan, FLAGS, OPTION)
      else:
          from __genetic_layer import genetic_layer
          genetic_layer_obj = genetic_layer()
          res = genetic_layer_obj.main(sess, dcgan, FLAGS, OPTION)

      print("final res")
      print(res)

if __name__ == '__main__':
  tf.app.run()
