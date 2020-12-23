# a module for converting keycodes used in Windows KLC files.

def getQwertyDvorakTranslations():
    return qwertyDvorakTranslations


def getDvorakQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyDvorakTranslations()]

# format a list of tuples
# The first entry is the keycode
# The second is the Virtual keycode (in the VK_ column) of
#  where to move the key with that key code to in order to change the keyboard layout away from Qwerty.
# i.e. (source_key_code, destination_key_code)


qwertyDvorakTranslations = [
    # The numbers row
    ('OEM_MINUS', 'OEM_7'),  # -
    ('OEM_PLUS', 'OEM_6'),  # =
    # # The row below the numbers row:
    ('Q', 'X'),  # q in QWERTY
    ('W', 'OEM_COMMA'),  # w in QWERTY
    ('E', 'D'),  # e in QWERTY
    ('R', 'O'),  # r in QWERTY
    ('T', 'K'),  # t in QWERTY
    ('Y', 'T'),  # y in QWERTY
    ('U', 'F'),  # u in QWERTY
    ('I', 'G'),  # i in QWERTY
    ('O', 'S'),  # o in QWERTY
    ('P', 'R'),  # p
    ('OEM_4', 'OEM_MINUS'),  # [
    ('OEM_6', 'OEM_PLUS'),  # ]
    ('OEM_5', 'OEM_5'),  # \
    # # Next row:
    ('A', 'A'),  # a
    ('S', 'OEM_1'),  # s
    ('D', 'H'),  # d
    ('F', 'Y'),  # f
    ('G', 'U'),  # g
    ('H', 'J'),  # h
    ('J', 'C'),  # j
    ('K', 'V'),  # k
    ('L', 'P'),  # l
    ('OEM_1', 'Z'),  # ;
    ('OEM_7', 'Q'),  # '
    # # Next row (the row above the space bar):
    ('Z', 'OEM_2'),  # z
    ('X', 'B'),  # x
    ('C', 'I'),  # c
    ('V', 'OEM_PERIOD'),  # v
    ('B', 'N'),  # b
    ('N', 'L'),  # n
    ('M', 'M'),  # m
    ('OEM_COMMA', 'W'),  # ,
    ('OEM_PERIOD', 'E'),  # .
    ('OEM_2', 'OEM_4'),  # /
]
