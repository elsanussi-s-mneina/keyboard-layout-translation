# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re
from keycodeTranslations import (
    qwertyColemakDvorakTranslations,
    getQwertyDvorakTranslations,
)


def extractOutput(keyCode1, xmlInput):
    regularExpression = r"code=\"" + str(keyCode1) + '"' + r"\s+output=\"(.*?)\""
    output1 = re.search(regularExpression, xmlInput)
    if not output1:
        return xmlInput
    return output1.group(1)


def makeReplacementFunction(replacementOutput):
    return lambda matchObject: matchObject.group(1) + replacementOutput + '"'


def replaceOutput(keyCode1, newOutput, xmlInput):
    regularExpression = r"(code=\"" + str(keyCode1) + '"' + r"\s+output=\")(.*?)\""
    return re.sub(regularExpression, makeReplacementFunction(newOutput), xmlInput)


# Note swapping more than two keys will not work for converting a whole layout. This is due to the fact that the order those swaps happen makes a difference.


def swapKeyOutputs(keyCode1, keyCode2, xmlInput):
    """This is only useful for swapping two keys at a time. It becomes a mess when
    you need to swap more than two keys. This function is not as useful as I thought it would be."""
    output1 = extractOutput(keyCode1, xmlInput)
    output2 = extractOutput(keyCode2, xmlInput)
    if not output1 or not output2:
        return xmlInput

    print("keycode:", keyCode1, "output:", output1)
    print("keycode:", keyCode2, "output:", output2)
    result = replaceOutput(keyCode1, output2, xmlInput)
    result = replaceOutput(keyCode2, output1, result)

    return result


def convertKeyMapUsingTranslation(xmlForAKeyMap, keyCodeTranslationList):
    # Calculate all the changes we need to make. I.e. determine
    # what character belongs in which key.
    changesToWrite = []
    for (sourceKeyCode, destinationKeyCode) in keyCodeTranslationList:
        # records that we are to set the output of the key at the dvorakCode,
        # to what the output is in the key at the qwerty code.
        outputOnKey = extractOutput(sourceKeyCode, xmlForAKeyMap)
        changeToWrite = (destinationKeyCode, outputOnKey)
        changesToWrite.append(changeToWrite)

    result = xmlForAKeyMap
    # Make those changes
    for (keyCode, output) in changesToWrite:
        result = replaceOutput(keyCode, output, result)

    return result


def convertKeyMapFromQwertyToDvorak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getQwertyDvorakTranslations())
