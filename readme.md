# Split Dataset

This is a `MATLAB` script to split a dataset into training, validation and test sets.

## Usage

There are serveral parameters should be costomized before running the script:

- `train_p`: the percentage of the dataset to be used for training, it can be any numeric value (not matter it is a `int` or `float`) but `0`.
- `val_p`: the percentage of the dataset to be used for validation, it can be any numeric value (not matter it is a `int` or `float`) but `0`.
- `test_p`: the percentage of the dataset to be used for testing, it can be any numeric value (not matter it is a `int` or `float`) but `0`.
- `source_dir`: the directory of the source dataset.
- `annotation_dir`: the directory of the annotation file.
- `traget_dir`: the directory of the target dataset.
- `data_suffix`: the suffix of the data file, such as `.jpg`, `.png`, `.mat`, etc.
- `annotation_suffix`: the suffix of the annotation file, such as `.xml`, `.txt`, `.json`, etc.

After customizing the parameters, you can run the script, it will split the dataset into training, validation and test sets and save them into the target directory.

## Limitations

- The script only supports `MATLAB` version, and a `python` version will be released later.