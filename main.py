import pandas as pd
import numpy as np
from model_coach import Train

# buy = df.sort_values('PlayTennis')

class Main:
    def __init__(self):
        self.df = pd.read_csv('PlayTennis.csv')
    if __name__ == "__main__":
        o1 = Train(self.df)
        data = create_counter('PlayTennis')
        calculate(data, 'PlayTennis', 'Sunny', 'Hot', 'High', False)






print(data)