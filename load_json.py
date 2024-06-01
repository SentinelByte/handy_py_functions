import json

# Parsing JSON string
# Change the data as U need within the data param
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)

# Converting Python object to JSON string
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)
print(json_string)
