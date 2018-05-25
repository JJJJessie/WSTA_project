import json
# import os
# print os.getcwd()

with open('/Users/yifan/Desktop/WSTA_project/project_files/Elbert_buffer1.py') as f:
  data = json.load(f)


print data
# for state in data['states']:
#   del state['area_codes']
# 
# with open('new_states.json', 'w') as f:
#   json.dump(data, f, indent=2)