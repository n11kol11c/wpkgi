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

def menu():
    menu = f"""
\t{Fore.YELLOW}[{Fore.RED}00{Fore.YELLOW}]{Fore.YELLOW} Microsoft.VCRedist.2015+.x64                 {Fore.YELLOW}[{Fore.RED}14{Fore.YELLOW}]{Fore.YELLOW} Adobe Acrobat Reader               {Fore.YELLOW}[{Fore.RED}28{Fore.YELLOW}]{Fore.YELLOW} Steam   
\t{Fore.YELLOW}[{Fore.RED}01{Fore.YELLOW}]{Fore.YELLOW} Microsoft.DotNet.DesktopRuntime.6            {Fore.YELLOW}[{Fore.RED}15{Fore.YELLOW}]{Fore.YELLOW} 7-Zip                              {Fore.YELLOW}[{Fore.RED}29{Fore.YELLOW}]{Fore.YELLOW} Epic Games Launcher
\t{Fore.YELLOW}[{Fore.RED}02{Fore.YELLOW}]{Fore.YELLOW} PowerToys                                    {Fore.YELLOW}[{Fore.RED}16{Fore.YELLOW}]{Fore.YELLOW} Everything - file search           {Fore.YELLOW}[{Fore.RED}30{Fore.YELLOW}]{Fore.YELLOW} MSIAfterburner
\t{Fore.YELLOW}[{Fore.RED}03{Fore.YELLOW}]{Fore.YELLOW} Windows Terminal                             {Fore.YELLOW}[{Fore.RED}17{Fore.YELLOW}]{Fore.YELLOW} Google Chrome                      {Fore.YELLOW}[{Fore.RED}31{Fore.YELLOW}]{Fore.YELLOW} RazerCortex
\t{Fore.YELLOW}[{Fore.RED}04{Fore.YELLOW}]{Fore.YELLOW} WSL                                          {Fore.YELLOW}[{Fore.RED}18{Fore.YELLOW}]{Fore.YELLOW} Firefox
\t{Fore.YELLOW}[{Fore.RED}05{Fore.YELLOW}]{Fore.YELLOW} Malwarebytes                                 {Fore.YELLOW}[{Fore.RED}19{Fore.YELLOW}]{Fore.YELLOW} Edge
\t{Fore.YELLOW}[{Fore.RED}06{Fore.YELLOW}]{Fore.YELLOW} CCleaner                                     {Fore.YELLOW}[{Fore.RED}20{Fore.YELLOW}]{Fore.YELLOW} Discord
\t{Fore.YELLOW}[{Fore.RED}07{Fore.YELLOW}]{Fore.YELLOW} Git                                          {Fore.YELLOW}[{Fore.RED}21{Fore.YELLOW}]{Fore.YELLOW} Slack
\t{Fore.YELLOW}[{Fore.RED}08{Fore.YELLOW}]{Fore.YELLOW} Python                                       {Fore.YELLOW}[{Fore.RED}22{Fore.YELLOW}]{Fore.YELLOW} Zoom
\t{Fore.YELLOW}[{Fore.RED}09{Fore.YELLOW}]{Fore.YELLOW} Node.js                                      {Fore.YELLOW}[{Fore.RED}23{Fore.YELLOW}]{Fore.YELLOW} Teams
\t{Fore.YELLOW}[{Fore.RED}10{Fore.YELLOW}]{Fore.YELLOW} Docker                                       {Fore.YELLOW}[{Fore.RED}24{Fore.YELLOW}]{Fore.YELLOW} VLC
\t{Fore.YELLOW}[{Fore.RED}11{Fore.YELLOW}]{Fore.YELLOW} Visual Studio Code                           {Fore.YELLOW}[{Fore.RED}25{Fore.YELLOW}]{Fore.YELLOW} GIMP
\t{Fore.YELLOW}[{Fore.RED}12{Fore.YELLOW}]{Fore.YELLOW} JetBrains Toolbox                            {Fore.YELLOW}[{Fore.RED}26{Fore.YELLOW}]{Fore.YELLOW} Audacity
\t{Fore.YELLOW}[{Fore.RED}13{Fore.YELLOW}]{Fore.YELLOW} Microsoft Office (or LibreOffice)            {Fore.YELLOW}[{Fore.RED}27{Fore.YELLOW}]{Fore.YELLOW} OBSStudio

    """
    print(menu)