import ijson
from tqdm import tqdm

def read_json_from_index(file_path, start_index, batch_size=10):
    results = []
    with open(file_path, 'rb') as f:
        # Initialize JSON parser
        parser = ijson.items(f, 'item')
        
        # Initialize tqdm progress bar for skipping items
        for _ in tqdm(range(start_index), desc="Skipping to start index"):
            next(parser, None)

        # Initialize tqdm progress bar for reading the batch of items
        for i, item in tqdm(enumerate(parser), total=batch_size, desc="Reading batch"):
            if i < batch_size:
                results.append(item)
            else:
                break

    return results
