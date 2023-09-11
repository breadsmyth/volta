import pygame
import re
resolution_pattern = re.compile(r'(\d+)[xX](\d+)')

option_details = {
    # name          type        default value
    'fps':          ('int',     60),
    'resolution':   ('intxint', '800x600'),
    'zoom':         ('int',     1),

    'up':           ('key',     'W'),
    'left':         ('key',     'A'),
    'down':         ('key',     'S'),
    'right':        ('key',     'D'),

    'use':          ('key',     'Z'),
    'fire':         ('key',     'X'),
    'menu':         ('key',     'C'),
    'inv':          ('key',     'I'),
    'status':       ('key',     'TAB'),

    'next':         ('key',     'E'),
    'prev':         ('key',     'Q'),
}

def is_opt(line):
    line = line.lstrip()
    return len(line) and not line.startswith('#')

def read():
    with open('options.txt') as opt_file:
        options = opt_file.readlines()

    options = [line[:-1] for line in options if is_opt(line)]

    opt_dict = {}
    for opt in options:
        name, _, value = opt.partition(':')
        opt_type, opt_default = option_details[name]

        # Parse numbers
        try:
            if opt_type == 'int':
                value = int(value)

            elif opt_type == 'intxint':
                matches = resolution_pattern.match(value)
                if matches is None:
                    raise ValueError

                value = (int(matches.group(1)), int(matches.group(2)))

            elif opt_type == 'key':
                pygame.key.key_code(value.lower())

        except ValueError:
            print(f"options.txt: bad value for '{name}'! defaulting to {opt_default}")
            value = opt_default

        opt_dict[name] = value

    # Fill in missing values
    for name, opt_tuple in option_details.items():
        _, opt_default = opt_tuple

        if name not in opt_dict.keys():
            print(f"options.txt: no entry for '{name}'! defaulting to {opt_default}")
            opt_dict[name] = opt_default

    return opt_dict