import os
import sys
from typing import Optional

# Assuming `colorama` is imported to use color formatting
from colorama import Fore, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Define the 'onload' class for handling file actions and function decoration
class onload(object):
    # Initialize the class with optional 'type_t' and 'file_path' parameters
    def __init__(self, type_t: Optional[str], file_path: Optional[str]):
        self.type_t = type_t  # Store the type of action ('e', 'i', or 's')
        self.file_path = file_path  # Store the file path for file-related actions
        
        # Define possible types for the 'type_t' parameter (Error, Information, Success)
        self.types = {
            "e",  # Type for error handling
            "i",  # Type for information display
            "s"   # Type for success display (potentially)
        }

    # The __call__ method allows instances of this class to be used as decorators
    def __call__(self, function):
        # Wrapper function is called when the decorated function is executed
        def wrapper(*args, **kwargs):
            # Check if both 'type_t' and 'file_path' are strings
            if isinstance(self.type_t, str) and isinstance(self.file_path, str):
                # Handle the 'error' type ('e' or 'E')
                if self.type_t == "e" or self.type_t.lower() == "e":
                    try:
                        # Attempt to open the specified file in read mode
                        with open(self.file_path, 'r') as file:
                            # Read the content of the file
                            data = file.read()
                            # Print the file content in red (error color)
                            print(f"{Fore.RED}{data}{Fore.RESET}")
                    except Exception as e:
                        # If there's an error (e.g., file not found), print the error in red
                        print(f"{Fore.RED}Error: {e}{Fore.RESET}")

                # Handle the 'information' type ('i' or 'I')
                elif self.type_t == "i" or self.type_t.lower() == "i":
                    # Print a success message or any informational message in green
                    print(f"{Fore.GREEN}Information loaded successfully!{Fore.RESET}")

                # Optionally, add logic for 'success' type ('s' or 'S')
                elif self.type_t == "s" or self.type_t.lower() == "s":
                    # Print a success message in cyan
                    print(f"{Fore.CYAN}Success: File action completed.{Fore.RESET}")

                # After handling the file operation or type-based action, call the original function
                return function(*args, **kwargs)

        # Return the wrapper function to replace the original function
        return wrapper
