def array_to_json(columns, data):
    # Convert the list of dictionaries to a JSON object
    return [{columns[i]: row[i] for i in range(len(columns))} for row in data]
