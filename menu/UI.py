from calc_naive_bayes.check import Check
from calc_naive_bayes.model_coach import Train
from calc_naive_bayes.classification import Classify

class Menu:
    def __init__(self,df):
        self.df = df
    def menu(self):
        cond = True
        while cond:
            print('=======Menu=======')
            navigation = input(f"1. Your values\n"
                               f"2. Check data\n"
                               f"0. Exit\n")
            if navigation == '1':
                self.choose_values()
            elif navigation == '2':
                self.choice_check_data()
            elif navigation == '0':
                cond = False
            else:
                print("Invalid value\n"
                      "Please try again!")
    def choose_values(self):
        cond = False
        columns = self.df.columns.tolist()
        col_not_target = []
        target = ''
        while not cond:
            print("What is your target:")
            options = []
            for i,col in enumerate(columns):
                options.append(f'{i+1}')
                print(f"{i+1}. {col}")
            target = input()
            if target in options:
                cond = True
                col_not_target = [feature for feature in columns if feature != columns[int(target)-1]]
            if not cond:
                print('Invalid value\n'
                      'Please try again!')
        count = 0
        values = []
        while count < len(col_not_target):
            possible_values = self.df[columns[count]].unique().tolist()
            print(f"What the {columns[count]}:")
            options = []
            for i,val in enumerate(possible_values):
                print(f"{i+1}. {val}")
                options.append(f'{i+1}')
            choice = input()
            if choice in options:
                count += 1
                values.append(possible_values[int(choice)-1])
                print(possible_values[int(choice)-1])
                print(type(possible_values[int(choice)-1]))
            else:
                print('Invalid value\n'
                      'Please try again!')
        couch = Train(self.df)
        calc = Classify(self.df)
        result = calc.calculate(couch.create_counter(columns[int(target) - 1]), columns[int(target) - 1], values)
        sumi = 0
        for val in result.values():
            sumi += val
        final_answer = ''
        is_first = True
        for item in result.items():
            print(f"{item[0]}: {(item[1]/sumi)*100}%")
            if is_first:
                final_answer = item[0]
                is_first = False
            if item[1] > result[final_answer]:
                final_answer = item[0]
        print(f'The answer is {final_answer}!')

    def choice_check_data(self):
        check = Check(self.df)
        cond = True
        from_data = ''
        target = ''
        while cond:
            print(f"What is your target line:")
            for i,col in enumerate(self.df.columns):
                print(f'{i+1}. {col}')
            target = input()
            from_data = input(f"How many from {len(self.df)} do you want to check:\n")
            if target.isdigit() and from_data.isdigit():
                from_data = int(from_data)
                target = int(target)
                if from_data < len(self.df) and target <= len(self.df.columns):
                    cond = False
                else:
                    print('Invalid value\n'
                          'Please try again!')
            else:
                print('Invalid value\n'
                      'Please try again!')
        check.check_data(from_data,self.df.columns.tolist()[target-1])

# o1 = Check(pd.read_csv('phishing.csv'))
# o1.check_data(3300,'class')