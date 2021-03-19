import pandas
import json

excel_data_df = pandas.read_excel('records.xlsx', sheet_name='Sheet1')

json_str = excel_data_df.to_json()
print(json_str)
#convert python object to a json string 
json_object = json.dumps(json_str, indent = 4) 

print('Excel Sheet to JSON:\n', json_object)
with open("records.json", "w") as outfile: 
    outfile.write(json_object) 