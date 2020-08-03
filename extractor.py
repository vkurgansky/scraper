import re
from common import log, garbage_list, reg_all, reg_link, reg_header_start, reg_header_end, reg_garbage, \
    reg_paragraph_start, reg_paragraph_end, LINK_TAG_START, LINK_TAG_CLOSE, IMG_TAG_START, TAG_END


class Extractor:
    def __init__(self, config):
        self.__config = config

    def get_clear_content_from_html(self, html):
        """
        Get content without html-tags from html source

        :param html: HTML web-page source
        :return: content without html-tags
        """
        log("Getting content from html...")
        main_content = re.findall(reg_all, html)
        return self.__get_context_without_tags(main_content)

    def __get_context_without_tags(self, content):
        """
        Clear content from html-tags

        :param content: source content
        :return: content without html-tags
        """
        log("Clearing content...")
        clear_content = []

        if not isinstance(content, list):
            content = [content]

        # cleansing occurs line by line
        for idx, line in enumerate(content):
            clear_line = self.__get_clear_line(line)
            clear_content.append(clear_line)

        return clear_content

    def __get_clear_line(self, line):
        """
        Get line without html-tags

        :param line: html line
        :return: line without html-tags
        """
        # clear line from <p></p> tags
        line = re.sub(reg_paragraph_start, "", line)
        line = re.sub(reg_paragraph_end, "", line)

        # clear line from <h[1-9]></h[1-9]> tags
        line = re.sub(reg_header_start, "", line)
        line = re.sub(reg_header_end, "", line)

        # clear line from links
        line = Extractor.__get_line_with_formatted_links(line, self.__config["link_format"])

        # clear line from another garbage (unsupported tags and so on)
        line = Extractor.__get_line_without_garbage(line)

        return line

    @staticmethod
    def __get_line_with_formatted_links(line, link_format):
        """
        Get line with links in link_format

        :param line: source line
        :param link_format: format for link
        :return: Line with link in link_format
        """
        result_line = []
        # find all links with positions in line
        links = [match.group() for match in re.finditer(reg_link, line)]

        for link in links:
            href_start = line.find(LINK_TAG_START)
            img_start = line.find(IMG_TAG_START)

            if href_start != -1:
                # if href tag was found, then replace it on the link from tag
                tag_end = line[href_start:].find(TAG_END) + 1
                line = line.replace(line[href_start: tag_end + href_start], link_format.format(link))
                result_line.append(line[:line.find(LINK_TAG_START)].replace(LINK_TAG_CLOSE, ""))
                line = line.replace(line[:line.find(LINK_TAG_START)], "")
            elif img_start != -1:
                # if img tag was found, then replace it on img link
                tag_end = line[img_start:].find(TAG_END) + 1
                line = line.replace(line[img_start: tag_end + img_start], link_format.format(link))
                result_line.append(line[:line.find(IMG_TAG_START)])
                line = line.replace(line[:line.find(IMG_TAG_START)], "")

        return "".join(result_line) + line

    @staticmethod
    def __get_line_without_garbage(line):
        """
        Get line without tags, which mentioned in common.py

        :param line: source line
        :return: line without garbage
        """
        garbage_list_reg = re.findall(reg_garbage, line)
        if garbage_list_reg:
            garbage_list.extend(list(garbage_list_reg))

        for garbage_line in garbage_list:
            line = line.replace(garbage_line, " ")

        return line
