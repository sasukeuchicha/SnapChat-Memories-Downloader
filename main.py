from DownloadFromAWSLinks import AWSGetLinkGenerator
from DownloadMemoriesHistory import MemoriesDownloader
import time

if __name__ == '__main__':
    PATH_TO_INPUT = r'./SnapChat-Input'
    PATH_TO_JSON = PATH_TO_INPUT+r'/memories_history.json'
    PATH_TO_OUTPUT_JSON = PATH_TO_INPUT+r'/aws_links.json'
    PATH_TO_DOWNLOADED_FILES = r'\Memories-Output'
    NUMBER_OF_THREADS_DEFAULT = 3
    link_generator = AWSGetLinkGenerator(PATH_TO_JSON, PATH_TO_OUTPUT_JSON)
    link_generator.load_json()
    link_generator.handle_link_generation()
    memories_downloader = MemoriesDownloader(PATH_TO_OUTPUT_JSON, PATH_TO_DOWNLOADED_FILES, NUMBER_OF_THREADS_DEFAULT)
    memories_downloader.load_json()
    memories_downloader.download_memories()