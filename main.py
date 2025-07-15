import pandas as pd
from menu.UI import Menu
from utils import load_df
from utils.load_df import MyUtils

if __name__ == "__main__":
    util = MyUtils()
    o1 = Menu(util.load_data())
    o1.menu()






