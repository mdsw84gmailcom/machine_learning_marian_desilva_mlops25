from constants import DATA_PATH
import pandas as pd
from pprint import pprint
import json

df = pd.read_csv(DATA_PATH / "Sales.csv")


class DataExplorer:
    def __init__(self, limit=100):
        # _ private by convention
        # OK to acess within class, but not from outside
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

    def kpis(self, country: str):
        df_by_country = df.query("Country.str.casefold() == @country.casefold()")

        return {
            "total_profit": str(df_by_country["Profit"].sum()),
            "total_cost": str(df_by_country["Cost"].sum()),
            "number_of_purchases": str(len(df_by_country)),
            # more kpis
        }

    def json_response(self):
        json_data = self.df.to_json(orient="records")
        return json.loads(json_data)


if __name__ == "__main__":
    data_explorer = DataExplorer(limit=2)
    pprint(data_explorer.summary().json_response())
