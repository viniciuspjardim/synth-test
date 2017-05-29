
"""Note sequence samples"""

# Europe - Final Countdown. Good at 120 bpm and 12 tone shift
final_countdown = [
    ['B2', 4 / 1.5], ['B3', 16], ['A3', 16], 'B3', 'E3',
    ['C3', 4 / 1.5], ['C4', 16], ['B3', 16], ['C4', 8], ['B3', 8],
    'A3',
    ['E3', 4 / 1.5], ['C4', 16], ['B3', 16], 'C4', 'E3',
    ['F#3', 4 / 1.5], ['A3', 16], ['G3', 16], ['A3', 8], ['G3', 8],
    ['F#3', 8], ['G3', 8],

    ['B2', 4 / 1.5], ['B3', 16], ['A3', 16], 'B3', 'E3',
    ['C3', 4 / 1.5], ['C4', 16], ['B3', 16], ['C4', 8], ['B3', 8],
    'A3',
    ['E3', 4 / 1.5], ['C4', 16], ['B3', 16], 'C4', 'E3',
    ['F#3', 4 / 1.5], ['A3', 16], ['G3', 16], ['A3', 8], ['G3', 8],
    ['F#3', 8], ['G3', 8],

    ['G3', 4 / 1.5], ['F#3', 16], ['G3', 16], ['A3', 4 / 1.5],
    ['G3', 16], ['A3', 16],
    ['B3', 8], ['A3', 8], ['G3', 8], ['F#3', 8], 'E3', 'C4',
    ['B3', 4 / 3], ['B3', 16], ['C4', 16], ['B3', 16], ['A3', 16],
    ['B3', 1]
]

# Happy birthday to you. Good at 120 bpm and 48 tone shift
# First position it's the note pitch, the second is the note
happy_birthday = [
    [None, 2], [0, 8], [0, 8],
    2, 0, 5,
    4, None, [0, 8], [0, 8],
    2, 0, 7,
    5, None, [0, 8], [0, 8],
    12, 9, 5,
    4, [2, 2],
    [None, 2], [10, 8], [10, 8],
    9, 5, 7,
    [5, 2], None
]

# Deep Purple - Smoke on the water. Good at 112 bpm and 44 tone shift
smoke_on_the_water = [
    [2, 8], [None, 8], [5, 8], [None, 8], 7, [None, 8], [2, 8],
    [None, 8], [5, 8], [None, 8], [8, 8], 7, None,
    [2, 8], [None, 8], [5, 8], [None, 8], 7, [None, 8], [5, 8],
    [None, 8], [2, 1.6], None
]

# C scale notes sequence. Good at 280 bpm and 24 tone shift
c_scale = [
    0, 2, 4, 5,
    2, 4, 5, 7,
    4, 5, 7, 9,
    5, 7, 9, 11,

    12, 14, 16, 17,
    14, 16, 17, 19,
    16, 17, 19, 21,
    17, 19, 21, 23,

    24, 26, 28, 29,
    26, 28, 29, 31,
    28, 29, 31, 33,
    29, 31, 33, 35
]

# Major scale starting in C. Good at 120 bpm and 36 tone shift
major_c_scale = [
    [0, 1], [2, 1], [4, 1],
    [5, 1], [7, 1], [9, 1],
    [11, 1], [12, 1]
]

# Guitar default E2 tune. Good at 120 bpm and 0 tone shift
guitar_tune = [
    ["E2", 0.5], None,
    ["A2", 0.5], None,
    ["D3", 0.5], None,
    ["G3", 0.5], None,
    ["B3", 0.5], None,
    ["E4", 0.5], None,
]
