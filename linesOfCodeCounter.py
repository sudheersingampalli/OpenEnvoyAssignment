from abc import ABC, abstractmethod

class LineCounter(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.blank_lines = 0
        self.comment_lines = 0
        self.code_lines = 0
        self.total_lines = 0

    def count_lines(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            self.total_lines = len(lines)

            for line in lines:
                self.process_line(line.strip())

        self.print_results()

    @abstractmethod
    def process_line(self, line):
        pass

    def print_results(self):
        print(f'Blank: {self.blank_lines}')
        print(f'Comments: {self.comment_lines}')
        print(f'Code: {self.code_lines}')
        print(f'Total: {self.total_lines}')
