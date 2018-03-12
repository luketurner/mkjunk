from sys import argv, stderr
from itertools import cycle, islice
from humanfriendly import parse_size
from click import command, option, argument

@command()
@argument('num_bytes')
@option('--seed', '-s', default='junk', help='alternate seed text for generation')
def main(num_bytes, seed):
    """Accepts a NUM_BYTES (which can be human-readable, e.g. "1mb") and writes that many bytes of junk characters to STDOUT. The junk is just a single "seed string" repeated."""
    output = ''.join(list(islice(cycle(seed), parse_size(num_bytes))))
    print('Generating', len(output), 'bytes...', file=stderr)
    print(output, end='')

if __name__ == '__main__':
    main()