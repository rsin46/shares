import pandas as pd
import pickle
import os
import yahoo_fin.stock_info as si

df_asx = pd.read_csv('asx.csv')
df_asx.set_index('Code', inplace = True)

files = os.listdir('input/')

for index, row in df_asx.iterrows():
    print(index)
    if f"{index}.p" in files:
        continue

    try:
        insert_data = si.get_financials(f"{index}.ax")

        with open(f'input/{index}.p', 'wb') as handle:
            pickle.dump(insert_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    except (IndexError, KeyError, TypeError):
        pass

    # with open('filename.pickle', 'rb') as handle:
        # b = pickle.load(handle)
