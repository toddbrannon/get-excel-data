import pandas as pd 

spreadsheet_file = pd.ExcelFile('C:/Users/Public/TQB/Python/test_files/Monthly_Savings_report.xlsx')
worksheets = spreadsheet_file.sheet_names
month = 'April'
appended_data = []

for sheet_data_name in worksheets:   
    df = pd.read_excel(spreadsheet_file, sheet_data_name, header=2)
    df = df[['COID', month]].where(df[month] > 0)
    df = df.dropna()
    df['Init ID'] = sheet_data_name
    df = df[['Init ID', 'COID', month]]
    appended_data.append(df)

appended_data = pd.concat(appended_data)

appended_data['Init ID'] = pd.to_numeric(appended_data['Init ID'])

appended_data.to_excel('C:/Users/Public/TQB/Python/test_files/Savings Upload ' + month + ' 2019.xlsx', index=False)
print('Upload file created!')