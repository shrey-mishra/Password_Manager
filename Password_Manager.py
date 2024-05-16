from cryptography.fernet import Fernet

# Function to generate and write a new encryption key to a file (key.key)
# Note: This function is commented out as it's assumed that the key is already generated and saved.
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# Uncomment the following line to generate a new encryption key
# write_key()
'''

# Function to load the encryption key from the key file (key.key)
def load_key():
    # Open the key file in binary mode and read the key
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Get the master password from the user
master_pwd = input("what is the master password? ")

# Load the encryption key from the key file and concatenate it with the master password
key = load_key() + master_pwd.encode()
# Create a Fernet instance using the concatenated key
fer = Fernet(key)

# Function to view decrypted passwords
def view():
    # Open the passwords file
    with open("passwords.txt", 'r') as f:
        # Read each line in the file
        for line in f.readlines():
            # Remove trailing whitespace and split the line into username and encrypted password
            data = (line.rstrip())
            user , passw = data.split("|")
            # Decrypt the password using the Fernet instance and print the username and decrypted password
            print("Username : ", user , "| Password : ", fer.decrypt(passw.encode()).decode())

# Function to add a new password
def add():
    # Get the account name and password from the user
    name = input("Account Name: ")
    pwd = input("Password Name: ")

    # Open the passwords file in append mode and write the encrypted account name and password
    with open("passwords.txt", 'a') as f:
        f.write( name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop to interact with the user
while True:
    # Prompt the user for action (view passwords, add new password, or quit)
    mode = input("Would you like to add a new password or view existing ones (view, add) or press 'q' to quit: ")
    # Check the user's input
    if mode.lower() == "q":
        # If 'q' is entered, break out of the loop to quit the program
        break
    elif mode.lower() == "view":
        # If 'view' is entered, call the view() function to display existing passwords
        view()
    elif mode.lower() == "add":
        # If 'add' is entered, call the add() function to add a new password
        add()
    else:
        # If an invalid input is provided, inform the user
        print("Bad Request")
        # Continue to the next iteration of the loop
        continue
