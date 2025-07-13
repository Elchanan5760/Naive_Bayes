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
            print(variable)
            for j,col in enumerate(dataframe_dict[variable]):
                print(col)
                for val in dataframe_dict[variable][col].items():
                    print(val)
                    if col != instance and my_values[j] == val[0]:
                        res *= (val[1] / (dataframe_dict[variable][instance][variable] + (
                                    len(dataframe_dict[variable][col])-1)))
                        print(
                            f"{val[1]} / {dataframe_dict[variable][instance][variable]} + {(len(dataframe_dict[variable][col]) - 1)}")
                        print(res)
            print(f"{res} * {dataframe_dict[variable][instance][variable]} / {(self.df[instance].count() + len(dataframe_dict[variable][instance]))}")
            dict_of_res[variable] = res * (dataframe_dict[variable][instance][variable] / (self.df[instance].count() + len(dataframe_dict[variable][instance])))
            print(len(dataframe_dict[variable][instance]))
        print(variable_list)
        print(dict_of_res)

        return dict_of_res

