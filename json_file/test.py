import json


with open("json_file/DB.json","r+") as json_file:

    
    dict_ = json.load(json_file)

    if len(dict_) > 0:
    
        N = max([dict_[x]["id"] for x in range(len(dict_))])+1
    else:
        N=1

    dicdzd = {"id":N,"word":"ndoez","definition":"ncoqjnsd"}

    dict_.append(dicdzd)

with open("json_file/DB.json","w") as file:
    json.dump(dict_,file)






