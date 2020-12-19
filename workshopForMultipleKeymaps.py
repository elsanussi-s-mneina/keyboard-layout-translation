from main import convertKeyMapsFromQwertyToDvorak


# Replace the following string with the QWERTY keymap XML you want to convert.
sampleQWERTY = """        <keyMap index="7">
            <key code="0" output="&#x0001;"/>
            <key code="1" output="&#x0013;"/>
            <key code="2" output="&#x0004;"/>
            <key code="3" output="&#x0006;"/>
            <key code="4" output="&#x0008;"/>
            <key code="5" output="&#x0007;"/>
            <key code="6" output="&#x001A;"/>
            <key code="7" output="&#x0018;"/>
            <key code="8" output="&#x0003;"/>
            <key code="9" output="&#x0016;"/>
            <key code="10" output="0"/>
            <key code="11" output="&#x0002;"/>
            <key code="12" output="&#x0011;"/>
            <key code="13" output="&#x0017;"/>
            <key code="14" output="&#x0005;"/>
            <key code="15" output="&#x0012;"/>
            <key code="16" output="&#x0019;"/>
            <key code="17" output="&#x0014;"/>
            <key code="18" output="1"/>
            <key code="19" output="2"/>
            <key code="20" output="3"/>
            <key code="21" output="4"/>
            <key code="22" output="6"/>
            <key code="23" output="5"/>
            <key code="24" output="="/>
            <key code="25" output="9"/>
            <key code="26" output="7"/>
            <key code="27" output="&#x001F;"/>
            <key code="28" output="8"/>
            <key code="29" action="6"/>
            <key code="30" output="&#x001D;"/>
            <key code="31" output="&#x000F;"/>
            <key code="32" output="&#x0015;"/>
            <key code="33" output="&#x001B;"/>
            <key code="34" output="&#x0009;"/>
            <key code="35" output="&#x0010;"/>
            <key code="36" output="&#x000D;"/>
            <key code="37" output="&#x000C;"/>
            <key code="38" output="&#x000A;"/>
            <key code="39" output="&#x0027;"/>
            <key code="40" output="&#x000B;"/>
            <key code="41" output=";"/>
            <key code="42" output="&#x001C;"/>
            <key code="43" output=","/>
            <key code="44" output="/"/>
            <key code="45" output="&#x000E;"/>
            <key code="46" output="&#x000D;"/>
            <key code="47" output="."/>
            <key code="48" output="&#x0009;"/>
            <key code="49" action="0"/>
            <key code="50" output="`"/>
            <key code="51" output="&#x0008;"/>
            <key code="52" output="&#x0003;"/>
            <key code="53" output="&#x001B;"/>
            <key code="65" output="."/>
            <key code="66" output="&#x001D;"/>
            <key code="67" output="*"/>
            <key code="69" output="+"/>
            <key code="70" output="&#x001C;"/>
            <key code="71" output="&#x001B;"/>
            <key code="72" output="&#x001F;"/>
            <key code="75" output="/"/>
            <key code="76" output="&#x0003;"/>
            <key code="77" output="&#x001E;"/>
            <key code="78" output="-"/>
            <key code="81" output="="/>
            <key code="82" output="0"/>
            <key code="83" output="1"/>
            <key code="84" output="2"/>
            <key code="85" output="3"/>
            <key code="86" output="4"/>
            <key code="87" output="5"/>
            <key code="88" output="6"/>
            <key code="89" output="7"/>
            <key code="91" output="8"/>
            <key code="92" output="9"/>
            <key code="96" output="&#x0010;"/>
            <key code="97" output="&#x0010;"/>
            <key code="98" output="&#x0010;"/>
            <key code="99" output="&#x0010;"/>
            <key code="100" output="&#x0010;"/>
            <key code="101" output="&#x0010;"/>
            <key code="102" output="&#x0010;"/>
            <key code="103" output="&#x0010;"/>
            <key code="104" output="&#x0010;"/>
            <key code="105" output="&#x0010;"/>
            <key code="106" output="&#x0010;"/>
            <key code="107" output="&#x0010;"/>
            <key code="108" output="&#x0010;"/>
            <key code="109" output="&#x0010;"/>
            <key code="110" output="&#x0010;"/>
            <key code="111" output="&#x0010;"/>
            <key code="112" output="&#x0010;"/>
            <key code="113" output="&#x0010;"/>
            <key code="114" output="&#x0005;"/>
            <key code="115" output="&#x0001;"/>
            <key code="116" output="&#x000B;"/>
            <key code="117" output="&#x007F;"/>
            <key code="118" output="&#x0010;"/>
            <key code="119" output="&#x0004;"/>
            <key code="120" output="&#x0010;"/>
            <key code="121" output="&#x000C;"/>
            <key code="122" output="&#x0010;"/>
            <key code="123" output="&#x001C;"/>
            <key code="124" output="&#x001D;"/>
            <key code="125" output="&#x001F;"/>
            <key code="126" output="&#x001E;"/>
        </keyMap>"""


# print("converted from Qwerty to DVORAK:")
print(convertKeyMapFromQwertyToDvorak(sampleQWERTY))