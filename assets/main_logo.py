import colorama as cr # Import colors for logo
from colorama import (
    Back, # Back-face colors
    Fore, # Fore-face colors
    Style, # Styles
    init # Init
)

# Import info about tool
from .info import ( 
    __author__,
    __github__
)

# Import tool version
from core import (__version__)

cr.init(autoreset=True) # Auto reset colors 

def main_logo():
    logo = f"""
    
\t██╗    ██╗██████╗ ██╗  ██╗ ██████╗ ██╗            Author: {__author__}
\t██║    ██║██╔══██╗██║ ██╔╝██╔════╝ ██║            Github: {__github__}
\t██║ █╗ ██║██████╔╝█████╔╝ ██║  ███╗██║
\t██║███╗██║██╔═══╝ ██╔═██╗ ██║   ██║██║
\t╚███╔███╔╝██║     ██║  ██╗╚██████╔╝██║
\t ╚══╝╚══╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝            Version: {__version__}
                                   
    """

    print(Fore.MAGENTA + logo + Fore.RESET)