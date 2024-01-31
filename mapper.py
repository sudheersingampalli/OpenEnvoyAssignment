from pythonLineCounter import PythonLineCounter
from javaLineCounter import JavaLineCounter

global fileTypeDict

fileTypeDict = {
    ".py" : PythonLineCounter,
    ".java" : JavaLineCounter 
}
