# format a list of tuples
# the first entry is the keycode for QWERTY,
# the second entry is the keycode for DVORAK,
# the third entry is the keycode for COLEMAK


# This one only works for lowercase DVORAK.
qwertyColemakDvorakTranslations = [
    # The numbers row
    (27, 27, 39),  # -
    (24, 24, 30),  # =
    # The row below the numbers row:
    (12, 12, 7),  # q in QWERTY
    (13, 13, 43),  # w in QWERTY
    (14, 40, 2),  # e in QWERTY
    (15, 1, 31),  # r in QWERTY
    (17, 3, 40),  # t in QWERTY
    (16, 31, 17),  # y in QWERTY
    (32, 34, 3),  # u in QWERTY
    (34, 37, 5),  # i in QWERTY
    (31, 41, 1),  # o in QWERTY
    (35, 15, 15),  # p
    (33, 33, 27),  # [
    (30, 30, 24),  # ]
    (42, 42, 42),  # \
    # Next row:
    (0, 0, 0),  # a
    (1, 2, 41),  # s
    (2, 5, 4),  # d
    (3, 14, 16),  # f
    (5, 17, 32),  # g
    (4, 4, 38),  # h
    (38, 16, 8),  # j
    (40, 45, 9),  # k
    (37, 32, 35),  # l
    (41, 35, 6),  # ;
    (39, 39, 12),  # '
    # Next row (the row above the space bar):
    (6, 6, 44),  # z
    (7, 7, 11),  # x
    (8, 8, 34),  # c
    (9, 9, 47),  # v
    (11, 11, 45),  # b
    (45, 38, 37),  # n
    (46, 46, 46),  # m
    (43, 43, 13),  # ,
    (47, 47, 14),  # .
    (44, 44, 33),  # /
]
