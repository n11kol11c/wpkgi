import os
import sys
import typing
import json
from typing import Union, Optional, List

# Define a class to handle package configuration loaded from a JSON file
class PackageConfig(object):
    
    # Initialize the class, accepts a file path to a JSON file
    def __init__(self, json_file: Optional[str]):
        # Load the JSON file using the load_file method
        self.json_file = self.load_file(json_file)

    # A static method to load the content of the JSON file
    @staticmethod
    def load_file(file_f: Optional[str]):
        # Check if the provided file path is a string (a valid file path)
        if isinstance(file_f, str):
            try:
                # Attempt to open the file in read mode and load its content as JSON
                with open(file_f, mode='r', encoding='utf-8') as f:
                    return json.load(f)  # Return the JSON content as a Python object (usually a dict or list)
            except FileNotFoundError as e:
                # Handle file not found error
                print(f"Error: {e}")
                return {}  # Return an empty dictionary if the file doesn't exist
            except json.JSONDecodeError as e:
                # Handle errors related to JSON parsing
                print(f"JSON Error: {e}")
                return {}  # Return an empty dictionary if JSON is not correctly formatted
        else:
            # If the file path isn't a valid string, return an empty dictionary
            return {}

    # Method to search for a package by its 'id' field
    def find_by_id(self, search_id: Union[str, int]):
        # Check if the JSON file content is a list (it should be a list of packages)
        if isinstance(self.json_file, list):
            # Iterate through each item (which is expected to be a dictionary) in the list
            for line in self.json_file:
                # If the item is a dictionary and has a matching 'id', return that item
                if isinstance(line, dict) and line.get('id') == search_id:
                    return line
        # Return None if no matching package is found
        return None
