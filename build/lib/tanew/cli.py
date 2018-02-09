"""
tanew

Usage:
  tanew status
  tanew linkaccount
  tanew [-n] generatelists
  tanew [-n] backup <file>
  tanew [-n] unfollowall
  tanew -h, --help
  tanew --version

Options:
  -n, --no-act
  -h, --help
  --version
"""

from inspect import getmembers, isclass

from docopt import docopt

from __init__ import __version__ as VERSION

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
