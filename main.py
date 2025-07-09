import pandas as pd
import numpy as np
df = pd.read_csv('PlayTennis.csv')
# buy = df.sort_values('PlayTennis')



def create_counter(instance):
    values = df[instance].unique()
    # print(values)
    list_instance = []
    for option in values:
        list_instance.append(df[(df[instance] == option)])

        # print(option)


    data = {}
    for variable in list_instance:
        print(variable)
        dict_col = {}
        for col in variable:
            print(col)
            dict_val = dict.fromkeys(df[col].unique(),1)
            for val in variable[col]:
                print(val)
                dict_val[val] += 1
            dict_col[col] = dict_val
        data[variable.head(1)[instance].iloc[0]] = dict_col
    return data

def calculate(dataframe_dict,instance,*args):
    res_2 = 1
    res_1 = 1
    variable_list = []
    for i,variable in enumerate(dataframe_dict.keys()):
        res = 1
        counter = 0
        variable_list.append(variable)
        print(variable)
        for j,col in enumerate(dataframe_dict[variable]):
            print(f"j {j}")
            print(col)
            for val in dataframe_dict[variable][col].items():
                print(val)
                if j < len(dataframe_dict[variable])-1:
                    print(f"{type(args[j])} {args[j]} == {type(val[0])} {val[0]}")
                    if args[j] == val[0]:
                        print(args[j])
                        res *= (val[1] / (dataframe_dict[variable][instance][variable] + (len(dataframe_dict[variable][col])-1)))
                        print(f"{val[1]} / {dataframe_dict[variable][instance][variable]} + {(len(dataframe_dict[variable][col])-1)}")
                        print(res)
                else:
                    if i == 0:
                        print(f"{res} * {dataframe_dict[variable][instance][variable]} / {(df[instance].count() + len(dataframe_dict[variable][col]))}")
                        res_1 = res * (dataframe_dict[variable][instance][variable] / (df[instance].count() + len(dataframe_dict[variable][col])))
                    elif i == 1:
                        print(f"{res} * {dataframe_dict[variable][instance][variable]} / {(df[instance].count() + len(dataframe_dict[variable][col]))}")
                        res_2 = res * (dataframe_dict[variable][instance][variable] / (df[instance].count() + len(dataframe_dict[variable][col])))
            print(len(dataframe_dict[variable][col]))


    print(res_1)
    print(res_2)


# def menu():
#     print("=====Menu=====")
#     columns = [input(f'What the Outlook\n'
#                      f'1 Sunny\n'
#                      f'2 Overcast\n'
#                      f'3 Rainy\n'),
#                input(f'What the Temperature\n'
#                      f'1 Hot\n'
#                      f'2 Mild\n'
#                      f'3 Cool\n'),
#                input(f'What the Humidity\n'
#                      f'1 High\n'
#                      f'2 Normal\n'),
#                input(f'Is it the Windy\n'
#                      f'1 True\n'
#                      f'2 False\n')]
#     data = create_counter()

    # calculate(data)#,columns[0],columns[1],columns[2],columns[3])
    # print(data)

data = create_counter('PlayTennis')

calculate(data,'PlayTennis','Sunny', 'Hot', 'High', False)
print(data)