import json

import pandas as pd

# 读取表格数据
df = pd.read_excel('test.xlsx', sheet_name="Sheet2")  # 替换成你的表格文件名或路径

# 将数据转换为JSON键值对格式
#json_data = df.set_index('数据项代码').to_dict()['数据项名称']
# 初始化空字典用于存储 JSON 键值对
json_data = {}

# 遍历表格的每一行，跳过第一行（标题行）
for index, row in df.iterrows():
    if index == 1:
        continue
    code = row['数据项代码']
    if code not in json_data:
        json_data[code] = row['数据项名称']
    else:
        print(row)


 # 将数据保存到 JSON 文件
    with open("prop_header.json", 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)