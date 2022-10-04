from collections import defaultdict
import json

def dynamic_dict():
    return defaultdict(dynamic_dict)

d = dynamic_dict()
d["root"]["level_1"]["one"] = "Bacon"
d["root"]["level_1"]["two"] = "Eggs"
d["root"]["level_2"]["something_else"] = "Spam"

stringified = json.dumps(d)
d = json.loads(stringified)

print(d)

# {'root': {'level_1': {'one': 'Bacon', 'two': 'Eggs'}, 'level_2': {'something_else': 'Spam'}}}
