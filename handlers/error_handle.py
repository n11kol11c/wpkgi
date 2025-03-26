import os 
import sys 
import random
import io 
import re 
from typing import Optional, Union, List

# Importing custom decorators for handling syntax errors, loading events, and file events.
from classes.SyntaxError import handleSyntax
from classes.OnLoad import onload
from classes.FileEvent import fileEvent

class ErrorHandling:
    """
    A class that provides standardized error messages for exceptions and syntax errors.

    Features:
    - Uses decorators for logging and syntax validation.
    - Provides error messages in a structured format.
    """

    @staticmethod
    @fileEvent(filename='')  # Logs the error message to a file
    @handleSyntax(mode=1, file_path='')  # Handles syntax-related errors
    @onload(type_t='s', file_path='')  # Indicates a successful file operation
    def exceptionErrorMessage(
        message_content: Optional[Union[str, bool]] = None
    ) -> Union[str, bool, None]:
        """
        Generates an exception error message.

        Args:
            message_content (Optional[Union[str, bool]]): The error message content.

        Returns:
            Union[str, bool, None]: Formatted error message or a default error string if no input is provided.
        """
        if message_content and isinstance(message_content, str):
            return f"ExceptionError: {message_content}"
        return f"Error in {ErrorHandling.exceptionErrorMessage.__name__} function, missing argument"

    @staticmethod
    @fileEvent(filename='')  # Logs the syntax error message to a file
    @handleSyntax(mode=1, file_path='')  # Handles syntax-related errors
    @onload(type_t='s', file_path='')  # Indicates a successful file operation
    def syntaxErrorMessage(
        message_content: Optional[Union[str, bool]] = None
    ) -> Union[str, bool, None]:
        """
        Generates a syntax error message.

        Args:
            message_content (Optional[Union[str, bool]]): The syntax error message content.

        Returns:
            Union[str, bool, None]: Formatted syntax error message or a default error string if no input is provided.
        """
        if message_content and isinstance(message_content, str):
            return f"SyntaxError: {message_content}"
        return f"Error in {ErrorHandling.syntaxErrorMessage.__name__} function, missing argument"
