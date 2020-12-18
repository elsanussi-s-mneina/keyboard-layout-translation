import unittest

from mac_keymap_translation import extractOutput


class TestMacKeymapTransaltion(unittest.TestCase):
    def test_extract_output(self):
        input = """		<key code="0" output="A"/>
					<key code="1" output="S"/>"""
        expectedOutput = "A"
        actualOutput = extractOutput(0, input)
        self.assertEqual(actualOutput, expectedOutput)
