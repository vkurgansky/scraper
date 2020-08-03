from datetime import datetime as dt
from json import load


# reg strings
reg_header = r'\<h[1-9]\>.*\<\/h[1-9]\>'
reg_paragraph = r'\<p\>.*\<\/p\>'
reg_all = r'\<[ph][1-9]?\>.*\<\/[ph][1-9]?\>'

reg_header_start = r'\<h[1-9]\>'
reg_header_end = r'\<\/h[1-9]\>'

reg_paragraph_start = r'\<p\>'
reg_paragraph_end = r'\<\/p\>'

reg_link = r'https?:\/\/[^"]+'
reg_protocol = r'https?\:?\/{2}'

reg_garbage = r'\<\/?[\w\"\=\s\'\-,А-я]*\>'


# consts
garbage_list = [
    '&mdash;',
    '&ndash;',
    '&raquo;',
    '&laquo;',
    '&nbsp;',
    '&mbsp;',
    '&lt;',
    '&gt;'
]

LINK_TAG_CLOSE = '</a>'
TAG_END = '>'
LINK_TAG_START = '<a '
IMG_TAG_START = '<img '

TRY_AGAIN_STR = "Please, enter url as parameter using '--url' or '-u' and try again."

# config consts
CONFIG_PATH = "./config.json"
DEFAULT_CONFIG = {
    "line_length": 80,
    "link_format": "[{0}] "
}


# logger
LOG_STR = '{0} {1}'


def log(message):
    print(LOG_STR.format(dt.now().time(), message))


# config loading
def __load_config(path):
    """
    Try to load config from path.
    If file doesn't exist, then will be loaded default values.

    :param path: path to config file
    :return: dict with values from config
    """
    log(f"Loading config from '{path}'...")
    try:
        with open(path, 'r') as file:
            temp_config = load(file)
    except Exception as e:
        log(f"Error has occurred while loading config with details: '{e}'.")
        temp_config = None

    if not temp_config:
        log("Setting default config values...")
        temp_config = DEFAULT_CONFIG

    return temp_config


def init_config():
    return __load_config(CONFIG_PATH)
