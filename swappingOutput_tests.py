from swappingOutput import swapKeyOutputs, convertKeyMapFromQwertyToDvorak

print("running tests")

input = """		<key code="0" output="A"/>
			<key code="1" output="S"/>"""

expectedOutput = """		<key code="0" output="S"/>
			<key code="1" output="A"/>"""


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
			<key code="39" output="&#39;"/> <!-- Single quote -->

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


output = swapKeyOutputs(0, 1, input)
print("expected:\n", expectedOutput)
print("actual:\n", output)

print("converted from Qwerty to DVORAK:")
print(convertKeyMapFromQwertyToDvorak(sampleQWERTY))