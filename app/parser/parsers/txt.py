from parser.interface import ParserInterface


class TxtParser(ParserInterface):
    def parse(file_path) -> str:
        with open(file_path, "r") as file:
            txt = file.read()

        return txt
