import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))


def translate(p):
    p = p.lower()
    if p in data:
        return data[p]
    elif len(get_close_matches(p, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if Yes or N if No : " % get_close_matches(p, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(p, data.keys())[0]]
        elif yn == "N":
            return "The Word does not exit, Please Double Check Again !"
        else:
            return "We  did not Understand your Enter Input Value .!"
    else:
        return "The Word does not exit, Please Double Check Again .!"


word = input("Enter Your Word : ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
