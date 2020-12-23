# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re
from keycodeTranslations import (
    getQwertyColemakTranslations,
    getQwertyDvorakTranslations,
    getQwertyWorkmanTranslations,
    getDvorakQwertyTranslations,
    getColemakQwertyTranslations,
)


def extractOutput(keyCode1, xmlInput):
    regularExpression = r"code=\"" + str(keyCode1) + '"' + r"\s+output\s*=\s*\"(.*?)\""
    output1 = re.search(regularExpression, xmlInput)
    if output1:
        return output1.group(1)
    else:
        return None


def extractOutputOrAction(keyCode1, xmlInput):
    """Sometimes a key starts an action, this will allow replacement of those keys"""
    regularExpression = (
        r"code=\"" + str(keyCode1) + '"' + r"\s+(output=\".*?\"|action=\".*?\")"
    )
    output1 = re.search(regularExpression, xmlInput)
    if output1:
        return output1.group(1)
    else:
        return None


def makeReplacementFunction(replacementOutput):
    """
    changes something like 'output="S"' to 'output="D"'
    """
    return lambda matchObject: matchObject.group(1) + replacementOutput + '"'


def makeAttributeReplacementFunction(replacementOutput):
    """
    changes something like 'output="S"' to 'action="act1"'
    """
    return lambda matchObject: matchObject.group(1) + replacementOutput


def replaceOutput(keyCode1, newOutput, xmlInput):
    regularExpression = (
        r"(code=\"" + str(keyCode1) + '"' + r"\s+output\s*=\s*\")(.*?)\""
    )
    if re.search(regularExpression, xmlInput):
        return re.sub(regularExpression, makeReplacementFunction(newOutput), xmlInput)
    else:
        return xmlInput


def replaceOutputOrAction(keyCode1, newOutput, xmlInput):
    regularExpression = (
        r"(code=\""
        + str(keyCode1)
        + r"\"\s+)(output\s*=\s*\".*?\"|action\s*=\s*\".*?\")"
    )
    if re.search(regularExpression, xmlInput):
        return re.sub(
            regularExpression, makeAttributeReplacementFunction(newOutput), xmlInput
        )
    else:
        return xmlInput


# Note swapping more than two keys will not work for converting a whole layout. This is due to the fact that the order those swaps happen makes a difference.


def convertKeyMapUsingTranslation(xmlForAKeyMap, keyCodeTranslationList):
    # Calculate all the changes we need to make. I.e. determine
    # what character belongs in which key.
    print(keyCodeTranslationList)
    changesToWrite = []
    for (sourceKeyCode, destinationKeyCode) in keyCodeTranslationList:
        # records that we are to set the output of the key at the dvorakCode,
        # to what the output is in the key at the qwerty code.
        outputOnKey = extractOutputOrAction(sourceKeyCode, xmlForAKeyMap)
        if outputOnKey is not None:
            changeToWrite = (destinationKeyCode, outputOnKey)
            changesToWrite.append(changeToWrite)

    result = xmlForAKeyMap
    print("changes to write:")
    if changesToWrite:
        print("\n".join(map(str, sorted(changesToWrite))))
    # Make those changes
    for (keyCode, output) in changesToWrite:
        result = replaceOutputOrAction(keyCode, output, result)

    return result


def convertKeyMapFromQwertyToDvorak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getQwertyDvorakTranslations())


def convertKeyMapFromQwertyToColemak(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getQwertyColemakTranslations())


def convertKeyMapFromQwertyToWorkman(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getQwertyWorkmanTranslations())


def convertKeyMapFromDvorakToQwerty(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getDvorakQwertyTranslations())


def convertKeyMapFromDvorakToColemak(xmlForAKeyMap):
    return convertKeyMapFromQwertyToColemak(
        convertKeyMapFromDvorakToQwerty(xmlForAKeyMap)
    )


def convertKeyMapFromDvorakToWorkman(xmlForAKeyMap):
    return convertKeyMapFromQwertyToWorkman(
        convertKeyMapFromDvorakToQwerty(xmlForAKeyMap)
    )


def convertKeyMapFromColemakToDvorak(xmlForAKeyMap):
    return convertKeyMapFromQwertyToDvorak(
        convertKeyMapFromColemakToQwerty(xmlForAKeyMap)
    )


def convertKeyMapFromColemakToQwerty(xmlForAKeyMap):
    return convertKeyMapUsingTranslation(xmlForAKeyMap, getColemakQwertyTranslations())


def convertKeyMapFromColemakToWorkman(xmlForAKeyMap):
    return convertKeyMapFromQwertyToWorkman(
        convertKeyMapFromColemakToQwerty(xmlForAKeyMap)
    )
