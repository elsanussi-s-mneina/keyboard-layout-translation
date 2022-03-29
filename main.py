# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re
from mac_keymap_translation import (
    convertKeyMapFromQwertyToDvorak,
    convertKeyMapFromQwertyToColemak,
    convertKeyMapFromQwertyToWorkman,
    convertKeyMapFromDvorakToQwerty,
    convertKeyMapFromDvorakToColemak,
    convertKeyMapFromDvorakToWorkman,
    convertKeyMapFromColemakToDvorak,
    convertKeyMapFromColemakToQwerty,
    convertKeyMapFromColemakToWorkman,
)

from keymap_splitter import splitIntoKeymapsAndPartsBeforeAndAfterKeymaps


def convertKeyMapsFromOneLayoutToAnother(xmlForKeyMaps, layoutConversionFunction):
    keymaps = splitIntoKeymapsAndPartsBeforeAndAfterKeymaps(xmlForKeyMaps)
    return "".join(layoutConversionFunction(keymap) for keymap in keymaps)


def convertKeyMapsFromQwertyToDvorak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromQwertyToDvorak
    )


def convertKeyMapsFromQwertyToColemak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromQwertyToColemak
    )


def convertKeyMapsFromQwertyToWorkman(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromQwertyToWorkman
    )


def convertKeyMapsFromDvorakToQwerty(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromDvorakToQwerty
    )


def convertKeyMapsFromDvorakToColemak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromDvorakToColemak
    )


def convertKeyMapsFromDvorakToWorkman(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromDvorakToWorkman
    )


def convertKeyMapsFromColemakToQwerty(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromColemakToQwerty
    )


def convertKeyMapsFromColemakToDvorak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromColemakToDvorak
    )


def convertKeyMapsFromColemakToWorkman(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromColemakToWorkman
    )
