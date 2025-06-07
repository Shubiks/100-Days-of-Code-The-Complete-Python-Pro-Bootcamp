PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        c = contents.replace(PLACEHOLDER,stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx","w") as out:
            f = out.writelines(c)