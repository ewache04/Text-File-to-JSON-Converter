import json

# Author: Jeremiah E. Ochepo
# Last Updated: 3/23/2017
# Description: This Python script reads the content of a text
# file, stores it in a JSON file, and then displays the content from the JSON file.


# Open and Read Text File
def readTextFile():
    fileName = 'text.txt'
    try:
        with open(fileName, 'r') as fileObject:
            fileContent = fileObject.read()
    except FileNotFoundError:
        print(f"Sorry! File '{fileName}' not found in the directory.")
        return None
    else:
        return fileContent


# Store Text File Content in JSON
def storeTextFileInJson():
    textString = readTextFile()
    if textString is not None:
        fileName = 'text_string.json'
        try:
            with open(fileName, 'w') as fileObject:
                json.dump(textString, fileObject)
        except Exception as e:
            print(f"An error occurred while storing data in JSON: {e}")
        else:
            print(f"Text file content has been successfully stored in '{fileName}'.")


# Display Text File Content from JSON
def displayTextFileFromJson():
    fileName = 'text_string.json'
    try:
        with open(fileName) as fileObject:
            fileContent = json.load(fileObject)
            print(fileContent)
    except FileNotFoundError:
        print(f"Sorry! File '{fileName}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON content in '{fileName}'. Make sure the file contains valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call functions
storeTextFileInJson()
displayTextFileFromJson()
