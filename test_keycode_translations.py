import unittest

from keycodeTranslations import (
    qwertyColemakTranslations,
    qwertyDvorakTranslations,
    qwertyWorkmanTranslations,
)


class TestKeycodeTranslations(unittest.TestCase):
    def assert_no_duplicate_key_codes(
        self, translationTable, sourceName, destinationName
    ):
        sourceSet = set()
        destinationSet = set()
        sourceSetSize = 0
        destinationSetSize = 0

        duplicatesFound = False

        for (sourceKeyCode, destinationKeyCode) in translationTable:
            sourceSet.add(sourceKeyCode)
            destinationSet.add(destinationKeyCode)

            if sourceSetSize == len(sourceSet):
                duplicatesFound = True
                print(
                    "There is a duplicate key code on",
                    sourceName,
                    "key code:",
                    sourceKeyCode,
                )

            if destinationSetSize == len(destinationSet):
                duplicatesFound = True
                print(
                    "There is a duplicate key code on",
                    destinationName,
                    "key code:",
                    destinationKeyCode,
                )

            sourceSetSize += 1
            destinationSetSize += 1
        self.assertFalse(duplicatesFound)

    def test_lack_of_duplicates_in_colemak_translation_table(self):
        self.assert_no_duplicate_key_codes(
            qwertyColemakTranslations, "qwerty", "colemak"
        )

    def test_lack_of_duplicates_in_dvorak_translation_table(self):
        self.assert_no_duplicate_key_codes(qwertyDvorakTranslations, "qwerty", "dvorak")

    def test_lack_of_duplicates_in_workman_translation_table(self):
        self.assert_no_duplicate_key_codes(
            qwertyWorkmanTranslations, "qwerty", "workman"
        )
