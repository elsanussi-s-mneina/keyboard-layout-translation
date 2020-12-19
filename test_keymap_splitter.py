import unittest

from keymap_splitter import hasKeyMap, splitIntoKeymaps


class TestKeymapSplitter(unittest.TestCase):
    def test_has_key_map_empty_string_has_no_keymap(self):
        input = """"""
        expectedOutput = False
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map_spaces_string_has_no_keymap(self):
        input = """   \t   \n   """
        expectedOutput = False
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__only_opening_tag__does_not_count(self):
        input = """   \t   \n <keymap>  """
        expectedOutput = False
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__only_closing_tag__does_not_count(self):
        input = """   \t   \n </keyMap>  """
        expectedOutput = False
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__open_and_closing_tag__does_count(self):
        input = """ \t   \n<keymap> </keyMap>  """
        expectedOutput = True
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__open_and_closing_tag__extra_spaces_allowed(self):
        input = """ \t   \n<  keymap> </keyMap>  """
        expectedOutput = True
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__open_and_closing_tag__extra_spaces_allowed(self):
        input = """ \t   \n<  keymap> < /keymap>  """
        expectedOutput = True
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__open_and_closing_tag__extra_spaces_allowed(self):
        input = """ \t   \n<  keymap   > < /  keymap      >  """
        expectedOutput = True
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_has_key_map__open_and_closing_tag__extra_spaces_allowed(self):
        input = """ \t   \n<  keymap \t > </\tkeymap  \t   >  """
        expectedOutput = True
        actualOutput = hasKeyMap(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__open_and_closing_tag__extra_spaces_allowed(self):
        input = """ \t   \n<  keymap \t > < /\tkeymap  \t   >  """
        expectedOutput = ["<  keymap \t > </keyMap>"]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__two_key_maps(self):
        input = """<keymap>abc</keyMap><keymap>defg</keyMap>"""
        expectedOutput = ["<keymap>abc</keyMap>", "<keymap>defg</keyMap>"]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__two_key_maps_with_attributes(self):
        input = """<keyMap index="0" baseMapSet="mapSet" baseIndex="3">abc</keyMap><keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>"""
        expectedOutput = [
            """<keyMap index="0" baseMapSet="mapSet" baseIndex="3">abc</keyMap>""",
            """<keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>""",
        ]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__two_key_maps_with_attributes_and_spaces(self):
        input = """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>  <keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>     """
        expectedOutput = [
            """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>""",
            """<keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>""",
        ]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__three_key_maps_with_attributes_and_spaces(self):
        input = """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>  <keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>     <keyMap index="3">abcd xyz</keyMap>"""
        expectedOutput = [
            """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>""",
            """<keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>""",
            """<keyMap index="3">abcd xyz</keyMap>""",
        ]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_split_into_key_maps__four_key_maps_with_attributes_and_spaces(self):
        input = """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>  <keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>     <keyMap index="3">abcd xyz</keyMap><keyMap index="4">a xyz</keyMap>"""
        expectedOutput = [
            """<keyMap index="0" baseMapSet="mapSet" baseIndex="3"> abc </keyMap>""",
            """<keyMap index="1" baseMapSet="mapSet" baseIndex="3">defg</keyMap>""",
            """<keyMap index="3">abcd xyz</keyMap>""",
            """<keyMap index="4">a xyz</keyMap>""",
        ]
        actualOutput = splitIntoKeymaps(input)
        self.assertEqual(actualOutput, expectedOutput)
