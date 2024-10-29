import ijson

def read_json_from_index(file_path, start_index, batch_size=10):
    results = []
    with open(file_path, 'rb') as f:
        # Initialize JSON parser
        parser = ijson.items(f, 'item')

        # Skip items until reaching the start index
        for _ in range(start_index):
            next(parser, None)

        # Read the next `batch_size` items starting from `start_index`
        for i, item in enumerate(parser):
            if i < batch_size:
                results.append(item)
            else:
                break
    return results
