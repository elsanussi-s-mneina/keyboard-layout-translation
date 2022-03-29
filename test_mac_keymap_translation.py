import unittest

from mac_keymap_translation import (
    convertKeyMapFromQwertyToDvorak,
    extractOutput,
    extractOutputOrAction,
    replaceOutput,
    replaceOutputOrAction,
    replaceKeyCode,
)


class TestMacKeymapTranslation(unittest.TestCase):
    def test_extract_output(self):
        input = """		<key code="0" output="A"/>
					<key code="1" output="S"/>"""
        expectedOutput = "A"
        actualOutput = extractOutput(0, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_spaces_should_not_matter(self):
        input = """		<key code="0" output   \t= "A"/>
					<key code="1" output="S"/>"""
        expectedOutput = "A"
        actualOutput = extractOutput(0, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_does_not_extract_action(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = None
        actualOutput = extractOutput(0, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_when_key_code_not_found_returns_none(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = None
        actualOutput = extractOutput(7777, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_or_action_does_extract_action_with_attribute(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = 'action="AnAction"'
        actualOutput = extractOutputOrAction(0, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_or_action_does_extract_output_with_attribute(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = 'output="S"'
        actualOutput = extractOutputOrAction(1, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_extract_output_or_action_returns_none_when_missing(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = None
        actualOutput = extractOutputOrAction(93, input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_when_key_code_missing_does_not_change_xml(self):
        xmlInput = """	<hi thet nothing is around> """
        expectedOutput = xmlInput
        actualOutput = replaceOutput(93, 'output="R"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_does_replace_output(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = """		<key code="0" action="AnAction"/>
					<key code="1" output="E"/>"""
        actualOutput = replaceOutput(1, "E", input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_spaces_do_not_matter_but_are_preserved(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output\t  =   "S"/>"""
        expectedOutput = """		<key code="0" action="AnAction"/>
					<key code="1" output\t  =   "M"/>"""
        actualOutput = replaceOutput(1, "M", input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_does_not_replace_action(self):
        input = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        actualOutput = replaceOutput(0, "E", input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_when_key_code_missing_does_not_change_xml(self):
        xmlInput = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = xmlInput
        actualOutput = replaceOutputOrAction(93, 'output="R"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_when_key_code_missing_does_not_change_xml(self):
        xmlInput = """   """
        expectedOutput = xmlInput
        actualOutput = replaceOutputOrAction(93, 'output="R"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_replaces_action_with_output(self):
        xmlInput = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = """		<key code="0" output="R"/>
					<key code="1" output="S"/>"""
        actualOutput = replaceOutputOrAction(0, 'output="R"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_replaces_output_with_action(self):
        xmlInput = """		<key code="0" action="AnAction"/>
					<key code="1" output="S"/>"""
        expectedOutput = """		<key code="0" action="AnAction"/>
					<key code="1" action="act78"/>"""
        actualOutput = replaceOutputOrAction(1, 'action="act78"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_replaces_output_with_action(self):
        xmlInput = """		<key code="0" action="AnAction"/>
					<key code="7" action="otherAct2"/>"""
        expectedOutput = """		<key code="0" action="AnAction"/>
					<key code="7" action="otherAct4"/>"""
        actualOutput = replaceOutputOrAction(7, 'action="otherAct4"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_replaces_output_with_output(self):
        xmlInput = """		<key code="9" output="x"/>
					<key code="7" output="q"/>"""
        expectedOutput = """		<key code="9" output="x"/>
					<key code="7" output="y"/>"""
        actualOutput = replaceOutputOrAction(7, 'output="y"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_output_or_action_spaces_should_not_matter(self):
        xmlInput = """		<key code="9" output =  "x"/>
					<key code="7" output ="q"/>"""
        expectedOutput = """		<key code="9" output =  "x"/>
					<key code="7" output="y"/>"""
        actualOutput = replaceOutputOrAction(7, 'output="y"', xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_replace_key_code(self):
        xmlInput = """<key code="26" output="forever"/>"""
        expectedOutput = """<key code="33" output="forever"/>"""
        actualOutput = replaceKeyCode(26, 33, xmlInput)
        self.assertEqual(actualOutput, expectedOutput)

    def test_convert_from_qwerty_to_dvorak_when_some_key_codes_are_missing(self):
        # The following is from the Unicode Hex input keyboard layout
        sampleQWERTY = """
        <keyMap index="3">
            <key code="0" action="a10"/>
            <key code="2" action="a13"/>
            <key code="3" action="a15"/>
            <key code="8" action="a12"/>
            <key code="11" action="a11"/>
            <key code="14" action="a14"/>
            <key code="18" action="a1"/>
            <key code="19" action="a2"/>
            <key code="20" action="a3"/>
            <key code="21" action="a4"/>
            <key code="22" action="a6"/>
            <key code="23" action="a5"/>
            <key code="25" action="a9"/>
            <key code="26" action="a7"/>
            <key code="28" action="a8"/>
            <key code="29" action="a0"/>
            <key code="82" action="a0"/>
            <key code="83" action="a1"/>
            <key code="84" action="a2"/>
            <key code="85" action="a3"/>
            <key code="86" action="a4"/>
            <key code="87" action="a5"/>
            <key code="88" action="a6"/>
            <key code="89" action="a7"/>
            <key code="91" action="a8"/>
            <key code="92" action="a9"/>
        </keyMap>
"""
        expectedDvorak = """          <keyMap index="3">
            <key code="0" action="a10"/>
            <key code="4" action="a14"/>
            <key code="16" action="a15"/>
            <key code="34" action="a12"/>
            <key code="45" action="a11"/>
            <key code="2" action="a14"/>
            <key code="18" action="a1"/>
            <key code="19" action="a2"/>
            <key code="20" action="a3"/>
            <key code="21" action="a4"/>
            <key code="22" action="a6"/>
            <key code="23" action="a5"/>
            <key code="25" action="a9"/>
            <key code="26" action="a7"/>
            <key code="28" action="a8"/>
            <key code="29" action="a0"/>
            <key code="82" action="a0"/>
            <key code="83" action="a1"/>
            <key code="84" action="a2"/>
            <key code="85" action="a3"/>
            <key code="86" action="a4"/>
            <key code="87" action="a5"/>
            <key code="88" action="a6"/>
            <key code="89" action="a7"/>
            <key code="91" action="a8"/>
            <key code="92" action="a9"/>
        </keyMap>
"""
        # print("converted from Qwerty to DVORAK:")
        actualDvorak = convertKeyMapFromQwertyToDvorak(sampleQWERTY)
        # print(actualDvorak)
        self.assertEqual(actualDvorak.strip(), expectedDvorak.strip())

        
    def test_convert_from_qwerty_to_dvorak(self):
        sampleQWERTY = """		<keyMap index="0" baseMapSet="mapSet" baseIndex="3">
		<!-- Top row, from left to right on ANSI Keyboard -->
			<key code="50" output="`"/>
			<key code="18" output="1"/>
			<key code="19" output="2"/>
			<key code="20" output="3"/>
			<key code="21" output="4"/>
			<key code="23" output="5"/>
			<key code="22" output="6"/>
			<key code="26" output="7"/>
			<key code="28" output="8"/>
			<key code="25" output="9"/>
			<key code="29" output="0"/>
			<key code="27" output="-"/>
			<key code="24" output="="/>

		<!-- Second row from top, from left to right -->
			<key code="12" output="q"/>
			<key code="13" output="w"/>
			<key code="14" output="e"/>
			<key code="15" output="r"/>
			<key code="17" output="t"/>
			<key code="16" output="y"/>
			<key code="32" output="u"/>
			<key code="34" output="i"/>
			<key code="31" output="o"/>
			<key code="35" output="p"/>
			<key code="33" output="["/>
			<key code="30" output="]"/>
			<key code="42" output="\"/>

		<!-- Third row from top, from left to right -->
			<key code="0" output="a"/>
			<key code="1" output="s"/>
			<key code="2" output="d"/>
			<key code="3" output="f"/>
			<key code="5" output="g"/>
			<key code="4" output="h"/>
			<key code="38" output="j"/>
			<key code="40" output="k"/>
			<key code="37" output="l"/>
			<key code="41" output=";"/>
			<key code="39" output="&#39;"/>

		<!-- Fourth row from top, from left to right -->
			<key code="6" output="z"/>
			<key code="7" output="x"/>
			<key code="8" output="c"/>
			<key code="9" output="v"/>
			<key code="11" output="b"/>
			<key code="45" output="n"/>
			<key code="46" output="m"/>
			<key code="43" output=","/>
			<key code="47" output="."/>
			<key code="44" output="/"/>
		</keyMap>
		"""
        expectedDvorak = """		<keyMap index="0" baseMapSet="mapSet" baseIndex="3">
		<!-- Top row, from left to right on ANSI Keyboard -->
			<key code="50" output="`"/>
			<key code="18" output="1"/>
			<key code="19" output="2"/>
			<key code="20" output="3"/>
			<key code="21" output="4"/>
			<key code="23" output="5"/>
			<key code="22" output="6"/>
			<key code="26" output="7"/>
			<key code="28" output="8"/>
			<key code="25" output="9"/>
			<key code="29" output="0"/>
			<key code="27" output="["/>
			<key code="24" output="]"/>

		<!-- Second row from top, from left to right -->
			<key code="12" output="&#39;"/>
			<key code="13" output=","/>
			<key code="14" output="."/>
			<key code="15" output="p"/>
			<key code="17" output="y"/>
			<key code="16" output="f"/>
			<key code="32" output="g"/>
			<key code="34" output="c"/>
			<key code="31" output="r"/>
			<key code="35" output="l"/>
			<key code="33" output="/"/>
			<key code="30" output="="/>
			<key code="42" output="\"/>

		<!-- Third row from top, from left to right -->
			<key code="0" output="a"/>
			<key code="1" output="o"/>
			<key code="2" output="e"/>
			<key code="3" output="u"/>
			<key code="5" output="i"/>
			<key code="4" output="d"/>
			<key code="38" output="h"/>
			<key code="40" output="t"/>
			<key code="37" output="n"/>
			<key code="41" output="s"/>
			<key code="39" output="-"/>

		<!-- Fourth row from top, from left to right -->
			<key code="6" output=";"/>
			<key code="7" output="q"/>
			<key code="8" output="j"/>
			<key code="9" output="k"/>
			<key code="11" output="x"/>
			<key code="45" output="b"/>
			<key code="46" output="m"/>
			<key code="43" output="w"/>
			<key code="47" output="v"/>
			<key code="44" output="z"/>
		</keyMap>
		"""
        # print("converted from Qwerty to DVORAK:")
        actualDvorak = convertKeyMapFromQwertyToDvorak(sampleQWERTY)
        # print(actualDvorak)
        self.assertEqual(actualDvorak, expectedDvorak)
