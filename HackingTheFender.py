# Hacking The Fender
# Password.csv and other directories exist in codeacademy 
import csv
import json

compromised_users = []

# Step 1: Read and process the CSV file
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row)
        compromised_users.append(password_row['Username'])
        print(password_row)  # Print the entire row
        print(password_row['Username'])  # Print the username

# Step 2: Write to compromised_users.txt
with open('compromised_users.txt', 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        print("Writing to file:", compromised_user)  # Debug output
        compromised_user_file.write(str(compromised_user) + "\n")

# Step 3: Create and write JSON message
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    print("Boss Message Dict:", boss_message_dict)  # Debug output
    json.dump(boss_message_dict, boss_message)

# Step 4: Write ASCII art to new_passwords.csv
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
    print("Slash Null Signature:")  # Debug output
    print(slash_null_sig)  # Print ASCII art
    new_passwords_obj.write(slash_null_sig)
