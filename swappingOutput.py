# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re

input = """		<key code="0" output="A"/>
			<key code="1" output="S"/>"""

expectedOutput = """		<key code="0" output="S"/>
			<key code="1" output="A"/>"""


def extractOutput(keyCode1, xmlInput):
    regularExpression = r"code=\"" + str(keyCode1) + '"' + r"\s+output=\"(.*?)\""
    output1 = re.search(regularExpression, xmlInput)
    return output1.group(1)


def makeReplacementFunction(replacementOutput):
    return lambda matchObject: matchObject.group(1) + replacementOutput + '"'


def replaceOutput(keyCode1, newOutput, xmlInput):
    regularExpression = r"(code=\"" + str(keyCode1) + '"' + r"\s+output=\")(.*?)\""
    return re.sub(regularExpression, makeReplacementFunction(newOutput), xmlInput)


def swapKeyOutputs(keyCode1, keyCode2, xmlInput):
    output1 = extractOutput(keyCode1, xmlInput)
    output2 = extractOutput(keyCode2, xmlInput)
    print("keycode:", keyCode1, "output:", output1)
    print("keycode:", keyCode2, "output:", output2)
    result = replaceOutput(keyCode1, output2, xmlInput)
    result = replaceOutput(keyCode2, output1, result)
    return result


output = swapKeyOutputs(0, 1, input)
print("expected:\n", expectedOutput)
print("actual:\n", output)
