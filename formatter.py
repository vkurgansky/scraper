from common import log


class Formatter:
    def __init__(self, config):
        self.__config = config

    def get_formatted_content(self, content):
        """
        Get formatted content according config.json

        :param content: source content
        :return: formatted content
        """
        log("Formatting content...")
        result_content = []

        length = self.__config['line_length']
        if not isinstance(content, list):
            content = [content]

        for line in content:
            new_lines = []
            space_pos = -1

            while len(line) > length and space_pos != 0:
                temp_line = line[:length]
                space_pos = temp_line.rfind(' ')
                new_lines.append(line[:space_pos])
                line = line[space_pos:]

            new_lines.append(line + "\n")

            result_content.extend(new_lines)

        return result_content

