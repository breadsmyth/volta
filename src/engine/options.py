import re
resolution_pattern = re.compile(r'(\d+)[xX](\d+)')

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
        # Parse numbers
        if name == 'fps':
            try:
                value = int(value)

            except ValueError:
                print("options.txt: bad value for 'fps'! defaulting to 60")
                value = 60

        elif name == 'resolution':
            try:
                matches = resolution_pattern.match(value)
                if matches is None:
                    raise ValueError

                value = (int(matches.group(1)), int(matches.group(2)))

            except ValueError:
                print("options.txt: bad value for 'resolution'! defaulting to 800x600")
                value = (800, 600)

        elif name == 'zoom':
            try:
                value = int(value)

            except ValueError:
                print("options.txt: bad value for 'zoom'! defaulting to 1")
                value = 1

        opt_dict[name] = value

        # Fill in missing values
        # (TODO)

    return opt_dict