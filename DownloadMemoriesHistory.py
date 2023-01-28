import json, requests, os, uuid
from os import path
from concurrent.futures import ThreadPoolExecutor


class MemoriesDownloader:

    # Initialise
    def __init__(self, path_to_json, download_location, thread_count=3):
        # Initialise locations
        self.path_to_json = path_to_json
        self.download_location = download_location
        # Initialise Thread count
        self.thread_count = thread_count

        self.split_memories = []
        self.json_data = []

    def split_into_n_parts(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i: i+n]

    # Read the JSON file made previously
    def load_json(self):
        with open(self.path_to_json) as json_file:
            self.json_data = json.load(json_file)
        self.split_memories = list(self.split_into_n_parts(self.json_data, 
                                                                self.thread_count))

    # Each Thread accesssing to download
    def handle_download(self, memories_list):
        for memory in memories_list:
            file_name = str(uuid.uuid4().hex)
            file_name+='.'+memory['fileType']
            file_path = path.join(os.getcwd()+self.download_location, file_name)
            print('downloading ', file_name)
            url = memory['awsLink']
            response = requests.get(url)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print('downloaded ', file_name)

    def download_memories(self):
        executor = ThreadPoolExecutor(self.thread_count)
        futures = [executor.submit(self.handle_download, memories) for memories in self.split_memories]


