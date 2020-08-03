import argparse
from scraper import Scraper
from common import init_config, TRY_AGAIN_STR
from extractor import Extractor
from formatter import Formatter
from saver import ContentSaver

"""
Short algo:
    0st - initialize config
    1st - get html with scrapper
    2nd - clear tags and so on with extractor
    3rd - format content with formatter
    4th - save content with saver
"""

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, help="url to get readable context")
args = parser.parse_args()

if args.url:
    config = init_config()
    html = Scraper.get_content_in_html(args.url)
    clear_content = Extractor(config).get_clear_content_from_html(html)
    formatted_content = Formatter(config).get_formatted_content(clear_content)
    ContentSaver.save_content(formatted_content, args.url)
else:
    print(TRY_AGAIN_STR)
