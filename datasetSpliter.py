from pathlib import Path
import random
from tqdm import tqdm


class DatasetSpliter:
    def __init__(self, dataset_path='.', output_path='.', pattern="*.jpg", split_ratio=[0.7, 0.2, 0.1]):
        self.dataset_path = Path(dataset_path)
        self.output_path = Path(output_path)
        self.pattern = pattern
        self.split_ratio = [ratio/sum(split_ratio) for ratio in split_ratio]
        self.val = True if len(split_ratio) == 3 else False
        self.data = [path for path in self.dataset_path.glob(
            self.pattern) if path.is_file()]
        self.data_num = len(self.data)

        print(f"{self.data_num} datas are found in {self.dataset_path}")
        self.__call__()

    def __call__(self):
        if self.dataset_path.exists():
            # check if dataset path exists
            if self.val:
                # both train, val and test folders will be created
                print("Splitting dataset into train, val and test folders...")
                ret = self.split_dataset3()
            else:
                # only train and test folders will be created
                print("Splitting dataset into train and test folders...")
                ret = self.split_dataset2()
        else:
            # dataset path does not exist
            ret = False
            print("Dataset path does not exist!")

        if ret:
            print("Dataset split successfully!")
        else:
            print("Dataset split failed!")
        return ret

    def split_dataset2(self):
        # create train and test folders
        train_path = self.output_path / 'train'
        test_path = self.output_path / 'test'
        train_path.mkdir(parents=True, exist_ok=True)
        test_path.mkdir(parents=True, exist_ok=True)

        # split data into train and test folders
        random.shuffle(self.data)
        train_num = int(self.data_num * self.split_ratio[0])
        train_data = self.data[:train_num]
        test_data = self.data[train_num:]

        # move train data to train folder
        for data in tqdm(train_data, desc="Train"):
            self.move_data(data, train_path / data.name)
        for data in tqdm(test_data, desc="Test"):
            self.move_data(data, test_path / data.name)

        return True

    def split_dataset3(self):
        # create train, val and test folders
        train_path = self.output_path / 'train'
        val_path = self.output_path / 'val'
        test_path = self.output_path / 'test'
        train_path.mkdir(parents=True, exist_ok=True)
        val_path.mkdir(parents=True, exist_ok=True)
        test_path.mkdir(parents=True, exist_ok=True)

        # split data into train, val and test folders
        random.shuffle(self.data)
        train_num = int(self.data_num * self.split_ratio[0])
        val_num = int(self.data_num * self.split_ratio[1])
        train_data = self.data[:train_num]
        val_data = self.data[train_num:train_num+val_num]
        test_data = self.data[train_num+val_num:]

        # move train data to train folder
        for data in tqdm(train_data, desc="Train"):
            self.move_data(data, train_path / data.name)
        for data in tqdm(val_data, desc="Val"):
            self.move_data(data, val_path / data.name)
        for data in tqdm(test_data, desc="Test"):
            self.move_data(data, test_path / data.name)

        return True

    @staticmethod
    def move_data(data, dst_path):
        try:
            # if file already exists in dst_path, remove it first
            if dst_path.exists():
                dst_path.unlink()
            # move data to dst_path
            data.rename(dst_path)
        except FileExistsError as e:
            print(f"Error occurred: {e}")
