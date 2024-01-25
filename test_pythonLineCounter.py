# test_python_line_counter.py
import unittest
from pythonLineCounter import PythonLineCounter

class TestPythonLineCounter(unittest.TestCase):

    def setUp(self):
        self.python_line_counter = PythonLineCounter("pythontestfile.py")

    def test_blank_lines(self):
        self.python_line_counter.count_lines()
        self.assertEqual(self.python_line_counter.blank_lines, 4)

    def test_comment_lines(self):
        self.python_line_counter.count_lines()
        self.assertEqual(self.python_line_counter.comment_lines, 7)

    def test_code_lines(self):
        self.python_line_counter.count_lines()
        self.assertEqual(self.python_line_counter.code_lines, 10)

    def test_total_lines(self):
        self.python_line_counter.count_lines()
        self.assertEqual(self.python_line_counter.total_lines, 21)

if __name__ == '__main__':
    unittest.main()
