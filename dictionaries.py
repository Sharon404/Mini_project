import json
import difflib

# Assuming 'data.json' contains your JSON data
try:
    with open('data.json', 'r') as file:
        json_data = file.read()
except FileNotFoundError:
    print("Error: The file 'data.json' does not exist.")

# Loading JSON data into a Python dictionary
python_dict = json.loads(json_data)

# Now 'python_dict' contains your JSON data as a dictionary
#print(python_dict)

word = str(input("Enter a word to find the definition: "))
word_lower = word.lower()
print(word_lower)

#Try to see if the word entered by the user is in the dictionary and print the error if not
try:  
    if  word_lower in python_dict:
         word_lower = python_dict[word_lower]
         print(word_lower)
    else:
        close_matches = difflib.get_close_matches(word_lower, python_dict)
        if close_matches:
            suggestions = close_matches[0]
            print("Did you mean:", suggestions, "?")
            
            confirmation = input('Enter Yes if correct and no otherwise: ')
            if confirmation.lower() == 'yes':
                print(python_dict[suggestions])
            else:
                print('User did not confirm the suggesion')
          
        else:
            print("No matching word found in the dictionary.")
    
except KeyError:
    print('Error! Enter a valid Word')
    

    

