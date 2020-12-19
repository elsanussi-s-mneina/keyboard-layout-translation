# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re
from keycodeTranslations import (
    getQwertyColemakTranslations,
    getQwertyDvorakTranslations,
    getColemakDvorakTranslations,
    getDvorakColemakTranslations,
    getDvorakQwertyTranslations,
    getColemakQwertyTranslations,
)


def extractOutput(keyCode1, xmlInput):
    regularExpression = r"code=\"" + str(keyCode1) + '"' + r"\s+output=\"(.*?)\""
    output1 = re.search(regularExpression, xmlInput)
    if output1:
        return output1.group(1)
    else:
        return None


def makeReplacementFunction(replacementOutput):
    return lambda matchObject: matchObject.group(1) + replacementOutput + '"'


def replaceOutput(keyCode1, newOutput, xmlInput):
    regularExpression = r"(code=\"" + str(keyCode1) + '"' + r"\s+output=\")(.*?)\""
    if re.search(regularExpression, xmlInput):
        return re.sub(regularExpression, makeReplacementFunction(newOutput), xmlInput)
    else:
        return xmlInput


# Note swapping more than two keys will not work for converting a whole layout. This is due to the fact that the order those swaps happen makes a difference.


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


def convertKeyMapFromQwertyToColemak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getQwertyColemakTranslations())


def convertKeyMapFromDvorakToQwerty(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getDvorakQwertyTranslations())


def convertKeyMapFromDvorakToColemak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getDvorakColemakTranslations())


def convertKeyMapFromColemakToDvorak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getColemakDvorakTranslations())


def convertKeyMapFromColemakToQwerty(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getColemakQwertyTranslations())
