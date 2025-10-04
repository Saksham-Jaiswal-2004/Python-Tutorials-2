with open("names.txt") as file:
    names = file.readlines()

with open("starting_letter.txt") as letter_file:
    content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace("[name]", stripped_name)

        with open(f"./ReadyToSendMails/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)