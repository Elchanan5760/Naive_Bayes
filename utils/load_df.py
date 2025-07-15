import pandas as pd

class MyUtils:
    def load_data(self,data):
        df = pd.read_csv(data)
        return df