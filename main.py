from pythonLineCounter import PythonLineCounter
from javaLineCounter import JavaLineCounter
from mapper import fileTypeDict
import os

if __name__ == "__main__":

    fileName = input("enter file name")
    _ , fileType = os.path.splitext(fileName)

    classType = fileTypeDict[fileType]
    classType(fileName).count_lines()
    # if fileType == 'py':
    #     print('Python file details')
    #     python_counter = PythonLineCounter("pythontestfile.py")
    #     python_counter.count_lines()


    # #  Example usage for Java source file
    # print('Java file details')
    # java_counter = JavaLineCounter("javatestfile.java")
    # java_counter.count_lines()
