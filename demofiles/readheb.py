import json
from types import DynamicClassAttribute

with open('Lang\Language_definitions.json', encoding="utf-8") as f:
    data = json.load(f)
    print(data)

