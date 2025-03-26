import os 
import sys 
import typing
import json
from typing import List, Union, Optional

# Define a class to handle syntax-related errors and writing them to a file
class handleSyntax:
    # Initialize the class with optional 'mode' and 'file_path'
    def __init__(self, mode: typing.Optional[str], file_path: typing.Optional[str]):
        self.mode = mode  # Store the mode (1 or 2) indicating how to handle the error
        self.file_path = file_path  # Store the file path where the error messages will be written
        self.modes = {1, 2}  # Define valid modes for error handling (mode 1 or mode 2)

    # Define the error message format for mode 1
    @staticmethod
    def msg_mode_1() -> typing.Optional[str]:
        # This will return a generic error message format for mode 1
        return "Error in syntax: Invalid syntax encountered in the input."

    # Define the error message format for mode 2
    @staticmethod
    def msg_mode_2() -> typing.Optional[str]:
        # This will return a generic error message format for mode 2
        return "Error in syntax: Please check the command syntax."

    # The __call__ method allows instances of this class to be used as decorators
    def __call__(self, function):
        # Wrapper function is called when the decorated function is executed
        def wrapper(*args, **kwargs):
            # Check if the mode is an integer and file_path is a string
            if isinstance(self.mode, int) and isinstance(self.file_path, str):
                # Handle mode 1: Write message for syntax error in mode 1 to file
                if self.mode == 1 or 1 in self.modes:
                    try:
                        with open(file=self.file_path, mode='a', encoding='utf-8') as file:
                            msg = self.msg_mode_1()  # Get the error message for mode 1
                            file.write(msg)  # Write the error message to the file
                    except (Exception, FileNotFoundError, FileExistsError) as e:
                        # Catch any exceptions related to file access or writing
                        return f"Error occurred: {e}"
                    finally:
                        pass  # Ensure execution moves forward even after file operation (no special handling needed here)

                # Handle mode 2: Write message for syntax error in mode 2 to file
                if self.mode == 2 or 2 in self.modes:
                    try:
                        with open(file=self.file_path, mode='a', encoding='utf-8') as file:
                            msg = self.msg_mode_2()  # Get the error message for mode 2
                            file.write(msg)  # Write the error message to the file
                    except (Exception, FileNotFoundError, FileExistsError) as e:
                        # Catch any exceptions related to file access or writing
                        return f"Error occurred: {e}"
                    finally:
                        pass  # Ensure execution moves forward even after file operation

            # Call the original function and return its result
            func = function(*args, **kwargs)
            return func 

        return wrapper
