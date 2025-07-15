import pandas as pd
import numpy as np
from UI import Menu

if __name__ == "__main__":
    o1 = Menu(pd.read_csv('phishing.csv'))
    o1.menu()






