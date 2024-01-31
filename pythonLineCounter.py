from linesOfCodeCounter import LineCounter

class PythonLineCounter(LineCounter):
    def process_line(self, line):
        if self.multiline_start == False:
            if not line:
                self.blank_lines += 1
            elif line.startswith('#'):
                self.comment_lines += 1
            elif line.startswith("'''"):
                self.multiline_start =True
                self.multi_comment_lines += 1
                return
            else:
                self.code_lines += 1
        
        if self.multiline_start == True:
            if line.startswith("'''"):
                self.multiline_start = False
            self.multi_comment_lines += 1

