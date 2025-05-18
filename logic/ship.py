ORIENTATION = {
    'hl': (0, -1), 'hr': (0, 1),
    'vu': (-1, 0), 'vd': (1, 0),
    'dlu': (-1, -1), 'dld': (1, -1),
    'dru': (-1, 1),  'drd': (1, 1)
}

SHIPS = [
    ('destroyer', 2, ['hl', 'hr', 'vu', 'vd']),
    ('submarine', 3, ['dlu', 'dld', 'dru', 'drd']),
    ('cruiser',   3, ['hl', 'hr', 'vu', 'vd'])
]