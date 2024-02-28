import os
from sys import platform


def clear(force: bool = False) -> None:
    """Flush the Windows command line output."""

    # This is not complete nor correct, but in most cases it should work.
    if platform == 'win32' and not force:
        exit_code = os.system('cls')
        if exit_code != 0:
            raise OSError(f'could not clear console (exit code: {exit_code})')
    else:
        raise OSError('WinClear should only be installed on Windows')
