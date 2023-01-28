import sys, requests, json

class AWSGetLinkGenerator:

    def __init__(self, path_to_json, path_to_output_json):
        # Initialise path
        self.path_to_json = path_to_json
        self.path_to_output_json = path_to_output_json
        
        # Initialize for links
        self.aws_links = []
        self.memories_data = []

        # Initialise names
        self.JSON_KEY_TO_DOWNLOAD_LINKS_KEY = r'Saved Media'
        self.FAKE_DOWNLOAD_LINKS_KEY = r'Download Link'
        self.MEDIA_TYPE = r'Media Type'

    # Open the json file and read contents 
    def load_json(self):
        with open(self.path_to_json) as json_file:
            self.memories_data = json.load(json_file)

    # Get the custom url in between
    def get_file_type(self, media_type):
        if media_type=='Image': return 'png'
        elif media_type=='Video': return 'mp4'
        else: return 'mp4'


    def handle_link_generation(self):
        # Array to catch real downloadable links
        aws_links_list = []
        # Iterate over the JSON data
        TOTAL_LINKS = len(self.memories_data[self.JSON_KEY_TO_DOWNLOAD_LINKS_KEY])
        for linkcount, memory in enumerate(self.memories_data[self.JSON_KEY_TO_DOWNLOAD_LINKS_KEY]):
            # Send POST request for actual download links
            response = requests.post(memory[self.FAKE_DOWNLOAD_LINKS_KEY])
            url = response.content.decode('utf-8')
            aws_links_list.append({
                'date': memory['Date'][:len(memory['Date']) - 4],
                'fileType': self.get_file_type(memory[self.MEDIA_TYPE]),
                'awsLink': url
            })
            # Count real time and check download links
            sys.stdout.write(f'Link parsed : {linkcount} out of {TOTAL_LINKS}\r')

        # Write Output URL off to JSON 
        with open(self.path_to_output_json, 'w') as output:
            json.dump(aws_links_list, output)
            
        # Iterate all the download links and send post requests to AWS server and save links in array

