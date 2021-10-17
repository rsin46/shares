import pandas as pd
import yahoo_fin.stock_info as si

df_asx = pd.read_csv('asx.csv')
df_asx.set_index('Code', inplace = True)

# balance_sheet = si.get_balance_sheet("cba.ax").transpose()

# Get first frame as dataframe not series
# df_data = balance_sheet.iloc[[0]]

# Add new column for code
# df_data["Code"] = "CBA"
df_data = pd.DataFrame()

for index, row in df_asx.iterrows():
    print(index)
    try:
        insert_data = si.get_balance_sheet(f"{index}.ax")
        insert_data = insert_data.transpose().iloc[0]
        insert_data["Code"] = index
    except IndexError:
        insert_data = pd.DataFrame()
        insert_data["Code"] = [index]

    df_data = df_data.append(insert_data)

    df_data.to_csv('balance_sheet.csv')

