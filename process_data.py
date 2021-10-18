import pandas as pd
import pickle
import os

files = os.listdir('input/')
frames = ['yearly_income_statement',  'yearly_balance_sheet',  'yearly_cash_flow',  'quarterly_income_statement',  'quarterly_balance_sheet',  'quarterly_cash_flow']
OUTPUT = 'ASXFY21.xlsx'

# Empty data frames for each type of data for four time periods
out_list = [{}, {}, {}, {}]

for out_dict in out_list:
    for statement_type in frames:
        out_dict[statement_type] = pd.DataFrame()

def save_data(data_dict, code_file, out_dict, index):
    code = code_file.split('.')[0]
    print(code)
    for statement_type in frames:
        statement = data_dict[statement_type]

        try:
            insert_data = statement.transpose().iloc[index]
            insert_data["Code"] = code
        except IndexError:
            insert_data = pd.DataFrame()
            insert_data["Code"] = [code]

        out_dict[statement_type] = out_dict[statement_type].append(insert_data)

    return out_dict

for code_file in files:
    if code_file.endswith('.p'):
        with open(f'input/{code_file}', 'rb') as handle:
            data_dict = pickle.load(handle)

        # Save data for each time period. First in the list is most recent('21), last is oldest ('18)
        for i, _ in enumerate(out_list):
            out_list[i] = save_data(data_dict, code_file, out_list[i], i)

with pd.ExcelWriter(OUTPUT) as writer:
    for i, out_dict in enumerate(out_list):
        for statement_type in frames:
            out_dict[statement_type].to_excel(writer,f'{statement_type}{i}')
    writer.save()
    
