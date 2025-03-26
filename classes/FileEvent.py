import os 
import sys 
import typing
from typing import Union, Optional, List

# Define a class to handle file events
class fileEvent(object):
    # Initialize the fileEvent class with an optional filename parameter
    def __init__(self, filename: str | bool = None):
        self.filename = filename  # Store the filename for future use
    
    # Define the __call__ method to make an instance of fileEvent callable
    def __call__(self, function):
        # This wrapper function is used to wrap any function passed to fileEvent
        def wrapper(*args, **kwargs):
            try:
                # Execute the function and store its result
                func = function(*args, **kwargs)
                
                # Open the specified file in append mode, if a filename is provided
                if self.filename:
                    with open(file=self.filename, mode="a") as file:
                        # Write the result of the function call to the file
                        file.write(func)
                
            except Exception as e:
                # If there is an error, prepare an error message
                content = "Error in filename."
                exceptionErrorMessage(message_content=content)  # Handle the error message (function not defined here)
                
                # Print the actual exception message for debugging purposes
                print(e)
            
            # Return the result of the original function (regardless of error)
            return func
        
        # Return the wrapper function, so it can replace the original function
        return wrapper
