# This is the start of a Python script to swap keys on a keyboard layout file
# for Mac OS Catalina.
# Started December 2020.
import re
from mac_keymap_translation import (
    convertKeyMapFromQwertyToDvorak,
    convertKeyMapFromQwertyToColemak,
    convertKeyMapFromDvorakToQwerty,
    convertKeyMapFromDvorakToColemak,
    convertKeyMapFromColemakToDvorak,
    convertKeyMapFromColemakToQwerty,
)

from keymap_splitter import splitIntoKeymaps


def convertKeyMapsFromOneLayoutToAnother(xmlForKeyMaps, layoutConversionFunction):
    keymaps = splitIntoKeymaps(xmlForKeyMaps)
    return "".join(layoutConversionFunction(keymap) for keymap in keymaps)


def convertKeyMapsFromQwertyToDvorak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromQwertyToDvorak
    )


def convertKeyMapsFromQwertyToColemak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromQwertyToColemak
    )


def convertKeyMapsFromDvorakToQwerty(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromDvorakToQwerty
    )


def convertKeyMapsFromDvorakToColemak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromDvorakToColemak
    )


def convertKeyMapsFromColemakToQwerty(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromColemakToQwerty
    )


def convertKeyMapsFromColemakToDvorak(xmlForKeyMaps):
    return convertKeyMapsFromOneLayoutToAnother(
        xmlForKeyMaps, convertKeyMapFromColemakToDvorak
    )
