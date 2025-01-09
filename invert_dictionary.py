from collections import defaultdict
import pprint

# Function to read a dictionary from a file
def read_dictionary(file_name):
    """Reads a dictionary from a text file."""
    dictionary = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Validate and parse lines in the format "key: value1, value2"
                if ': ' in line:
                    key, value = line.strip().split(': ')
                    dictionary[key] = value.split(', ')
                else:
                    print(f"Skipped invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return dictionary

# Function to invert a dictionary
def invert_dictionary(dictionary):
    """Inverts a dictionary so values become keys and keys become values."""
    inverted = defaultdict(list)  # Using defaultdict for efficiency
    for key, values in dictionary.items():
        for value in values:
            inverted[value].append(key)  # Avoids manual checks for key existence
    return dict(inverted)  # Convert back to a regular dictionary for compatibility

# Function to write a dictionary to a file
def write_dictionary(dictionary, file_name):
    """Writes a dictionary to a text file."""
    try:
        with open(file_name, 'w') as file:
            for key, values in dictionary.items():
                file.write(f"{key}: {', '.join(values)}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    input_file = 'input_dict.txt'
    output_file = 'inverted_dict.txt'

    # Read the dictionary from a file
    original_dict = read_dictionary(input_file)

    # Process only if the dictionary was successfully loaded
    if original_dict:
        # Invert the dictionary
        inverted_dict = invert_dictionary(original_dict)

        # Write the inverted dictionary to a file
        write_dictionary(inverted_dict, output_file)

        # Print dictionaries for verification using pprint
        print("Original Dictionary:")
        pprint.pprint(original_dict, indent=4)
        print("\nInverted Dictionary:")
        pprint.pprint(inverted_dict, indent=4)
