# import json
# # import os
# # print os.getcwd()
# 
# with open('/Users/yifan/Desktop/WSTA_project/project_files/Elbert_buffer1.py') as f:
#   data = json.load(f)
# 
# 
# print data
# # for state in data['states']:
# #   del state['area_codes']
# # 
# # with open('new_states.json', 'w') as f:
# #   json.dump(data, f, indent=2)



# with open('/Users/yifan/Desktop/WSTA_project/project_files/names 0.27679 copy 2.csv') as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# # content = [x.strip() for x in content] 
# 
# print content

import fileinput

# with fileinput.FileInput('/Users/yifan/Desktop/WSTA_project/project_files/names 0.27679 copy 2.csv') as file:
#     for line in file:
#         if '\"' in line:
#             print line
#             # print(line.replace(text_to_search, replacement_text), end='')
            
f = fileinput.input(files=('/Users/yifan/Desktop/WSTA_project/project_files/names 0.27679 copy 2.csv'))

for line in f:
    if '\"' in line:
        line.replace(text_to_search, replacement_text)

f.close()