import os
import sys
import subprocess
import io
import re
import asyncio
import math
import string
import typing
import colorama
from classes.PackageConfig import PackageConfig

def main():
    try:
        import core
        from typing import Union, Optional, List
        from assets import info, main_logo, menu
        from classes.FileEvent import fileEvent
        from classes.OnLoad import onload
        from classes.SyntaxError import handleSyntax
        from core.config import Config
        from handlers.error_handle import ErrorHandling
    except (ImportError, Exception) as e:  # Proper multiple exception handling
        print(f"Error: {e}")  # Print error instead of returning
    else:
        # Ensure `Config` initializes only if no errors occur
        wpkgi = Config(config_file='./core/packages.json')
        wpkgi.logo(display_ok=True)
        wpkgi.menu(display_ok=True)
        wpkgi.run()

if __name__ == "__main__":
    main()