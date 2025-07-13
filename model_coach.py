

class Train:
    def __init__(self,df):
        self.df = df
    def create_counter(self,instance):
        values = self.df[instance].unique()
        # print(values)
        list_instance = []
        for option in values:
            list_instance.append(self.df[(self.df[instance] == option)])
        data = {}
        for variable in list_instance:
            print(variable)
            dict_col = {}
            for col in variable:
                print(col)
                dict_val = dict.fromkeys(self.df[col].unique(),1)
                for val in variable[col]:
                    print(val)
                    dict_val[val] += 1
                dict_col[col] = dict_val
            data[variable.head(1)[instance].iloc[0]] = dict_col
        return data