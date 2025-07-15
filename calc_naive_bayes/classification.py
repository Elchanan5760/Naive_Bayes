import pandas as pd

class Classify:
    def __init__(self,df):
        self.df = df
    def calculate(self,dataframe_dict, instance, my_values):
        variable_list = []
        dict_of_res = {}
        for i, variable in enumerate(dataframe_dict.keys()):
            res = 1
            variable_list.append(variable)
            for j,col in enumerate(dataframe_dict[variable]):
                for val in dataframe_dict[variable][col].items():
                    if col != instance and my_values[j] == val[0]:
                        res *= (val[1] / (dataframe_dict[variable][instance][variable] + (
                                    len(dataframe_dict[variable][col])-1)))
            dict_of_res[variable] = res * (dataframe_dict[variable][instance][variable] / (self.df[instance].count() + len(dataframe_dict[variable][instance])))
        return dict_of_res

