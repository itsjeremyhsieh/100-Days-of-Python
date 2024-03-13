#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Input/Letters/starting_letter.txt")
content = f.read()
f.close()
names = open("Input/Names/Invited_names.txt")
for name in names.readlines():
    name = name.strip()
    content_tmp = content.replace("[name]", name)
    print(content_tmp)

    letter_name = "Output/ReadyToSend/" + name + ".txt"
    new_letter = open(letter_name, "w")
    new_letter.write(content_tmp)
    new_letter.close()
names.close()

