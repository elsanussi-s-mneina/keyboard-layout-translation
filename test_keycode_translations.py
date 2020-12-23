import unittest

from keycodeTranslations import qwertyColemakDvorakWorkmanTranslations


class TestKeycodeTranslations(unittest.TestCase):
    def test_there_should_be_no_duplicate_keys_in_any_column(self):
        qwertySet = set()
        colemakSet = set()
        dvorakSet = set()
        workmanSet = set()
        duplicatesFound = False

        currentQwertySetSize = 0
        currentColemakSetSize = 0
        currentDvorakSetSize = 0
        currentWorkmanSetSize = 0
        for (
            qwerty,
            colemak,
            dvorak,
            workman,
        ) in qwertyColemakDvorakWorkmanTranslations:
            qwertySet.add(qwerty)
            colemakSet.add(colemak)
            dvorakSet.add(dvorak)
            workmanSet.add(workman)

            if currentQwertySetSize == len(qwertySet):
                duplicatesFound = True
                print("There is a duplicate key code on QWERTY:", qwerty)

            if currentColemakSetSize == len(colemakSet):
                duplicatesFound = True
                print("There is a duplicate key code on Colemak:", colemak)

            if currentDvorakSetSize == len(dvorakSet):
                duplicatesFound = True
                print("There is a duplicate key code on Dvorak:", dvorak)

            if currentWorkmanSetSize == len(workmanSet):
                duplicatesFound = True
                print("There is a duplicate key code on workman:", workman)

            currentQwertySetSize += 1
            currentDvorakSetSize += 1
            currentColemakSetSize += 1
            currentWorkmanSetSize += 1

        self.assertFalse(duplicatesFound)
