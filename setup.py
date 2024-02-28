from setuptools import setup
from sys import platform

if __name__ == "__main__":
    if platform != 'win32':
        raise OSError(
            'aborting installation: WinClear should only be installed on'
            f' Windows platforms (found: {platform})')

    setup()
