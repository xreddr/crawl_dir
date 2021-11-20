#Compare crawled json objects!
import os
import datetime
import json

with open("crawlData.json", "r") as infile:
    input_object = json.load(infile)
infile.close()

target_dir = input_object["criteria"]
totalFiles = 0
totalDir = 0
date = str(datetime.datetime.now())
data_list = []

for root, dirs, files in os.walk(target_dir):
    #print("Searching in : ", root)
    for directories in dirs:
        data_list.append(os.path.join(root, directories))
        #print(os.path.join(root, directories))
        totalDir += 1
    for Files in files:
        data_list.append(os.path.join(root, Files))
        #print(os.path.join(root, Files))
        totalFiles += 1
    break

data_object = {
    "criteria" : target_dir,
    "paths" : data_list,
    "files" : totalFiles,
    "directories" : totalDir,
    "date" : date
}

del_list = [item for item in input_object["paths"] if item not in data_object["paths"]]
add_list = [item for item in data_object["paths"] if item not in input_object["paths"]]

report_object = json.dumps(data_object, indent=2)
print("Current content: ")
print(report_object)

if bool(del_list) == False:
    print("No items deleted.")
else:
    print("Removed items: ")
    print(json.dumps(del_list, indent=2))
    
if bool(add_list) == False:
    print("No items added.")
else:
    print("Added items: ")
    print(json.dumps(add_list, indent=2))
print("Since: " + input_object["date"])
