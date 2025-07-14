

class Train:
    def __init__(self,df):
        self.df = df
    def create_counter(self,target):
        values = self.df[target].unique()
        # print(values)
        list_instance = []
        for option in values:
            list_instance.append(self.df[(self.df[target] == option)])
        data = {}
        for variable in list_instance:
            dict_col = {}
            for col in variable:
                dict_val = dict.fromkeys(self.df[col].unique(),1)
                for val in variable[col]:
                    dict_val[val] += 1
                dict_col[col] = dict_val
            data[variable.head(1)[target].iloc[0]] = dict_col
        return data