r"""
This script manages package installations using `winget`.

Features:
- Loads a configuration file (`config_file`) containing a list of packages.
- Allows users to select and install packages interactively.
- Uses `colorama` for colored terminal output.
- Includes error handling for invalid input and out-of-range selections.
- Provides an option to exit the program by entering 'e'.

Classes:
- Config:
  - Handles configuration loading and package installations.
  - Provides a menu interface for user interaction.

External Dependencies:
- colorama (for terminal color styling)
- JSON (for configuration file parsing)
- os, sys (for system operations)
"""

import os
import json
import sys  
import time
from assets.main_logo import main_logo
from typing import Optional, Union

import colorama
colorama.init(autoreset=True)

from colorama import Fore
from classes.SyntaxError import handleSyntax
from classes.OnLoad import onload
from assets.menu import menu

class Config:
    def __init__(self, config_file: str):
        """Initialize the Config class and load packages from the given JSON config file."""
        self.packages = self.load_packages(config_file)

    def load_packages(self, config_file: str) -> list:
        """
        Load package configurations from a JSON file.
        
        Args:
            config_file (str): Path to the configuration JSON file.

        Returns:
            list: List of package configurations if successful, else an empty list.
        """
        try:
            with open(config_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"{Fore.RED}Error: Configuration file '{config_file}' not found.{Fore.RESET}")
        except json.JSONDecodeError:
            print(f"{Fore.RED}Error: Failed to parse JSON from '{config_file}'.{Fore.RESET}")
        return []  # Return an empty list if an error occurs

    @staticmethod
    def download(package: Optional[str]) -> Union[str, bool]:
        """
        Installs a package using `winget`.

        Args:
            package (Optional[str]): The package ID to install.

        Returns:
            Union[str, bool]: Success message on completion, False if no package is provided.
        """
        if package:
            try:
                os.system(f'winget install --id={package} -e --silent')
                return f"{Fore.GREEN}Package '{package}' installed successfully.{Fore.RESET}"
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Installation interrupted by user.{Fore.RESET}")
                sys.exit(1)
        return False 

    @staticmethod
    def logo(display_ok: bool = False):
        """
        Displays the logo if display_ok is True.

        Args:
            display_ok (bool, optional): Determines whether to show the logo. Defaults to False.
        """
        if display_ok:
            main_logo()
        else:
            return -1

    @staticmethod
    def menu(display_ok: bool = False):
        """
        Displays the package selection menu if display_ok is True.

        Args:
            display_ok (bool, optional): Determines whether to show the menu. Defaults to False.
        """
        if display_ok:
            menu()
        else:
            return -1

    def run(self):
        """Runs the interactive menu for package selection and installation."""
        if not self.packages:
            print(f"{Fore.RED}No packages loaded. Exiting...{Fore.RESET}")
            sys.exit(1)

        while True:
            os.system('cls')
            self.logo(display_ok=True)
            self.menu(display_ok=True)
            try:
                choice = input(f"\n\t{Fore.MAGENTA}Enter a choice (or 'e' to exit):{Fore.RESET} ").strip()
                
                if choice.lower() == 'e':
                    print(f"{Fore.RED}Exiting program...{Fore.RESET}")
                    sys.exit()

                indices = choice.split(',')
                
                for index in indices:
                    index = index.strip()
                    
                    if index.isdigit():
                        p = int(index)
                        
                        if 0 <= p < len(self.packages):
                            package_id = self.packages[p].get('value')
                            
                            if package_id:
                                result = self.download(package_id)
                                if result:
                                    print(result)
                                    time.sleep(0.8)
                                    self.run()
                            else:
                                print(f"{Fore.RED}Package at index {p} is missing a 'value' field.{Fore.RESET}")
                        else:
                            print(f"{Fore.RED}Index {p} is out of range. Valid range: 0-{len(self.packages) - 1}{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}Invalid input: '{index}'. Please enter a valid number or 'e' to exit.{Fore.RESET}")

            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Exiting program due to user interruption.{Fore.RESET}")
                sys.exit(1)
