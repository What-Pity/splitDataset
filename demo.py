from datasetSpliter import DatasetSpliter as dss
import argparse
import numpy as np


# parse the command line arguments
parser = argparse.ArgumentParser(
    description='Split a dataset into training, validation and testing sets.')
parser.add_argument('--origin', '-o', type=str, default='.',
                    help='path to the dataset')
parser.add_argument('--destination', '-d', type=str, default='.',
                    help='destination path for the splitted dataset')
parser.add_argument('--pattern', '-p', type=str, default='*',
                    help='pattern of validation set')
parser.add_argument('--ratio', '-r', type=float, nargs='+', default=[
                    0.8, 0.1, 0.1], help='ratio of training, validation and testing sets, can be two or three numbers separated by space, the last number will be used for the testing set if there are only two numbers')
args = parser.parse_args()


# create a DatasetSpliter object
if all(np.array(args.ratio) > 0):
    splitter = dss(args.origin, args.destination, args.pattern, args.ratio)
else:
    print("Ratio must be positive numbers")
    exit()
