import json


format_list = []

with open(r"C:\Users\benco\Desktop\cool\Py\py-dl\Pinna Park [7uYv1pbjsYU].info.json", mode="r", encoding="UTF-8") as file:
    output = json.load(file)

# for outputs in enumerate(output["formats"]):
#     print(f"{outputs[0]} - {outputs[1]["resolution"]} - {outputs[1]["ext"]}")
#     format_list.append(outputs[1]["format_id"])

# print("")

# for v in format_list:
#     print(v)

#using a for loop seems to step up for the index from the given index
print(output["formats"][0]["ext"])


#identify, cut out, reintroduce (sometimes)

#1 cor 10:31
# Do I still go to God when this is in my life?
# Can I do this for the glory of God? 
# If it were gone, would I lack?