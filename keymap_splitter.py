# For splitting one XML string into multiple ones each with only one keymap at most.
import re

oneKeymapRegExp = re.compile(r"(<\s*keyMap.*?>.*?<\s*/\s*keyMap\s*>)", flags=re.IGNORECASE | re.DOTALL)

beforeFirstKeymapRegExp = re.compile(r"^(.*?)<\s*keymap.*?>", flags=re.IGNORECASE | re.DOTALL)
allKeyMapRegExp = re.compile(r"(<\s*keyMap.*?>.*<\s*/\s*keyMap\s*>)", flags=re.IGNORECASE | re.DOTALL) 
# This one is greedy and will take from the first keymap element to the last one.

afterLastKeymapRegExp = re.compile(r"(?<=</keymap>)(.*?)$", flags=re.IGNORECASE | re.DOTALL)

def hasKeyMap(xmlInput):
    return oneKeymapRegExp.search(xmlInput) is not None


def hasCloseKeyMapTag(xmlInput):
    return keymapCloseRegExp.search(xmlInput) is not None

def splitIntoKeymapsAndPartsBeforeAndAfterKeymaps(xmlInput):
    xmlBeforeKeymapsInput = beforeFirstKeymapRegExp.search(xmlInput)
    xmlKeymapsInput = allKeyMapRegExp.search(xmlInput)
    xmlAfterKeymapsInput = xmlInput[len(xmlKeymapsInput.group(1)) + len(xmlBeforeKeymapsInput.group(1)):]
    
    keymaps = splitIntoKeymaps(xmlKeymapsInput.group(1))
    output = []
    if xmlBeforeKeymapsInput:
        output.append(xmlBeforeKeymapsInput.group(1))
    for keymap in keymaps:
        output.append(keymap)


    if xmlAfterKeymapsInput:
        output.append(xmlAfterKeymapsInput)
    return output

def splitIntoKeymaps(xmlInput):
    keymaps = re.split(r"<\s*/\s*keyMap\s*>", xmlInput, flags=re.IGNORECASE)
    keymapsRejoined = []  # we need to rejoin the closing tags


    for i in range(len(keymaps)):
        if len(keymaps[i].strip()) > 0:
            keymapsRejoined.append(keymaps[i].lstrip() + "</keyMap>")
    return keymapsRejoined
