import re
import pathlib
from common import log, reg_protocol


class ContentSaver:
    @staticmethod
    def save_content(content, url):
        """
        Save content to file path according url

        :param content: source content
        :param url: source url
        """

        filepath = ContentSaver.__get_filepath_from_url(url)

        log(f"Saving content in '{filepath}'...")
        with open(f"{filepath}", "w") as file:
            if isinstance(content, list):
                for line in content:
                    file.write(line + "\n")
            else:
                file.write(content)
        log(f"Content has been saved in '{filepath}'.")

    @staticmethod
    def __get_filepath_from_url(url):
        """
        Get file path from url and create folders, if they don't exist

        :param url: source url
        :return: file path
        """
        path = pathlib.Path.cwd()

        result_path = re.sub(reg_protocol, "", url)
        result_path = result_path.split('/')
        result_path = [element for element in result_path if element]
        for current in result_path:
            path = path / current
            try:
                pathlib.Path.mkdir(path)
            except FileExistsError:
                continue

        return path / "index.txt"
