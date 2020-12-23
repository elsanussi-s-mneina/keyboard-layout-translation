def getQwertyColemakTranslations():
    return qwertyColemakTranslations


def getQwertyDvorakTranslations():
    return qwertyDvorakTranslations


def getQwertyWorkmanTranslations():
    return qwertyWorkmanTranslations


def getDvorakQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyDvorakTranslations()]


def getColemakQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyColemakTranslations()]


def getWorkmanQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyWorkmanTranslations()]


# format a list of tuples
# The first entry is the keycode
# The second is the keycode of
#  where to move the key with that key code to in order to change the keyboard layout away from Qwerty.
# i.e. (source_key_code, destination_key_code)

qwertyColemakTranslations = [
    # The numbers row
    (27, 27),  # -
    (24, 24),  # =
    # The row below the numbers row:
    (12, 12),  # q in QWERTY
    (13, 13),  # w in QWERTY
    (14, 40),  # e in QWERTY
    (15, 1),  # r in QWERTY
    (17, 3),  # t in QWERTY
    (16, 31),  # y in QWERTY
    (32, 34),  # u in QWERTY
    (34, 37),  # i in QWERTY
    (31, 41),  # o in QWERTY
    (35, 15),  # p
    (33, 33),  # [
    (30, 30),  # ]
    (42, 42),  # \
    # Next row:
    (0, 0),  # a
    (1, 2),  # s
    (2, 5),  # d
    (3, 14),  # f
    (5, 17),  # g
    (4, 4),  # h
    (38, 16),  # j
    (40, 45),  # k
    (37, 32),  # l
    (41, 35),  # ;
    (39, 39),  # '
    # Next row (the row above the space bar):
    (6, 6),  # z
    (7, 7),  # x
    (8, 8),  # c
    (9, 9),  # v
    (11, 11),  # b
    (45, 38),  # n
    (46, 46),  # m
    (43, 43),  # ,
    (47, 47),  # .
    (44, 44),  # /
]


qwertyDvorakTranslations = [
    # The numbers row
    (27, 39),  # -
    (24, 30),  # =
    # The row below the numbers row:
    (12, 7),  # q in QWERTY
    (13, 43),  # w in QWERTY
    (14, 2),  # e in QWERTY
    (15, 31),  # r in QWERTY
    (17, 40),  # t in QWERTY
    (16, 17),  # y in QWERTY
    (32, 3),  # u in QWERTY
    (34, 5),  # i in QWERTY
    (31, 1),  # o in QWERTY
    (35, 15),  # p
    (33, 27),  # [
    (30, 24),  # ]
    (42, 42),  # \
    # Next row:
    (0, 0),  # a
    (1, 41),  # s
    (2, 4),  # d
    (3, 16),  # f
    (5, 32),  # g
    (4, 38),  # h
    (38, 8),  # j
    (40, 9),  # k
    (37, 35),  # l
    (41, 6),  # ;
    (39, 12),  # '
    # Next row (the row above the space bar):
    (6, 44),  # z
    (7, 11),  # x
    (8, 34),  # c
    (9, 47),  # v
    (11, 45),  # b
    (45, 37),  # n
    (46, 46),  # m
    (43, 13),  # ,
    (47, 14),  # .
    (44, 33),  # /
]


qwertyWorkmanTranslations = [
    # The numbers row
    (27, 27),  # -
    (24, 24),  # =
    # The row below the numbers row:
    (12, 12),  # q in QWERTY
    (13, 15),  # w in QWERTY
    (14, 40),  # e in QWERTY
    (15, 14),  # r in QWERTY
    (17, 3),  # t in QWERTY
    (16, 4),  # y in QWERTY
    (32, 34),  # u in QWERTY
    (34, 41),  # i in QWERTY
    (31, 37),  # o in QWERTY
    (35, 31),  # p
    (33, 33),  # [
    (30, 30),  # ]
    (42, 42),  # \
    # Next row:
    (0, 0),  # a
    (1, 1),  # s
    (2, 13),  # d
    (3, 32),  # f
    (5, 5),  # g
    (4, 2),  # h
    (38, 16),  # j
    (40, 45),  # k
    (37, 46),  # l
    (41, 35),  # ;
    (39, 39),  # '
    # Next row (the row above the space bar):
    (6, 6),  # z
    (7, 7),  # x
    (8, 9),  # c
    (9, 11),  # v
    (11, 17),  # b
    (45, 38),  # n
    (46, 8),  # m
    (43, 43),  # ,
    (47, 47),  # .
    (44, 44),  # /
]
