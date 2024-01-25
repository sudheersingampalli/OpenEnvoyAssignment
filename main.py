from pythonLineCounter import PythonLineCounter
from javaLineCounter import JavaLineCounter

if __name__ == "__main__":
    # Example usage for Python source file
    print('Python file details')
    python_counter = PythonLineCounter("pythontestfile.py")
    python_counter.count_lines()

    #  Example usage for Java source file
    print('Java file details')
    java_counter = JavaLineCounter("javatestfile.java")
    java_counter.count_lines()
