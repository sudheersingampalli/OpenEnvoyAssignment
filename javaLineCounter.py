from linesOfCodeCounter import LineCounter

class JavaLineCounter(LineCounter):
    def process_line(self, line):
        
        if not line:
            self.blank_lines += 1
        elif line.startswith('//'):
            self.comment_lines += 1
        else:
            self.code_lines += 1