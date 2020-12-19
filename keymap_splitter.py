# For splitting one XML string into multiple ones each with only one keymap at most.
import re

keymapRegExp = re.compile(r"(<\s*keyMap.*?>.*?<\s*/\s*keyMap\s*>)", flags=re.IGNORECASE)


def hasKeyMap(xmlInput):
    return keymapRegExp.search(xmlInput) is not None


def hasCloseKeyMapTag(xmlInput):
    return keymapCloseRegExp.search(xmlInput) is not None


def splitIntoKeymaps(xmlInput):
    keymaps = re.split(r"<\s*/\s*keyMap\s*>", xmlInput, flags=re.IGNORECASE)
    keymapsRejoined = []  # we need to rejoin the closing tags

    for i in range(len(keymaps)):
        if len(keymaps[i].strip()) > 0:
            keymapsRejoined.append(keymaps[i].lstrip() + "</keyMap>")

    return keymapsRejoined
