#!c:\users\flore\uw3\flask-todo\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'lock==2018.3.25.2110','console_scripts','lock'
__requires__ = 'lock==2018.3.25.2110'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('lock==2018.3.25.2110', 'console_scripts', 'lock')()
    )
