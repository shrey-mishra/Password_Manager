Secure Password Manager

Secure Password Manager is a Python-based application that ensures safe and efficient management of your passwords. Using the cryptography library, it encrypts your credentials and secures them with a master password.


---

Requirements

Python 3.x

cryptography library
Install via pip:

pip install cryptography



---

Features

Strong Encryption: Passwords are encrypted using the Fernet symmetric encryption algorithm provided by the cryptography library.

Master Password: A master password is required to access and manage stored credentials. It combines with an encryption key for enhanced security.

Add and View Passwords: Securely add new credentials and retrieve existing ones.



---

Encryption Details

Passwords are encrypted with the Fernet symmetric encryption algorithm, ensuring data security.
The encryption key is derived from:

1. A key file (key.key).


2. The user's master password.




---

File Structure

password_manager.py: Main script implementing the password manager.

passwords.txt: Stores encrypted passwords.

key.key: Contains the encryption key.



---

Usage

1. Clone the Repository:

git clone <repository-url>
cd SecurePasswordManager


2. Install Dependencies:
Ensure Python and the cryptography library are installed.


3. Run the Application:

python password_manager.py


4. Master Password: Enter your master password when prompted.


5. Options: Choose to either:

Add a new password.

View existing passwords.





---

Contribution

Contributions are welcome!

1. Fork the repository.


2. Create a feature branch.


3. Commit your changes.


4. Submit a pull request.




---

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Feel free to reach out for support or additional features!

