student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
new_dict = {row.student:row.score for (index, row) in student_data_frame.iterrows()}
# print(new_dict)
    
    

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dixt = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dixt)

# TODO2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
phonetic_list = [nato_dixt[letter] for letter in user_input if letter in nato_dixt]
print(phonetic_list)