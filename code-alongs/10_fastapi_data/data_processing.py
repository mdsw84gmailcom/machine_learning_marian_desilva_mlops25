from constants import DATA_PATH
import pandas as pd
from pprint import pprint
import json

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit=100):
        self._df = df.head(limit)
        self._df_full = df

    @property
    def df(self):
        return self._df

    def summary(self):
        self._df = (
            self._df_full.describe()
            .T.drop(["count"], axis=1)
            .drop(["Day", "Year"])
            .reset_index()
        )
        return self  # allows for method chaining

    def json_response(self):
        json_data = self.df.to_json(orient="records")
        return json.loads(json_data)


if __name__ == "__main__":
    data_explorer = DataExplorer(limit=2)
    pprint(data_explorer.summary().json_response())
