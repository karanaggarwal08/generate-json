import os
import json

PREFIX = "IVT_PUMKIN134"
my_array = []

for name, value in os.environ.items():
    if name.startswith(PREFIX):
        # Split name and convert to lowercase
        parts = name.split("_")
        product = parts[2].lower()
        tag = parts[3].lower()
        infra = parts[4].lower()

        dict = {
            "infra_name": infra,
            "product": product,
            "tag": tag,
            "additonal_data": value,
        }
        # Append JSON string to array
        my_array.append(dict)
json_str = json.dumps(my_array)
env_file = os.getenv("GITHUB_ENV")
# print(json_str)
with open(env_file, "a") as myfile:
    myfile.write("ADDITIONAL_INFRA={}".format(json_str))
