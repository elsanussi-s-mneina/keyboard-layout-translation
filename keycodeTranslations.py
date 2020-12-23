# format a list of tuples
# the first entry is the keycode for QWERTY,
# the second entry is the keycode for DVORAK,
# the third entry is the keycode for COLEMAK


def getQwertyColemakTranslations():
    return [
        (qwerty, colemak)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getQwertyDvorakTranslations():
    return [
        (qwerty, dvorak)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getQwertyWorkmanTranslations():
    return [
        (qwerty, workman)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getColemakDvorakTranslations():
    return [
        (colemak, dvorak)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getColemakWorkmanTranslations():
    return [
        (colemak, workman)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getDvorakWorkmanTranslations():
    return [
        (dvorak, workman)
        for (qwerty, colemak, dvorak, workman) in qwertyColemakDvorakWorkmanTranslations
    ]


def getDvorakColemakTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getColemakDvorakTranslations()]


def getDvorakQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyDvorakTranslations()]


def getColemakQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyColemakTranslations()]


def getWorkmanQwertyTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getQwertyWorkmanTranslations()]


def getWorkmanColemakTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getColemakWorkmanTranslations()]


def getWorkmanDvorakTranslations():
    return [tuple(reversed(aTuple)) for aTuple in getDvorakWorkmanTranslations()]


# This one only works for lowercase DVORAK.
qwertyColemakDvorakWorkmanTranslations = [
    # The numbers row
    (27, 27, 39, 27),  # -
    (24, 24, 30, 24),  # =
    # The row below the numbers row:
    (12, 12, 7, 12),  # q in QWERTY
    (13, 13, 43, 15),  # w in QWERTY
    (14, 40, 2, 40),  # e in QWERTY
    (15, 1, 31, 14),  # r in QWERTY
    (17, 3, 40, 3),  # t in QWERTY
    (16, 31, 17, 4),  # y in QWERTY
    (32, 34, 3, 34),  # u in QWERTY
    (34, 37, 5, 41),  # i in QWERTY
    (31, 41, 1, 37),  # o in QWERTY
    (35, 15, 15, 31),  # p
    (33, 33, 27, 33),  # [
    (30, 30, 24, 30),  # ]
    (42, 42, 42, 42),  # \
    # Next row:
    (0, 0, 0, 0),  # a
    (1, 2, 41, 1),  # s
    (2, 5, 4, 13),  # d
    (3, 14, 16, 32),  # f
    (5, 17, 32, 5),  # g
    (4, 4, 38, 2),  # h
    (38, 16, 8, 16),  # j
    (40, 45, 9, 45),  # k
    (37, 32, 35, 46),  # l
    (41, 35, 6, 35),  # ;
    (39, 39, 12, 39),  # '
    # Next row (the row above the space bar):
    (6, 6, 44, 6),  # z
    (7, 7, 11, 7),  # x
    (8, 8, 34, 9),  # c
    (9, 9, 47, 11),  # v
    (11, 11, 45, 17),  # b
    (45, 38, 37, 38),  # n
    (46, 46, 46, 8),  # m
    (43, 43, 13, 43),  # ,
    (47, 47, 14, 47),  # .
    (44, 44, 33, 44),  # /
]
