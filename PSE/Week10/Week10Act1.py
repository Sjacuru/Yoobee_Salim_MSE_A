class DataAnalyzer:
    """
    Analyzes a given input (either a string or a list) to calculate 
    its total length and count the number of uppercase characters 
    if the input contains strings.
    """    
    def __init__(self, data):
        """
        Initializes the DataAnalyzer with the input data.
        Args:
            data (str or list): The data to be analyzed.     
        Raises:
            TypeError: If the input is not a string or a list.
        """
        if not isinstance(data, (str, list)):
            raise TypeError("Input data must be a string or a list.")
        self._data = data
    @property
    def data(self):
        """Getter for the data."""
        return self._data
    def calculate_total_length(self):
        """
        Calculates the total length of the data.
        - For a string, it's the number of characters.
        - For a list, it's the number of elements.
        Returns:
            int: The total length.
        """
        return len(self._data)
    def count_uppercase_chars(self):
        """
        Determines the number of uppercase characters.
        - For a string, it counts the uppercase characters directly.
        - For a list, it iterates through all string elements and 
          counts their uppercase characters. Non-string elements are ignored.
        Returns:
            int: The total count of uppercase characters.
        """
        total_uppercase = 0
        if isinstance(self._data, str):
            # Analysis for a string
            for char in self._data:
                if char.isupper():
                    total_uppercase += 1
        elif isinstance(self._data, list):
            # Analysis for a list: iterate through elements and check if they are strings
            for item in self._data:
                # We only check for uppercase inside string elements
                if isinstance(item, str):
                    for char in item:
                        if char.isupper():
                            total_uppercase += 1
        return total_uppercase
# --- Example Usage ---
# 1. Example with a String
print("--- String Analysis ---")
STRING_DATA = "Hello World! This is a test."
STRING_ANALYZER = DataAnalyzer(STRING_DATA)

string_length = STRING_ANALYZER.calculate_total_length()
STRING_UPPERCASE = STRING_ANALYZER.count_uppercase_chars()

print(f"Data: '{STRING_DATA}'")
print(f"Total Length: {string_length}")
print(f"Total Uppercase Characters: {STRING_UPPERCASE}")
print("-" * 30)

# 2. Example with a List
print("--- List Analysis ---")
list_data = ["AppLE", "bAnAnA", 123, "Orange Juice", "LAST"]
list_analyzer = DataAnalyzer(list_data)

list_length = list_analyzer.calculate_total_length()
LIST_UPPERCASE = list_analyzer.count_uppercase_chars()

print(f"Data: {list_data}")
print(f"Total Length (Number of elements): {list_length}")
print(f"Total Uppercase Characters (across all strings): {LIST_UPPERCASE}")
print("-" * 30)

# 3. Example with another String
print("--- String Analysis (Pure Caps) ---")
ALL_CAPS = "PYTHON IS OBJECT ORIENTED"
caps_analyzer = DataAnalyzer(ALL_CAPS)

print(f"Data: '{ALL_CAPS}'")
print(f"Total Length: {caps_analyzer.calculate_total_length()}")
print(f"Total Uppercase Characters: {caps_analyzer.count_uppercase_chars()}")
print("-" * 30)

