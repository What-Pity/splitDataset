# Split Dataset

This is a `Python` script to split a dataset into training, validation and test sets. The script takes in the path of the dataset and the percentage of data to be used for training, validation and test sets. The script creates three new folders in the same directory as the dataset folder, namely, `train`, `val` and `test`. The script then copies the required percentage of data from the original dataset folder to the new folders.

Main function is achieved through the class `datasetSpliter.DatasetSpliter`, there is also a `demo.py` file to demonstrate the usage of the class.

## Requirements

To use datasetSpliter.py, all you need is to install `tqdm` library using the following command:

```cmd
pip install tqdm
```

If you want to run the `demo.py` file, you also need to install `numpy` library using the following command:

```cmd
pip install numpy
```

## Usage

Each arguement of the `DatasetSpliter` class is explained in `demo.py` file, but here is a brief explanation:

- `dataset_path`: path to the dataset folder
- `output_path`: destination path for the splitted dataset
- `pattern`: pattern of validation set. For example, `"*jpg"` will select all jpg files in the dataset folder
- `split_ratio`: ratio of training, validation and testing sets, can be two or three numbers separated by space, the last number will be used for the testing set if there are only two numbers
