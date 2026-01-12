from constants import DATA_PATH
import pandas as pd

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit=100):
        self._df = df.head(limit)

    @property
    def df(self):
        return self._df


if __name__ == "__main__":
    data_explorer = DataExplorer(limit=5)
    print(data_explorer.df)
