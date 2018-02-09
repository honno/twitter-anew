"""
tanew

Usage:
  tanew status
  tanew
  tanew access
  tanew listify
  tanew unfollow
  tanew -h | --help
  tanew --version

Options:
  -h --help
  --version
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    import commands
    options = docopt(__doc__, version=VERSION)

    for k, v in options.iteritems():
        if hasattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
